# 📘 Guide de Projet : Application de Paris Sportifs (« Paris Entre Amis »)

Ce projet consiste à développer une application Web de gestion de paris sportifs simplifiée, fonctionnant comme un tableau de bord partagé. Afin de se concentrer sur l'architecture et le flux de données, le système d'authentification est exclu du périmètre. L'identification des utilisateurs se fera par la saisie libre d'un pseudonyme lors de chaque action.

---

## 🎯 Objectifs Principaux

* **Interconnecter** les composants d'une architecture full-stack moderne (Nuxt, FastAPI, PostgreSQL).
* **Consommer une API REST externe** pour récupérer, store et mettre à jour des données en temps réel.
* **Assurer la persistance des données** dans une base de données relationnelle.
* **Gérer le cycle de vie de la base de données** à l'aide d'un outil de migration (Alembic).
* **Auto-générer une documentation d'API interactive et moderne** avec Scalar via `scalar-fastapi`.
* **Virtualiser l'environnement de données** via Docker pour garantir la portabilité du projet.

---

## 🛠️ Stack Technique

* **Infrastructure :** Docker
* **Base de données :** PostgreSQL `timescaledb`
* **Gestion des Migrations :** Alembic
* **Back-end :** Python (FastAPI) & Scalar (Documentation API via `scalar-fastapi`)
* **Front-end :** Nuxt 3 (Vue.js + Nuxt Core)

---

## 🏗️ Phase 1 : Infrastructure, Base de Données, Migrations et Récolte

*L'objectif de cette phase est de mettre en place l'environnement de stockage, d'initialiser le système de gestion de versions de la base de données, et de créer le script Python capable de la populer avec des données réelles.*

### 1.1 L'environnement de données (Docker & Postgres)
* **Objectif :** Initialiser la base de données de manière isolée. `FAIT`
* **Livrable :** Un fichier `docker-compose.yml` configuré pour lancer un conteneur PostgreSQL. `FAIT`

### 1.2 Schéma et Migrations (Alembic & SQLAlchemy)
* **Objectif :** Déclarer les modèles Python et gérer les versions de la base de données sans utiliser le mode automatique destructif (`create_all`).
* **Livrable :** Un environnement Alembic initialisé générant le premier fichier de migration pour créer les tables nécessaires, appliqué avec succès sur le conteneur PostgreSQL.

### 1.3 Le script de récolte et de stockage (Python & API Externe)
* **Objectif :** Automatiser la récupération des événements sportifs.
* **Livrable :** Un script Python autonome utilisant la bibliothèque `requests` pour interroger l'API publique *TheSportsDB*. Les données récupérées (matchs, scores actuels, statuts des matchs) doivent être insérées dans la base PostgreSQL.

---

## 🧠 Phase 2 : L'API REST & Documentation Interactive (FastAPI & Scalar)

*L'objectif de cette phase est de concevoir le serveur d'API servant de passerelle entre la base de données, l'API externe et l'interface utilisateur, tout en exposant une documentation Scalar moderne.*

### 2.1 Création des endpoints de lecture, d'écriture et de clôture
* **Objectif :** Rendre les données accessibles et implémenter la logique métier du calcul des paris.
* **Livrables :** Quatre routes principales avec validation stricte des données entrantes (via Pydantic) :
    * `GET /matches` : Lit la base PostgreSQL et renvoie la liste des matchs.
    * `POST /bets` : Reçoit un pronostic (pseudo, identifiant du match, choix, mise) et l'insère en base de données avec le statut par défaut `En cours`.
    * `GET /bets` : Renvoie l'historique de tous les paris enregistrés.
    * `POST /matches/settle` : Réinterroge l'API externe pour obtenir les scores finaux, clôture les matchs et met à jour le statut des paris concernés (`Gagné` ou `Perdu`).

### 2.2 Documentation Auto-générée avec `scalar-fastapi`
* **Objectif :** Remplacer l'interface Swagger par défaut de FastAPI par Scalar pour offrir une documentation interactive et un client de test d'API plus esthétique et professionnel.
* **Livrable :** Une route `/scalar` exposant l'interface HTML de Scalar permettant de visualiser et de tester en direct les 4 endpoints.

---

## 🎨 Phase 3 : L'Interface Utilisateur (Nuxt 3)

*L'objectif de cette phase est de développer l'application cliente en utilisant l'architecture basée sur les fichiers de Nuxt 3 pour rendre le projet interactif.*

### 3.1 Le Tableau de Bord Full-Stack
* **Objectif :** Connecter le visuel aux données du Back-end en profitant des fonctionnalités de récupération de données de Nuxt (`useFetch`).
* **Livrables :** Une application Nuxt 3 structurée :
    * Une page principale `app.vue` ou `pages/index.vue` orchestrant l'affichage.
    * Un affichage des matchs sous forme de cartes avec un badge visuel pour le statut (En cours / Terminé).
    * Un formulaire de saisie réactif pour l'enregistrement d'un pari.
    * Un bouton global "Mettre à jour les résultats" qui déclenche l'appel vers la route `POST /matches/settle`.
    * Un tableau listant l'ensemble des paris, appliquant un code couleur selon leur état (`Gagné`, `Perdu`, `En cours`).

---

## 🏁 Critères de Validation

Le projet sera considéré comme finalisé lorsque le scénario suivant sera opérationnel :
1. L'interface Nuxt 3 affiche les matchs récupérés et stockés en base.
2. Un utilisateur peut soumettre un pari via le formulaire dédié.
3. La documentation de toutes les routes est accessible, moderne et testable depuis l'interface `/scalar`.
4. L'action sur le bouton de mise à jour synchronise les scores finaux et actualise visuellement les paris en `Gagné` ou `Perdu`.
5. **Test de persistance :** Après un arrêt et un redémarrage complet des services, l'intégralité des données reste accessible et inchangée.
