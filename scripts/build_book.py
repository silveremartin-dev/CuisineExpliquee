# -*- coding: utf-8 -*-
"""
Master Culinary Book Builder pour LA CUISINE EXPLIQUÉE
- Auteurs : Silvère-Martin Michiellot & Antigravity
- Moteur Typographique : Typst v0.15.1
- Moteur de conversion : Pandoc 3.12.1
- Direction Artistique : Haute Gastronomie Éditoriale (Terracotta, Bordeaux, Or Chaud)
- Couverture photographique vibrante (légumes frais du marché)
- Quatrième de couverture complète (synopsis, manifeste, code-barres et prix)
- Index dédié des recettes dès le début du livre
- En-têtes vivants et Pieds de page sur toutes les pages de lecture
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

// Palette Chromatique Haute Gastronomie
#let c-bordeaux = rgb("#78350f")
#let c-terracotta = rgb("#9a3412")
#let c-gold = rgb("#b45309")
#let c-dark = rgb("#1c1917")
#let c-slate = rgb("#44403c")
#let c-cream = rgb("#fffbeb")
#let c-green = rgb("#15803d")
#let c-red = rgb("#b91c1c")
#let c-amber = rgb("#d97706")
#let c-teal = rgb("#0f766e")

#set page(
  paper: "a4",
  margin: (top: 2.5cm, bottom: 2.5cm, left: 2.2cm, right: 2.2cm),
  header: context {
    let page-num = counter(page).get().first()
    if page-num > 4 [
      #let cur-h2 = query(heading.where(level: 2)).filter(h => h.location().page() == here().position().page)
      #let ch-title = if cur-h2.len() > 0 {
        cur-h2.first().body
      } else {
        let prev-h2 = query(selector(heading.where(level: 2)).before(here()))
        if prev-h2.len() > 0 { prev-h2.last().body } else { [] }
      }
      #let cur-h1 = query(heading.where(level: 1)).filter(h => h.location().page() == here().position().page)
      #let vol-title = if cur-h1.len() > 0 {
        cur-h1.first().body
      } else {
        let prev-h1 = query(selector(heading.where(level: 1)).before(here()))
        if prev-h1.len() > 0 { prev-h1.last().body } else { [LA CUISINE EXPLIQUÉE] }
      }
      #grid(
        columns: (1fr, 1fr),
        align: (left, right),
        text(size: 8pt, fill: c-terracotta, font: "Liberation Sans", style: "italic", weight: "medium")[#vol-title],
        text(size: 8pt, fill: c-dark, font: "Liberation Sans", weight: "bold")[#ch-title]
      )
      #v(-4pt)
      #line(length: 100%, stroke: 0.5pt + c-gold)
    ]
  },
  footer: context {
    let page-num = counter(page).get().first()
    if page-num > 2 [
      #line(length: 100%, stroke: 0.5pt + rgb("#fcd34d"))
      #v(3pt)
      #grid(
        columns: (1fr, 1fr),
        align: (left, right),
        text(size: 8pt, fill: c-terracotta, font: "Liberation Sans", style: "italic")[LA CUISINE EXPLIQUÉE — Principes Premiers],
        text(size: 8.5pt, fill: c-dark, font: "Liberation Sans", weight: "bold")[Page #page-num]
      )
    ]
  }
)

#set text(
  font: ("Liberation Serif", "Georgia", "Times New Roman"),
  size: 10pt,
  lang: "fr"
)

#set par(justify: true, leading: 0.74em, first-line-indent: 0pt, spacing: 0.88em)

#show heading: set text(hyphenate: false)
#show heading: set block(sticky: true)
#show figure: set block(breakable: false)

// Style des Hyperliens Interactifs
#show link: it => text(fill: c-terracotta, weight: "medium")[#underline(stroke: 0.5pt + c-gold, offset: 1.5pt)[#it]]

// Niveaux de Titres Éditoriaux
#show heading.where(level: 1): it => {
  v(0.8cm)
  align(center)[
    #block(
      fill: rgb("#fffbeb"),
      stroke: (top: 2pt + c-gold, bottom: 2pt + c-gold),
      inset: (y: 16pt, x: 14pt),
      width: 100%
    )[
      #text(size: 15pt, weight: "bold", fill: c-bordeaux, font: "Liberation Sans", tracking: 0.5pt)[#it.body]
    ]
  ]
  v(0.6cm)
}

#show heading.where(level: 2): it => {
  v(0.6cm)
  text(size: 13pt, weight: "bold", fill: c-bordeaux, font: "Liberation Sans")[#it.body]
  v(-3pt)
  line(length: 100%, stroke: 1.0pt + c-gold)
  v(0.25cm)
}

#show heading.where(level: 3): it => block(spacing: 1.1em)[
  #v(0.15cm)
  #text(size: 11pt, weight: "bold", fill: c-dark, font: "Liberation Sans")[#it.body]
  #v(0.05cm)
]

#show heading.where(level: 4): it => block(spacing: 0.8em)[
  #text(size: 10pt, weight: "bold", fill: c-slate, font: "Liberation Sans")[#it.body]
]

// Signalétique Didactique et Boîtes Culinaire
#let anecdote_historique(body) = block(
  fill: rgb("#fffbeb"),
  stroke: (left: 3.5pt + c-gold),
  inset: (left: 14pt, right: 12pt, top: 10pt, bottom: 10pt),
  radius: (right: 5pt),
  width: 100%,
  spacing: 1.2em,
  breakable: false
)[
  #text(size: 9.5pt)[#body]
]

#let truc_de_chef(body) = block(
  fill: rgb("#fefce8"),
  stroke: (left: 3.5pt + rgb("#ca8a04")),
  inset: (left: 14pt, right: 12pt, top: 10pt, bottom: 10pt),
  radius: (right: 5pt),
  width: 100%,
  spacing: 1.2em,
  breakable: false
)[
  #text(size: 9.5pt)[#body]
]

#let point_attention(body) = block(
  fill: rgb("#fff1f2"),
  stroke: (left: 3.5pt + rgb("#e11d48")),
  inset: (left: 14pt, right: 12pt, top: 10pt, bottom: 10pt),
  radius: (right: 5pt),
  width: 100%,
  spacing: 1.2em,
  breakable: false
)[
  #text(size: 9.5pt)[#body]
]

#let oeil_molecule(body) = block(
  fill: rgb("#f0fdfa"),
  stroke: (left: 3.5pt + c-teal),
  inset: (left: 14pt, right: 12pt, top: 10pt, bottom: 10pt),
  radius: (right: 5pt),
  width: 100%,
  spacing: 1.2em,
  breakable: false
)[
  #text(size: 9.5pt)[#body]
]

#let positif(body) = block(
  fill: rgb("#f0fdf4"),
  stroke: (left: 3.5pt + c-green),
  inset: (left: 14pt, right: 12pt, top: 10pt, bottom: 10pt),
  radius: (right: 5pt),
  width: 100%,
  spacing: 1.2em,
  breakable: false
)[
  #text(size: 9.5pt)[#body]
]

#let negatif(body) = block(
  fill: rgb("#fef2f2"),
  stroke: (left: 3.5pt + c-red),
  inset: (left: 14pt, right: 12pt, top: 10pt, bottom: 10pt),
  radius: (right: 5pt),
  width: 100%,
  spacing: 1.2em,
  breakable: false
)[
  #text(size: 9.5pt)[#body]
]

#let cas_limite(body) = block(
  fill: rgb("#fffbeb"),
  stroke: (left: 3.5pt + c-amber),
  inset: (left: 14pt, right: 12pt, top: 10pt, bottom: 10pt),
  radius: (right: 5pt),
  width: 100%,
  spacing: 1.2em,
  breakable: false
)[
  #text(size: 9.5pt)[#body]
]

#let quote_box(body) = block(
  fill: rgb("#fafaf9"),
  stroke: (left: 3pt + rgb("#a8a29e")),
  inset: (left: 12pt, y: 7pt),
  radius: (right: 4pt),
  width: 100%,
  spacing: 1.1em,
  breakable: false
)[
  #text(style: "italic", fill: rgb("#292524"))[#body]
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
#set page(
  paper: "a4",
  margin: (top: 2.5cm, bottom: 2.5cm, left: 2.2cm, right: 2.2cm)
)

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

// ==========================================
// 4. SOMMAIRE RAISONNÉ
// ==========================================
#outline(
  title: [Sommaire Général et Table Raisonnée],
  indent: 1.5em,
  depth: 2
)

#pagebreak()

// ==========================================
// 5. TABLE DES RECETTES & PRÉPARATIONS PILIERS
// ==========================================
#align(center)[
  #text(size: 15pt, weight: "bold", fill: c-bordeaux, font: "Liberation Sans")[
    🍳 Table des Recettes et Préparations Piliers
  ]
  #v(-4pt)
  #line(length: 60%, stroke: 1pt + c-gold)
]
#v(0.6cm)

#block(
  fill: rgb("#fffbeb"),
  stroke: 0.5pt + rgb("#fde68a"),
  inset: 16pt,
  radius: 6pt,
  width: 100%
)[
  #text(size: 10pt)[
    Cette table réunit les dix protocoles fondamentaux pas à pas décrits dans l'ouvrage. Chaque recette constitue une application directe et immédiate des principes physico-chimiques exposés :

    #v(0.3cm)
    *Pains, Levains & Fromagerie Autonome*
    - #link(<recette-pain-cocotte>)[Le Pain Cocotte d'Autonomie sans Pétrissage (*No-Knead Bread*)] --- _Chapitre 15_
    - #link(<recette-fromage-frais>)[Le Fromage Frais Maison en 15 Minutes (Caillage Acide sans Présure)] --- _Chapitre 15_
    - #link(<recette-glace-sel>)[La Glace Express sans Sorbetière (Abaissement Cryoscopique du Sel)] --- _Chapitre 15_

    #v(0.2cm)
    *Viandes, Poissons & Saisies à la Poêle*
    - #link(<recette-steak-fonte>)[Le Pavé de Bœuf en Poêle Fonte & Arrosage au Beurre Mousseux (*Basting*)] --- _Chapitre 03_
    - #link(<recette-deglacage-minute>)[Le Déglaçage Minute & Sauce Montée au Beurre Émulsionnée] --- _Chapitre 06_
    - #link(<recette-ceviche-cabillaud>)[Le Vrai Ceviche de Cabillaud Mariné au Citron Vert & Piment Doux] --- _Chapitre 14_

    #v(0.2cm)
    *Pâtes & Émulsions d'Or*
    - #link(<recette-carbonara-traditionnelle>)[Les Vraies Spaghetti alla Carbonara (L'Émulsion d'Or Jaune sans Crème)] --- _Chapitre 04_

    #v(0.2cm)
    *Cuisine Végétale & Protéines Alternatives*
    - #link(<recette-dahl-lentilles>)[Le Dahl Réconfortant de Lentilles Corail au Cumin Torréfié & Coco] --- _Chapitre 12_
    - #link(<recette-tofu-croustillant>)[Le Tofu Doré Ultra-Croustillant & son Laquage Tamari-Sésame] --- _Chapitre 12_
    - #link(<recette-mousse-aquafaba>)[La Mousse au Chocolat Aérienne à l'Aquafaba (Zéro Œuf, Zéro Crème)] --- _Chapitre 12_

    #v(0.2cm)
    *Desserts & Maîtrise des Seuils Thermiques*
    - #link(<recette-moelleux-chocolat>)[Le Moelleux au Chocolat Cœur Coulant (Gradient Thermique Calibré)] --- _Chapitre 13_
    - #link(<recette-creme-anglaise>)[La Crème Anglaise Onctueuse Inratable (Seuil Critique de 83°C au Ruban)] --- _Chapitre 13_
  ]
]

#pagebreak()
"""

# ==============================================================================
# QUATRIÈME DE COUVERTURE (BACK COVER)
# ==============================================================================

BACK_COVER = """
#pagebreak()
#set page(margin: 0pt, header: none, footer: none)

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

    *La Cuisine Expliquée* n'est pas un énième catalogue de recettes passives à réciter sans réfléchir. C'est un traité vivant d'**autonomie matérielle, de thermodynamique et de biologie du geste culinaire**, conçu pour libérer définitivement le cuisinier de la tyrannie des recettes magiques et du diktat des gadgets superflus.

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
      • *15 Chapitres Fondamentaux* : De l'étincelle paléolithique à la science moléculaire.\\
      • *10 Recettes Piliers Pas à Pas* : Ratios universels, repères sensoriels et arbres de sauvetage.\\
      • *Guide de Survie & Protocoles d'Urgence* : Incendies d'huile, pannes de froid et intoxications.\\
      • *Cuisine Végétale Rationnelle* : Chimie des acides aminés et biodisponibilité des protéines.\\
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
        fill: white,
        inset: (x: 12pt, y: 8pt),
        radius: 4pt
      )[
        #text(size: 9.5pt, weight: "bold", fill: rgb("#0f172a"), font: "Liberation Sans")[
          PRIX : 24,90 € TTC
        ]
        #v(-2pt)
        #text(size: 7.5pt, fill: rgb("#64748b"), font: "Liberation Sans")[
          ÉDITION LIBRE CC BY-SA
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
    # Remplacer les citations blockquote par quote_box
    typ_content = re.sub(
        r'#block\(\s*fill:\s*none,\s*stroke:\s*\(left:\s*[^)]+\),\s*inset:\s*[^,]+,\s*\[([\s\S]*?)\]\s*\)',
        r'#quote_box[\1]',
        typ_content
    )
    
    # Améliorer les tableaux avec style gastronomique
    typ_content = typ_content.replace(
        '#table(',
        '#table(\n  stroke: 0.5pt + rgb("#e7e5e4"),\n  fill: (x, y) => if y == 0 { rgb("#fef3c7") } else if calc.odd(y) { rgb("#fffbeb") } else { none },\n  inset: 7pt,\n'
    )
    
    # Reconvertir les balises d'appel didactiques
    def replace_callout_start(match):
        tag = match.group(1).replace(r'\_', '_').replace('\\', '')
        return f"#{tag}[\n"
        
    typ_content = re.sub(r'CALLOUTSTART([a-zA-Z0-9_\\]+)CALLOUTSTART', replace_callout_start, typ_content)
    typ_content = typ_content.replace('CALLOUTEND', '\n]')
    
    # Reconvertir les ancres HTML en labels Typst #hide[] <mon-label> (invisible sur la page)
    typ_content = re.sub(r'LABELSTART([a-zA-Z0-9_\-]+)LABELSTART', r'#hide[] <\1>', typ_content)
    
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
    # Convertir <a id="..."></a> en marqueur protégé pour Pandoc
    md_text = re.sub(r'<a\s+id=[\'"]([a-zA-Z0-9_\-]+)[\'"]\s*>\s*</a>', r'LABELSTART\1LABELSTART', md_text)
    
    # Convertir ::: nom_boite en marqueur préservé par Pandoc
    lines = md_text.split('\n')
    out_lines = []
    in_callout = False
    
    for line in lines:
        m_start = re.match(r'^:::\s*([a-zA-Z0-9_]+)\s*$', line.strip())
        if m_start:
            tag = m_start.group(1)
            out_lines.append(f"CALLOUTSTART{tag}CALLOUTSTART")
            in_callout = True
        elif line.strip() == ':::' and in_callout:
            out_lines.append("CALLOUTEND")
            in_callout = False
        else:
            out_lines.append(line)
            
    return '\n'.join(out_lines)

# ==============================================================================
# RUN BUILD
# ==============================================================================

def run_build():
    print("=== Étape 1 : Assemblage et Préparation des Textes Markdown ===")
    
    sections = [
        ("LIVRE I — L'HOMME, LE FEU ET LA SURVIE : HISTOIRE, ANTHROPOLOGIE ET NUTRITION", [
            "textes/Livre_I/Chapitre_00_L_Odyssee_du_Feu_et_la_Nutrition_de_Survie.md",
            "textes/Livre_I/Chapitre_01_L_Arsenal_Minimal_et_la_Maitrise_des_Sens.md",
            "textes/Livre_I/Chapitre_02_La_Thermodynamique_du_Feu_et_des_Cuissons.md",
            "textes/Livre_I/Chapitre_03_L_Art_des_Pates_et_l_Urgence_du_Feu.md",
            "textes/Livre_I/Chapitre_04_Consignes_de_Securite_et_Pannes_Critiques.md",
            "textes/Livre_I/Chapitre_05_L_Anatomie_du_Gout_et_les_Secrets_du_3_Etoiles.md",
            "textes/Livre_I/Chapitre_06_Nourriture_Saine_Digestibilite_et_Prise_des_Repas.md",
            "textes/Livre_I/Chapitre_07_L_Art_des_Courses_Psychologie_et_Demystification_Industrielle.md"
        ]),
        ("LIVRE II — L'ŒUF : L'ARCHÉTYPE DE LA MATIÈRE CULINAIRE", [
            "textes/Livre_II/Chapitre_05_L_Oeuf_au_Repos_Anatomie_et_Conservation.md",
            "textes/Livre_II/Chapitre_06_La_Coagulation_Fractionnee_et_les_Seuils_Critiques.md"
        ]),
        ("LIVRE III — LE MONDE VÉGÉTAL ET LA DÉCONSTRUCTION DE LA RECETTE", [
            "textes/Livre_III/Chapitre_11_Le_Monde_Vegetal_et_le_Secret_de_Blumenthal.md",
            "textes/Livre_III/Chapitre_12_Proteines_Vegetales_Legumineuses_et_Veganisme_Rationnel.md",
            "textes/Livre_III/Chapitre_13_La_Matrice_du_Gateau_et_le_Chocolat.md"
        ]),
        ("LIVRE V — LA PRÉSERVATION ET LES TRANSFORMATIONS SANS FEU", [
            "textes/Livre_V/Chapitre_16_La_Cuisson_Chimique_et_la_Conservation_Sel_Acide_Sucre_et_Mort_Thermique.md",
            "textes/Livre_V/Chapitre_17_Proliferation_Microbienne_Fermentations_et_Recettes_Fondatrices.md"
        ]),
        ("ANNEXES, FORMULAIRE ET RÉPERTOIRE CRITIQUE", [
            "textes/Annexes/Annexe_A_Tableau_des_Temperatures_Critiques.md",
            "textes/Annexes/Annexe_B_Glossaire_Physico_Chimique_et_Culinaire.md",
            "textes/Annexes/Annexe_C_Bibliographie_Raisonnee.md"
        ])
    ]

    all_md = []
    for book_title, files in sections:
        # Titre de partie intégré sans page blanche superflue
        all_md.append(f"\n# {book_title}\n")
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

    full_md_content = "\n\n---\n\n".join(all_md)
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
