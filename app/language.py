import re

def detect_language(text: str) -> str:
    """
    Détecte si le texte est en français ou en anglais.
    Retourne 'fr' ou 'en'
    """
    text_lower = text.lower().strip()
    
    # Mots très fréquents exclusifs à chaque langue
    french_markers = [
        "bonjour", "salut", "merci", "projet", "compétence", "contact",
        "quels", "quelles", "comment", "pourquoi", "aide", "aider",
        "je", "tu", "nous", "vous", "mon", "ton", "son", "mes", "tes", "ses"
    ]
    
    english_markers = [
        "hello", "hi", "thanks", "project", "skill", "contact",
        "what", "how", "why", "help", "can", "could", "would",
        "i", "you", "we", "my", "your", "our"
    ]
    
    french_count = sum(1 for word in french_markers if word in text_lower)
    english_count = sum(1 for word in english_markers if word in text_lower)
    
    if french_count > english_count:
        return "fr"
    elif english_count > french_count:
        return "en"
    
    # Si indéterminé, vérifier les caractères accentués (français)
    if re.search(r'[éèêëàâîïôûùç]', text_lower):
        return "fr"
    
    # Par défaut : français
    return "fr"
EOF