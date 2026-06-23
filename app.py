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
            "liste_projets": [
                {
                    "titre": "Projet universitaire n.3, S3",
                    "contenu": """Le projet est sur le thème de la diffusion sonore, l’objectif de ce projet est de créer une application utilisable pour les magasin afin qu’ils puissent diffuser de la musique tout au long de la journée, avec une capacité à pouvoir générer des plaist qui vont être utiliser pour la diffusion des musique et de pouvoir interrompre ces playlist à n’importe quel moment pour pouvoir diffuser des publicité commercial.
Sur ce projet ma tâches principales accomplis étais sur la partie de diffusion des publicité, mon objectif était de pouvoir stopper interagir avec le lecteur de diffusion du magasin afin de lui transmettre un fichier mp3 d’une annonce publicitaire afin que lorsque qu’il reçoit ce fichier, il met la playlist en pause pour diffuser la publicité dans le magasin et, une fois que la publicité a fini d'être diffuser, la playlist reprend. En tâches secondaires, j’ai travaillé sur des documents de rendu tels que les besoin critique.
Ce projet m’a permis d'acquérir de nouvelle compétence en développement web avec le langage python, au premier semestre, on a eu un cours sur le langage python afin qu’on puisse apprendre à coder dans ce langage notamment pour ce projet, je ne n’ais jamais vraiment coder en python donc cela m’a permis d’apprendre à coder avec ce langage et de pouvoir pratiquer dans un projet complet qui requiert un minimum de compétence en python pour avoir un résultat concret et fonctionnel. Cela m’a aussi permis de mieux communiquer avec mes camarades, de ne pas hésiter à solliciter de l’aide en cas de blocage, d’échanger afin qu’on puisse tous donner nos idées et avis pour la réalisation de ce projet. Cette communication a été cruciale pour la réussite de ce projet et cela m’a permis de mieux communiquer et de réaliser à quel point c’est nécessaire lors d’un projet de groupe.
Pour le projet n.2 de S4, je pourrais davantage communiquer avec mon équipe, être plus vocal sur les problèmes qu’on peut rencontrer ou tout simplement sur l'avancée du projet, ne pas me focaliser seulement sur ma partie mais aussi sur celle des autres afin d’apporter mon aide pour une avancée collective du projet.""",
                    "icone": "fa-server",
                    "tags": [
                        {"nom": "Python", "icone": "fa-brands fa-python"},
                    ],
                    "lien_github": "https://github.com/Hachimohammed/MYSKY_SAE"
                },
                {
                    "titre": "Projet universitaire n.4, S4",
                    "contenu": """L’objectif de ce projet est d’analyser les différents projets réaliser par tout les groupe de S3 afin d’en choisir un et de faire une analyse des points à améliorer et par la suite les changer en améliorant le projet.
Après une analyse de tous les projets, on a décidé de choisir le projet « SoundStream ». Par la suite on a effectué une répartition des tâches pour mener à bien le déroulement du projet.
Mes principales tâches étaient de m’occuper de la partie Marketing et des organisations du projet. Sur le projet initial, les utilisateurs avec le rôle de marketing avaient accès à des droits qu’ils ne sont pas censés avoir, les droits étaient les même que les utilisateurs Admin or ce n’étais pas censé être le cas donc j’ai changé ceci afin que les marketing aient juste les droits de marketing. Pour les organisations, j’ai ajouté la fonctionnalité pour les utilisateurs Admin de créer, modifier et supprimer les organisations du projet. Mes tâches secondaires étaient de modifier des aspects visuels du projet comme le header, changer les liens de redirection.
En termes de compétences techniques, je n’en ai pas acquis de nouvelle car il s’agissait de techniques qu’on avait déjà réaliser lors du projet de S3. Travailler sur un projet qui n’est pas le tient de base va quand même tester des compétences techniques et t’a capaciter d’adaptation mais globalement sur un plan technique, c’étais pas très différent de ce qu’on a pu faire pour le projet de S3.
En termes de compétences transversale, comme ce projet n’était de base pas le nôtre, il a fallu prendre le temps de comprendre le code qui a été réaliser, savoir qu’elle endroit il fallait modifier pour un changement précis. Tous ces points requièrent un minimum de technique et de compréhension pour bien prendre la main sur le projet. Le groupe avec lequel on a travaillé sur ce projet de S4 n’était pas le même avec qui j’ai effectué le projet de S3, donc là aussi il a fallu apprendre à travailler ensemble, s’adapter à une nouvelle méthodologie de travail, par exemple on a beaucoup fait d’appelle en vocal avec des partages d’écran afin que l’échange soit fluide et qu’on ait un visuel sur des points précis. Cette façon de travailler était selon moi très intéressante, la communication était tellement fluide que j’ai eu le sentiment que le projet a été réaliser rapidement sans difficulté.
Pour le BUT 3, je pense qu’il faudra que moi-même et ma future équipe de projet communique d’avantage comme on a pu le faire pour le projet de S4, pour mon projet de S3, le manque de communication s’est fait ressentir et il y avait un manque de compréhension sur la répartition des tâches. Une bonne communication et répartition des tâches facilite la réalisation du projet et donne même envie de fournir les efforts et de travailler pour bien réaliser le projet d’un point de vue individuel mais aussi collectif. Ce projet de S4 a été placer après le stage dans un timing très serrer en vue de la fin d’années et le fait que ce soit la suite du projet de S3 ne nous a pas vraiment motiver à travailler d’arrache pieds pour la réalisation de ce projet, à l’avenir peu importe la situation, il faudra qu’on soit d’avantage motiver pour travailler et réaliser les projets demander.""",
                    "icone": "fa-chart-line",
                    "tags": [
                        {"nom": "Python", "icone": "fa-brands fa-python"},
                    ],
                    "lien_github": "https://github.com/yunes-bouabta/S401"
                }
            ]
        },
        {
            "id": "stage",
            "titre": "Bilan de mon Stage",
            "nav_titre": "Stage",
            "contenu": """Pour ce stage, j’ai travaillé dans le service informatique d’une entreprise de flocage et de textile et comme mission, j’ai développer de nouvelles fonctionnalités pour le site de l’entreprise, avoir un visuel sur les factures avec des tableau et graphique, une page de suivi sur la livraison des colis qu’il effectue pour leurs clients ou encore une page de gestion de leurs logo qu’il réalise pour le flocage et la broderie des vêtements pour les clients. ça a été un stage particulier pour moi, les méthode de travail de l’entreprise était peu spécial, être plusieurs dans la même pièce à travailler sur la même table toute la journée m’a un peu perturbé mais cela reste tout de même une expérience de travaille à en tirer. La communication en entreprise est quelque chose de crucial, communiquer avec mes collègues stagiaires m’a beaucoup aidé pour résoudre les problèmes que je rencontrais lors de la réalisation de mes tâches.
Sur les compétences techniques, ce stage m’a permis de coder avec le langage de programmation PHP que je connaissais déjà mais avec un méthode différente, la méthode PDO, j’ai appris à coder avec la méthode PDO et implémenter mon code avec la technique AJAX pour que mes requêtes soient plus fluide. Les 8 semaines de pratique m’ont vraiment permis de renforcer mes compétences et permis de découvrir de nouvelle manière de coder afin que ce soit plus fluide et efficace. Les missions que l’entreprise m’a confiées ont été réalisées avec succès.
Sur les compétences transversales, ce stage m’a permis de plus communiquer avec les autres, la communication a été essentielle pour la réussite de mes missions. Malgré le fait qu’on n'était pas sur les mêmes missions, mes collègues stagiaires m’ont été d’une grande aide pour résoudre les points de blocages que je rencontrais pendant ce stage. Sans eux, le stage aurait été plus compliqué et même sur l'aspect de l’ambiance, c’est plus agréable de travailler avec des personnes avec qui on peut communiquer.
"""
        },
        {
            "id": "objectifs",
            "titre": "Mes Objectifs",
            "nav_titre": "Objectif futur",
            "contenu": """Mes objectifs sont dans un premier temps de valider mon BUT informatique, j’aimerais bien pour mon stage de troisième années faire un stage en Typescript pour voir si c’est vraiment un langage qui puisse me plaire pour mon futur, j’ai passer beaucoup de temps à faire des recherche sur le langage et les débouchés que ça peut m’apporter de me spécialiser sur ce langage, il ne manque plus que de l'expérience en entreprise avec ce langage pour me fixer sur ça.
Par la suite, j’aimerais continuer mes études vers un Master, je ne sais pas encore quel Master précisément mais je ne souhaite pas m'arrêter avec un BAC +3, je veux mettre le plus de chance de mon côté pour trouver un bon emploi en fin d’étude même si ça va me prendre plus de temps, un BAC +5 serait l’idéal pour moi. Comme pour le stage de troisième années, une alternance avec une entreprise qui code en Typescript serait l'idéal, avoir plus d'expériences et de compétences sur ce langage serait bénéfique pour moi.
En sortie d’études, un emploi en tant que Développeur Web Full Stack est certainement la voie que je prendre, je ne sais pas encore sur quel langage et avec quel technologie, je prendrai le temps de me fixer là dessus avec mes expériences professionnel et recherche personnel.
Je ne sais pas si c’est quelque chose que je vais faire toute ma vie, je ne suis pas le genre de personne qui prévoit son futur sur du long terme, je pense que mes expériences en étude et post étude vont m’aider sur ce point mais ce qui est sûr, c’est qu'à l'heure actuelle, je me vois continuer dans le monde du  développement car coder est vraiment quelque chose que j’aime faire."""
        }
    ]
}

# --- CONTRÔLEUR ---
@app.route('/')
def index():
    return render_template('index.html', data=portfolio_data)

if __name__ == '__main__':
    app.run(debug=True)