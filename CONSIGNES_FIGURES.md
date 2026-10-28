# CONSIGNES DE CONCEPTION DES FIGURES VECTORIELLES SVG
## Projet : « LA CUISINE EXPLIQUÉE »

Ce document régit la production, la normalisation et la vérification de toutes les illustrations graphiques de l'ouvrage.

---

## 1. PRINCIPES GÉNÉRAUX ET EXIGENCE VECTORIELLE

1. **Aucun dessin en caractères ASCII ou boîte :** L'usage de caractères de traçage (`─ │ ┌ ▲ ► / \ ● ○ ■`) dans les blocs de texte est formellement interdit. Tout schéma, graphique thermique, diagramme de phase, structure moléculaire ou arbre décisionnel doit être un fichier SVG autonome.
2. **Autonomie et Compatibilité Typst :** Chaque fichier SVG doit être autonome :
   - Attributs `xmlns="http://www.w3.org/2000/svg"`, `viewBox="0 0 W H"`.
   - Pas de balises `<foreignObject>`, pas de feuilles de styles CSS externes, pas de polices distantes.
   - Polices système lisibles : `font-family="Liberation Sans, Arial, Helvetica, sans-serif"`.
   - Tailles de police : minimum `11px` pour les légendes secondaires, `13-14px` pour le corps de schéma, `16-18px` pour les titres d'axes ou de blocs.
   - Échappement rigoureux XML : `&` → `&amp;`, `<` → `&lt;`, `>` → `&gt;`.

---

## 2. PALETTE CHROMATIQUE OFFICIELLE

Toute illustration doit employer strictement la palette sémantique du projet :

| Rôle Sémantique | Code Hexadécimal | Variantes / Arrière-plans | Usage Culinaire |
| :--- | :--- | :--- | :--- |
| **Énergie Thermique / Chaleur** | `#dc2626` (Rouge) | `#ef4444` / Fond `#fef2f2` | Flamme, conduction, réaction de Maillard, protéines dénaturées, zone critique |
| **Eau / Milieu Hydrique** | `#2563eb` (Bleu roi) | `#3b82f6` / Fond `#eff6ff` | Eau libre, vapeur, bouillons, émulsion phase continue aqueuse |
| **Froid / Cristallisation** | `#0284c7` (Bleu cyan) | `#38bdf8` / Fond `#f0f9ff` | Réfrigérateur ($4^\circ\mathrm{C}$), glace ($0^\circ\mathrm{C}$), repos de viande, maintien du froid |
| **Lipides / Caramélisation** | `#d97706` (Ambre) | `#f59e0b` / Fond `#fffbeb` | Huile, beurre clarifié, micelles hydrophobes, sucres caramélisés, croûte dorée |
| **Acidité / Équilibre / Succès** | `#16a34a` (Vert émeraude) | `#22c55e` / Fond `#f0fdf4` | Acidité (citron/vinaigre), sel équilibré, lacto-fermentation saine, validation |
| **Encre / Métal / Parois** | `#0f172a` (Ardoise sombre) | `#334155` / Fond `#f8fafc` | Casserole, couteau, boîte, flèches d'axe, contours structurants |
| **Liaisons / Grille / Neutre** | `#94a3b8` (Gris ardoise) | `#cbd5e1` / `#e2e8f0` | Graduations de repère, séparateurs, grilles de fond |

---

## 3. ARCHITECTURE DES RÉPERTOIRES GRAPHIQUES

Les figures sont organisées par Livre thématique :
```text
figures/
├── livre_1/   (Thermodynamique, Outils minimaux, Flux de chaleur, Repos)
├── livre_2/   (Œuf anatomie, Coagulation fractionnée, Émulsions, Mousses)
├── livre_3/   (Cellules végétales, Pectine, Amidon, Caramélisation)
├── livre_4/   (Structure musculaire, Maillard, Collagène, Lipides)
├── livre_5/   (Osmose saline, Acidité ceviche, Activité eau aw, Pasteurisation)
└── annexes/   (Arbres de diagnostic, Thermomètre absolu des cuissons)
```

Chaque fichier est nommé de façon explicite : `fig_<chapitre>_<sujet>.svg` (ex. `fig_05_oeuf_anatomie_barriere.svg`, `fig_06_coagulation_temperature.svg`, `fig_07_micelle_emulsion.svg`).

---

## 4. TYPOLOGIE DES FIGURES ATTENDUES

1. **Diagrammes d'Énergie et Courbes Physico-Chimiques :**
   - Évolution de la température à cœur selon la géométrie et l'épaisseur (gradient de conduction thermique).
   - Cinétique de dénaturation des fractions protéiques de l'œuf en fonction de la température ($58^\circ\mathrm{C} \to 85^\circ\mathrm{C}$).
   - Diagramme d'activité de l'eau ($a_w$) vs prolifération bactérienne.
2. **Schémas Mécaniques et Moléculaires Didactiques :**
   - Anatomie de l'œuf : cuticule perméable au gaz, coquille poreuse, chambre à air, chalazes, albumen épais/fluide, membrane vitelline.
   - Micelle de lécithine : tête polaire hydrophile orientée vers l'eau, queue lipophile orientée vers la gouttelette d'huile.
   - Dénaturation et réseau fibrillaire : pelote repliée $\to$ déploiement $\to$ emprisonnement d'eau $\to$ surcoagulation et expulsion d'eau (synérèse).
3. **Arbres de Décision Opérationnels :**
   - Échec d'émulsion : cause $\to$ état du cul-de-poule $\to$ geste correctif immédiat.
   - Choix du mode de cuisson selon la teneur en collagène et le calibre de la pièce.
4. **Schémas de Gestes et d'Instruments :**
   - La prise en main ergonomique du couteau de chef (pincement de lame).
   - Les transferts thermiques dans une poêle en fonte épaisse vs aluminium mince.

---

## 5. PROCESSUS DE VALIDATION

Tout SVG créé doit faire l'objet d'une double vérification :
1. **Validation syntaxique XML :** Analyse avec un parseur XML (`xml.etree.ElementTree` en Python) pour garantir l'absence d'erreurs de syntaxe ou de caractères non échappés.
2. **Validation par compilation Typst :** Intégration dans le moteur Typst sans avertissement ni débordement d'image.
