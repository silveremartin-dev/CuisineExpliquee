
#set document(
  title: "COOKING DECODED — First Principles, Pure Physics, and Minimalist Tools",
  author: "Silvère-Martin Michiellot & Antigravity"
)

// Noble High-Gastronomy Color Palette
#let c-ink = rgb("#242124")        // Noble deep ink
#let c-charcoal = rgb("#383330")   // Deep charcoal
#let c-slate = rgb("#5c5549")      // Warm slate brown
#let c-bordeaux = rgb("#701c1a")   // Culinary burgundy
#let c-terracotta = rgb("#a3432b") // Rich terracotta
#let c-bronze = rgb("#d4a373")     // Aged bronze / brass gold
#let c-cream = rgb("#fffdfa")      // Soft cream paper background
#let c-sand = rgb("#f7f4eb")       // Soft linen
#let c-olive = rgb("#5a6e54")      // Muted bay-leaf sage
#let c-rust = rgb("#92400e")       // Deep amber

// Page break to odd page with section markers
#let recto() = {
  [#metadata("fin-section") <fin-section>]
  pagebreak(weak: true, to: "odd")
  [#metadata("debut-section") <debut-section>]
}

// Running headers and footers
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
      let title-left = if cur-h1.len() > 0 { cur-h1.last().body } else { [COOKING DECODED] }
      text(font: "Liberation Serif", size: 8.5pt, fill: c-bordeaux, tracking: 0.08em)[
        #smallcaps[#title-left] #h(1fr) #emph[Cooking Decoded]
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
  lang: "en"
)

#set par(justify: true, leading: 0.75em, first-line-indent: 0pt, spacing: 0.88em)

#show heading: set text(hyphenate: false)
#show figure.where(kind: table): set block(breakable: true)
#show figure.caption: it => [
  #v(7pt)
  #text(size: 8.8pt, style: "italic", fill: c-slate, font: "Liberation Serif")[#it]
  #v(13pt)
]

// Interactive Hyperlinks
#show link: it => text(fill: c-terracotta, weight: "medium")[#underline(stroke: 0.5pt + c-bronze, offset: 1.5pt)[#it]]

// Diptych Book Openings: Verso Full Image + Recto Portal
#let portail_livre_verso(img_path, legende_image) = block(width: 100%, height: 100%, fill: rgb("#1c1917"))[
  #align(center + horizon)[
    #v(1.2cm)
    #image(img_path, width: 92%, height: 74%, fit: "contain")
    #v(0.6cm)
    #block(width: 86%, fill: none, inset: (x: 0cm, y: 0cm))[
      #align(left)[
        #text(size: 8.5pt, fill: c-bronze, font: "Liberation Sans", weight: "bold")[BOOK ICONOGRAPHIC OPENING]
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

// Level 1 Headings: Chapters & Appendices
#show heading.where(level: 1): it => {
  pagebreak(weak: true, to: "odd")
  v(0.3cm)
  align(left)[
    #text(size: 9pt, tracking: 0.2em, fill: c-bordeaux, weight: "bold", font: "Liberation Sans")[#smallcaps[Treatise on Culinary Physics & First Principles]]
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

// Didactic Signaletic Boxes
#let chef_tip(body) = block(
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

#let truc_de_chef(body) = chef_tip(body)

#let historical_anecdote(body) = block(
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

#let anecdote_historique(body) = historical_anecdote(body)

#let positive(body) = block(
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

#let positif(body) = positive(body)

#let negative(body) = block(
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

#let negatif(body) = negative(body)

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

#let warning(body) = block(
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

#let point_attention(body) = warning(body)

#let molecular_view(body) = block(
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

#let oeil_molecule(body) = molecular_view(body)

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

#let check_box = box(width: 8pt, height: 8pt, stroke: 0.7pt + c-slate, radius: 1.5pt, baseline: 0.5pt)
#let case_cocher = check_box

// ==========================================
// 1. NOBLE PHOTOGRAPHIC COVER
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
        COOKING DECODED
      ]
      #v(0.3cm)
      #text(size: 13.5pt, weight: "medium", fill: rgb("#fed7aa"), font: "Liberation Sans")[
        First Principles, Pure Physics, and Minimalist Tools
      ]
      #v(0.6cm)
      #line(length: 100%, stroke: 1.5pt + rgb("#f59e0b"))
      #v(0.5cm)
      #text(size: 10pt, fill: rgb("#e7e5e4"), font: "Liberation Serif", style: "italic")[
        A master treatise on anthropology, thermodynamics, and the biology of culinary technique.\
        Understanding raw matter, mastering heat flows, and cooking in sovereign freedom with five tools.
      ]
      #v(0.8cm)
      #grid(
        columns: (1fr, auto),
        align: (left + horizon, right + horizon),
        text(size: 9pt, weight: "bold", fill: rgb("#fcd34d"), font: "Liberation Sans")[
          INTERNATIONAL ANGLOPHONE EDITION — 2026
        ],
        text(size: 8.5pt, fill: rgb("#a8a29e"), font: "Liberation Sans")[
          OPEN ACCESS CC BY-SA 4.0
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

// PAGE 1 — HALF-TITLE (SILENT)
#align(center + horizon)[
  #text(size: 22pt, weight: "bold", fill: c-ink, font: "Liberation Serif", tracking: 0.06em)[COOKING DECODED]
]
#pagebreak()
#box()
#pagebreak()

// PAGE 3 — MAIN TITLE (SILENT)
#align(center)[
  #v(3.5cm)
  #text(size: 12pt, weight: "bold", fill: c-bordeaux, tracking: 0.15em, font: "Liberation Sans")[SILVÈRE-MARTIN MICHIELLOT & ANTIGRAVITY]
  #v(1.6cm)
  #text(size: 32pt, weight: "bold", fill: c-ink, font: "Liberation Serif")[COOKING DECODED]
  #v(0.5cm)
  #line(length: 30%, stroke: 0.5pt + c-bronze)
  #v(0.5cm)
  #text(size: 14pt, fill: c-terracotta, font: "Liberation Serif", style: "italic")[First Principles, Pure Physics,#linebreak()and Minimalist Tools]
  #v(1fr)
  #text(size: 10pt, fill: c-slate, font: "Liberation Sans", tracking: 0.1em)[INTERNATIONAL REFERENCE EDITION — 2026]
  #v(0.2cm)
  #text(size: 9pt, fill: c-slate, font: "Liberation Sans")[Open Access Treatise under Creative Commons CC BY-SA 4.0]
  #v(1.5cm)
]
#pagebreak()

// PAGE 4 — LEGAL NOTICES (SILENT)
#align(bottom)[
  #block(
    fill: rgb("#fafaf9"),
    stroke: 0.5pt + rgb("#e7e5e4"),
    inset: 16pt,
    radius: 6pt,
    width: 100%
  )[
    #text(size: 8.5pt, fill: rgb("#57534e"))[
      *COOKING DECODED — First Principles, Pure Physics, and Minimalist Tools*\
      International Revised & Augmented Edition © 2026 Silvère-Martin Michiellot & Antigravity.\
      \
      *Open Access License:* This treatise is published under the terms of the *Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0)*.\
      *Dual Metrology System:* All measurements are given continuously in dual units: Celsius ($upright("C")$) and Fahrenheit ($upright("F")$), grams ($upright("g")$) and ounces ($upright("oz")$), milliliters/liters and cups/fluid ounces.\
      *Flour & Butter Standardization:* Includes comparative classifications between European ash standards (T45/T55/T65) and Anglo-American protein standards (Pastry/AP/Bread Flour), as well as butterfat variances (82% European vs 80% USDA).\
      *Composition:* Typeset with Typst v0.15.1, Liberation Serif & Liberation Sans open fonts.
    ]
  ]
]
#pagebreak()

// PAGE 5 — INAUGURAL EPIGRAPH (SILENT)
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
      “Cooking is of all the arts the one which has done the most to advance civilization; for the necessities of the kitchen have taught us the use of fire, and it is by fire that man has subdued nature.”
    ]
    #v(8pt)
    #align(right)[#text(size: 9.5pt, weight: "bold", fill: c-terracotta)[— Jean Anthelme Brillat-Savarin, *The Physiology of Taste* (1825)]]
  ]
  #v(2.5cm)
  #text(size: 10.5pt, style: "italic", fill: rgb("#78716c"))[
    To all who seek to free themselves from the tyranny of blind recipes,\
    and reclaim the sovereign liberty of understanding what they do.
  ]
]
#pagebreak()
#box()
#pagebreak()

// TABLE OF CONTENTS
#outline(
  title: [Table of Contents & Analytical Summary],
  indent: 1.5em,
  depth: 2
)

#recto()

// ==========================================
// TABLE OF THE TWENTY-SIX FOUNDATION PROTOCOLS
// ==========================================
#align(left)[
  #text(size: 15pt, weight: "bold", fill: c-bordeaux, font: "Liberation Serif")[
    🍳 Table of the Twenty-Six Foundation Recipes and Protocols
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
    This table brings together the twenty-six step-by-step master protocols described in the treatise. Each protocol is a direct, living application of physical, chemical, and biological principles:

    #v(0.15cm)
    *1. Starches, Grains & Plant Proteins (Book III)*
    - #link(<recette-carbonara-traditionnelle>)[*Protocol 01:* Authentic Spaghetti alla Carbonara (The Golden Starch-Egg Emulsion)] --- _Chapter 09_
    - #link(<recette-dahl-lentilles>)[*Protocol 02:* Comforting Red Lentil Dahl with Toasted Cumin & Coconut] --- _Chapter 09_
    - #link(<recette-tofu-croustillant>)[*Protocol 03:* Ultra-Crispy Pan-Seared Tofu with Tamari-Sesame Glaze] --- _Chapter 09_
    - #link(<recette-pommes-sarladaises>)[*Protocol 04:* Golden Sarladaise Potatoes in Duck Fat & Garlic] --- _Chapter 09_
    - #link(<recette-grand-aioli>)[*Protocol 05:* Provençal Mortar-Crushed Grand Aïoli] --- _Chapter 09_

    #v(0.12cm)
    *2. Plant Mechanics, Cellular Turgor & Salads (Book III)*
    - #link(<recette-puree-blumenthal>)[*Protocol 06:* Silky Potato Purée after Blumenthal & Peel Infusion] --- _Chapter 10_
    - #link(<recette-carottes-glacees>)[*Protocol 07:* Butter-Glazed Carrots under Parchment Cartouche] --- _Chapter 10_
    - #link(<recette-salade-croquante>)[*Protocol 08:* Crisp Market Salad, Ice Shock & Osmotic Vinaigrette] --- _Chapter 11_

    #v(0.12cm)
    *3. Water Chemistry, Noble Stocks & Meat Glazes (Book III)*
    - #link(<recette-bouillon-glace>)[*Protocol 09:* Golden Bone Broth & Pure Collagen Meat Glaze (*Glace de Viande*)] --- _Chapter 12_
    - #link(<recette-consomme-clarifie>)[*Protocol 10:* Crystal-Clear Consommé Clarified with Egg Albumen Raft] --- _Chapter 12_

    #v(0.12cm)
    *4. Animal Searing, Maillard Reactions & Deglazing (Book III)*
    - #link(<recette-steak-fonte>)[*Protocol 11:* Thick Cast-Iron Skillet Steak with Foaming Butter Convection] --- _Chapter 14_
    - #link(<recette-deglacage-minute>)[*Protocol 12:* Flash Pan Deglazing & Pan Sauce Mounted with Cold Butter] --- _Chapter 14_
    - #link(<recette-ceviche-cabillaud>)[*Protocol 13:* Bright Lime-Cured Cod Ceviche with Red Onion & Chili] --- _Chapter 14_

    #v(0.12cm)
    *5. The Archetype of the Egg & Mother Emulsions (Book III)*
    - #link(<recette-oeuf-mollet>)[*Protocol 14:* The Perfect 6-Minute Soft-Boiled Egg & the 64°C / 147°F Egg] --- _Chapter 15_
    - #link(<recette-oeuf-poche>)[*Protocol 15:* Infallible Vinegar-Free Poached Egg through Fine Sieve] --- _Chapter 15_
    - #link(<recette-mayonnaise>)[*Protocol 16:* Foolproof Hand-Whisked Homemade Cold Mayonnaise] --- _Chapter 15_
    - #link(<recette-sauce-hollandaise>)[*Protocol 17:* Velvety Warm Hollandaise Emulsion in a Double Boiler] --- _Chapter 15_
    - #link(<recette-sauce-bechamel>)[*Protocol 18:* White Roux & Lump-Free Silky Béchamel Sauce] --- _Chapter 16_

    #v(0.12cm)
    *6. Fermentations, Wild Breads & Autonomous Dairy (Book IV)*
    - #link(<recette-pain-cocotte>)[*Protocol 19:* Autonomous Artisan No-Knead Dutch Oven Bread] --- _Chapter 17_
    - #link(<recette-pickles-lactofermentes>)[*Protocol 20:* Crunchy Lactofermented Pickles in 3% Saline Brine] --- _Chapter 17_
    - #link(<recette-fromage-frais>)[*Protocol 21:* 15-Minute Homemade Fresh Cheese (82°C / 180°F Acid Curdling)] --- _Chapter 18_

    #v(0.12cm)
    *7. Matrix Pastry, Pyrolysis & Deep Cold (Book IV)*
    - #link(<recette-moelleux-chocolat>)[*Protocol 22:* Molten Dark Chocolate Lava Cake (Thermal Gradient)] --- _Chapter 20_
    - #link(<recette-pate-brisee>)[*Protocol 23:* Pure Butter Shortcrust Pastry (Gluten Inhibition Sablage)] --- _Chapter 20_
    - #link(<recette-mousse-aquafaba>)[*Protocol 24:* Airy Aquafaba Chocolate Mousse (Zero-Egg)] --- _Chapter 20_
    - #link(<recette-omelette-norvegienne>)[*Protocol 25:* Baked Alaska Minute (Air-Insulated Meringue Shield)] --- _Chapter 21_
    - #link(<recette-glace-sel>)[*Protocol 26:* Rapid Ice Cream without Churn via Salt Cryoscopic Depression] --- _Chapter 21_
  ]
]

#metadata("debut-texte") <debut-texte>

#include "en/book1.typ"
#include "en/book2.typ"
#include "en/book3.typ"
#include "en/book4.typ"
#include "en/book5.typ"
#include "en/book6.typ"
#include "en/appendices.typ"
