import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from app.config import MODEL_NAME, MODEL_CACHE_DIR, GENERATION_CONFIG

class PortfolioLLM:
    def __init__(self):
        self.device = torch.device("cpu")
        self.model = None
        self.tokenizer = None
    
    def load(self):
        """Charge le modèle en mémoire"""
        print(f"📦 Chargement de {MODEL_NAME}...")
        print("   ⏳ Première fois : téléchargement de ~5 Go...")
        print("   ⏳ Les fois suivantes : chargement depuis le cache...")
        
        self.tokenizer = AutoTokenizer.from_pretrained(
            MODEL_NAME,
            cache_dir=MODEL_CACHE_DIR,
            trust_remote_code=True
        )
        
        # Ajouter un token de padding si absent
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token
        
        self.model = AutoModelForCausalLM.from_pretrained(
            MODEL_NAME,
            cache_dir=MODEL_CACHE_DIR,
            torch_dtype=torch.float32,  # CPU : float32 obligatoire
            trust_remote_code=True,
            low_cpu_mem_usage=True
        )
        
        self.model.to(self.device)
        self.model.eval()
        
        print("✅ Modèle chargé avec succès !")
        return self
    
    def generate(self, prompt: str) -> str:
        """Génère une réponse à partir d'un prompt"""
        inputs = self.tokenizer(
            prompt,
            return_tensors="pt",
            truncation=True,
            max_length=512
        ).to(self.device)
        
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                **GENERATION_CONFIG,
                pad_token_id=self.tokenizer.pad_token_id,
                eos_token_id=self.tokenizer.eos_token_id,
            )
        
        # Décoder et nettoyer
        full_response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Enlever le prompt de la réponse
        if prompt in full_response:
            response = full_response[len(prompt):].strip()
        else:
            response = full_response.strip()
        
        # Nettoyer : prendre jusqu'au premier saut de ligne multiple
        response = response.split("\n\n")[0].strip()
        
        return response

# Instance globale (chargée une seule fois)
llm = PortfolioLLM()
EOF