# 📝 Django To‑Do List — Vision & Plan de Développement

## 🎯 Vision & périmètre

### But

Une app web où chaque utilisateur peut :

* Créer un compte et se connecter
* Gérer ses tâches : créer, lister, filtrer, marquer “fait”, modifier, supprimer

### Fonctionnalités indispensables (MVP)

* Authentification (inscription, connexion, déconnexion)
* CRUD tâches (titre, description optionnelle, statut fait/non fait)
* Liste filtrable/cherchable, tri basique
* Sécurité : un utilisateur ne voit que **ses** tâches

### Critères de réussite

* Un utilisateur part de zéro → s’inscrit → crée 3 tâches → en termine 1 → retrouve ses tâches après reconnexion
* Aucune tâche d’un autre utilisateur n’est visible ou modifiable
* Les erreurs courantes affichent des messages clairs (ex. champs requis)

---

## 🧭 Phase 1 — Préparation

### Organisation du dépôt

* Créer un repo Git (branche `main`, branches `feature/*`, PR simples)
* Ajouter un fichier `README` (objectif, installation, lancement, comptes de test)
* Ajouter un fichier `LICENSE` (si besoin) et `.gitignore` (venv, pycache, etc.)

### Environnement

* Créer un environnement virtuel Python propre
* Créer un fichier `requirements.txt` pour figer les dépendances
* Décider la version Django (stable récente)

### Conception rapide

* Schéma des entités : `User` natif + `Task(user, title, description?, completed, created_at)`
* Parcours utilisateur (user flow) : *sign-up → login → liste → créer → marquer fait → modifier → supprimer*
* Wireframe très simple des 3 vues : liste, formulaire, confirmation suppression

**Livrables** : README initial, plan des écrans (même griffonné), diagramme simple du modèle
**Go/No-Go** : périmètre validé, repo prêt, environnement fonctionnel

---

## 🧱 Phase 2 — Démarrage projet Django

### Initialisation

* Créer projet Django + app `tasks`
* Activer l’app dans la config, activer les templates & fichiers statiques

### Paramètres clés

* Définir les URLs de base (inclusion routes app)
* Réglages d’auth (login/logout redirect)
* Emplacements `templates/` et `static/`

**Livrables** : arborescence projet propre, serveur qui démarre
**Go/No-Go** : page d’accueil “hello” minimaliste qui s’affiche

---

## 🧬 Phase 3 — Données & Admin

### Modèle

* Créer le modèle `Task` avec les champs définis + relation à `User`

### Migrations

* Générer et appliquer les migrations en local

### Admin

* Enregistrer `Task` dans l’admin
* Configurer listes/filtre/recherche pour accélérer les tests

**Livrables** : base de données initialisée, admin accessible, création de tâches depuis l’admin
**Go/No-Go** : on peut créer/voir des `Task` en admin sans erreur

---

## 🧭 Phase 4 — Authentification (UX minimale)

### Pages d’auth

* Ajouter routes `login`, `logout`, `signup` (inscription via formulaire natif)
* Définir redirections cohérentes (après login, aller sur la liste des tâches)

### Protection

* Protéger les vues de l’app avec `login_required`
* Navigation : si non connecté → rediriger vers login

**Livrables** : inscription, connexion, déconnexion opérationnelles
**Go/No-Go** : nouvel utilisateur peut s’inscrire et arriver sur la liste (vide)

---

## 🧰 Phase 5 — Vues métier (CRUD)

### Liste

* Lister uniquement les tâches de l’utilisateur connecté
* Ajouter recherche par mot-clé
* Ajouter filtre “toutes / à faire / terminées”
* Tri : non faites d’abord, puis plus récentes

### Créer / Modifier

* Formulaire unique (création & édition)
* Affecter automatiquement `user = utilisateur connecté`

### Bascule fait/non fait

* Action rapide pour inverser l’état d’une tâche

### Supprimer

* Page de confirmation avant suppression

**Livrables** : toutes les routes CRUD fonctionnelles et testées à la main
**Go/No-Go** : parcours complet CRUD sans toucher l’admin

---

## 🎨 Phase 6 — Templates & UI

### Base layout

* Gabarit `base` (header avec liens auth, zone messages, container)

### Pages

* Liste (table/ul + actions)
* Formulaire (labels clairs, messages d’erreurs)
* Confirmation suppression
* Login / Signup minimalistes mais propres

### Style

* Framework CSS (ex. Bootstrap) ou CSS léger maison
* Messages flash (succès/erreur/info) visibles

**Livrables** : UI propre, accessible, cohérente
**Go/No-Go** : test UX “5 minutes” : on comprend tout sans explication

---

## 🛡️ Phase 7 — Sécurité & protection des données

**Checklist impérative :**

* Chaque `read/update/delete` filtre par `user=request.user`
* Les vues utilisent une récupération sécurisée (404 si objet d’autrui)
* CSRF activé sur tous les formulaires
* Pas d’infos sensibles dans les messages d’erreur
* `DEBUG=False` uniquement en prod (on garde `True` en local)

**Livrables** : revue sécurité, tests manuels multi-comptes
**Go/No-Go** : impossible d’accéder aux tâches d’autrui (même en forgeant l’URL)

