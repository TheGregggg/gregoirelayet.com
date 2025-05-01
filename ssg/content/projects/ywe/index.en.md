+++
title = "You Will Eat : A meal recommendation system that considers physical activities for students"
date = 2025-05-01
[extra]
short_description = "You will Eat est un projet universitaire réalisé lors de l’année 2023-2024 dans le cadre de la Conférence PeiP 2024. YWE est une application de recommandation de repas prenant en compte vos goûts, vos dépenses énergétiques et la salubrité des plats."

image = "projects/ywe/banniere_ywe.png"
image_alt = ""

technologies = ["Flutter", "FastAPI", "ESP32", "BLE", "Ansible"]
links = ["https://polytech.univ-nantes.fr/fr/une-ecole-sur-3-campus/actualites/la-conference-peip-2024"]
repo_link = ""
+++

You will Eat est un projet universitaire réalisé lors de l’année 2023-2024 dans le cadre de la Conférence PeiP 2024. YWE est une application de recommandation de repas prenant en compte vos goûts, vos dépenses énergétiques et la salubrité des plats. L’application communique avec un serveur où est exécuté l’algorithme de recommandation et où est stockée les données. La communication entre les deux est réalisée par une API FastAPI. Des tests unitaires et déploiement automatique avec ansible ont été mis en place pour le code de l’API. L'application est en Flutter. L’application communique avec une montre connectée estimant les dépenses énergétiques en Bluetooth low energy. La montre est un ESP32 avec un accéléromètre et un écran.

L’algorithme de recommandation et les notions nutritionnelles utilisées dans le programme sont basés sur de multiples papiers scientifiques et nutritionnistes.

J’ai été le chef de projet et j’ai géré 11 autres personnes pour le bon développement de YWE ainsi qu’une partie du développement informatique.