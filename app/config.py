import os

# ============================================
# CONFIGURATION DU MODÈLE
# ============================================
MODEL_NAME = "microsoft/phi-2"
MODEL_CACHE_DIR = "./models"

# Paramètres de génération
GENERATION_CONFIG = {
    "max_new_tokens": 200,
    "temperature": 0.7,
    "do_sample": True,
    "top_p": 0.9,
    "top_k": 50,
}

# ============================================
# PROMPTS SYSTÈME (personnalité de l'assistant)
# ============================================
SYSTEM_PROMPTS = {
    "fr": """Tu es RandyBot, l'assistant virtuel du portfolio de Randy, un développeur full-stack.

RÈGLES STRICTES :
1. Réponds UNIQUEMENT en français
2. Maximum 3 phrases par réponse
3. Sois professionnel mais chaleureux
4. Suggère des liens du portfolio : /projects, /skills, /contact
5. Si on te demande tes projets : mentionne Vue.js, TypeScript, Python, PyTorch
6. Si tu ne sais pas : propose d'aller sur /contact

EXEMPLES :
- "Quels sont tes projets ?" → "Randy a réalisé 5 projets dont un e-commerce Vue.js et une API REST. Découvrez-les sur /projects !"
- "Comment te contacter ?" → "Utilisez le formulaire sur /contact ou réservez un appel de 15 minutes directement !"
""",
    
    "en": """You are RandyBot, the virtual assistant for Randy's portfolio, a full-stack developer.

STRICT RULES:
1. Answer ONLY in English
2. Maximum 3 sentences per response
3. Be professional but friendly
4. Suggest portfolio links: /projects, /skills, /contact
5. If asked about projects: mention Vue.js, TypeScript, Python, PyTorch
6. If you don't know: suggest visiting /contact

EXAMPLES:
- "What are your projects?" → "Randy built 5 projects including a Vue.js e-commerce and a REST API. Check them out on /projects!"
- "How can I contact you?" → "Use the form on /contact or book a 15-minute call directly!"
"""
}

# ============================================
# CONNAISSANCES DU PORTFOLIO
# ============================================
PORTFOLIO_KNOWLEDGE = {
    "accueil": {
        "fr": "Page d'accueil avec présentation, compétences et aperçu des projets",
        "en": "Home page with presentation, skills and project overview",
        "route": "/",
        "keywords": ["accueil", "home", "début", "présentation", "qui es-tu", "about", "who are you"]
    },
    "projets": {
        "fr": "5 projets : e-commerce Vue.js, API REST Node.js, portfolio Nuxt 3, app mobile React Native, dashboard Python",
        "en": "5 projects: Vue.js e-commerce, Node.js REST API, Nuxt 3 portfolio, React Native mobile app, Python dashboard",
        "route": "/projects",
        "keywords": ["projet", "project", "réalisation", "travail", "work", "code"]
    },
    "competences": {
        "fr": "Vue.js, TypeScript, Python, PyTorch, Docker, PostgreSQL, Node.js",
        "en": "Vue.js, TypeScript, Python, PyTorch, Docker, PostgreSQL, Node.js",
        "route": "/skills",
        "keywords": ["compétence", "skill", "techno", "tech", "stack", "langage"]
    },
    "contact": {
        "fr": "Formulaire de contact et réservation d'appel via Calendly",
        "en": "Contact form and call booking via Calendly",
        "route": "/contact",
        "keywords": ["contact", "email", "appel", "call", "message", "joindre"]
    },
    "ia": {
        "fr": "Randy maîtrise PyTorch et le Deep Learning : réseaux de neurones, classification d'images (MNIST), NLP",
        "en": "Randy masters PyTorch and Deep Learning: neural networks, image classification (MNIST), NLP",
        "route": "/projects",
        "keywords": ["ia", "ai", "pytorch", "deep learning", "intelligence artificielle", "machine learning", "réseau de neurones"]
    }
}
EOF