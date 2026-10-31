# CONSIGNES DE CONCEPTION DES FIGURES VECTORIELLES SVG & NORMES ICONOGRAPHIQUES
## Projet : « LA CUISINE EXPLIQUÉE — Principes Premiers, Maîtrise de la Matière et Minimalisme Instrumental »

> **NOTE D'INTÉGRATION :** Ce document a été consolidé et fusionné directement au sein du manifeste maître **`AGENTS.MD`** (voir la **Section 5 : Consignes de Conception des Figures Vectorielles SVG & Normes Iconographiques**). Il est conservé ici comme mémento technique direct pour les opérations de génération et de vérification graphique.

---

## 1. PRINCIPES GÉNÉRAUX & EXIGENCE VECTORIELLE

1. **Aucun dessin en caractères ASCII ou boîte :** L'usage de caractères de traçage (`─ │ ┌ ▲ ► / \ ● ○ ■`) dans les blocs de texte est formellement interdit. Tout schéma, graphique thermique, diagramme de phase, structure moléculaire ou arbre décisionnel doit être un fichier SVG autonome ou un tableau Typst structuré.
2. **Autonomie et Compatibilité Typst :** Chaque fichier SVG doit être autonome :
   - Attributs obligatoires : `xmlns="http://www.w3.org/2000/svg"`, `viewBox="0 0 W H"`.
   - Pas de balises `<foreignObject>`, pas de feuilles de styles CSS externes, pas de polices distantes.
   - Polices système lisibles : `font-family="Liberation Sans, Arial, Helvetica, sans-serif"`.
   - Tailles de police : minimum `11px` pour les légendes secondaires, `13-14px` pour le corps de schéma, `16-18px` pour les titres d'axes ou de blocs.
   - Échappement rigoureux XML : `&` → `&amp;`, `<` → `&lt;`, `>` → `&gt;`.

---

## 2. PALETTE CHROMATIQUE OFFICIELLE DU PROJET

Toute illustration technique doit employer strictement la palette sémantique du projet :

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

## 3. DIMENSIONNEMENT ET GESTION DES SAUTS DE PAGE

Pour garantir un flux continu sans vides béants dans Typst :
- **Photographies de recettes (`figures/nourriture/`) :** Hauteur maximale contrainte à **`23%`** de la hauteur de page (`width: 85%`, `fit: "cover"`).
- **Schémas SVG :** Hauteur maximale contrainte à **`30% à 32%`** (`fit: "contain"`).
- **Portraits historiques :** Hauteur maximale contrainte à **`35%`**.
- **Images d'ouverture de Livre :** Présentation noble sans rognage (`width: 92%`, `height: 74%`, `fit: "contain"` sur fond noir `#1c1917`).

---

## 4. PROCESSUS DE VALIDATION TECHNIQUE

1. **Validation syntaxique XML :** Analyse avec un parseur XML (`xml.etree.ElementTree` en Python).
2. **Validation des magic bytes :** Contrôle des en-têtes binaires (JPEG `\xff\xd8`, PNG `\x89PNG`).
3. **Compilation Typst :** Vérification avec code de retour 0 du script `scripts/build_book.py`.
