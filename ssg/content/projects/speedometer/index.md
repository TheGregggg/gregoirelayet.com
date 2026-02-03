+++
title = "Création d'un compte tour pour le simracing"
date = 2025-11-01
draft = true
[extra]
short_description = "You will Eat est un projet universitaire réalisé lors de l’année 2023-2024 dans le cadre de la Conférence PeiP 2024. YWE est une application de recommandation de repas prenant en compte vos goûts, vos dépenses énergétiques et la salubrité des plats."

image = "projects/ywe/banniere_ywe.png"
image_alt = ""

technologies = ["C", "Arduino", "Modélisation 3D"]
links = []
repo_link = "https://github.com/TheGregggg/arduino-speedometer"
+++


J'avais envie d'améliorer mon expérience de simracing en créant un compte tour analogique. l'idée est d'avoir un cadran ressemblant a une voiture et qui permet d'avoir le nb de tour et aussi de rajouter un compteur de vitesse.
l'objectif est de permettre une meilleure immersion tout en permettant d'enlever ces informations sur l'écran et de gagner en visibilité dans le jeu.
Le système a concevoir prend pour entrer les informations du jeu vidéo. En sortie il amène un feedback réel avec une aiguille pour le compte tour et un nombre pour la vitesse.

Les différents contraintes sont les suivantes :
fréquence de rafraîchissement de la sortie suffisamment rapide pour une utilisation reel.
affichage du compte tour avec une aiguille dans un cercle.
affichage de la vitesse par un nombre.
affichage visible et lisible à 1m de distance.
fonctionner avec forza et asseto corsa.
utilisation des pièces que je possède, je veux acheter aucune pieces pour réaliser se projet.

Caractérisation fonctionnelle
Dans un premier temps, le système doit réaliser l'acquisition des données du jeu et les traités pour récupérer uniquement les informations nécessaires (nb de tour/min et vitesse). Par la suite, afin de permettre une réponse dans le monde réel, il est clair qu'une conversion est nécessaire, prenant les informations filtré en entrée et permettant l'affichage à l'utilisateur en sortie.

Cela permet d'établir deux bloc : acquisition et affichage.

##Caracterisation des solutions techniques
Bloc acquisition
Pour récupérer les données du jeu et les traités pour obtenir uniquement le compte tour et la vitesse, une application software suffit. Il est nécessaire d'adapter l'acquisition à chaque jeu.

Bloc Affichage
Le cahier des charges impose la forme de l'information à afficher. Une aiguille pour le compte tour et un nombre pour la vitesse.

Un servo moteur est utilisable pour réaliser le compte tour. il répond au cahier des charges. L'angle de l'aiguille contrôler par le servo ne peut donc que être de 180 degré maximum, cela est un compromis que l'on doit réaliser. Il est possible d'obtenir un compte tour similaires z une vrai voiture en ayant un angle de 270 deg max. Cependant pour arriver a cela avec un servl il faudrait utiliser des mécanismes plus complexes comme des engrenages avec démultiplication ou un servo 360 degré avec un mécanisme de détection de l'aiguille a une certaine position de référence. L'objectif du projet est d'utiliser les pièces à disposition et de rester fiable et simple. les solutions plus complexes nécessitant plus de pieces sont donc écarté.

Le servo utiliser est un : . Sa vitesse est de :. Pour passer de 0 a 180 degré, cela prend X seconds. A titre de comparaison, une Mazda 787b en pleine accélération passe de 800 au maximum du compte tour en X secondes.
Le servo utilisé est suffisamment rapide pour être utilisé en temps réel.

Pour afficher la vitesse, il est tout à fait convenable d'utiliser un afficheur 7 segments 4 chiffres. Le modèle utilisé est un : . Un test de lisibilité a permis de déterminer que cette piece est suffisante et réalise parfaitement l'affaire la vitesse.

Une interface de contrôle est nécessaire pour contrôler le servo et l'afficheur. Pour cela une Arduino Uno sera utilisé.

De plus, pour apprendre le fonctionnement d'un serial in parralel out shift register, je vais utiliser un (JSP) avec l'afficheur. Cela a pour objectif de réduire le nombre de pin utilisé sur le microcontrôleur. Cela est purement à but éducatif, car l'Arduino uno possède assez de pin pour utiliser l'afficheur sans le shift register. Dans ce cas, je vais utiliser le shift register pour les 7 LEDs d'un chiffre et une LED pour le point (donc 8 output du microcontrôleur). Cela va permettre de contrôler un chiffre de l'afficheur avec uniquement une communication série uni-directionnel asynchrone par 2 outputs : DATA et CLK.

La communication serie sera utilisée pour la communication entre le logiciel sur l'ordinateur et l'arduino. Il sera nécessaire de tester une grande vitesse de transmission pour obtenir un transfert assez rapide.

Toutes ces pièces sont déjà présentes dans mes différents kits d'électronique, aucun achats n'est donc prévu !

Premier prototype
software et transmission de données
le software est réalisé en language C.
Dans un premier temps, les tests seront effectués sur le jeux Forza Horizon 4/5 car leur mécanisme pour accéder aux informations et relativement simple.
Il suffit d'indiquer l'adresse d'un serveur udp et le jeu va envoyer 60 fois par seconde les informations au serveur.

Le software est donc un serveur udp recevant les informations du jeu. Il faut ensuite récupérer les bons bytes du message pour obtenir la vitesse du véhicule et la vitesse de rotation du moteur. Beaucoups de traitement sont nécessaires.

En effet la vitesse est récupérée du jeu au format long float IEEE JSP, sur 4 bytes, et en mètre par seconde. Il faut donc le convertir en kilomètres heure. De plus, la vitesse d'un véhicule étant rarement supérieur a 1024 km/h, l'information peut être stocké sur 10 bits comme entier.

La vitesse de rotation du moteur est elle récupéré au format tour / min donc aucune convertion n'est nécessaire. Pour transmettre l'information sur un octet, il est nécessaire de down sampler l'information. Le choix a été fait de diviser par 100.
en effet, on peut aisément posé un maximum de 15000 tour minutes donc en divisant par 100 on arrive a 150. Cela tient sur une un octet.

Pour éviter les problèmes de communication entre l'ordinateur et le microcontrôleur, un flag de début et de fin de tram est envoyé.
Une tram est donc composé des éléments suivants :
octet de début = 255
octet partie haute vitesse
octet partie basse vitesse
octet compte tour
octet de fin = 254

L'utilisation de balises de début et de fin permet de s'assurer que tout les octets sont reçus. Si l'octet de fin n'est pas reçu au 4 octet après la balises de début, le paquet n'est pas compté et le buffer de communication série est vidé. Le but est d'éviter les décalages.
Ce procédé est nécessaire, sans celui-ci, les paquets se décaler à la moindre mauvaise transmission.

La vitesse étant codé sur 10 bits, ils sont divisés en deux mots de 5 bits ajusté à droite pour former deux mots de 8 bits. Le maximum de chaque mot est donc de 32.
Le maximum fixé pour le comte tour est de 150. Cela permet de s'assurer que les données ne peuvent pas être interprété comme des balises de début et de fin.

La fréquence de transmission des informations séries est fixé a 4 MHz sur le prototype. cette valeur est arbitraire mais permet un latence de transmission très faible.

Compte tenu de la fréquence élevée du microprocesseur et de la vitesse de transmission comparé au donné du jeu reçu à 60Hz, c'est cette fréquence qui dicte la latence du système.
Le système a donc une latence de 1/60 secondes.

Compte tour
Le contrôle du servo moteur est réalisé avec la librairie Servo.h pour le prototype.

Afficheur de vitesse