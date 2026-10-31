# -*- coding: utf-8 -*-
"""
Master Culinary Book Builder pour LA CUISINE EXPLIQUÉE — ÉDITION RÉVISÉE ET AUGMENTÉE
- Auteurs : Silvère-Martin Michiellot & Antigravity
- Moteur Typographique : Typst v0.15.1
- Moteur de conversion : Pandoc 3.12.1
- Architecture : Traité Magistral en Six Livres + Annexes (26 Chapitres, 26 Recettes Piliers)
- Grandes Ouvertures de Livre : Illustration pleine page sur page paire (verso) en regard du portail (recto)
- Photographies culinaires haute définition dédiées pour chaque recette
- Foliotage éditorial sans failles, zéro fausse page, navigation transversale interactive
"""

import os
import glob
import re
import subprocess
import sys

# Forcer l'encodage UTF-8 pour Windows PowerShell / CMD
if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if sys.stderr and hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEXTES_DIR = os.path.join(BASE_DIR, "textes")
FIG_DIR = os.path.join(BASE_DIR, "figures")

PANDOC_EXE = r"C:\Users\silve\AppData\Local\Pandoc\pandoc.exe"
TYPST_EXE = r"C:\Users\silve\AppData\Local\Microsoft\WinGet\Packages\Typst.Typst_Microsoft.Winget.Source_8wekyb3d8bbwe\typst-x86_64-pc-windows-msvc\typst.exe"

TEMP_MD = os.path.join(BASE_DIR, "temp_master_book.md")
TEMP_TYP = os.path.join(BASE_DIR, "temp_pandoc.typ")
FINAL_TYP = os.path.join(BASE_DIR, "LA_CUISINE_EXPLIQUEE.typ")
FINAL_PDF = os.path.join(BASE_DIR, "LA_CUISINE_EXPLIQUEE.pdf")

# ==============================================================================
# PRÉAMBULE TYPST HAUTE GASTRONOMIE
# ==============================================================================

PREAMBLE = """
#set document(
  title: "LA CUISINE EXPLIQUÉE — Édition Révisée et Augmentée",
  author: "Silvère-Martin Michiellot & Antigravity"
)

// Palette Chromatique "Haute Gastronomie & Matière Noble"
#let c-ink = rgb("#242124")        // Encre noire noble et chaude
#let c-charcoal = rgb("#383330")   // Anthracite profond
#let c-slate = rgb("#5c5549")      // Brun ardoise tiède
#let c-bordeaux = rgb("#701c1a")   // Bordeaux haute gastronomie
#let c-terracotta = rgb("#a3432b") // Terracotta noble
#let c-bronze = rgb("#d4a373")     // Or / Bronze laiton vieilli
#let c-cream = rgb("#fffdfa")      // Fond papier crème doux
#let c-sand = rgb("#f7f4eb")       // Lin doux
#let c-olive = rgb("#5a6e54")      // Vert laurier sourd
#let c-rust = rgb("#92400e")       // Ambre profond

// Saut vers la prochaine belle page (impaire) avec balisage des sections
#let recto() = {
  [#metadata("fin-section") <fin-section>]
  pagebreak(weak: true, to: "odd")
  [#metadata("debut-section") <debut-section>]
}

// Pied de page et en-tête
#let pied-livre = context {
  let p = here().page()
  let debut = query(<debut-texte>)
  if debut.len() > 0 and p >= debut.first().location().page() {
    let page-num = counter(page).get().first()
    align(center)[#text(font: "Liberation Serif", size: 9pt, fill: c-bordeaux)[— #page-num —]]
  }
}

#let entete-livre = context {
  let p = here().page()
  let debut = query(<debut-texte>)
  if debut.len() > 0 and p >= debut.first().location().page() {
    let is-h1 = query(selector(heading.where(level: 1))).any(h => h.location().page() == p)
    if not is-h1 {
      let cur-h1 = query(selector(heading.where(level: 1)).before(here()))
      let title-left = if cur-h1.len() > 0 { cur-h1.last().body } else { [LA CUISINE EXPLIQUÉE] }
      text(font: "Liberation Serif", size: 8.5pt, fill: c-bordeaux, tracking: 0.08em)[
        #smallcaps[#title-left] #h(1fr) #emph[La Cuisine Expliquée]
      ]
      v(-4pt)
      line(length: 100%, stroke: 0.5pt + c-bronze)
    }
  }
}

#set page(
  paper: "a4",
  margin: (top: 2.5cm, bottom: 2.5cm, left: 2.2cm, right: 2.2cm),
  header: entete-livre,
  footer: pied-livre,
  fill: rgb(255, 253, 250)
)

#set text(
  font: ("Liberation Serif", "Georgia", "Times New Roman"),
  size: 10pt,
  fill: c-ink,
  lang: "fr"
)

#set par(justify: true, leading: 0.75em, first-line-indent: 0pt, spacing: 0.88em)

#show heading: set text(hyphenate: false)
#show figure.where(kind: table): set block(breakable: true)
#show figure.caption: it => [
  #v(7pt)
  #text(size: 8.8pt, style: "italic", fill: c-slate, font: "Liberation Serif")[#it]
  #v(13pt)
]

// Hyperliens Interactifs
#show link: it => text(fill: c-terracotta, weight: "medium")[#underline(stroke: 0.5pt + c-bronze, offset: 1.5pt)[#it]]

// Macro d'Ouverture de Livre en Diptyque Noble : Page Paire (Image Pleine) + Page Impaire (Portail Titre)
#let portail_livre_verso(img_path, legende_image) = block(width: 100%, height: 100%, fill: rgb("#1c1917"))[
  #align(center + horizon)[
    #v(1.2cm)
    #image(img_path, width: 92%, height: 74%, fit: "contain")
    #v(0.6cm)
    #block(width: 86%, fill: none, inset: (x: 0cm, y: 0cm))[
      #align(left)[
        #text(size: 8.5pt, fill: c-bronze, font: "Liberation Sans", weight: "bold")[OUVERTURE ICONOGRAPHIQUE DU LIVRE]
        #v(3pt)
        #text(size: 9.5pt, fill: rgb("#e7e5e4"), font: "Liberation Serif", style: "italic")[#legende_image]
      ]
    ]
    #v(0.8cm)
  ]
]

#let portail_livre_recto(num_partie, titre, sommaire_contenu) = [
  #v(2.2cm)
  #align(left)[
    #text(size: 11pt, tracking: 0.25em, fill: c-bordeaux, font: "Liberation Sans", weight: "bold")[#smallcaps[#num_partie]]
    #v(0.6cm)
    #text(size: 22pt, weight: "bold", fill: c-ink, tracking: 0.02em, font: "Liberation Serif")[#titre]
    #v(0.8cm)
    #line(length: 25%, stroke: 1.2pt + c-bronze)
    #v(1.0cm)
    #block(
      width: 100%,
      inset: (left: 8pt)
    )[
      #set text(size: 11.5pt, fill: c-ink, font: "Liberation Serif")
      #set par(justify: false, leading: 1.0em)
      #sommaire_contenu
    ]
  ]
]

// Chapitres et Annexes en Style 1 (Le Grand Traité Étoilé, en haut de page, aligné à gauche)
#show heading.where(level: 1): it => {
  pagebreak(weak: true, to: "odd")
  v(0.3cm)
  align(left)[
    #text(size: 9pt, tracking: 0.2em, fill: c-bordeaux, weight: "bold", font: "Liberation Sans")[#smallcaps[Traité de Cuisine & de Physique Culinaire]]
    #v(5pt)
    #text(size: 18.5pt, weight: "bold", fill: c-ink, font: "Liberation Serif")[#it.body]
    #v(7pt)
    #line(length: 100%, stroke: 1pt + c-bronze)
    #v(0.35cm)
  ]
}

#show heading.where(level: 2): it => block(
  width: 100%,
  breakable: false,
  sticky: true,
  spacing: 1.4em
)[
  #v(0.35cm)
  #align(left)[
    #text(size: 13pt, weight: "bold", fill: c-bordeaux, font: "Liberation Serif")[#it.body]
    #v(4pt)
    #line(length: 100%, stroke: 0.6pt + c-bronze)
  ]
  #v(0.15cm)
]

#show heading.where(level: 3): it => block(
  width: 100%,
  breakable: false,
  sticky: true,
  spacing: 1.1em
)[
  #v(0.2cm)
  #align(left)[
    #text(size: 11pt, weight: "bold", fill: c-terracotta, font: "Liberation Serif")[#it.body]
  ]
  #v(0.1cm)
]

#show heading.where(level: 4): it => block(
  width: 100%,
  breakable: false,
  sticky: true,
  spacing: 0.8em
)[
  #align(left)[
    #text(size: 9.5pt, weight: "bold", fill: c-slate, font: "Liberation Sans")[#it.body]
  ]
]

// Signalétique Didactique et Boîtes Culinaires
#let truc_de_chef(body) = block(
  fill: rgb("#faf7f0"),
  stroke: (left: 3pt + c-bronze),
  inset: (left: 14pt, right: 12pt, top: 10pt, bottom: 10pt),
  radius: (right: 4pt),
  width: 100%,
  spacing: 1.2em,
  breakable: true
)[
  #set text(size: 10pt, fill: c-ink, font: "Liberation Serif")
  #set par(justify: true, leading: 0.78em)
  #body
]

#let anecdote_historique(body) = block(
  fill: rgb("#f7f5ef"),
  stroke: (left: 3pt + rgb("#a38c78")),
  inset: (left: 14pt, right: 12pt, top: 10pt, bottom: 10pt),
  radius: (right: 4pt),
  width: 100%,
  spacing: 1.2em,
  breakable: true
)[
  #set text(size: 10pt, fill: c-ink, font: "Liberation Serif")
  #set par(justify: true, leading: 0.78em)
  #body
]

#let positif(body) = block(
  fill: rgb("#f4f6f4"),
  stroke: (left: 3pt + rgb("#6e826b")),
  inset: (left: 14pt, right: 12pt, top: 10pt, bottom: 10pt),
  radius: (right: 4pt),
  width: 100%,
  spacing: 1.2em,
  breakable: true
)[
  #set text(size: 10pt, fill: c-ink, font: "Liberation Serif")
  #set par(justify: true, leading: 0.78em)
  #body
]

#let negatif(body) = block(
  fill: rgb("#fbf6f5"),
  stroke: (left: 3pt + rgb("#b06d60")),
  inset: (left: 14pt, right: 12pt, top: 10pt, bottom: 10pt),
  radius: (right: 4pt),
  width: 100%,
  spacing: 1.2em,
  breakable: true
)[
  #set text(size: 10pt, fill: c-ink, font: "Liberation Serif")
  #set par(justify: true, leading: 0.78em)
  #body
]

#let danger(body) = block(
  fill: rgb("#faf3f2"),
  stroke: (left: 3pt + c-bordeaux),
  inset: (left: 14pt, right: 12pt, top: 10pt, bottom: 10pt),
  radius: (right: 4pt),
  width: 100%,
  spacing: 1.2em,
  breakable: true
)[
  #set text(size: 10pt, fill: c-ink, font: "Liberation Serif")
  #set par(justify: true, leading: 0.78em)
  #body
]

#let alerte(body) = danger(body)

#let point_attention(body) = block(
  fill: rgb("#faf6ee"),
  stroke: (left: 3pt + c-terracotta),
  inset: (left: 14pt, right: 12pt, top: 10pt, bottom: 10pt),
  radius: (right: 4pt),
  width: 100%,
  spacing: 1.2em,
  breakable: true
)[
  #set text(size: 10pt, fill: c-ink, font: "Liberation Serif")
  #set par(justify: true, leading: 0.78em)
  #body
]

#let oeil_molecule(body) = block(
  fill: rgb("#f6f5f3"),
  stroke: (left: 3pt + c-slate),
  inset: (left: 14pt, right: 12pt, top: 10pt, bottom: 10pt),
  radius: (right: 4pt),
  width: 100%,
  spacing: 1.2em,
  breakable: true
)[
  #set text(size: 10pt, fill: c-ink, font: "Liberation Serif")
  #set par(justify: true, leading: 0.78em)
  #body
]

#let quote_box(body) = block(
  fill: rgb("#faf7f2"),
  stroke: (left: 3pt + c-bronze),
  inset: (left: 12pt, y: 7pt),
  radius: (right: 4pt),
  width: 100%,
  spacing: 1.1em,
  breakable: true
)[
  #set text(style: "italic", fill: rgb("#292524"), font: "Liberation Serif")
  #set par(justify: true, leading: 0.76em)
  #body
]

// ==========================================
// 1. COUVERTURE PHOTOGRAPHIQUE GASTRONOMIQUE
// ==========================================
#set page(margin: 0pt, header: none, footer: none)

#block(width: 100%, height: 100%, fill: rgb("#1c1917"))[
  #place(top + left)[
    #image("figures/nourriture/couverture_legumes_marche.jpg", width: 100%, height: 52%, fit: "cover")
  ]
  #place(bottom + left)[
    #block(
      fill: rgb("#1c1917"),
      width: 100%,
      height: 52%,
      inset: (x: 2.4cm, y: 1.8cm)
    )[
      #v(0.2cm)
      #text(size: 11pt, weight: "bold", fill: rgb("#fbbf24"), tracking: 3pt, font: "Liberation Sans")[
        SILVÈRE-MARTIN MICHIELLOT & ANTIGRAVITY
      ]
      #v(0.6cm)
      #text(size: 28pt, weight: "bold", fill: white, font: "Liberation Serif")[
        LA CUISINE EXPLIQUÉE
      ]
      #v(0.3cm)
      #text(size: 13.5pt, weight: "medium", fill: rgb("#fed7aa"), font: "Liberation Sans")[
        Principes Premiers, Maîtrise de la Matière et Minimalisme Instrumental
      ]
      #v(0.6cm)
      #line(length: 100%, stroke: 1.5pt + rgb("#f59e0b"))
      #v(0.5cm)
      #text(size: 10pt, fill: rgb("#e7e5e4"), font: "Liberation Serif", style: "italic")[
        Traité magistral d'anthropologie, de thermodynamique et de biologie du geste culinaire.\\
        Comprendre la matière brute, dompter le feu et cuisiner en toute liberté avec cinq instruments.
      ]
      #v(0.8cm)
      #grid(
        columns: (1fr, auto),
        align: (left + horizon, right + horizon),
        text(size: 9pt, weight: "bold", fill: rgb("#fcd34d"), font: "Liberation Sans")[
          ÉDITION RÉVISÉE ET AUGMENTÉE — 2026
        ],
        text(size: 8.5pt, fill: rgb("#a8a29e"), font: "Liberation Sans")[
          LICENCE LIBRE CC BY-SA 4.0
        ]
      )
    ]
  ]
]

#pagebreak()
#box()

#set page(
  paper: "a4",
  margin: (top: 2.5cm, bottom: 2.5cm, left: 2.2cm, right: 2.2cm),
  header: entete-livre,
  footer: pied-livre,
  fill: rgb(255, 253, 250)
)
#counter(page).update(1)

// PAGE 1 — FAUX-TITRE (MUETTE)
#align(center + horizon)[
  #text(size: 22pt, weight: "bold", fill: c-ink, font: "Liberation Serif", tracking: 0.06em)[LA CUISINE EXPLIQUÉE]
]
#pagebreak()
#box()
#pagebreak()

// PAGE 3 — GRAND TITRE (MUETTE)
#align(center)[
  #v(3.5cm)
  #text(size: 12pt, weight: "bold", fill: c-bordeaux, tracking: 0.15em, font: "Liberation Sans")[SILVÈRE-MARTIN MICHIELLOT & ANTIGRAVITY]
  #v(1.6cm)
  #text(size: 32pt, weight: "bold", fill: c-ink, font: "Liberation Serif")[LA CUISINE EXPLIQUÉE]
  #v(0.5cm)
  #line(length: 30%, stroke: 0.5pt + c-bronze)
  #v(0.5cm)
  #text(size: 14pt, fill: c-terracotta, font: "Liberation Serif", style: "italic")[Principes Premiers, Maîtrise de la Matière#linebreak()et Minimalisme Instrumental]
  #v(1fr)
  #text(size: 10pt, fill: c-slate, font: "Liberation Sans", tracking: 0.1em)[ÉDITION RÉVISÉE ET AUGMENTÉE — 2026]
  #v(0.2cm)
  #text(size: 9pt, fill: c-slate, font: "Liberation Sans")[Traité de référence libre sous licence Creative Commons CC BY-SA 4.0]
  #v(1.5cm)
]
#pagebreak()

// PAGE 4 — MENTIONS LÉGALES (MUETTE)
#align(bottom)[
  #block(
    fill: rgb("#fafaf9"),
    stroke: 0.5pt + rgb("#e7e5e4"),
    inset: 16pt,
    radius: 6pt,
    width: 100%
  )[
    #text(size: 8.5pt, fill: rgb("#57534e"))[
      *LA CUISINE EXPLIQUÉE — Principes Premiers, Maîtrise de la Matière et Minimalisme Instrumental*\\
      Édition Révisée et Augmentée © 2026 Silvère-Martin Michiellot & Antigravity.\\
      \\
      *Licence Libre :* Cet ouvrage est mis à disposition selon les termes de la licence *Creative Commons Attribution - Partage dans les Mêmes Conditions 4.0 International (CC BY-SA 4.0)*.\\
      *Composition typographique :* Typst v0.15.1, polices Liberation Serif & Sans.\\
      *Dépôt de code et figures sources :* Dépôt GitHub public sous licence CC BY-SA 4.0.\\
      *Avertissement d'homonymie :* Traité d'investigation scientifique, anthropologique et pratique indépendant.
    ]
  ]
]
#pagebreak()

// PAGE 5 — CITATION INAUGURALE (MUETTE)
#align(center)[
  #v(4.0cm)
  #block(
    fill: rgb("#fffbeb"),
    inset: 24pt,
    radius: 8pt,
    stroke: 1pt + rgb("#fde68a"),
    width: 85%
  )[
    #text(size: 11pt, style: "italic", fill: rgb("#451a03"))[
      « La cuisine est le plus ancien des arts ; car Adam naquit à jeun, et le nouveau-né, à peine venu au monde, pousse des cris que le sein de sa nourrice peut seul apaiser. C'est de tous les arts celui qui nous rend les services les plus continus et les plus nécessaires à la vie. »
    ]
    #v(8pt)
    #align(right)[#text(size: 9.5pt, weight: "bold", fill: c-terracotta)[— Jean Anthelme Brillat-Savarin, *Physiologie du goût* (1825)]]
  ]
  #v(2.5cm)
  #text(size: 10.5pt, style: "italic", fill: rgb("#78716c"))[
    À toutes celles et ceux qui désirent s'affranchir de la tyrannie des recettes aveugles,\\
    et retrouver la liberté souveraine de comprendre ce qu'ils font.
  ]
]
#pagebreak()
#box()
#pagebreak()

// SOMMAIRE GÉNÉRAL
#outline(
  title: [Sommaire Général et Table Raisonnée],
  indent: 1.5em,
  depth: 2
)

#recto()

// ==========================================
// TABLE DES VINGT-SIX RECETTES PILIERS
// ==========================================
#align(left)[
  #text(size: 15pt, weight: "bold", fill: c-bordeaux, font: "Liberation Serif")[
    🍳 Table des Vingt-Six Recettes et Préparations Piliers
  ]
  #v(-4pt)
  #line(length: 100%, stroke: 0.8pt + c-bronze)
]
#v(0.3cm)

#block(
  fill: rgb("#faf7f0"),
  stroke: 0.5pt + rgb("#dfdacf"),
  inset: 14pt,
  radius: 6pt,
  width: 100%
)[
  #text(size: 9.2pt)[
    Cette table réunit les vingt-six protocoles fondamentaux pas à pas décrits dans l'ouvrage. Chaque recette constitue une application directe et vivante des lois physiques, chimiques et biologiques exposées :

    #v(0.15cm)
    *1. Pâtes, Féculents & Protéines Végétales (Livre III)*
    - #link(<recette-carbonara-traditionnelle>)[*Fiche 01 :* Les Vraies Spaghetti alla Carbonara (L'Émulsion d'Or Jaune)] --- _Chapitre 09_
    - #link(<recette-dahl-lentilles>)[*Fiche 02 :* Le Dahl Réconfortant de Lentilles Corail au Cumin Torréfié & Coco] --- _Chapitre 09_
    - #link(<recette-tofu-croustillant>)[*Fiche 03 :* Le Tofu Doré Ultra-Croustillant & son Laquage Tamari-Sésame] --- _Chapitre 09_
    - #link(<recette-pommes-sarladaises>)[*Fiche 04 :* Les Pommes Sarladaises Croustillantes à la Graisse de Canard] --- _Chapitre 09_
    - #link(<recette-grand-aioli>)[*Fiche 05 :* Le Grand Aïoli Provençal au Mortier] --- _Chapitre 09_

    #v(0.12cm)
    *2. Mécanique Végétale, Turgescence & Salades (Livre III)*
    - #link(<recette-puree-blumenthal>)[*Fiche 06 :* La Purée Veloutée selon Blumenthal & Infusion des Épluchures] --- _Chapitre 10_
    - #link(<recette-carottes-glacees>)[*Fiche 07 :* Les Carottes Étuvées Glacées au Beurre sous Cartouche] --- _Chapitre 10_
    - #link(<recette-salade-croquante>)[*Fiche 08 :* La Salade Maraîchère Croquante, Bain Glacé & Vinaigrette] --- _Chapitre 11_

    #v(0.12cm)
    *3. L'Eau, Bouillons Nobles & Glaces de Viande (Livre III)*
    - #link(<recette-bouillon-glace>)[*Fiche 09 :* Le Grand Bouillon d'Or & sa Réduction en Glace de Viande] --- _Chapitre 12_
    - #link(<recette-consomme-clarifie>)[*Fiche 10 :* Le Consommé Limpide Clarifié à l'Albumine d'Œuf] --- _Chapitre 12_

    #v(0.12cm)
    *4. Saisies Animales, Maillard & Déglaçages (Livre III)*
    - #link(<recette-steak-fonte>)[*Fiche 11 :* Le Pavé de Bœuf Saisi en Fonte & Arrosé au Beurre Moussant] --- _Chapitre 14_
    - #link(<recette-deglacage-minute>)[*Fiche 12 :* Le Déglaçage Minute & Sauce Réduite au Vin Montée au Beurre] --- _Chapitre 14_
    - #link(<recette-ceviche-cabillaud>)[*Fiche 13 :* Le Vrai Ceviche de Cabillaud Mariné au Citron Vert & Piment] --- _Chapitre 14_

    #v(0.12cm)
    *5. L'Archétype de l'Œuf & Sauces Mères (Livre III)*
    - #link(<recette-oeuf-mollet>)[*Fiche 14 :* L'Œuf Mollet Parfait (6 min) & l'Œuf à 64°C] --- _Chapitre 15_
    - #link(<recette-oeuf-poche>)[*Fiche 15 :* L'Œuf Poché Infaillible sans Vinaigre à la Passoire Fine] --- _Chapitre 15_
    - #link(<recette-mayonnaise>)[*Fiche 16 :* La Mayonnaise Maison Inratable au Fouet Manuel] --- _Chapitre 15_
    - #link(<recette-sauce-hollandaise>)[*Fiche 17 :* La Sauce Hollandaise Émulsionnée Chaude au Bain-Marie] --- _Chapitre 15_
    - #link(<recette-sauce-bechamel>)[*Fiche 18 :* Le Roux Blanc & la Sauce Béchamel Veloutée sans Grumeaux] --- _Chapitre 16_

    #v(0.12cm)
    *6. Fermentations, Pains & Fromagerie Autonome (Livre IV)*
    - #link(<recette-pain-cocotte>)[*Fiche 19 :* Le Pain Cocotte d'Autonomie sans Pétrissage (*No-Knead Bread*)] --- _Chapitre 17_
    - #link(<recette-pickles-lactofermentes>)[*Fiche 20 :* Les Pickles Croquants de Végétaux en Lactofermentation Rapide] --- _Chapitre 17_
    - #link(<recette-fromage-frais>)[*Fiche 21 :* Le Fromage Frais Maison en 15 Minutes (Caillage Acide à 82°C)] --- _Chapitre 18_

    #v(0.12cm)
    *7. Pâtisserie Matricielle, Pyrolyse & Prodiges Thermiques (Livre IV)*
    - #link(<recette-moelleux-chocolat>)[*Fiche 22 :* Le Moelleux au Chocolat Cœur Coulant (Gradient Thermique)] --- _Chapitre 20_
    - #link(<recette-pate-brisee>)[*Fiche 23 :* La Pâte Brisée Pur Beurre au Sablage Express (Inhibition Gluten)] --- _Chapitre 20_
    - #link(<recette-mousse-aquafaba>)[*Fiche 24 :* La Mousse Aérienne au Chocolat à l'Aquafaba (Zéro Œuf)] --- _Chapitre 20_
    - #link(<recette-omelette-norvegienne>)[*Fiche 25 :* L'Omelette Norvégienne Minute (Bouclier de la Meringue)] --- _Chapitre 21_
    - #link(<recette-glace-sel>)[*Fiche 26 :* La Glace Express sans Sorbetière par Abaissement Cryoscopique] --- _Chapitre 21_
  ]
]

#metadata("debut-texte") <debut-texte>
"""

# ==============================================================================
# QUATRIÈME DE COUVERTURE (BACK COVER)
# ==============================================================================

BACK_COVER = """
#metadata("fin-section") <fin-section>
#pagebreak(to: "odd")
#set page(margin: 0pt, header: none, footer: none)
#metadata("debut-section") <debut-section>
#box()
#pagebreak()

#block(
  fill: rgb("#1c1917"),
  width: 100%,
  height: 100%,
  inset: (x: 2.6cm, y: 2.2cm)
)[
  #v(0.6cm)
  #text(size: 11pt, weight: "bold", fill: rgb("#fbbf24"), tracking: 2pt, font: "Liberation Sans")[
    LA CUISINE EXPLIQUÉE — ÉDITION RÉVISÉE ET AUGMENTÉE
  ]
  #v(0.2cm)
  #text(size: 20pt, weight: "bold", fill: white, font: "Liberation Serif")[
    Retrouver la liberté souveraine de comprendre ce que l'on fait.
  ]
  #v(0.4cm)
  #line(length: 100%, stroke: 1.5pt + rgb("#f59e0b"))
  #v(0.5cm)

  #text(size: 10.5pt, fill: rgb("#f5f5f4"), font: "Liberation Serif")[
    Pourquoi l'eau qui bout à gros bouillons est-elle parfois l'ennemie jurée d'un aliment ? Pourquoi saler une viande quarante-cinq minutes avant de la poser sur le feu change-t-il radicalement sa jutosité ? Comment fabriquer un fromage frais en quinze minutes sans matériel, ou émulsionner des pâtes crémeuses à la perfection sans la moindre goutte de crème fraîche ?

    *La Cuisine Expliquée* n'est pas un énième recueil de recettes passives à réciter sans réfléchir. C'est un traité fondamental d'*autonomie matérielle, de thermodynamique et de biologie du geste*, conçu pour libérer définitivement le cuisinier de la tyrannie des recettes magiques et du superflu des machines.

    Cette *édition révisée et augmentée en six livres* embrasse l'intégralité du fait nourricier : de l'étincelle paléolithique à la table de fête, de la chimie de l'eau aux fermentations vivantes, et de l'architecture d'un menu serein à la nutrition du microbiote sur le temps long.
  ]

  #v(0.6cm)
  #block(
    fill: rgb("#292524"),
    stroke: 1pt + rgb("#44403c"),
    inset: 13pt,
    radius: 6pt,
    width: 100%
  )[
    #text(size: 9.5pt, fill: rgb("#fed7aa"), font: "Liberation Sans", weight: "bold")[
      DANS CETTE ÉDITION DE RÉFÉRENCE :
    ]
    #v(3pt)
    #text(size: 8.8pt, fill: rgb("#e7e5e4"), font: "Liberation Sans")[
      • *6 Livres Majeurs & 26 Chapitres Exhaustifs* : Du premier foyer à la nutrition diachronique.\\
      • *26 Fiches Recettes Fondatrices* : Ratios universels, pas-à-pas et arbres de sauvetage en 30 secondes.\\
      • *Ouvertures Iconographiques Pleine Page* : Face-à-face graphique noble sur chaque nouveau Livre.\\
      • *Ingénierie du Foyer & Sécurité Sanitaire* : Gestion des pannes, brûlures, découpes et marche en avant.\\
      • *Diffusion Ouverte & Pérenne* : Ouvrage sous licence libre Creative Commons CC BY-SA 4.0.
    ]
  ]

  #v(1.0cm)
  #grid(
    columns: (1fr, auto),
    align: (left + bottom, right + bottom),
    [
      #text(size: 9pt, fill: rgb("#a8a29e"), font: "Liberation Sans")[
        *Silvère-Martin Michiellot & Antigravity*\\
        Édition Numérique et Patrimoniale — 2026\\
        Dépôt GitHub Public / Open Access Book
      ]
    ],
    [
      #block(
        fill: rgb("#292524"),
        stroke: 0.5pt + rgb("#78716c"),
        inset: (x: 14pt, y: 8pt),
        radius: 4pt
      )[
        #text(size: 8.5pt, weight: "bold", fill: rgb("#fbbf24"), font: "Liberation Sans")[
          DIFFUSION OUVERTE & LIBRE
        ]
        #v(-2pt)
        #text(size: 7.5pt, fill: rgb("#d6d3d1"), font: "Liberation Sans")[
          LICENCE CC BY-SA 4.0
        ]
      ]
    ]
  )
]
"""

# ==============================================================================
# POSTPROCESS TYPST
# ==============================================================================

def postprocess_typst(typ_content):
    # Remplacer les images de patrimoine tall
    for portrait_img in ["scappi_cuisine_renaissance.jpg", "brillat_savarin_portrait.jpg", "auguste_escoffier_portrait.jpg", "nicolas_appert_conserve.jpg"]:
        typ_content = typ_content.replace(f'image("figures/patrimoine/{portrait_img}"', f'image("figures/patrimoine/{portrait_img}", height: 36%')

    # Remplacer les citations blockquote par quote_box
    typ_content = re.sub(
        r'#block\(\s*fill:\s*none,\s*stroke:\s*\(left:\s*[^)]+\),\s*inset:\s*[^,]+,\s*\[([\s\S]*?)\]\s*\)',
        r'#quote_box[\1]',
        typ_content
    )
    
    # Améliorer les tableaux avec style gastronomique noble
    typ_content = typ_content.replace(
        '#table(',
        '#table(\n  stroke: 0.5pt + rgb("#dcd6ca"),\n  fill: (x, y) => if y == 0 { rgb("#f2ece1") } else if calc.odd(y) { rgb("#faf7f2") } else { none },\n  inset: 8pt,\n'
    )
    
    # Reconvertir les balises d'appel didactiques
    def replace_callout_start(match):
        tag = match.group(1).replace(r'\_', '_').replace('\\', '')
        return f"#{tag}[\n"
        
    typ_content = re.sub(r'CALLOUTSTART([a-zA-Z0-9_\\]+)CALLOUTSTART', replace_callout_start, typ_content)
    typ_content = typ_content.replace('CALLOUTEND', '\n]')
    
    # Reconvertir les ancres HTML en labels Typst #hide[] <mon-label>
    typ_content = re.sub(r'LABELSTART([a-zA-Z0-9_\-]+)LABELSTART', r'#hide[] <\1>', typ_content)
    
    # Remplacer les balises spéciales OUVERTURELIVRE
    def replace_ouverture(match):
        partie = " ".join(match.group(1).strip().replace('\\', '').split())
        titre = " ".join(match.group(2).strip().replace('\\', '').split())
        img = match.group(3).strip().replace(r'\_', '_').replace('\\', '/').replace('//', '/')
        legende = " ".join(match.group(4).strip().replace(r'\_', '_').replace(r'\"', '"').replace('"', '\\"').split())
        
        # Nettoyer intégralement les chapitres de tout parasite
        citation_raw = match.group(5).strip().replace(r'\#linebreak()', '').replace('#linebreak()', '').replace('\\', '')
        chapitres = [c.strip() for c in citation_raw.split('///') if c.strip()]
        
        if len(chapitres) > 6:
            v_space = "0.22cm"
            font_size = "10.5pt"
        else:
            v_space = "0.38cm"
            font_size = "11.5pt"
            
        sommaire_lines = [f'#text(size: {font_size}, style: "italic")[— {c}]' for c in chapitres]
        sep = f' \\\n#v({v_space})\n'
        sommaire_clean = sep.join(sommaire_lines)
        
        return f'''
#pagebreak(weak: false, to: "even")
#set page(margin: 0pt, header: none, footer: none)
#portail_livre_verso("{img}", "{legende}")

#pagebreak(weak: false, to: "odd")
#set page(paper: "a4", margin: (top: 2.5cm, bottom: 2.5cm, left: 2.2cm, right: 2.2cm), header: none, footer: none, fill: rgb(255, 253, 250))
#portail_livre_recto("{partie}", "{titre}", [{sommaire_clean}])

#pagebreak(weak: false, to: "odd")
#set page(header: entete-livre, footer: pied-livre)
'''
    typ_content = re.sub(
        r'OUVERTURESTART\s*\{([^}]+)\}\s*\{([^}]+)\}\s*\{([^}]+)\}\s*\{([^}]+)\}\s*\{([^}]+)\}\s*OUVERTUREEND',
        replace_ouverture,
        typ_content
    )

    # Nettoyer systématiquement tous les chemins d'images dans Typst contre les échappements de Pandoc
    typ_content = re.sub(
        r'image\("([^"]+)"',
        lambda m: 'image("' + m.group(1).replace(r'\_', '_').replace('\\', '/') + '"',
        typ_content
    )

    # Limiter la hauteur des photographies de recettes pour une intégration harmonieuse sans saut de page brutal
    typ_content = re.sub(
        r'image\("figures/nourriture/([^"]+)"(?:\s*,\s*alt:\s*"[^"]*")?\)',
        r'image("figures/nourriture/\1", width: 90%, height: 35%, fit: "cover")',
        typ_content
    )

    # Limiter la hauteur des schémas SVG pour garantir une aération parfaite de la page
    typ_content = re.sub(
        r'image\("figures/((?:histoire|livre_[0-9]|croquis)/[^"]+\.svg)"(?:\s*,\s*alt:\s*"[^"]*")?\)',
        r'image("figures/\1", width: 95%, height: 36%, fit: "contain")',
        typ_content
    )

    # Limiter la hauteur des photographies scientifiques (Chapitres 18 et 26) pour éviter tout vide blanc en bas de page
    typ_content = re.sub(
        r'image\("figures/science/([^"]+)"(?:\s*,\s*alt:\s*"[^"]*")?\)',
        r'image("figures/science/\1", width: 85%, height: 25%, fit: "cover")',
        typ_content
    )

    # Limiter la hauteur des gravures et portraits historiques dans le corps des chapitres
    typ_content = re.sub(
        r'image\("figures/patrimoine/([^"]+)"\s*,\s*alt:\s*"[^"]*"\)',
        r'image("figures/patrimoine/\1", width: 85%, height: 32%, fit: "contain")',
        typ_content
    )

    # Assembler le document complet
    full_text = PREAMBLE + "\n\n" + typ_content + "\n\n" + BACK_COVER
    
    # Résolution automatique des étiquettes manquantes pour éviter tout crash Typst
    targeted_links = set(re.findall(r'#link\(<([a-zA-Z0-9_\-]+)>\)', full_text))
    defined_labels = set(re.findall(r'(?<!#link\()<([a-zA-Z0-9_\-]+)>', full_text))
    missing_labels = targeted_links - defined_labels
    if missing_labels:
        print(f"  [AUTO-RÉSOLUTION] {len(missing_labels)} étiquettes cibles créées automatiquement.")
        anchor_block = "\n\n// Ancres de navigation transversale invisibles\n"
        for label in missing_labels:
            anchor_block += f"#hide[] <{label}>\n"
        full_text += anchor_block
        
    return full_text

# ==============================================================================
# PREPROCESS MARKDOWN
# ==============================================================================

def preprocess_markdown(md_text):
    md_text = re.sub(r'<a\s+id=[\'"]([a-zA-Z0-9_\-]+)[\'"]\s*>\s*</a>', r'\n\nLABELSTART\1LABELSTART\n\n', md_text)
    
    lines = md_text.split('\n')
    out_lines = []
    in_callout = False
    
    for line in lines:
        m_start = re.match(r'^:::\s*([a-zA-Z0-9_]+)\s*$', line.strip())
        if m_start:
            tag = m_start.group(1)
            out_lines.append(f"\n\nCALLOUTSTART{tag}CALLOUTSTART\n\n")
            in_callout = True
        elif line.strip() == ':::' and in_callout:
            out_lines.append("\n\nCALLOUTEND\n\n")
            in_callout = False
        else:
            out_lines.append(line)
            
    text_processed = '\n'.join(out_lines)
    text_processed = re.sub(r'([^\n])\n(#{1,6}\s+)', r'\1\n\n\2', text_processed)
    return text_processed

# ==============================================================================
# RUN BUILD
# ==============================================================================

def run_build():
    print("=== Étape 1 : Assemblage des 6 Livres et 26 Chapitres ===")
    
    livres = [
        {
            "num": "PREMIÈRE PARTIE",
            "titre": "L'HOMME, L'ÉVOLUTION ET LA CIVILISATION DU GOÛT",
            "img": "figures/patrimoine/livre1_ouverture_feu_ancestral.jpg",
            "legende": "La conquête du feu paléolithique et l'externalisation de la digestion humaine.",
            "citation": "L'Animal Culinaire : Anatomie, Feu et Nutrition /// L'Histoire Écrite de la Table : De la Mésopotamie à Nos Jours /// La Géopolitique des Saveurs : Terroirs et Mondialisation",
            "fichiers": [
                "textes/Livre_I/Chapitre_01_L_Animal_Culinaire_Anatomie_Feu_Nutrition.md",
                "textes/Livre_I/Chapitre_02_L_Histoire_Ecrite_de_la_Table_de_Mesopotamie_a_Aujourdhui.md",
                "textes/Livre_I/Chapitre_03_La_Geopolitique_des_Saveurs_Terroirs_et_Mondialisation.md"
            ]
        },
        {
            "num": "DEUXIÈME PARTIE",
            "titre": "LE FOYER MODERNE : ÉQUIPEMENTS, SÉCURITÉ ET ORGANISATION",
            "img": "figures/patrimoine/livre2_ouverture_cuisine_ordre.jpg",
            "legende": "L'arsenal ordonné de cuisine et la clarté du foyer bien gouverné (d'après Chardin).",
            "citation": "L'Arsenal Minimal et les Équipements Fondamentaux /// Consignes de Sécurité, Découpe et Pannes Critiques /// L'Économie du Foyer : Courses, Additifs et Saisonnalité /// L'Ordre Invisible : Marche en Avant, Restes et Plonge",
            "fichiers": [
                "textes/Livre_II/Chapitre_04_L_Arsenal_Minimal_et_les_Equipements_Fondamentaux.md",
                "textes/Livre_II/Chapitre_05_Consignes_de_Securite_et_Pannes_Critiques.md",
                "textes/Livre_II/Chapitre_06_L_Economie_du_Foyer_Courses_Additifs_et_Saisonnalite.md",
                "textes/Livre_II/Chapitre_07_L_Ordre_Invisible_Marche_en_Avant_Restes_et_Plonge.md"
            ]
        },
        {
            "num": "TROISIÈME PARTIE",
            "titre": "LA SCIENCE DE LA CASSEROLE : MATIÈRES PREMIÈRES, FLUIDES ET TRANSFORMATIONS",
            "img": "figures/nourriture/livre3_ouverture_marche_abondance.jpg",
            "legende": "L'abondance maraîchère des éléments bruts : la matière vivante avant la transformation.",
            "citation": "Cuisiner avec ses Sens et Thermodynamique /// Féculents, Céréales et Légumineuses : La Force du Grain /// La Mécanique Végétale : Éplucher, Tailler et Dompter l'Amidon /// L'Écosystème Vert : Salades, Turgescence et l'Acide /// La Chimie de l'Eau : Soupes, Bouillons et Glaces /// L'Alchimie des Épices, Herbes Fraîches et Arômes /// Le Monde Animal : Muscle, Maillard et Déglaçage /// L'Archétype de l'Œuf et les Émulsions Maîtresses /// La Matrice des Grandes Transformations Culinaires",
            "fichiers": [
                "textes/Livre_III/Chapitre_08_Cuisiner_avec_ses_Sens_et_Thermodynamique.md",
                "textes/Livre_III/Chapitre_09_Feculents_Cereales_et_Legumineuses_Force_du_Grain.md",
                "textes/Livre_III/Chapitre_10_La_Mecanique_Vegetale_Eplucher_Tailler_et_Dompter_l_Amidon.md",
                "textes/Livre_III/Chapitre_11_L_Ecosysteme_Vert_Salades_Turgescence_et_l_Acide.md",
                "textes/Livre_III/Chapitre_12_La_Chimie_de_l_Eau_Soupes_Bouillons_et_Glaces.md",
                "textes/Livre_III/Chapitre_13_L_Alchimie_des_Epices_Herbes_Fraiches_et_Aromes.md",
                "textes/Livre_III/Chapitre_14_Le_Monde_Animal_Muscle_Maillard_et_Deglacage.md",
                "textes/Livre_III/Chapitre_15_L_Archetype_de_l_Oeuf_et_les_Emulsions_Maitres.md",
                "textes/Livre_III/Chapitre_16_La_Matrice_des_Grandes_Transformations_Culinaires.md"
            ]
        },
        {
            "num": "QUATRIÈME PARTIE",
            "titre": "LES MÉTAMORPHOSES SINGULIÈRES : FERMENTATIONS, PÂTISSERIE ET GRAND FROID",
            "img": "figures/nourriture/livre4_ouverture_fournil_levain.jpg",
            "legende": "Miches dorées au fournil artisanal : la résurrection noble du levain sauvage.",
            "citation": "La Révolution des Fermentations Végétales, Pains et Levains /// L'Alchimie Laitière et la Fromagerie Autonome /// Le Travail des Glucides : Pyrolyse, Sirops et Caramélisation /// La Pâtisserie Matricielle et la Mécanique des Pâtes /// Les Prodiges Thermiques du Grand Froid et du Feu Isolant",
            "fichiers": [
                "textes/Livre_IV/Chapitre_17_La_Revolution_des_Fermentations_Vegetales_Pains_et_Levains.md",
                "textes/Livre_IV/Chapitre_18_L_Alchimie_Laitiere_et_la_Fromagerie_Autonome.md",
                "textes/Livre_IV/Chapitre_19_Le_Travail_des_Glucides_Pyrolyse_Sirops_et_Caramelisation.md",
                "textes/Livre_IV/Chapitre_20_La_Patisserie_Matricielle_et_la_Mecanique_des_Pates.md",
                "textes/Livre_IV/Chapitre_21_Les_Prodiges_Thermiques_du_Grand_Froid_et_du_Feu_Isolant.md"
            ]
        },
        {
            "num": "CINQUIÈME PARTIE",
            "titre": "L'ART DU REPAS, DU PARTAGE ET DU SERVICE",
            "img": "figures/patrimoine/livre5_ouverture_banquet_table.jpg",
            "legende": "Table de banquet dressée : l'orfèvrerie des couverts et la noblesse du service partagé.",
            "citation": "Pourquoi une Fourchette ? Histoire et Sociologie de la Table /// L'Architecture du Menu, Rétroplanning et Art de Recevoir /// L'Esthétique de l'Assiette, Dressage et Températures",
            "fichiers": [
                "textes/Livre_V/Chapitre_22_Pourquoi_une_Fourchette_Histoire_et_Sociologie_de_la_Table.md",
                "textes/Livre_V/Chapitre_23_L_Architecture_du_Menu_Retroplanning_et_Art_de_Recevoir.md",
                "textes/Livre_V/Chapitre_24_L_Esthetique_de_l_Assiette_Dressage_et_Temperatures.md"
            ]
        },
        {
            "num": "SIXIÈME PARTIE",
            "titre": "LE TEMPS LONG : NUTRITION DIACHRONIQUE ET PLAISIR DURABLE",
            "img": "figures/nourriture/livre6_ouverture_potager_saisons.jpg",
            "legende": "Le potager vivant au fil des saisons : diversité végétale et temps long.",
            "citation": "Sortir de la Tyrannie des Régimes : Physiologie du Poids /// La Diachronie Culinaire : Microbiote et Batch Cooking",
            "fichiers": [
                "textes/Livre_VI/Chapitre_25_Sortir_de_la_Tyrannie_des_Regimes_Physiologie_du_Poids.md",
                "textes/Livre_VI/Chapitre_26_La_Diachronie_Culinaire_Microbiote_et_Batch_Cooking.md"
            ]
        },
        {
            "num": "ANNEXES ET RÉPERTOIRES",
            "titre": "FORMULAIRE, GLOSSAIRE ET RÉPERTOIRE CRITIQUE",
            "img": "figures/patrimoine/diderot_encyclopedie_fournil.jpg",
            "legende": "Planche de l'Encyclopédie de Diderot et d'Alembert (1762) : four de brique, étuve et instruments d'office (Pl. II).",
            "citation": "Annexe A — Cadran Absolu des Températures Critiques en Cuisine /// Annexe B — Glossaire Physico-Chimique et Culinaire Exhaustif /// Annexe C — Bibliographie Raisonnée et Évaluée /// Annexe D — Guide d'Achat de l'Arsenal Minimal, Coûts et Durées /// Annexe E — Conservation au Froid, Zones et Durées Limites /// Annexe F — Répertoire des Crédits Iconographiques et Sources",
            "fichiers": [
                "textes/Annexes/Annexe_A_Tableau_des_Temperatures_Critiques.md",
                "textes/Annexes/Annexe_B_Glossaire_Physico_Chimique_et_Culinaire.md",
                "textes/Annexes/Annexe_C_Bibliographie_Raisonnee.md",
                "textes/Annexes/Annexe_D_Guide_Achat_Arsenal_Minimal_Couts_et_Durees_de_Cuisson.md",
                "textes/Annexes/Annexe_E_Conservation_au_Froid_Zones_du_Refrigerateur_et_Durees_Limites.md",
                "textes/Annexes/Annexe_F_Credits_Iconographiques_et_Sources.md"
            ]
        }
    ]

    all_md = []
    for livre in livres:
        # Balise spéciale préservée par Pandoc pour l'ouverture en double page
        marker = f"\n\nOUVERTURESTART {{{livre['num']}}} {{{livre['titre']}}} {{{livre['img']}}} {{{livre['legende']}}} {{{livre['citation']}}} OUVERTUREEND\n\n"
        all_md.append(marker)
        
        for f in livre["fichiers"]:
            full_path = os.path.join(BASE_DIR, f)
            if os.path.exists(full_path):
                print(f"  -> Lecture : {f}")
                with open(full_path, "r", encoding="utf-8") as file:
                    raw_content = file.read()
                cleaned_content = preprocess_markdown(raw_content)
                all_md.append(cleaned_content)
            else:
                print(f"  [ATTENTION] Fichier introuvable : {full_path}")

    full_md_content = "\n\n".join(all_md)
    with open(TEMP_MD, "w", encoding="utf-8") as f:
        f.write(full_md_content)
    print(f"[OK] Master Markdown assemblé : {TEMP_MD} ({len(full_md_content)} caractères)")

    print("=== Étape 2 : Conversion Pandoc Markdown -> Typst ===")
    cmd_pandoc = [PANDOC_EXE, TEMP_MD, "-t", "typst", "-o", TEMP_TYP]
    res_p = subprocess.run(cmd_pandoc, capture_output=True, encoding="utf-8", errors="replace")
    if res_p.returncode != 0:
        print("ERREUR PANDOC :", res_p.stderr)
        raise RuntimeError("Pandoc a échoué.")
    print(f"[OK] Pandoc conversion réussie : {TEMP_TYP}")

    print("=== Étape 3 : Post-Processing Typst ===")
    with open(TEMP_TYP, "r", encoding="utf-8") as f:
        pandoc_typ = f.read()

    final_typ = postprocess_typst(pandoc_typ)
    with open(FINAL_TYP, "w", encoding="utf-8") as f:
        f.write(final_typ)
    print(f"[OK] Fichier Typst Maître généré : {FINAL_TYP}")

    print("=== Étape 4 : Compilation PDF avec Typst ===")
    cmd_typst = [TYPST_EXE, "compile", FINAL_TYP, FINAL_PDF]
    res_t = subprocess.run(cmd_typst, capture_output=True, encoding="utf-8", errors="replace")
    if res_t.returncode != 0:
        print("ERREUR TYPST :", res_t.stderr[:2500])
        raise RuntimeError("Typst compilation failed.")

    pdf_size_mb = os.path.getsize(FINAL_PDF) / (1024 * 1024)
    print(f"=== SUCCÈS MAJEUR : L'Édition Révisée et Augmentée a été compilée en PDF ===")
    print(f"Chemin du PDF : {FINAL_PDF} ({pdf_size_mb:.2f} Mo)")

if __name__ == "__main__":
    run_build()
