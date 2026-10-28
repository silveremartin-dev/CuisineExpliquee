# -*- coding: utf-8 -*-
"""
Master Book Builder pour LA CUISINE EXPLIQUÉE
- Auteurs : Silvère-Martin Michiellot & Antigravity
- Typst Engine : Typst 0.15.1
- Pandoc Engine : Pandoc 3.12.1
- Sommaire interactif cliquable depth 2
- En-têtes vivants d'orientation et pieds de page
- Charte chromatique fonctionnelle (vert positif, rouge négatif, ambre cas limites)
"""

import os
import glob
import re
import subprocess
import sys

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
# PREAMBLE TYPST
# ==============================================================================

PREAMBLE = """
#set document(
  title: "LA CUISINE EXPLIQUÉE — Principes Premiers, Maîtrise de la Matière et Minimalisme Instrumental",
  author: "Silvère-Martin Michiellot & Antigravity"
)

#set page(
  paper: "a4",
  margin: (top: 2.4cm, bottom: 2.4cm, left: 2.2cm, right: 2.2cm),
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
        text(size: 8pt, fill: rgb("#64748b"), font: "Liberation Sans", style: "italic")[#vol-title],
        text(size: 8pt, fill: rgb("#0f172a"), font: "Liberation Sans", weight: "bold")[#ch-title]
      )
      #v(-4pt)
      #line(length: 100%, stroke: 0.5pt + rgb("#cbd5e1"))
    ]
  },
  footer: context {
    let page-num = counter(page).get().first()
    if page-num > 2 [
      #line(length: 100%, stroke: 0.5pt + rgb("#cbd5e1"))
      #v(3pt)
      #grid(
        columns: (1fr, 1fr),
        align: (left, right),
        text(size: 8pt, fill: rgb("#94a3b8"), font: "Liberation Sans", style: "italic")[LA CUISINE EXPLIQUÉE — Principes Premiers],
        text(size: 8.5pt, fill: rgb("#0f172a"), font: "Liberation Sans", weight: "bold")[Page #page-num]
      )
    ]
  }
)

#set text(
  font: ("Liberation Serif", "Georgia", "Times New Roman"),
  size: 10pt,
  lang: "fr"
)

#set par(justify: true, leading: 0.72em, first-line-indent: 0pt, spacing: 0.85em)

#show heading: set text(hyphenate: false)
#show heading: set block(sticky: true)
#show figure: set block(breakable: false)

// Palette Sémantique
#let c-red = rgb("#dc2626")
#let c-blue = rgb("#2563eb")
#let c-green = rgb("#16a34a")
#let c-amber = rgb("#d97706")
#let c-dark = rgb("#0f172a")
#let c-slate = rgb("#334155")

// Design des Niveaux de Titres
#show heading.where(level: 1): it => {
  pagebreak()
  v(1.2cm)
  align(center)[
    #block(
      fill: rgb("#f8fafc"),
      stroke: 2.5pt + c-blue,
      inset: 22pt,
      radius: 8pt,
      width: 100%
    )[
      #text(size: 17pt, weight: "bold", fill: c-dark, font: "Liberation Sans")[#it.body]
    ]
  ]
  v(1.0cm)
}

#show heading.where(level: 2): it => {
  v(0.6cm)
  text(size: 14pt, weight: "bold", fill: c-blue, font: "Liberation Sans")[#it.body]
  v(-3pt)
  line(length: 100%, stroke: 1.5pt + c-blue)
  v(0.3cm)
}

#show heading.where(level: 3): it => block(spacing: 1.2em)[
  #v(0.2cm)
  #text(size: 11.5pt, weight: "bold", fill: c-dark, font: "Liberation Sans")[#it.body]
  #v(0.1cm)
]

#show heading.where(level: 4): it => block(spacing: 0.9em)[
  #text(size: 10.5pt, weight: "bold", fill: c-slate, font: "Liberation Sans")[#it.body]
]

// Boîtes Didactiques Spécialisées
#let positif(title: [✓ Ce qu'il faut faire], body) = block(
  fill: rgb("#f0fdf4"),
  stroke: (left: 4pt + c-green),
  inset: (left: 14pt, right: 12pt, top: 10pt, bottom: 10pt),
  radius: (right: 6pt),
  width: 100%,
  spacing: 1.2em,
  breakable: false
)[
  #block(sticky: true, width: 100%)[
    #text(size: 10.5pt, weight: "bold", fill: c-green, font: "Liberation Sans")[#title]
    #v(3pt)
  ]
  #body
]

#let negatif(title: [✗ Ce qu'il faut absolument éviter], body) = block(
  fill: rgb("#fef2f2"),
  stroke: (left: 4pt + c-red),
  inset: (left: 14pt, right: 12pt, top: 10pt, bottom: 10pt),
  radius: (right: 6pt),
  width: 100%,
  spacing: 1.2em,
  breakable: false
)[
  #block(sticky: true, width: 100%)[
    #text(size: 10.5pt, weight: "bold", fill: c-red, font: "Liberation Sans")[#title]
    #v(3pt)
  ]
  #body
]

#let cas_limite(title: [🛠️ Le Laboratoire des Cas Limites], body) = block(
  fill: rgb("#fffbeb"),
  stroke: (left: 4pt + c-amber),
  inset: (left: 14pt, right: 12pt, top: 10pt, bottom: 10pt),
  radius: (right: 6pt),
  width: 100%,
  spacing: 1.2em,
  breakable: false
)[
  #block(sticky: true, width: 100%)[
    #text(size: 10.5pt, weight: "bold", fill: c-amber, font: "Liberation Sans")[#title]
    #v(3pt)
  ]
  #body
]

#let quote_box(body) = block(
  fill: rgb("#f8fafc"),
  stroke: (left: 3pt + rgb("#94a3b8")),
  inset: (left: 12pt, y: 7pt),
  radius: (right: 4pt),
  width: 100%,
  spacing: 1.1em,
  breakable: false
)[
  #text(style: "italic", fill: rgb("#334155"))[#body]
]

// ==========================================
// 1. COUVERTURE OFFICIELLE DE RÉFÉRENCE
// ==========================================
#set page(header: none, footer: none)

#align(center + horizon)[
  #block(
    fill: rgb("#0f172a"),
    inset: 32pt,
    radius: 14pt,
    width: 95%
  )[
    #v(0.6cm)
    #text(size: 13pt, weight: "bold", fill: rgb("#fbbf24"), tracking: 2pt, font: "Liberation Sans")[
      SILVÈRE-MARTIN MICHIELLOT & ANTIGRAVITY
    ]
    #v(1.0cm)
    #text(size: 30pt, weight: "bold", fill: white, font: "Liberation Serif")[
      LA CUISINE EXPLIQUÉE
    ]
    #v(0.3cm)
    #text(size: 14pt, weight: "bold", fill: rgb("#93c5fd"), font: "Liberation Sans")[
      Principes Premiers, Maîtrise de la Matière et Minimalisme Instrumental
    ]
    #v(0.8cm)
    #line(length: 60%, stroke: 2pt + rgb("#f59e0b"))
    #v(0.8cm)
    #text(size: 10.5pt, fill: rgb("#e2e8f0"), font: "Liberation Serif", style: "italic")[
      Traité de physique, de chimie et de gestuelle appliquée aux fourneaux.\\
      De l'étincelle paléolithique à la thermodynamique des émulsions et des chairs.\\
      Apprendre à dompter le feu et les ingrédients avec cinq ustensiles fondamentaux.
    ]
    #v(1.2cm)
    #block(
      fill: rgb("#1e293b"),
      inset: (x: 18pt, y: 10pt),
      radius: 6pt
    )[
      #text(size: 9.5pt, weight: "bold", fill: rgb("#38bdf8"), font: "Liberation Sans")[
        ÉDITION INTÉGRALE DE RÉFÉRENCE — 2026
      ]
    ]
    #v(0.6cm)
  ]
]

#pagebreak()

// ==========================================
// 2. PAGE DE COPYRIGHT ET MENTIONS
// ==========================================
#align(bottom)[
  #block(
    fill: rgb("#f8fafc"),
    stroke: 0.5pt + rgb("#cbd5e1"),
    inset: 16pt,
    radius: 6pt,
    width: 100%
  )[
    #text(size: 8.5pt, fill: rgb("#475569"))[
      *LA CUISINE EXPLIQUÉE — Principes Premiers, Maîtrise de la Matière et Minimalisme Instrumental*\\
      © 2026 Silvère-Martin Michiellot & Antigravity.\\
      \\
      *Licence Libre :* Cet ouvrage est mis à disposition sous licence *Creative Commons Attribution - Partage dans les Mêmes Conditions 4.0 International (CC BY-SA 4.0)*.\\
      Vous êtes libre de partager, copier, distribuer et adapter ce traité sous réserve de citer expressément les auteurs et de diffuser l'œuvre dérivée sous une licence identique.\\
      \\
      *Conception didactique et scientifique :* Silvère-Martin Michiellot & Antigravity.\\
      *Illustrations vectorielles :* Antigravity Visual Engine (norme SVG Byrne-Culinaire).\\
      *Typographie et composition :* Moteur Typst 0.15.1.\\
      *Dépôt officiel du code source et des figures :* Dépôt GitHub public.
    ]
  ]
]

#pagebreak()

// ==========================================
// 3. CITATION INAUGURALE
// ==========================================
#align(center)[
  #v(4.0cm)
  #block(
    fill: rgb("#f8fafc"),
    inset: 24pt,
    radius: 8pt,
    stroke: 1pt + rgb("#e2e8f0"),
    width: 85%
  )[
    #text(size: 11pt, style: "italic", fill: rgb("#334155"))[
      « La cuisine est le plus ancien des arts ; car Adam naquit à jeun, et le nouveau-né, à peine venu au monde, pousse des cris que le sein de sa nourrice peut seul apaiser. C'est de tous les arts celui qui nous rend les services les plus continus et les plus nécessaires à la vie. »
    ]
    #v(8pt)
    #align(right)[#text(size: 9.5pt, weight: "bold", fill: c-blue)[— Jean Anthelme Brillat-Savarin, *Physiologie du goût* (1825)]]
  ]
  #v(2.5cm)
  #text(size: 10.5pt, style: "italic", fill: rgb("#475569"))[
    À toutes celles et ceux qui désirent s'affranchir de la tyrannie des recettes aveugles,\\
    et retrouver la liberté souveraine de comprendre ce qu'ils font.
  ]
]

#pagebreak()

// ==========================================
// 4. SOMMAIRE DÉTAILLÉ
// ==========================================
#outline(
  title: [Sommaire Général et Table Raisonnée],
  indent: 1.5em,
  depth: 2
)

#pagebreak()
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
    
    # Améliorer les tableaux
    typ_content = typ_content.replace(
        '#table(',
        '#table(\n  stroke: 0.5pt + rgb("#cbd5e1"),\n  fill: (x, y) => if y == 0 { rgb("#f1f5f9") } else if calc.odd(y) { rgb("#f8fafc") } else { none },\n  inset: 7pt,\n'
    )
    
    return PREAMBLE + "\n\n" + typ_content

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
        all_md.append(f"\n# {book_title}\n")
        for f in files:
            full_path = os.path.join(BASE_DIR, f)
            if os.path.exists(full_path):
                print(f"  -> Lecture : {f}")
                with open(full_path, "r", encoding="utf-8") as file:
                    content = file.read()
                all_md.append(content)
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
