from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
from app.model import llm
from app.knowledge_base import KnowledgeBase
from app.language import detect_language
from app.config import SYSTEM_PROMPTS

# ============================================
# INITIALISATION
# ============================================
app = FastAPI(
    title="Portfolio Assistant API",
    description="Assistant IA pour portfolio Vue.js",
    version="1.0.0"
)

# CORS pour Vue.js
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En prod : restreindre au domaine
    allow_methods=["*"],
    allow_headers=["*"],
)

kb = KnowledgeBase()

# ============================================
# MODÈLES DE DONNÉES
# ============================================
class ChatRequest(BaseModel):
    message: str
    language: Optional[str] = None  # "fr", "en", ou None (auto-détection)

class ChatResponse(BaseModel):
    response: str
    suggested_route: Optional[str] = None
    language: str

# ============================================
# ROUTES
# ============================================
@app.on_event("startup")
async def startup():
    """Charge le modèle au démarrage du serveur"""
    llm.load()

@app.get("/")
async def root():
    return {
        "message": "Portfolio Assistant API",
        "model": "microsoft/phi-2",
        "endpoints": ["/chat", "/health", "/routes"]
    }

@app.get("/health")
async def health():
    return {
        "status": "ok",
        "model_loaded": llm.model is not None,
        "device": str(llm.device)
    }

@app.get("/routes")
async def list_routes():
    """Liste toutes les routes du portfolio"""
    return {
        "fr": kb.get_all_routes_summary("fr"),
        "en": kb.get_all_routes_summary("en")
    }

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Endpoint principal du chatbot"""
    
    # 1. Détection de langue
    language = request.language or detect_language(request.message)
    if language not in ["fr", "en"]:
        language = "fr"
    
    # 2. Vérifier la base de connaissances (réponse rapide sans LLM)
    kb_result = kb.search(request.message, language)
    if kb_result:
        response_text, route = kb_result
        return ChatResponse(
            response=response_text,
            suggested_route=route,
            language=language
        )
    
    # 3. Utiliser le LLM pour les questions complexes
    try:
        system_prompt = SYSTEM_PROMPTS[language]
        prompt = f"{system_prompt}\n\nQuestion: {request.message}\nRéponse:"
        
        response = llm.generate(prompt)
        
        if not response:
            response = (
                "Je n'ai pas compris. Essayez /projects ou /contact pour en savoir plus."
                if language == "fr"
                else "I didn't understand. Try /projects or /contact to learn more."
            )
        
        return ChatResponse(
            response=response,
            language=language
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erreur de génération: {str(e)}"
        )
EOF