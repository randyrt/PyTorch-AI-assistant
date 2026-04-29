cat > app/knowledge_base.py << 'EOF'
"""Base de connaissances du portfolio"""

from app.config import PORTFOLIO_KNOWLEDGE
from typing import Optional, Tuple

class KnowledgeBase:
    def __init__(self):
        self.knowledge = PORTFOLIO_KNOWLEDGE
    
    def search(self, query: str, language: str) -> Optional[Tuple[str, str]]:
        """
        Recherche par mots-clés dans la base de connaissances.
        Retourne (réponse, route) ou None si pas trouvé.
        """
        query_lower = query.lower()
        
        for key, info in self.knowledge.items():
            # Vérifier si un mot-clé est dans la question
            for keyword in info["keywords"]:
                if keyword in query_lower:
                    return (info[language], info["route"])
        
        return None
    
    def get_all_routes_summary(self, language: str) -> str:
        """Résumé de toutes les routes disponibles"""
        routes = []
        for key, info in self.knowledge.items():
            routes.append(f"{info['route']} - {info[language][:50]}...")
        return " | ".join(routes)
EOF