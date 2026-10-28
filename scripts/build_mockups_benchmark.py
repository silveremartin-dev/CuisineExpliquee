import os, subprocess

TYPST_BIN = r"C:\Users\silve\AppData\Local\Microsoft\WinGet\Packages\Typst.Typst_Microsoft.Winget.Source_8wekyb3d8bbwe\typst-x86_64-pc-windows-msvc\typst.exe"

content = """
// ==============================================================================
// BENCHMARK DE MAQUETTES ÉDITORIALES — 5 STYLES CULINAIRES x 5 PAGES (25 PAGES)
// ==============================================================================

#set document(title: "Benchmark de Maquettes Éditoriales — La Cuisine Expliquée", author: "La Cuisine Expliquée")

// ==============================================================================
// STYLE 1 : LE GRAND TRAITÉ ÉTOILÉ (Haute Gastronomie Classique & Prestige)
// 5 PAGES (Pages 1 à 5)
// ==============================================================================

#let style1(body) = {
  set page(
    paper: "a4",
    margin: (top: 2.5cm, bottom: 2.5cm, left: 2.2cm, right: 2.2cm),
    header: locate(loc => {
      text(font: "Linux Libertine", size: 8.5pt, fill: rgb("#701c1a"), tracking: 0.1em)[
        #smallcaps[Style 1 : Le Grand Traité Étoilé] #h(1fr) #emph[La Cuisine Expliquée]
      ]
    }),
    footer: locate(loc => {
      align(center)[#text(font: "Linux Libertine", size: 9pt, fill: rgb("#701c1a"))[— #loc.page() —]]
    }),
    fill: rgb("#fffdfa")
  )
  set text(font: "Linux Libertine", size: 10pt, fill: rgb("#242124"), lang: "fr")
  set par(justify: true, leading: 0.75em)
  body
}

#let style2(body) = {
  set page(
    paper: "a4",
    margin: (top: 2.2cm, bottom: 2.2cm, left: 2.2cm, right: 4.8cm), // Marge active à droite !
    header: locate(loc => {
      text(font: "Liberation Sans", size: 8.5pt, fill: rgb("#a3432b"), weight: "bold")[
        STYLE 2 : MAGAZINE BISTRONOMIQUE #h(1fr) #text(weight: "regular", fill: rgb("#64748b"))[PAGE ACTIVE #loc.page()]
      ]
    }),
    footer: none,
    fill: rgb("#faf7f2")
  )
  set text(font: "Liberation Sans", size: 9.5pt, fill: rgb("#1e293b"), lang: "fr")
  set par(justify: true, leading: 0.7em)
  body
}

#let style3(body) = {
  set page(
    paper: "a4",
    margin: (top: 2.2cm, bottom: 2.2cm, left: 2.2cm, right: 2.2cm),
    header: locate(loc => {
      text(font: "Liberation Mono", size: 8pt, fill: rgb("#0369a1"))[
        [EXP-LAB // STYLE 3 : THE FOOD LAB & MODERNIST PROTOCOLS] #h(1fr) [SEC: 04 // P.#loc.page()]
      ]
    }),
    footer: locate(loc => {
      line(length: 100%, stroke: 0.5pt + rgb("#0284c7"))
      v(2pt)
      text(font: "Liberation Mono", size: 7.5pt, fill: rgb("#64748b"))[Cuisine Expliquée / Rigueur Moléculaire et Métrologique]
    }),
    fill: rgb("#f8fafc")
  )
  set text(font: "Liberation Sans", size: 9.5pt, fill: rgb("#0f172a"), lang: "fr")
  set par(justify: true, leading: 0.68em)
  body
}

#let style4(body) = {
  set page(
    paper: "a4",
    margin: (top: 2.5cm, bottom: 2.5cm, left: 2.5cm, right: 2.5cm),
    header: locate(loc => {
      text(font: "Linux Libertine", style: "italic", size: 9pt, fill: rgb("#556b2f"))[
        Carnet d'Atelier & Terroirs Vivants #h(1fr) Feuille #loc.page()
      ]
    }),
    footer: locate(loc => {
      align(center)[#text(font: "Linux Libertine", size: 9pt, fill: rgb("#78350f"))[~ #loc.page() ~]]
    }),
    fill: rgb("#f5f2eb") // Teinte lin chaud
  )
  set text(font: "Linux Libertine", size: 10.5pt, fill: rgb("#2d2926"), lang: "fr")
  set par(justify: true, leading: 0.8em)
  body
}

#let style5(body) = {
  set page(
    paper: "a4",
    margin: (top: 3.2cm, bottom: 3.2cm, left: 3cm, right: 3cm), // Respirations gigantesques
    header: none,
    footer: locate(loc => {
      text(font: "Liberation Sans", size: 8.5pt, fill: rgb("#94a3b8"), tracking: 0.2em)[#loc.page()]
    }),
    fill: rgb("#ffffff")
  )
  set text(font: "Liberation Sans", size: 9pt, fill: rgb("#000000"), lang: "fr")
  set par(justify: true, leading: 0.85em)
  body
}

// ------------------------------------------------------------------------------
// STYLE 1 : GRAND TRAITÉ ÉTOILÉ (PAGES 1 À 5)
// ------------------------------------------------------------------------------
#show: style1

// Page 1 : Ouverture de Livre
#v(1cm)
#align(center)[
  #text(size: 11pt, tracking: 0.25em, fill: rgb("#701c1a"), weight: "bold")[LIVRE PREMIER]\
  #v(8pt)
  #text(size: 24pt, weight: "bold", fill: rgb("#242124"))[L'Homme, le Feu et la Règle du Foyer]\
  #v(10pt)
  #line(length: 25%, stroke: 1pt + rgb("#d4a373"))
  #v(10pt)
  #text(size: 10pt, style: "italic", fill: rgb("#5c5549"))[
    « L'homme ne devient véritablement humain que le jour où il cesse d'ingérer la chair crue\\
    pour la soumettre à la médiation alchimique de la braise. »\
    — Claude Lévi-Strauss
  ]
]

#v(1.5cm)
#columns(2, gutter: 18pt)[
  #dropcap(height: 2, gap: 4pt)[A]vant la casserole et avant le fournil, la cuisine est une conquête thermodynamique de l'espèce humaine. Richard Wrangham, dans ses travaux fondamentaux sur l'évolution, a démontré que l'invention du feu n'a pas seulement modifié notre régime : elle a remodelé notre tube digestif et permis l'expansion de notre néocortex.

  En cuisant les fibres végétales et le collagène coriace des viandes, le feu opère une prédigestion externe. L'énergie autrefois perdue à mâcher pendant six heures quotidiennes devient instantanément disponible pour le cerveau. 
]

#v(1cm)
#figure(
  image("figures/nourriture/steak_poele_fonte.jpg", width: 90%),
  caption: [La saisie en fonte brute : maîtrise du flux thermique à 180°C.]
)

#pagebreak()

// Page 2 : Théorie & Tableau comparatif
#heading(level: 2)[1. La Thermodynamique du Feu : Le Transfert Conductif]
#v(6pt)
La matière culinaire obéit strictement aux lois de Fourier et de Stefan-Boltzmann. Lorsqu'un steak de bœuf entre en contact avec la fonte chaude, le flux thermique surfacique $Phi$ s'exprime par :
$ Phi = - lambda dot (diff T) / (diff x) $
Ce gradient détermine la vitesse de formation de la croûte dorée sans calcination des tissus profonds.

#v(12pt)
#align(center)[
  #table(
    columns: (30%, 35%, 35%),
    stroke: 0.5pt + rgb("#d4a373"),
    fill: (x, y) => if y == 0 { rgb("#f2ece1") } else if calc.odd(y) { rgb("#faf7f2") } else { none },
    inset: 8pt,
    table.header([Paramètre Opératoire], [Le Geste Vertueux (À Faire)], [L'Écueil Critique (À Éviter)]),
    [#strong[Température Poêle]], [Préchauffer à sec à $190^\circ\mathrm{C}$ jusqu'à perle de Leidenfrost.], [Poser la viande dans une poêle tiède ($<120^\circ\mathrm{C}$) qui fait bouillir l'eau.],
    [#strong[Séchage Chair]], [Tamponner la viande au papier absorbant avant saisie.], [Saisir une viande humide : l'énergie sert à évaporer l'eau sans colorer.],
    [#strong[Repos Post-Cuisson]], [Laisser reposer sous cloche tiède $5\text{ min}$ (redistribution des sucs).], [Couper immédiatement : les fibres sous tension expulsent tout le jus.]
  )
]

#pagebreak()

// Page 3 : Fiche Recette
#heading(level: 2)[Fiche Recette Pilier : La Crème Anglaise au Degré Près]
#v(4pt)
#text(size: 9pt, style: "italic", fill: rgb("#701c1a"))[Le chef-d'œuvre de l'émulsion chaude : maîtriser la coagulation à 82°C sans aucun coagulant artificiel.]
#v(8pt)

#grid(
  columns: (40%, 60%),
  gutter: 15pt,
  [
    #rect(fill: rgb("#f7f4eb"), stroke: 0.5pt + rgb("#d4a373"), inset: 10pt, radius: 4pt, width: 100%)[
      #text(weight: "bold", fill: rgb("#701c1a"))[Ratios au Gramme :]
      - Lait entier : $500\text{ g}$
      - Jaunes d'œufs : $100\text{ g}$ (5 jaunes)
      - Sucre blanc : $80\text{ g}$
      - Gousse de vanille : 1 pièce
      - Énergie : Feu doux / Bain-marie
    ]
  ],
  [
    #text(weight: "bold")[Protocole Pas à Pas :]
    1. *L'Infusion Lactée :* Fendre la gousse de vanille, gratter les grains et chauffer avec le lait à $80^\circ\mathrm{C}$. Couvrir 15 min.
    2. *Le Blanchiment Doux :* Fouetter les jaunes et le sucre sans excès pour ne pas incorporer trop d'air isolant.
    3. *Le Tempérage :* Verser la moitié du lait chaud sur les jaunes en fouettant, puis reverser dans la casserole.
    4. *La Coagulation à la Spatule :* Cuire à feu très doux en formant des « 8 ». Stopper à $82^\circ\mathrm{C}$ pile.
  ]
)

#v(10pt)
#rect(fill: rgb("#faf7f2"), stroke: (left: 3pt + rgb("#701c1a")), inset: 8pt, width: 100%)[
  #text(weight: "bold", fill: rgb("#701c1a"))[🔬 L'Œil de la Molécule : Le Rubicon des 82°C] \
  À $82^\circ\mathrm{C}$, la lipovitelline du jaune déploie ses bras hydrophiles pour piéger l'eau dans un réseau onctueux. À $85^\circ\mathrm{C}$, les ponts disulfures se nouent de façon irréversible : l'eau est expulsée, la crème tourne en œufs brouillés.
]

#pagebreak()

// Page 4 : Infographie Technique
#heading(level: 2)[Analyse Visuelle : Les Transferts Thermiques en Cuisine]
#v(6pt)
Comprendre la cinétique de l'énergie dans les fluides et les solides permet d'éliminer toute incertitude :

#v(10pt)
#figure(
  image("figures/livre_1/fig_02_thermodynamique_transferts.svg", width: 85%),
  caption: [Figure 1.2 : Conduction, convection et rayonnement au service du geste culinaire.]
)

#v(10pt)
L'épaisseur du métal dicte l'inertie : la fonte emmagasine l'énergie pour la restituer sans faiblir, tandis que le cuivre propage instantanément les variations de la flamme.

#pagebreak()

// Page 5 : Répertoire & Guide Technique
#heading(level: 2)[Annexe Technique : Barème des Températures Critiques]
#v(6pt)
#table(
  columns: (25%, 35%, 40%),
  stroke: 0.5pt + rgb("#d4a373"),
  fill: (x, y) => if y == 0 { rgb("#f2ece1") } else if calc.odd(y) { rgb("#faf7f2") } else { none },
  inset: 7pt,
  table.header([Température], [Phénomène Moléculaire], [Conséquence en Bouche & Geste]),
  [$60^\circ\mathrm{C}\text{ à }65^\circ\mathrm{C}$], [Dénaturation myosine & début gélatinisation amidon], [La viande rosit, les grains de riz s'imbibent d'eau.],
  [$68^\circ\mathrm{C}$], [Dénaturation brutale de l'actine animale], [Resserrement élastique violent : expulsion de l'eau cellulaire.],
  [$82^\circ\mathrm{C}$], [Coagulation optimale des protéines du jaune d'œuf], [Nappage parfait de la crème anglaise et du sabayon.],
  [$140^\circ\mathrm{C}\text{ à }165^\circ\mathrm{C}$], [Réactions de Maillard (sucres réducteurs + acides aminés)], [Genèse des arômes complexes de croûte dorée et de pain grillé.],
  [$190^\circ\mathrm{C}$], [Point de fumée de l'huile d'olive extra-vierge], [Décomposition thermique des lipides en acroléine toxique.]
)

#pagebreak()

// ------------------------------------------------------------------------------
// STYLE 2 : MAGAZINE BISTRONOMIQUE (PAGES 6 À 10)
// ------------------------------------------------------------------------------
#show: style2

// Page 6 : Ouverture
#v(0.5cm)
#text(size: 10pt, weight: "bold", fill: rgb("#a3432b"), tracking: 0.15em)[ATELIER DE CUISINE MODERNE]
#v(4pt)
#text(size: 26pt, weight: "bold", fill: rgb("#0f172a"))[L'Art du Feu et le Sens de la Matière]
#v(10pt)
#text(size: 11pt, fill: rgb("#64748b"))[Pourquoi abandonner les dogmes poussiéreux pour comprendre la thermodynamique pure.]

#v(15pt)
#place(right, dx: 4.2cm, dy: 0cm, scope: "parent")[
  #rect(fill: rgb("#fef3c7"), stroke: 1pt + rgb("#f59e0b"), inset: 8pt, radius: 4pt, width: 3.8cm)[
    #text(size: 8pt, weight: "bold", fill: rgb("#b45309"))[REPÈRE CHEF]\
    #text(size: 7.5pt, fill: rgb("#78350f"))[La fonte ne pardonne pas l'approximation : chauffez toujours 5 min à sec avant d'huiler.]
  ]
]

La cuisine moderne ne commence pas par une liste de courses, mais par la maîtrise des flux d'énergie. En saisissant une viande dans une poêle en fonte surchauffée, vous n'obéissez pas à un rituel : vous déclenchez une cascade de réactions biochimiques orchestrées au degré près.

#v(15pt)
#figure(
  image("figures/nourriture/poireaux_frais.jpg", width: 95%),
  caption: [Légumes de pleine terre : la fraîcheur cellulaire avant transformation thermique.]
)

#pagebreak()

// Page 7 : Théorie
#heading(level: 2)[Thermodynamique : La Poêle en Fonte face à l'Inox]
#v(6pt)
#place(right, dx: 4.2cm, dy: 0cm, scope: "parent")[
  #rect(fill: rgb("#f1f5f9"), stroke: 0.5pt + rgb("#94a3b8"), inset: 8pt, radius: 4pt, width: 3.8cm)[
    #text(size: 8pt, weight: "bold", fill: rgb("#334155"))[LEIDENFROST]\
    #text(size: 7.5pt, fill: rgb("#475569"))[À 190°C, une goutte d'eau roule sans s'évaporer. C'est le signal de saisie parfait.]
  ]
]

Pourquoi les viandes attachent-elles désespérément au fond d'une poêle trop froide ? Lorsque la température de surface est inférieure à $140^\circ\mathrm{C}$, les protéines musculaires forment des liaisons covalentes avec les atomes de fer du métal. À $180^\circ\mathrm{C}$, la dessiccation instantanée crée un coussin de vapeur qui détache spontanément la pièce.

#v(10pt)
#table(
  columns: (35%, 35%, 30%),
  stroke: 0.5pt + rgb("#cbd5e1"),
  fill: (x, y) => if y == 0 { rgb("#e2e8f0") } else { rgb("#ffffff") },
  inset: 7pt,
  table.header([Matériau], [Avantage Clé], [Usage Idéal]),
  [Fonte Brute], [Inertie thermique colossale], [Saisir steaks, smash burgers],
  [Inox 18/10 3-ply], [Neutralité chimique absolue], [Déglaçages acides, sauces],
  [Cuivre Étamé], [Réactivité instantanée], [Sucres, confiseries fines]
)

#pagebreak()

// Page 8 : Fiche Recette Magazine
#heading(level: 2)[Recette Express : Le Dahl Velouté aux Lentilles Corail]
#v(4pt)
#place(right, dx: 4.2cm, dy: 0cm, scope: "parent")[
  #rect(fill: rgb("#ecfdf5"), stroke: 1pt + rgb("#10b981"), inset: 8pt, radius: 4pt, width: 3.8cm)[
    #text(size: 8pt, weight: "bold", fill: rgb("#047857"))[CHRONO 20 MIN]\
    #text(size: 7.5pt, fill: rgb("#065f46"))[Zéro trempage préalable : la cuticule cellulosique a été retirée à la meule.]
  ]
]

- **Préparation :** 5 min | **Cuisson :** 15 min | **Coût :** $< 1{,}50\text{ €/pers}$
- **Ingrédients :** $250\text{ g}$ lentilles corail, $400\text{ ml}$ lait de coco, 1 oignon, cumin, curcuma, citron vert.

#v(8pt)
#text(weight: "bold", fill: rgb("#a3432b"))[1. Torréfaction à sec (0 à 2 min) :] Jeter le cumin dans la casserole sans matière grasse. Dès que le parfum de noisette embaume, ajouter l'huile et l'oignon émincé.\
#text(weight: "bold", fill: rgb("#a3432b"))[2. Imperméabilisation lipidique (2 à 5 min) :] Verser les lentilles rincées et le curcuma. Remuer vivement pour enrober chaque grain de gras parfumé.\
#text(weight: "bold", fill: rgb("#a3432b"))[3. Mijotage onctueux (5 à 20 min) :] Ajouter l'eau et le coco. Cuire à feu doux. Saler et citronner uniquement hors du feu.

#pagebreak()

// Page 9 : Infographie
#heading(level: 2)[L'Europe des Trois Graisses et la Mécanique du Goût]
#v(6pt)
#figure(
  image("figures/livre_4/fig_carte_trois_graisses_terroirs.svg", width: 95%),
  caption: [Figure 2.1 : Beurre du Nord, graisse de canard du Sud-Ouest et huile d'olive du Midi.]
)

#pagebreak()

// Page 10 : Annexe Guide
#heading(level: 2)[Guide d'Entretien : Culotter sa Fonte en 3 Étapes]
#v(6pt)
1. **Lavage et décapage initial :** Frotter à l'eau très chaude sans détergent agressif.
2. **Le film d'huile ultra-fin :** Essuyer avec un chiffon imbibé d'huile de lin ou de tournesol ($0{,}5\text{ ml}$ suffisent).
3. **La polymérisation au four :** Enfourner 1 heure à $230^\circ\mathrm{C}$. Les chaînes d'acides gras insaturés se réticulent en un émail noir naturel inusable.

#pagebreak()

// ------------------------------------------------------------------------------
// STYLE 3 : LE LABORATOIRE CULINAIRE (PAGES 11 À 15)
// ------------------------------------------------------------------------------
#show: style3

// Page 11 : Ouverture Laboratoire
#v(0.5cm)
#rect(fill: rgb("#e0f2fe"), stroke: 1pt + rgb("#0284c7"), inset: 10pt, radius: 2pt, width: 100%)[
  #text(font: "Liberation Mono", size: 9pt, weight: "bold", fill: rgb("#0369a1"))[// PROTOCOLE LAB-MODERNIST-01 // ANTHROPOLOGIE THERMIQUE]\
  #text(size: 20pt, weight: "bold", fill: rgb("#0f172a"))[Étude Cinétique de la Dégradation Macromoléculaire]
]

#v(15pt)
#columns(2, gutter: 15pt)[
  *OBJECTIF :* Quantifier l'énergie d'activation requise pour rompre les ponts peptidiques du tissu collagénique sans provoquer la polymérisation toxique des acides gras libres.

  *MÉTHODOLOGIE :* Mesure par capteur thermocouple à compensation de soudure froide, spectrophotométrie d'absorption des composés néoformés et chromatographie en phase gazeuse des pyrazines volatiles.
]

#v(15pt)
#figure(
  image("figures/science/gouttelettes_emulsion_microscope.jpg", width: 85%),
  caption: [Fig 3.1 : Micelles lipidiques en émulsion métastable observées au grossissement x400.]
)

#pagebreak()

// Page 12 : Équations & Tableau Lab
#heading(level: 2)[Équation de Coagulation et Modèle Thermique Fractionné]
#v(6pt)
La dénaturation de l'ovalbumine suit une loi d'Arrhenius :
$ k = A dot e^(- E_a / (R T)) $
avec $E_a = 418\ "kJ/mol"$, expliquant pourquoi une élévation de seulement $2^\circ\mathrm{C}$ entre $63^\circ\mathrm{C}$ et $65^\circ\mathrm{C}$ multiplie la vitesse de gélification par dix.

#v(10pt)
#table(
  columns: (25%, 25%, 25%, 25%),
  stroke: 0.5pt + rgb("#0284c7"),
  fill: (x, y) => if y == 0 { rgb("#0284c7") } else { rgb("#ffffff") },
  inset: 6pt,
  table.header(
    [#text(fill: white)[Fraction Protéique]], 
    [#text(fill: white)[T° Dénaturation]], 
    [#text(fill: white)[État Physique]], 
    [#text(fill: white)[Viscosité Dynamique]]
  ),
  [Ovotransferrine], [$61{,}5^\circ\mathrm{C}$], [Gel laiteux fragile], [$12\ \mathrm{mPa} dot \mathrm{s}$],
  [Ovalbumine], [$84{,}5^\circ\mathrm{C}$], [Réseau rigide opaque], [$150\ \mathrm{mPa} dot \mathrm{s}$],
  [Lipovitelline (Jaune)], [$65^\circ\mathrm{C}\text{ à }70^\circ\mathrm{C}$], [Pâte crémeuse dense], [$85\ \mathrm{mPa} dot \mathrm{s}$],
  [Actine Musculaire], [$66^\circ\mathrm{C}$], [Rétractation fibrillaire], [Expulsion $30\%\ \mathrm{H}_2\mathrm{O}$]
)

#pagebreak()

// Page 13 : Fiche Expérimentale Recette
#heading(level: 2)[Fiche Expérimentale : L'Œuf Mollet Parfait à 64°C]
#v(6pt)
#rect(stroke: 0.5pt + rgb("#cbd5e1"), inset: 8pt, width: 100%)[
  *MATÉRIEL CRITIQUE :* Bain thermostaté à circulation d'eau ($\pm 0{,}1^\circ\mathrm{C}$), chronomètre digital, bol d'eau à $0^\circ\mathrm{C}$ saturé en glaçons.
]
#v(8pt)
1. Régler le bain à $64{,}0^\circ\mathrm{C}$ stables.
2. Immerger l'œuf intact pendant exactement 45 minutes.
3. Plonger 30 secondes dans le bain d'eau glacée pour figer la membrane coquillière.
4. Écaler délicatement : le blanc est soyeux comme une crème prise, le jaune est chaud et nappant.

#pagebreak()

// Page 14 : Infographie Lab
#heading(level: 2)[Cartographie des Températures de Coagulation]
#v(8pt)
#figure(
  image("figures/livre_2/fig_06_courbe_coagulation_oeuf.svg", width: 90%),
  caption: [Fig 3.2 : Cinétique comparée de prise du blanc et du jaune d'œuf selon la température.]
)

#pagebreak()

// Page 15 : Répertoire Additifs Lab
#heading(level: 2)[Contrôle Toxicologique des Additifs E249 à E252]
#v(6pt)
Les nitrites et nitrates industriels réagissent avec les amines secondaires en milieu gastrique acide pour synthétiser des $N$-nitrosamines cancérigènes :
$ \mathrm{R}_2\mathrm{NH} + \mathrm{HNO}_2 longrightarrow \mathrm{R}_2\mathrm{N-N=O} + \mathrm{H}_2\mathrm{O} $
Recommandation sanitaire formelle : privilégier les charcuteries fermières certifiées sans sel nitrité.

#pagebreak()

// ------------------------------------------------------------------------------
// STYLE 4 : LE CARNET D'ATELIER ARTISANAL (PAGES 16 À 20)
// ------------------------------------------------------------------------------
#show: style4

// Page 16 : Ouverture Terroir
#v(1cm)
#align(center)[
  #text(size: 13pt, fill: rgb("#78350f"), font: "Linux Libertine")[~ Carnet de Cuisine Vivante ~]\
  #v(8pt)
  #text(size: 22pt, weight: "bold", fill: rgb("#2d2926"))[La Mémoire du Pain et du Levain]\
  #v(6pt)
  #line(length: 40%, stroke: 0.5pt + rgb("#a3432b"))
]

#v(1cm)
Rien n'égale l'odeur d'une miche de pain qui sort du four à bois au petit matin. Ce miracle du quotidien ne réclame que trois ingrédients élémentaires : de la farine de meule paysanne, de l'eau de source et une pincée de sel marin. Le reste est l'œuvre silencieuse des levures sauvages et des bactéries lactiques qui dorment dans l'air de notre cuisine.

#v(1cm)
#figure(
  image("figures/nourriture/pain_levain_artisan_dore.jpg", width: 85%),
  caption: [La croûte dorée au levain naturel : alvéoles sauvages et caramélisation lente.]
)

#pagebreak()

// Page 17 : Théorie Artisanale
#heading(level: 2)[Le Secret du Levain : Symbiose entre Bactéries et Levures]
#v(6pt)
Dans un levain chef rafraîchi, deux micro-organismes collaborent en harmonie parfaite :
- *Les Levures Sauvages (Candida milleri) :* Elles fermentent le maltose sans toucher au saccharose, produisant les bulles de gaz carbonique ($CO_2$) qui soulèvent la pâte.
- *Les Bactéries Lactiques (Lactobacillus sanfranciscensis) :* Elles sécrètent de l'acide lactique et de l'acide acétique. Cette acidité abaisse le pH à $4{,}2$, empêchant toute moisissure parasite et prédigérant le gluten pour le rendre digeste.

#v(10pt)
#rect(fill: rgb("#fcfbf7"), stroke: 0.5pt + rgb("#d4a373"), inset: 10pt, radius: 4pt, width: 100%)[
  #text(weight: "bold", fill: rgb("#78350f"))[Règle d'or du boulanger :] Jamais d'eau chlorée du robinet pour rafraîchir un levain. Le chlore est un biocide conçu pour éradiquer les bactéries ; il tuerait votre colonie en quelques heures.
]

#pagebreak()

// Page 18 : Fiche Recette Pain
#heading(level: 2)[La Boule de Pain de Campagne en Cocotte de Fonte]
#v(6pt)
- **Farine T65 ou T80 de meule :** $500\text{ g}$
- **Eau tiède non chlorée :** $350\text{ g}$ (Hydratation à $70\%$)
- **Levain actif mûr :** $100\text{ g}$
- **Sel fin gris de Guérande :** $10\text{ g}$

#v(8pt)
1. *Autolyse (45 min) :* Mélanger la farine et l'eau grossièrement. Laisser reposer sous un linge : les enzymes de la farine développent le réseau de gluten sans pétrissage fatiguant.
2. *Ensemencement et Rabats :* Ajouter le levain et le sel. Donner 4 rabats espacés de 30 minutes.
3. *Apprêt au frais :* Laisser lever 12 heures au réfrigérateur dans un banneton fariné.
4. *Cuisson sous cloche en fonte :* Enfourner la cocotte fermée à $240^\circ\mathrm{C}$ pendant 25 min, puis 15 min sans couvercle pour dorer la croûte.

#pagebreak()

// Page 19 : Infographie Atelier
#heading(level: 2)[Le Plateau de Fromages au Fil des Saisons]
#v(6pt)
#figure(
  image("figures/nourriture/plateau_fromages_terroir.jpg", width: 85%),
  caption: [L'expression du terroir : chaque fromage atteint son apogée selon le cycle des pâturages.]
)

#pagebreak()

// Page 20 : Tableau de bord Saisons
#heading(level: 2)[Calendrier des Fromages à Point]
#v(6pt)
#table(
  columns: (30%, 35%, 35%),
  stroke: 0.5pt + rgb("#a3432b"),
  fill: (x, y) => if y == 0 { rgb("#f4eee1") } else { rgb("#fffdfa") },
  inset: 7pt,
  table.header([Saison Idéale], [Fromages à leur Apogée], [Raison Biologique & Pâturage]),
  [Printemps], [Chèvres frais, Saint-Marcellin], [Montée de lait frais parfumé aux jeunes pousses.],
  [Été], [Beaufort jeune, Reblochon fermier], [Vaches en alpage consommant fleurs et trèfles sauvages.],
  [Automne], [Comtés affinés 18 mois, Fourme], [Lait riche en carotènes des regain d'automne.],
  [Hiver], [Mont d'Or coulant, Raclette], [Lait d'étable riche en lipides, sangles d'épicéa.]
)

#pagebreak()

// ------------------------------------------------------------------------------
// STYLE 5 : LE MINIMALISME ÉDITORIAL NORDIQUE (PAGES 21 À 25)
// ------------------------------------------------------------------------------
#show: style5

// Page 21 : Ouverture Nordique
#v(3cm)
#text(size: 32pt, weight: "light", fill: rgb("#000000"), tracking: 0.05em)[01\\
DE LA MATIÈRE\\
BRUTE AU GESTE]

#v(2cm)
#text(size: 11pt, fill: rgb("#64748b"), tracking: 0.05em)[
  Rien de trop.\\
  Un couteau affûté.\\
  Une flamme pure.\\
  L'intelligence du temps.
]

#pagebreak()

// Page 22 : Théorie Nordique
#v(1cm)
#text(size: 18pt, weight: "regular")[L'Inertie Silencieuse]
#v(1cm)

Le feu ne se combat pas : il s'apprivoise. 

Quand l'acier rencontre la matière, il n'existe aucun compromis possible. Soit la température est exacte, soit la texture est brisée à tout jamais.

#v(2cm)
$ Delta E = m dot c_p dot Delta T $

#v(2cm)
#text(size: 10pt, fill: rgb("#475569"))[
  Un kilogramme de fonte stocke quatre cent cinquante joules par kelvin.\\
  C'est le bouclier qui empêche la chaleur de faiblir.
]

#pagebreak()

// Page 23 : Recette Nordique Épurée
#v(1cm)
#text(size: 18pt, weight: "regular")[Ceviche de Merlan]
#v(6pt)
#text(size: 10pt, fill: rgb("#94a3b8"))[Quinze minutes sous l'acide.]
#v(1.5cm)

*INGRÉDIENTS*
- Trois cents grammes de poisson blanc très frais
- Trois limes vertes pressées
- Un demi-oignon rouge lavé à l'eau glacée
- Une pincée de fleur de sel

#v(1cm)
*MÉCANIQUE*
1. Tailler en cubes de quinze millimètres.
2. Napper de jus de lime pur.
3. Attendre exactement neuf cents secondes.
4. Servir quand le pourtour blanchit et que le cœur reste translucide.

#pagebreak()

// Page 24 : Image Nordique
#v(1cm)
#figure(
  image("figures/nourriture/ceviche_poisson_frais.jpg", width: 100%),
  caption: [La dénaturation froide par l'acide citrique.]
)

#pagebreak()

// Page 25 : Table Nordique Finale
#v(2cm)
#text(size: 18pt, weight: "regular")[Précision des Seuils]
#v(1.5cm)

#table(
  columns: (40%, 60%),
  stroke: none,
  fill: none,
  inset: 10pt,
  table.hline(stroke: 1pt + black),
  table.header([Degré Celsius], [État de la Matière]),
  table.hline(stroke: 0.5pt + black),
  [$0^\circ\mathrm{C}$], [Cristallisation de l'eau pure],
  [$52^\circ\mathrm{C}$], [Bœuf saignant : relaxation parfaite],
  [$64^\circ\mathrm{C}$], [Prise onctueuse de l'albumine],
  [$82^\circ\mathrm{C}$], [Seuil absolu des liaisons lactées],
  [$100^\circ\mathrm{C}$], [Ébullition franche de l'eau],
  [$140^\circ\mathrm{C}$], [Éveil des réactions de Maillard],
  table.hline(stroke: 1pt + black)
)
"""

with open("maquettes_styles_cuisine.typ", "w", encoding="utf-8") as f:
    f.write(content)

print("maquettes_styles_cuisine.typ written successfully.")

cmd = [TYPST_BIN, "compile", "maquettes_styles_cuisine.typ", "maquettes_styles_cuisine.pdf"]
res = subprocess.run(cmd, capture_output=True, text=True)
print("Typst Return Code:", res.returncode)
if res.returncode == 0:
    print("SUCCESS: maquettes_styles_cuisine.pdf successfully compiled (25 pages)!")
else:
    print("STDOUT:", res.stdout)
    print("STDERR:", res.stderr)
