
Pour tout ce qui touche à la collecte de donnée

# Objectif de la collecte de données : 

  1) Collecter autant de donnée que possible sur le marché Belge de la vente de maison / appartement
  2) Mettre en place une routine pour mettre à jour les données disponibles





## plan

![https://github.com/Demesmaeker/Immo_BeCode/blob/master/Collect%20Data.svg](https://github.com/Demesmaeker/Immo_BeCode/blob/master/Collect%20Data.svg)


# Collecter les données :

Pré-requis : Définir une class contenant comme variable chaque donnée que l'on peut trouver sur un bien

| Données minimum  | Données optionnelles | Données descriptives | Données temporelles |
| ------------- | ------------- |------------- |------------- |
| Le prix  | Année de construction |  Surface du salon | date de creation du bien sur le site web
| La superficie du bien  | Parkings extérieurs  |   |date d’expiration de la page
| État du bien | Largeur de la façade | Nombre de sale de bain  | date d'enregistrement de la donnée
| Nombre de chambre | Type de cuisine |  Nombre de toilettes |
| Code postal | Nombre de façade | Surface des chambres   |
| Jardin (oui/non) | Surface du jardin  |  Nombre de buanderie |
| Terrace (oui/non) | Surface de la terrasse | Surface du bureau  |
|  | Rue & Numéro | Nombre de bureau  |
|  | garage | Surface du grenier  |
|  | surface du garage  | Raccordement à l'égout  |
|  |  | Eau, gaz & électricité |
|  |  |  Orientation de la terrasse |
|  |  | Consommation d'énergie primaire (PEB)  |
|  |  | Emission CO²  |
|  |  | Consommation théorique totale d'énergie primaire  |
|  |  | Type de chauffage  |
|  |  | Double vitrage  |
|  |  | Type de zone inondable	  |
|  |  |  grenier |
|  |  | veranda  |
|  |  | nb parkings (sans précision intérieur/extérieur)  |
|  |  |   |
|  |  |   |
|  |  |   |
|  |  |   |

Chaque variable de type string aura "No value found" par defaut

Chaque variable de type int aura -1 par defaut

Chaque variable de type date aura 01/01/0001 par defaut

## A) En scrappant des sites web

Mise en commun des 3 projets. Quels étaient les points fort de chacun ?

## B) En trouvant des API

A discuter. Est-ce qu'on va passer du temps la dessus ?
L'un n'empêche pas l'autre.

brouillon 

  - Immo/Zimmo/immo.vlan
  - recupération régulière des nouvelles données pour faire des analyses dans le temps
  - Données qu'on veut : date mise en vente, prix, type... ? EVERYTHING ! Identifier variables voulues, variables communes
  - Penser à collecter ok maps
  - Comment merger différents sites ?
  - Terrains à bâtir ?
  
 https://docs.google.com/document/d/1VbQlBBeQW9jCXNs_zTQ9vKxIA98yAnGEzPghZ5jW6vo/edit?usp=sharing
