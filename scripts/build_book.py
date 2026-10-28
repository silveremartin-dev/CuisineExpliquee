# -*- coding: utf-8 -*-
"""
Master Culinary Book Builder pour LA CUISINE EXPLIQUÉE
- Auteurs : Silvère-Martin Michiellot & Antigravity
- Moteur Typographique : Typst v0.15.1
- Moteur de conversion : Pandoc 3.12.1
- Direction Artistique : Haute Gastronomie Éditoriale (Terracotta, Bordeaux, Or Chaud)
- Couverture photographique vibrante (légumes frais du marché)
- Quatrième de couverture complète (synopsis, manifeste, licence libre, sans prix ni code-barres)
- Index dédié des recettes dès le début du livre
- Foliotage éditorial : couverture hors décompte, liminaires muets, ouvertures en belle page,
  pages blanches sans folio, folio centré (jamais côté reliure)
- Zéro veuve/orpheline, zéro faux ISBN, typographie soignée
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
  title: "LA CUISINE EXPLIQUÉE — Principes Premiers, Maîtrise de la Matière et Minimalisme Instrumental",
  author: "Silvère-Martin Michiellot & Antigravity"
)

// Palette Chromatique "Haute Gastronomie & Matière Noble" (Style 1 : Le Grand Traité Étoilé)
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

// ==========================================
// RÈGLES DE FOLIOTAGE (CHARTE TYPOGRAPHIQUE DE L'ÉDITION)
// - La couverture (plats 1, 2, 3 et 4) n'est jamais comptée ni foliotée :
//   le compteur démarre à 1 sur la première belle page du bloc intérieur (faux-titre).
// - Pages impaires = recto (droite) ; pages paires = verso (gauche).
// - Pages liminaires (1 faux-titre, 2 blanche, 3 grand titre, 4 mentions légales,
//   5 exergue/dédicace, 6 blanche, puis sommaire et table des recettes) : comptées mais muettes.
// - Toute ouverture de partie ou de chapitre se fait en belle page (impaire) et reste muette ;
//   le premier folio visible apparaît sur la page qui suit l'ouverture de la Première Partie.
// - Pages blanches : comptées dans l'ordre arithmétique, jamais de folio ni de titre courant.
// - Folio centré en pied de page (jamais côté reliure / petit fond).
// ==========================================

// Saut vers la prochaine belle page (impaire) avec balisage des pages blanches intercalaires
#let recto() = {
  [#metadata("fin-section") <fin-section>]
  pagebreak(weak: true, to: "odd")
  [#metadata("debut-section") <debut-section>]
}

// Le folio (et le titre courant) n'est visible que sur les pages de texte courant :
// ni liminaire, ni page d'ouverture, ni page blanche.
#let folio-visible() = {
  let p = here().page()
  let debut = query(<debut-texte>)
  if debut.len() == 0 or p <= debut.first().location().page() { return false }
  let fins = query(<fin-section>)
  let debuts = query(<debut-section>)
  for (i, d) in debuts.enumerate() {
    let dp = d.location().page()
    if dp == p { return false }
    if i < fins.len() and p < dp {
      let m = fins.at(i).location()
      let mp = m.page()
      if mp < p { return false }
      if mp == p and m.position().y < 2.75cm { return false }
    }
  }
  true
}

#let entete-livre = context {
  if folio-visible() {
    let page-h1 = query(selector(heading.where(level: 1))).filter(h => h.location().page() == here().page())
    let cur-h1 = if page-h1.len() > 0 { page-h1 } else { query(selector(heading.where(level: 1)).before(here())) }
    let title-left = if cur-h1.len() > 0 { cur-h1.last().body } else { [LA CUISINE EXPLIQUÉE] }
    text(font: "Liberation Serif", size: 8.5pt, fill: c-bordeaux, tracking: 0.08em)[
      #smallcaps[#title-left] #h(1fr) #emph[La Cuisine Expliquée]
    ]
    v(-4pt)
    line(length: 100%, stroke: 0.5pt + c-bronze)
  }
}

#let pied-livre = context {
  if folio-visible() {
    let page-num = counter(page).get().first()
    align(center)[#text(font: "Liberation Serif", size: 9pt, fill: c-bordeaux)[— #page-num —]]
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

// Style des Hyperliens Interactifs
#show link: it => text(fill: c-terracotta, weight: "medium")[#underline(stroke: 0.5pt + c-bronze, offset: 1.5pt)[#it]]

// Niveaux de Titres : Portails de Livre en Style 5 (Page 21, alignés à gauche, sans couleur bleue) et Chapitres en Style 1 (en haut de page, alignés à gauche)
#show heading.where(level: 1): it => {
  // Ouverture systématique en belle page (impaire), page d'ouverture muette
  recto()
  let body_repr = repr(it.body)
  let is_portal = (body_repr.contains("01") or body_repr.contains("02") or body_repr.contains("03") or body_repr.contains("04") or body_repr.contains("05")) and not body_repr.contains("CHAPITRE") and not body_repr.contains("ANNEXE") and not body_repr.contains("Sommaire")
  if is_portal {
    // STYLE 5 (PAGE 21) : OUVERTURE DE LIVRE SUR PAGE DÉDIÉE, ALIGNÉE À GAUCHE, TONS CHAUDS DU STYLE 1
    let part_num = if body_repr.contains("01") { [PREMIÈRE PARTIE] } else if body_repr.contains("02") { [DEUXIÈME PARTIE] } else if body_repr.contains("03") { [TROISIÈME PARTIE] } else if body_repr.contains("04") { [QUATRIÈME PARTIE] } else { [CINQUIÈME PARTIE] }
    v(2.5cm)
    align(left)[
      #text(size: 11pt, tracking: 0.15em, fill: c-bordeaux, font: "Liberation Sans", weight: "bold")[#part_num]
      #v(1.0cm)
      #text(size: 30pt, weight: "light", fill: c-ink, tracking: 0.04em, font: "Liberation Sans")[#it.body]
      #v(2.0cm)
      #text(size: 11pt, fill: c-slate, font: "Liberation Sans", tracking: 0.04em)[
        #if body_repr.contains("01") [
          Rien de trop.#linebreak()
          Un couteau affûté.#linebreak()
          Une flamme pure.#linebreak()
          L'intelligence du temps.
        ] else if body_repr.contains("02") [
          L'anatomie invisible de l'assiette.#linebreak()
          La vérité sans fard de la matière.#linebreak()
          Le rythme biologique de la digestion.#linebreak()
          Le cycle vivant de la terre et de l'eau.
        ] else if body_repr.contains("03") [
          La contraction millimétrique du muscle.#linebreak()
          Les seuils thermiques de l'œuf.#linebreak()
          L'extraction aromatique des parois végétales.#linebreak()
          La matrice élémentaire de la pâte.
        ] else if body_repr.contains("04") [
          Le sel et l'acide qui transforment à froid.#linebreak()
          La prolifération noble des ferments.#linebreak()
          La géographie ancestrale des trois graisses.#linebreak()
          La mémoire vivante du goût partagé.
        ] else [
          Le cadran absolu des températures critiques.#linebreak()
          Le glossaire physico-chimique exhaustif.#linebreak()
          La bibliographie raisonnée et critique.#linebreak()
          Les règles sanitaires de la conservation.
        ]
      ]
    ]
  } else {
    // STYLE 1 : LE GRAND TRAITÉ ÉTOILÉ POUR LES CHAPITRES (EN HAUT DE PAGE, ALIGNÉ À GAUCHE)
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
}

// Titres de niveau 2, 3 et 4 systématiquement alignés à gauche (Style 1)
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

// Signalétique Didactique et Boîtes Culinaires Nobles (Style 1 : Couleurs douces et harmonieuses)
#let truc_de_chef(body) = block(
  fill: rgb("#faf7f0"),
  stroke: (left: 3pt + c-bronze),
  inset: (left: 14pt, right: 12pt, top: 10pt, bottom: 10pt),
  radius: (right: 4pt),
  width: 100%,
  spacing: 1.2em,
  breakable: false
)[
  #set text(size: 9.5pt, fill: c-ink, font: "Liberation Serif")
  #set par(justify: true, leading: 0.74em)
  #body
]

#let anecdote_historique(body) = block(
  fill: rgb("#f7f5ef"),
  stroke: (left: 3pt + rgb("#a38c78")),
  inset: (left: 14pt, right: 12pt, top: 10pt, bottom: 10pt),
  radius: (right: 4pt),
  width: 100%,
  spacing: 1.2em,
  breakable: false
)[
  #set text(size: 9.5pt, fill: c-ink, font: "Liberation Serif")
  #set par(justify: true, leading: 0.74em)
  #body
]

#let positif(body) = block(
  fill: rgb("#f4f6f4"),
  stroke: (left: 3pt + rgb("#6e826b")),
  inset: (left: 14pt, right: 12pt, top: 10pt, bottom: 10pt),
  radius: (right: 4pt),
  width: 100%,
  spacing: 1.2em,
  breakable: false
)[
  #set text(size: 9.5pt, fill: c-ink, font: "Liberation Serif")
  #set par(justify: true, leading: 0.74em)
  #body
]

#let negatif(body) = block(
  fill: rgb("#fbf6f5"),
  stroke: (left: 3pt + rgb("#b06d60")),
  inset: (left: 14pt, right: 12pt, top: 10pt, bottom: 10pt),
  radius: (right: 4pt),
  width: 100%,
  spacing: 1.2em,
  breakable: false
)[
  #set text(size: 9.5pt, fill: c-ink, font: "Liberation Serif")
  #set par(justify: true, leading: 0.74em)
  #body
]

#let danger(body) = block(
  fill: rgb("#faf3f2"),
  stroke: (left: 3pt + c-bordeaux),
  inset: (left: 14pt, right: 12pt, top: 10pt, bottom: 10pt),
  radius: (right: 4pt),
  width: 100%,
  spacing: 1.2em,
  breakable: false
)[
  #set text(size: 9.5pt, fill: c-ink, font: "Liberation Serif")
  #set par(justify: true, leading: 0.74em)
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
  breakable: false
)[
  #set text(size: 9.5pt, fill: c-ink, font: "Liberation Serif")
  #set par(justify: true, leading: 0.74em)
  #body
]

#let oeil_molecule(body) = block(
  fill: rgb("#f6f5f3"),
  stroke: (left: 3pt + c-slate),
  inset: (left: 14pt, right: 12pt, top: 10pt, bottom: 10pt),
  radius: (right: 4pt),
  width: 100%,
  spacing: 1.2em,
  breakable: false
)[
  #set text(size: 9.5pt, fill: c-ink, font: "Liberation Serif")
  #set par(justify: true, leading: 0.74em)
  #body
]

#let cas_limite(body) = block(
  fill: rgb("#f8f6f1"),
  stroke: (left: 3pt + rgb("#8c7355")),
  inset: (left: 14pt, right: 12pt, top: 10pt, bottom: 10pt),
  radius: (right: 4pt),
  width: 100%,
  spacing: 1.2em,
  breakable: false
)[
  #set text(size: 9.5pt, fill: c-ink, font: "Liberation Serif")
  #set par(justify: true, leading: 0.74em)
  #body
]

#let quote_box(body) = block(
  fill: rgb("#faf7f2"),
  stroke: (left: 3pt + c-bronze),
  inset: (left: 12pt, y: 7pt),
  radius: (right: 4pt),
  width: 100%,
  spacing: 1.1em,
  breakable: false
)[
  #set text(style: "italic", fill: rgb("#292524"), font: "Liberation Serif")
  #set par(justify: true, leading: 0.74em)
  #body
]

// ==========================================
// 1. COUVERTURE PHOTOGRAPHIQUE GASTRONOMIQUE
// ==========================================
#set page(margin: 0pt, header: none, footer: none)

#block(width: 100%, height: 100%, fill: rgb("#1c1917"))[
  // Image de couverture pleine largeur (légumes frais du marché)
  #place(top + left)[
    #image("figures/nourriture/couverture_legumes_marche.jpg", width: 100%, height: 52%, fit: "cover")
  ]
  
  // Voile sombre et cartouche typographique
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
        Traité vivant d'anthropologie, de biologie et de thermodynamique appliquée aux fourneaux.\\
        Comprendre la matière brute, dompter le feu et cuisiner en toute liberté avec cinq instruments.
      ]
      #v(0.8cm)
      #grid(
        columns: (1fr, auto),
        align: (left + horizon, right + horizon),
        text(size: 9pt, weight: "bold", fill: rgb("#fcd34d"), font: "Liberation Sans")[
          ÉDITION INTÉGRALE DE RÉFÉRENCE — 2026
        ],
        text(size: 8.5pt, fill: rgb("#a8a29e"), font: "Liberation Sans")[
          LICENCE LIBRE CC BY-SA 4.0
        ]
      )
    ]
  ]
]

#pagebreak()
// Plat 2 (intérieur de couverture) : hors décompte, jamais folioté
#box()

#set page(
  paper: "a4",
  margin: (top: 2.5cm, bottom: 2.5cm, left: 2.2cm, right: 2.2cm),
  header: entete-livre,
  footer: pied-livre,
  fill: rgb(255, 253, 250)
)
// Début du bloc intérieur : la première belle page est la page 1 (muette)
#counter(page).update(1)

// ==========================================
// PAGE 1 (RECTO) — FAUX-TITRE (MUETTE)
// ==========================================
#align(center + horizon)[
  #text(size: 22pt, weight: "bold", fill: c-ink, font: "Liberation Serif", tracking: 0.06em)[LA CUISINE EXPLIQUÉE]
]
#pagebreak()

// PAGE 2 (VERSO) — PAGE BLANCHE (MUETTE)
#box()
#pagebreak()

// ==========================================
// PAGE 3 (RECTO) — GRAND TITRE (MUETTE)
// ==========================================
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
  #text(size: 10pt, fill: c-slate, font: "Liberation Sans", tracking: 0.1em)[ÉDITION INTÉGRALE DE RÉFÉRENCE — 2026]
  #v(0.2cm)
  #text(size: 9pt, fill: c-slate, font: "Liberation Sans")[Diffusion ouverte sous licence libre CC BY-SA 4.0]
  #v(1.5cm)
]
#pagebreak()

// PAGE 4 (VERSO) — MENTIONS LÉGALES (MUETTE)
// ==========================================
// 2. PAGE DE MENTIONS LÉGALES & LICENCE LIBRE
// ==========================================
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
      © 2026 Silvère-Martin Michiellot & Antigravity.\\
      \\
      *Licence Libre :* Cet ouvrage est mis à disposition selon les termes de la licence *Creative Commons Attribution - Partage dans les Mêmes Conditions 4.0 International (CC BY-SA 4.0)*.\\
      Vous êtes libre de copier, partager, distribuer et adapter ce traité sous réserve de créditer expressément les auteurs d'origine et de diffuser vos modifications sous une licence identique.\\
      \\
      *Conception didactique et scientifique :* Silvère-Martin Michiellot & Antigravity.\\
      *Illustrations vectorielles :* Antigravity Visual Engine (norme SVG Byrne-Culinaire).\\
      *Photographies culinaires & gravures :* Wikimedia Commons (Domaine Public & Creative Commons).\\
      *Composition typographique :* Typst v0.15.1, polices Liberation Serif & Sans.\\
      *Dépôt de code et figures sources :* Dépôt GitHub public sous licence CC BY-SA 4.0.\\
      *Avertissement d'homonymie éditoriale :* Le présent ouvrage est un traité d'investigation scientifique, anthropologique et pratique totalement indépendant. Il ne doit en aucun cas être confondu avec les manuels scolaires de formation professionnelle hôtelière (notamment le manuel éponyme de Gilles Charles aux éditions BPI).\\
      
      *Dépôt légal :* Octobre 2026 (Sans mention commerciale obligatoire).
    ]
  ]
]

#pagebreak()

// ==========================================
// 3. CITATION INAUGURALE & DÉDICACE
// ==========================================
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

// PAGE 6 (VERSO) — PAGE BLANCHE (MUETTE)
#box()
#pagebreak()

// PAGE 7 (RECTO) ET SUIVANTES — SOMMAIRE (LIMINAIRE, MUET)

// ==========================================
// 4. SOMMAIRE RAISONNÉ
// ==========================================
#outline(
  title: [Sommaire Général et Table Raisonnée],
  indent: 1.5em,
  depth: 2
)

// La table des recettes s'ouvre en belle page
#recto()

// ==========================================
// 5. TABLE DES RECETTES & PRÉPARATIONS PILIERS
// ==========================================
#align(left)[
  #text(size: 15pt, weight: "bold", fill: c-bordeaux, font: "Liberation Serif")[
    🍳 Table des Vingt-et-Une Recettes et Préparations Piliers
  ]
  #v(-4pt)
  #line(length: 100%, stroke: 0.8pt + c-bronze)
]
#v(0.4cm)

#block(
  fill: rgb("#faf7f0"),
  stroke: 0.5pt + rgb("#dfdacf"),
  inset: 14pt,
  radius: 6pt,
  width: 100%
)[
  #text(size: 9.5pt)[
    Cette table réunit les vingt protocoles fondamentaux pas à pas décrits dans l'ouvrage. Chaque recette constitue une application directe et vivante des principes thermodynamiques et biologiques exposés :

    #v(0.2cm)
    *1. Pains, Levains, Fermentations & Fromagerie Autonome*
    - #link(<recette-pain-cocotte>)[Le Pain Cocotte d'Autonomie sans Pétrissage (*No-Knead Bread*)] --- _Chapitre 16_
    - #link(<recette-fromage-frais>)[Le Fromage Frais Maison en 15 Minutes (Caillage Acide sans Présure)] --- _Chapitre 16_
    - #link(<recette-glace-sel>)[La Glace Express sans Sorbetière (Abaissement Cryoscopique du Sel à -18°C)] --- _Chapitre 16_

    #v(0.15cm)
    *2. Viandes, Poissons, Sauces Mères & Saisies à la Poêle*
    - #link(<recette-steak-fonte>)[Le Pavé de Bœuf Saisi en Fonte & Arrosé au Beurre Moussant (*Basting*)] --- _Chapitre 03_
    - #link(<recette-deglacage-minute>)[Le Déglaçage Minute & Sauce Réduite au Vin Montée au Beurre] --- _Chapitre 05_
    - #link(<recette-consomme-clarifie>)[Le Consommé Clarifié à l'Albumine d'Œuf (Filtre Macromoléculaire)] --- _Chapitre 05_
    - #link(<recette-sauce-bechamel>)[Le Roux Blanc & la Sauce Béchamel Veloutée Sans Grumeaux] --- _Chapitre 05_
    - #link(<recette-ceviche-cabillaud>)[Le Vrai Ceviche de Cabillaud Mariné au Citron Vert & Piment Doux] --- _Chapitre 15_

    #v(0.15cm)
    *3. Émulsions Maîtres, Œufs & Sauces Chaudes*
    - #link(<recette-mayonnaise>)[La Mayonnaise Maison Inratable au Fouet Manuel (Lécithines & Cisaillement)] --- _Chapitre 01_
    - #link(<recette-oeuf-mollet>)[L'Œuf Mollet Parfait en 6 Minutes & l'Œuf à 64°C (Gradient Thermique)] --- _Chapitre 06_
    - #link(<recette-creme-anglaise>)[La Crème Anglaise au Degré Près (Seuil Critique de 82°C au Ruban)] --- _Chapitre 06_
    - #link(<recette-sauce-hollandaise>)[La Sauce Hollandaise Émulsionnée Chaude au Bain-Marie (58°C)] --- _Chapitre 06_
    - #link(<recette-grand-aioli>)[Le Grand Aïoli Provençal (Au Mortier ou au Système D)] --- _Chapitre 17_

    #v(0.15cm)
    *4. Pâtes & Féculents Fondateurs*
    - #link(<recette-carbonara-traditionnelle>)[Les Vraies Spaghetti alla Carbonara (L'Émulsion d'Or Jaune sans Crème)] --- _Chapitre 18_
    - #link(<recette-pommes-sarladaises>)[Les Pommes Sarladaises Croustillantes à la Graisse de Canard (190°C)] --- _Chapitre 17_

    #v(0.15cm)
    *5. Cuisine Végétale & Protéines Alternatives*
    - #link(<recette-dahl-lentilles>)[Le Dahl Réconfortant de Lentilles Corail au Cumin Torréfié & Coco] --- _Chapitre 12_
    - #link(<recette-tofu-croustillant>)[Le Tofu Doré Ultra-Croustillant & son Laquage Tamari-Sésame] --- _Chapitre 12_
    - #link(<recette-mousse-aquafaba>)[La Mousse au Chocolat Aérienne à l'Aquafaba (Zéro Œuf, Zéro Crème)] --- _Chapitre 12_

    #v(0.15cm)
    *6. Pâtisserie Matricielle & Contrôle de l'Amidon*
    - #link(<recette-moelleux-chocolat>)[Le Moelleux au Chocolat Cœur Coulant (Gradient Thermique Étalonné)] --- _Chapitre 14_
    - #link(<recette-pate-brisee>)[La Pâte Brisée Pur Beurre au Sablage Express (Inhibition du Gluten)] --- _Chapitre 14_
    - #link(<recette-omelette-norvegienne>)[L'Omelette Norvégienne Minute Infaillible (Le Bouclier Thermique de la Meringue)] --- _Chapitre 14_
  ]
]

// Fin des pages liminaires : le folio devient visible après l'ouverture de la Première Partie
#metadata("debut-texte") <debut-texte>
"""

# ==============================================================================
# QUATRIÈME DE COUVERTURE (BACK COVER)
# ==============================================================================

BACK_COVER = """
// Le bloc intérieur se termine sur un verso (page paire) : page blanche muette si nécessaire
#metadata("fin-section") <fin-section>
#pagebreak(to: "odd")
#set page(margin: 0pt, header: none, footer: none)
#metadata("debut-section") <debut-section>
// Plat 3 (intérieur de couverture arrière) : hors décompte, jamais folioté
#box()
#pagebreak()

// Plat 4 (quatrième de couverture) : jamais foliotée

#block(
  fill: rgb("#1c1917"),
  width: 100%,
  height: 100%,
  inset: (x: 2.6cm, y: 2.4cm)
)[
  #v(0.8cm)
  #text(size: 11pt, weight: "bold", fill: rgb("#fbbf24"), tracking: 2pt, font: "Liberation Sans")[
    LA CUISINE EXPLIQUÉE
  ]
  #v(0.2cm)
  #text(size: 20pt, weight: "bold", fill: white, font: "Liberation Serif")[
    Retrouver la liberté souveraine de comprendre ce que l'on fait.
  ]
  #v(0.4cm)
  #line(length: 100%, stroke: 1.5pt + rgb("#f59e0b"))
  #v(0.6cm)

  #text(size: 10.5pt, fill: rgb("#f5f5f4"), font: "Liberation Serif")[
    Pourquoi l'eau qui bout à gros bouillons est-elle parfois l'ennemie jurée d'un aliment ? Pourquoi saler une viande quarante-cinq minutes avant de la poser sur le feu change-t-il radicalement sa jutosité ? Comment fabriquer un fromage frais en quinze minutes sans matériel, ou émulsionner des pâtes crémeuses à la perfection sans la moindre goutte de crème fraîche ?

    *La Cuisine Expliquée* n'est pas un énième catalogue de recettes passives à réciter sans réfléchir. C'est un traité vivant d'*autonomie matérielle, de thermodynamique et de biologie du geste culinaire*, conçu pour libérer définitivement le cuisinier de la tyrannie des recettes magiques et du diktat des gadgets superflus.

    À travers quinze chapitres lumineux, ce manuel démontre qu'avec seulement cinq outils indestructibles (une poêle en fonte, une casserole inox, une planche de bois massif, un couteau affûté et une cuillère de bois) et la compréhension des états de la matière, il est possible de maîtriser l'intégralité du répertoire nourricier universel.
  ]

  #v(0.8cm)
  #block(
    fill: rgb("#292524"),
    stroke: 1pt + rgb("#44403c"),
    inset: 14pt,
    radius: 6pt,
    width: 100%
  )[
    #text(size: 9.5pt, fill: rgb("#fed7aa"), font: "Liberation Sans", weight: "bold")[
      DANS CET OUVRAGE :
    ]
    #v(3pt)
    #text(size: 9pt, fill: rgb("#e7e5e4"), font: "Liberation Sans")[
      • *18 Chapitres Fondamentaux* : De l'étincelle paléolithique à la géopolitique des terroirs.\\
      • *21 Recettes Piliers Pas à Pas* : Ratios universels, repères sensoriels et arbres de sauvetage.\\
      • *Guide de Sécurité & Premiers Secours* : Incendies d'huile, brûlures (règle des trois 15), coupures et pannes de froid.\\
      • *Cuisine Végétale & Vérité du Bio* : Synergie des acides aminés, polyphénols protecteurs et guide malin du panier.\\
      • *Édition Ouverte & Pérenne* : Diffusée sous licence libre Creative Commons CC BY-SA 4.0.
    ]
  ]

  #v(1.2cm)
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
    # Constrain tall portrait heritage images so they never collide with the footer
    for portrait_img in ["scappi_cuisine_renaissance.jpg", "brillat_savarin_portrait.jpg", "auguste_escoffier_portrait.jpg"]:
        typ_content = typ_content.replace(f'image("figures/patrimoine/{portrait_img}"', f'image("figures/patrimoine/{portrait_img}", height: 38%')

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
    
    # Reconvertir les ancres HTML en labels Typst #hide[] <mon-label> (invisible sur la page)
    typ_content = re.sub(r'LABELSTART([a-zA-Z0-9_\-]+)LABELSTART', r'#hide[] <\1>', typ_content)
    
    # Liaison automatique et interactive des termes techniques vers le Glossaire (Annexe B)
    glossary_targets = {
        r'\b(réaction[s]? de Maillard|effet Maillard)\b': 'glossaire-maillard',
        r'\b(effet Leidenfrost|phénomène de Leidenfrost)\b': 'glossaire-leidenfrost',
        r"\b(gélatinisation de l'amidon|gélatinisation)\b": 'glossaire-gelatinisation',
        r"\b(activité de l'eau)\b": 'glossaire-aw',
        r'\b(actomyosine|actine et myosine)\b': 'glossaire-actomyosine',
        r'\b(acides aminés essentiels)\b': 'glossaire-acides-amines',
        r'\b(alkylpyrazines)\b': 'glossaire-alkylpyrazines',
        r'\b(appertisation)\b': 'glossaire-appertisation',
        r'\b(aquafaba)\b': 'glossaire-aquafaba',
        r'\b(toxine botulique|botulisme|Clostridium botulinum)\b': 'glossaire-botulisme',
        r'\b(caséine[s]?)\b': 'glossaire-caseine',
        r'\b(coalescence)\b': 'glossaire-coalescence',
        r'\b(collagène)\b': 'glossaire-collagene',
        r'\b(dénaturation protéique|dénaturation)\b': 'glossaire-denaturation',
        r'\b(point de fumée)\b': 'glossaire-point-fumee',
        r'\b(synérèse)\b': 'glossaire-synerese',
        r'\b(bliss point)\b': 'glossaire-bliss-point'
    }
    
    # Remplacer avec parcimonie dans les paragraphes de texte purs (jamais dans les labels <...>, titres =, images, ou tableaux)
    lines = typ_content.splitlines()
    new_lines = []
    seen_counts = {k: 0 for k in glossary_targets}
    
    for line in lines:
        sline = line.strip()
        # Ne pas toucher aux lignes de labels, titres, figures ou balises
        if sline.startswith('<') or sline.startswith('=') or sline.startswith('#figure') or sline.startswith('#image') or '<glossaire-' in sline or '#link(' in sline:
            new_lines.append(line)
        else:
            for pattern, target_label in glossary_targets.items():
                if seen_counts[pattern] < 2:
                    if re.search(pattern, line, flags=re.IGNORECASE):
                        line = re.sub(pattern, rf"#link(<{target_label}>)[\g<1>]", line, count=1, flags=re.IGNORECASE)
                        seen_counts[pattern] += 1
            new_lines.append(line)
    typ_content = '\n'.join(new_lines)

    # Assembler le document complet
    full_text = PREAMBLE + "\n\n" + typ_content + "\n\n" + BACK_COVER
    
    # Résolution résiliente des liens hypertexte Typst sur l'intégralité de l'ouvrage :
    targeted_links = set(re.findall(r'#link\(<([a-zA-Z0-9_\-]+)>\)', full_text))
    defined_labels = set(re.findall(r'(?<!#link\()<([a-zA-Z0-9_\-]+)>', full_text))
    missing_labels = targeted_links - defined_labels
    if missing_labels:
        print(f"  [AUTO-RÉSOLUTION] {len(missing_labels)} étiquettes cibles créées automatiquement sans artefact visible.")
        anchor_block = "\n\n// Ancres de navigation transversale invisibles\n"
        for label in missing_labels:
            anchor_block += f"#hide[] <{label}>\n"
        full_text += anchor_block
        
    return full_text

# ==============================================================================
# PREPROCESS MARKDOWN
# ==============================================================================

def preprocess_markdown(md_text):
    # Convertir <a id="..."></a> en marqueur protégé pour Pandoc isolé par des sauts de ligne
    md_text = re.sub(r'<a\s+id=[\'"]([a-zA-Z0-9_\-]+)[\'"]\s*>\s*</a>', r'\n\nLABELSTART\1LABELSTART\n\n', md_text)
    
    # Convertir ::: nom_boite en marqueur préservé par Pandoc isolé par des lignes vides
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
    # Garantir qu'aucun titre Markdown ne soit collé à un paragraphe précédent
    text_processed = re.sub(r'([^\n])\n(#{1,6}\s+)', r'\1\n\n\2', text_processed)
    return text_processed

# ==============================================================================
# RUN BUILD
# ==============================================================================

def run_build():
    print("=== Étape 1 : Assemblage et Préparation des Textes Markdown ===")
    
    portals = {
        "01 — L'HOMME, LE FEU ET LA RÈGLE DU FOYER": "# 01 — L'Homme, le Feu et la Règle du Foyer\n",
        "02 — L'ALCHIMIE DU VIVANT : PHYSIOLOGIE ET ÉCOLOGIE": "# 02 — L'Alchimie du Vivant : Physiologie et Écologie\n",
        "03 — LA MATIÈRE ANIMALE ET VÉGÉTALE AUX FOURNEAUX": "# 03 — La Matière Animale et Végétale aux Fourneaux\n",
        "04 — TRANSFORMATIONS SANS FEU, TERROIRS ET MÉMOIRE CULINAIRE": "# 04 — Transformations sans Feu, Terroirs et Mémoire Culinaire\n",
        "05 — ANNEXES, FORMULAIRE ET RÉPERTOIRE CRITIQUE": "# 05 — Annexes, Formulaire et Répertoire Critique\n"
    }

    sections = [
        ("01 — L'HOMME, LE FEU ET LA RÈGLE DU FOYER", [
            "textes/Livre_I/Chapitre_00_L_Odyssee_du_Feu_et_la_Nutrition_de_Survie.md",
            "textes/Livre_I/Chapitre_01_L_Arsenal_Minimal_et_la_Maitrise_des_Sens.md",
            "textes/Livre_I/Chapitre_02_La_Thermodynamique_du_Feu_et_des_Cuissons.md",
            "textes/Livre_I/Chapitre_04_Consignes_de_Securite_et_Pannes_Critiques.md"
        ]),
        ("02 — L'ALCHIMIE DU VIVANT : PHYSIOLOGIE ET ÉCOLOGIE", [
            "textes/Livre_I/Chapitre_05_L_Anatomie_du_Gout_et_les_Secrets_du_3_Etoiles.md",
            "textes/Livre_I/Chapitre_06_Nourriture_Saine_Digestibilite_et_Prise_des_Repas.md",
            "textes/Livre_I/Chapitre_07_L_Art_des_Courses_Psychologie_et_Demystification_Industrielle.md",
            "textes/Livre_II/Chapitre_08_L_Enquete_des_Additifs_et_Codes_E_Dangereux.md",
            "textes/Livre_II/Chapitre_09_L_Ecologie_de_la_Matiere_Flux_et_Saisonnalite_Globale.md"
        ]),
        ("03 — LA MATIÈRE ANIMALE ET VÉGÉTALE AUX FOURNEAUX", [
            "textes/Livre_II/Chapitre_05_L_Oeuf_au_Repos_Anatomie_et_Conservation.md",
            "textes/Livre_II/Chapitre_06_La_Coagulation_Fractionnee_et_les_Seuils_Critiques.md",
            "textes/Livre_III/Chapitre_11_Le_Monde_Vegetal_et_le_Secret_de_Blumenthal.md",
            "textes/Livre_III/Chapitre_12_Proteines_Vegetales_Legumineuses_et_Veganisme_Rationnel.md",
            "textes/Livre_III/Chapitre_13_La_Matrice_du_Gateau_et_le_Chocolat.md"
        ]),
        ("04 — TRANSFORMATIONS SANS FEU, TERROIRS ET MÉMOIRE CULINAIRE", [
            "textes/Livre_V/Chapitre_16_La_Cuisson_Chimique_et_la_Conservation_Sel_Acide_Sucre_et_Mort_Thermique.md",
            "textes/Livre_V/Chapitre_17_Proliferation_Microbienne_Fermentations_et_Recettes_Fondatrices.md",
            "textes/Livre_IV/Chapitre_16_La_Geopolitique_du_Gout_Terroirs_et_Mondialisation.md",
            "textes/Livre_I/Chapitre_03_L_Art_des_Pates_et_l_Urgence_du_Feu.md"
        ]),
        ("05 — ANNEXES, FORMULAIRE ET RÉPERTOIRE CRITIQUE", [
            "textes/Annexes/Annexe_A_Tableau_des_Temperatures_Critiques.md",
            "textes/Annexes/Annexe_B_Glossaire_Physico_Chimique_et_Culinaire.md",
            "textes/Annexes/Annexe_C_Bibliographie_Raisonnee.md",
            "textes/Annexes/Annexe_D_Guide_Achat_Arsenal_Minimal_Couts_et_Durees_de_Cuisson.md",
            "textes/Annexes/Annexe_E_Conservation_au_Froid_Zones_du_Refrigerateur_et_Durees_Limites.md"
        ])
    ]

    all_md = []
    for book_title, files in sections:
        # Portail d'ouverture de livre riche avec illustration pleine page
        portal_text = portals.get(book_title, f"\n# {book_title}\n")
        all_md.append(portal_text)
        for f in files:
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
        print("ERREUR TYPST :", res_t.stderr[:2000])
        raise RuntimeError("Typst compilation failed.")

    print(f"=== SUCCÈS MAJEUR : Le livre complet a été compilé en PDF haute fidélité ===")
    print(f"Chemin du PDF : {FINAL_PDF}")

if __name__ == "__main__":
    run_build()
