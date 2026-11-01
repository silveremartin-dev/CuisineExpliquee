
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

#let divider() = line(length: 100%, stroke: 0.5pt + c-bronze)

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

#let recto() = {
  [#metadata("fin-section") <fin-section>]
  pagebreak(weak: true, to: "odd")
  [#metadata("debut-section") <debut-section>]
}

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
