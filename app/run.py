import uvicorn

if __name__ == "__main__":
    print("=" * 50)
    print("🚀 Portfolio Assistant")
    print("=" * 50)
    print("\n📡 Démarrage du serveur...")
    print("📍 API : http://localhost:8000")
    print("📖 Docs : http://localhost:8000/docs")
    print("\nAttendez le chargement du modèle (2-3 min)...\n")
    
    uvicorn.run(
        "app.api:app",
        host="0.0.0.0",
        port=8000,
        reload=False 
    )
EOF