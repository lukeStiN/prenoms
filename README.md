# Tendance Prénoms

Cette application Streamlit analyse et visualise les données sur les prénoms des bébés en France. 
Les données incluent le nombre de naissances pour chaque prénom par année et par sexe.

## Fonctionnalités

### Page d'Accueil
- **🔍 Entrer un prénom** pour rechercher ses statistiques.
- **👧🏻 Afficher les prénoms féminins les plus populaires pour 2022**.
- **👦🏻 Afficher les prénoms masculins les plus populaires pour 2022**.
- **📅 Voir les prénoms les plus populaires pour une année sélectionnée**.

### Page de Recherche
- **🔎 Rechercher un prénom spécifique** pour voir ses statistiques de naissance.
- **📅 Ajuster la plage d'années** à l'aide d'un curseur.
- **📊 Afficher le nombre de naissances pour le prénom spécifié** avec un graphique en aires.

## Lien de Visualisation

Vous pouvez accéder à l'application via le lien suivant : [Tendance Prénoms](https://prenoms-fr.streamlit.app/)

## Données INSEE

Les données utilisées dans cette application proviennent de l'INSEE et incluent les prénoms attribués aux enfants nés en France entre 1900 et 2022. Les données avant 2012 concernent uniquement la France hors Mayotte. Chaque enregistrement contient le prénom, l'année de naissance, le sexe de l'enfant, et le nombre de naissances pour ce prénom.

### Avertissement

Les données sont basées sur les bulletins de naissance transmis à l'INSEE par les communes. L'exhaustivité n'est pas garantie, surtout pour les années antérieures à 1946. Des écarts peuvent exister par rapport au nombre de naissances annuel évalué par l'INSEE. Ces écarts diminuent après 1946.

### Précisions

- Les prénoms sont enregistrés tels que déclarés par les parents. 
- Les prénoms rares et les années où un prénom a été attribué moins de 3 fois sont regroupés sous des enregistrements spécifiques.
- Les personnes prises en compte sont celles nées en France et enregistrées à l'état civil, y compris Mayotte à partir de 2013. Les personnes nées à l'étranger sont exclues.

### Conditions d'inclusion des prénoms

1. De 1900 à 1945 : un prénom doit avoir été attribué au moins 20 fois.
2. De 1946 à 2022 : un prénom doit avoir été attribué au moins 20 fois.
3. Pour une année donnée : un prénom doit avoir été attribué au moins 3 fois.

### Source des Données

Ces fichiers proviennent de l'état civil et peuvent être consultés sur le site de l'INSEE : [INSEE - Prénoms](https://www.insee.fr/fr/statistiques/7633685).
