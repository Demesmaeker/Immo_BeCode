
# Objectif de la collecte de données : 

  1) Collecter autant de donnée que possible sur le marché Belge de la vente de maison / appartement
  2) Mettre en place une routine pour mettre à jour les données disponibles
  3) Vérifier qu'un même lien n'a pas été utilisé plusieurs fois

=> Sortir un fichier CSV contenant les données non triée (le plus brut possible)

## plan

![https://github.com/Demesmaeker/Immo_BeCode/blob/master/Collect%20Data.svg](https://github.com/Demesmaeker/Immo_BeCode/blob/master/Collect%20Data.svg)


# Collecter les données :

Pré-requis : sélectionner les données que l'ont veut récupérer.

| Données de base  | | Localisation|| Description du bien || Énergie| 
| ------------- |-------------|-------------|-------------|------------- |-------------|-------------| 
|Le prix|| Code postal|| Largeur de la façade ||Raccordement à l'égout| 
|Type de bien|| Nom de la rue || Nbr de salle de bain ||Eau, gaz & électricité| 
|La superficie du bien|| Numéro de la maison|| Nbr de toilettes ||Valeur du PEB| 
|État du bien|| Nom de la ville|| Nbr de bureau||Emission CO²| 
|Jardin (oui/non)|| Province|| Grenier (oui/non)||Type de chauffage| 
|Superficie du jardin|| Région|| Superficie du grenier ||Double vitrage| 
|Terrace (oui/non)|||| Superficie des chambres||| 
|Superficie de la terrace|||| Nbr de cave||| 
|Nombre de chambre||||Superficie de la cave ||| 
|Orientation de la terrasse||||Veranda (oui/non)|
| Année de construction | |||Superficie de la veranda|

| Suivit et actualisation des données |
| ------------- |
| Url de l'annonce |
| Date de création de l'annonce |
| Date d'expiration de l'annonce |
| Date d'enregistrement des données  |

Vincent : je pense qu'il faut donner une valeur par défaut différent de None ou 0 pour différencier une donnée non trouvée d'une donnée.
Qu'en pensez-vous ?

Chaque variable de type string aura "No value found" par defaut

Chaque variable de type int aura -1 par defaut

Chaque variable de type date aura 01/01/0001 par defaut

https://docs.google.com/document/d/1VbQlBBeQW9jCXNs_zTQ9vKxIA98yAnGEzPghZ5jW6vo/edit?usp=sharing

## A) En scrappant des sites web

Mise en commun des 3 projets. Quels étaient les points fort de chacun ?

  - Immo/Zimmo/immo.vlan

Rappel des étapes :

- Liste d'url de bien en vente
- Scrapper la page d'un bien
- Vérifier que l'url n'a pas déjà été scrappée ( Comment savoir s'il y a eu un update des données ?)
- Scrapper toutes les url

## B) En trouvant des API

A discuter. Est-ce qu'on va passer du temps la dessus ?
L'un n'empêche pas l'autre.

brouillon 

  - Terrains à bâtir ?
  
 
