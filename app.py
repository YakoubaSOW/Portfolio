from flask import Flask, render_template

app = Flask(__name__)


# --- MODÈLE ---
portfolio_data = {
    "nom": "Yakouba SOW",
    "titre": "Étudiant BUT 2 Informatique | Futur Développeur Back-End",
    "annee": 2026,
    "sections": [
        {
            "id": "presentation",
            "titre": "Présentation Personnelle",
            "nav_titre": "Présentation",
            "contenu": """Je m'appelle Yakouba SOW et je suis un étudiant en BUT 2 à l'Université Sorbonne Paris NORD.
J’ai choisi de m'orienter en informatique, plus précisément en développement web, car c’est un domaine qui me passionne. Développer des sites internet et des applications est quelque chose que j'affectionne au quotidien. À l’avenir, j’aimerais travailler en tant que développeur web Full Stack ou Back-End. Mes expériences en stage m'ont permis de découvrir le monde du travail, avec des demandes précises et des attentes professionnelles.
Mon projet est de me former davantage, notamment en Back-End. J'ai réalisé que je prends plus de plaisir à développer des fonctionnalités qu'à peaufiner l'aspect graphique. Je m'intéresse particulièrement à Python (Data/IA), TypeScript et React JS.
Cette année de BUT 2 m’a donné l’envie de renforcer mes acquis et de devenir un bien meilleur développeur, techniquement et mentalement, pour saisir les meilleures opportunités futures."""
        },
        {
            "id": "projets",
            "titre": "Bilan de mes Projets Universitaires",
            "nav_titre": "Projets Universitaires",
            "contenu": "Ici, tu peux détailler les projets sur lesquels tu as travaillé, les compétences que tu as développées et les résultats obtenus."
        },
        {
            "id": "stage",
            "titre": "Bilan de mon Stage",
            "nav_titre": "Stage",
            "contenu": """Pour ce stage, j’ai travaillé dans le service informatique d’une entreprise de flocage et de textile. J'ai développé de nouvelles fonctionnalités : visualisation des factures avec tableaux et graphiques, suivi de livraison, et gestion des logos clients.
Techniquement, j'ai codé en PHP avec la méthode PDO et implémenté des requêtes AJAX pour rendre l'interface plus fluide. Les 8 semaines de pratique m’ont vraiment permis de renforcer mes compétences. Les missions confiées ont été réalisées avec succès.
Sur le plan transversal, la communication a été essentielle. Mes collègues stagiaires m’ont été d’une grande aide pour résoudre les points de blocage. C’est beaucoup plus agréable de travailler avec des personnes avec qui l'on peut échanger et s'entraider."""
        },
        {
            "id": "objectifs",
            "titre": "Mes Objectifs",
            "nav_titre": "Objectif futur",
            "contenu": """Mes objectifs sont dans un premier temps de valider mon BUT. Pour ma troisième année, j’aimerais faire un stage en TypeScript pour confirmer mon attrait pour ce langage et ses débouchés.
Par la suite, je souhaite poursuivre vers un Master (Bac +5) pour maximiser mes chances de trouver un emploi de qualité, idéalement en alternance avec une entreprise utilisant TypeScript. En sortie d’études, je vise un poste de Développeur Web Full Stack ou Back-End. Bien que je ne prévoie pas tout sur le très long terme, je suis certain de vouloir continuer dans le développement car coder est vraiment ce que j'aime faire."""
        }
    ]
}

# --- CONTRÔLEUR ---
@app.route('/')
def index():
    return render_template('index.html', data=portfolio_data)

if __name__ == '__main__':
    app.run(debug=True)