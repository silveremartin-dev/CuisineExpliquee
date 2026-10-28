// ==============================================================================
// BENCHMARK DE MAQUETTES ÉDITORIALES — 5 STYLES CULINAIRES x 5 PAGES (25 PAGES)
// ==============================================================================

#set document(title: "Benchmark de Maquettes Éditoriales — La Cuisine Expliquée", author: "La Cuisine Expliquée")

// ------------------------------------------------------------------------------
// STYLE 1 : LE GRAND TRAITÉ ÉTOILÉ (Haute Gastronomie Classique & Prestige)
// Pages 1 à 5
// ------------------------------------------------------------------------------

#set page(
  paper: "a4",
  margin: (top: 2.5cm, bottom: 2.5cm, left: 2.2cm, right: 2.2cm),
  header: context {
    let p = counter(page).get().first()

    if p <= 5 {
      text(font: "Linux Libertine", size: 8.5pt, fill: rgb(112, 28, 26), tracking: 0.1em)[
        #smallcaps[Style 1 : Le Grand Traité Étoilé] #h(1fr) #emph[La Cuisine Expliquée]
      ]
    } else if p <= 10 {
      text(font: "Liberation Sans", size: 8.5pt, fill: rgb(163, 67, 43), weight: "bold")[
        STYLE 2 : MAGAZINE BISTRONOMIQUE #h(1fr) #text(weight: "regular", fill: rgb(100, 116, 139))[PAGE ACTIVE #p]
      ]
    } else if p <= 15 {
      text(font: "Liberation Mono", size: 8pt, fill: rgb(3, 105, 161))[
        [EXP-LAB -- STYLE 3 : THE FOOD LAB & MODERNIST PROTOCOLS] #h(1fr) [SEC: 04 -- P.#p]
      ]
    } else if p <= 20 {
      text(font: "Linux Libertine", style: "italic", size: 9pt, fill: rgb(85, 107, 47))[
        Carnet d'Atelier & Terroirs Vivants #h(1fr) Feuille #p
      ]
    } else {
      none
    }
  },
  footer: context {
    let p = counter(page).get().first()

    if p <= 5 {
      align(center)[#text(font: "Linux Libertine", size: 9pt, fill: rgb(112, 28, 26))[— #p —]]
    } else if p <= 10 {
      none
    } else if p <= 15 {
      line(length: 100%, stroke: 0.5pt + rgb(2, 132, 199))
      v(2pt)
      text(font: "Liberation Mono", size: 7.5pt, fill: rgb(100, 116, 139))[Cuisine Expliquée / Rigueur Moléculaire et Métrologique]
    } else if p <= 20 {
      align(center)[#text(font: "Linux Libertine", size: 9pt, fill: rgb(120, 53, 15))[~ #p ~]]
    } else {
      text(font: "Liberation Sans", size: 8.5pt, fill: rgb(148, 163, 184), tracking: 0.2em)[#p]
    }
  },
  fill: rgb(255, 253, 250)
)

#set text(font: "Linux Libertine", size: 10pt, fill: rgb(36, 33, 36), lang: "fr")
#set par(justify: true, leading: 0.75em)

// --- PAGE 1 (Style 1) : Ouverture de Partie ---
#v(1cm)
#align(center)[
  #text(size: 11pt, tracking: 0.25em, fill: rgb(112, 28, 26), weight: "bold")[STYLE 1 — HAUTE GASTRONOMIE ÉTOILÉE]\
  #v(8pt)
  #text(size: 24pt, weight: "bold", fill: rgb(36, 33, 36))[L'Homme, le Feu et la Règle du Foyer]\
  #v(10pt)
  #line(length: 25%, stroke: 1pt + rgb(212, 163, 115))
  #v(10pt)
  #text(size: 10pt, style: "italic", fill: rgb(92, 85, 73))[
    « L'homme ne devient véritablement humain que le jour où il cesse d'ingérer la chair crue\
    pour la soumettre à la médiation alchimique de la braise. »\
    — Claude Lévi-Strauss
  ]
]

#v(1.2cm)
#columns(2, gutter: 18pt)[
  Avant la casserole et avant le fournil, la cuisine est une conquête thermodynamique de l'espèce humaine. Richard Wrangham, dans ses travaux fondamentaux sur l'évolution, a démontré que l'invention du feu n'a pas seulement modifié notre régime : elle a remodelé notre tube digestif et permis l'expansion de notre néocortex.

  En cuisant les fibres végétales et le collagène coriace des viandes, le feu opère une prédigestion externe. L'énergie autrefois perdue à mâcher pendant six heures quotidiennes devient instantanément disponible pour le cerveau.
]

#v(1cm)
#align(center)[
  #image("figures/nourriture/steak_poele_fonte.jpg", width: 85%)
  #v(4pt)
  #text(size: 8.5pt, style: "italic", fill: rgb(92, 85, 73))[Figure 1.1 : La saisie en fonte brute : maîtrise du flux thermique à 180°C.]
]

#pagebreak()

// --- PAGE 2 (Style 1) : Théorie & Tableau Comparatif ---
#heading(level: 2)[1. La Thermodynamique du Feu : Le Transfert Conductif]
#v(6pt)
La matière culinaire obéit strictement aux lois de Fourier et de Stefan-Boltzmann. Lorsqu'un steak de bœuf entre en contact avec la fonte chaude, le flux thermique surfacique $Phi$ s'exprime par la relation de conduction :
$ Phi = - lambda dot (partial T) / (partial x) $
Ce gradient détermine la vitesse de formation de la croûte dorée sans calcination des tissus profonds.

#v(12pt)
#align(center)[
  #table(
    columns: (30%, 35%, 35%),
    stroke: 0.5pt + rgb(212, 163, 115),
    fill: (x, y) => if y == 0 { rgb(242, 236, 225) } else if calc.odd(y) { rgb(250, 247, 242) } else { none },
    inset: 8pt,
    table.header([*Paramètre Opératoire*], [*Le Geste Vertueux (À Faire)*], [*L'Écueil Critique (À Éviter)*]),
    [*Température Poêle*], [Préchauffer à sec à 190°C jusqu'à perle de Leidenfrost.], [Poser la viande dans une poêle tiède (moins de 120°C) qui fait bouillir l'eau.],
    [*Séchage Chair*], [Tamponner la viande au papier absorbant avant saisie.], [Saisir une viande humide : l'énergie sert à évaporer l'eau sans colorer.],
    [*Repos Post-Cuisson*], [Laisser reposer sous cloche tiède 5 min (redistribution des sucs).], [Couper immédiatement : les fibres sous tension expulsent tout le jus.]
  )
]

#pagebreak()

// --- PAGE 3 (Style 1) : Fiche Recette Pas à Pas ---
#heading(level: 2)[Fiche Recette Pilier : La Crème Anglaise au Degré Près]
#v(4pt)
#text(size: 9pt, style: "italic", fill: rgb(112, 28, 26))[Le chef-d'œuvre de l'émulsion chaude : maîtriser la coagulation à 82°C sans aucun coagulant artificiel.]
#v(8pt)

#grid(
  columns: (42%, 58%),
  gutter: 15pt,
  [
    #rect(fill: rgb(247, 244, 235), stroke: 0.5pt + rgb(212, 163, 115), inset: 10pt, radius: 4pt, width: 100%)[
      #text(weight: "bold", fill: rgb(112, 28, 26))[Ratios au Gramme :]\
      - Lait entier : 500 g\
      - Jaunes d'œufs : 100 g (5 pièces)\
      - Sucre blanc : 80 g\
      - Gousse de vanille : 1 pièce\
      - Température critique : 82°C
    ]
  ],
  [
    #text(weight: "bold")[Protocole Pas à Pas :]\
    1. *L'Infusion Lactée :* Fendre la gousse de vanille, gratter les grains et chauffer avec le lait à 80°C. Couvrir 15 min.\
    2. *Le Blanchiment Doux :* Fouetter les jaunes et le sucre sans excès pour ne pas incorporer trop d'air isolant.\
    3. *Le Tempérage :* Verser la moitié du lait chaud sur les jaunes en fouettant, puis reverser dans la casserole.\
    4. *La Coagulation à la Spatule :* Cuire à feu très doux en formant des « 8 ». Stopper à 82°C pile.
  ]
)

#v(12pt)
#rect(fill: rgb(250, 247, 242), stroke: (left: 3pt + rgb(112, 28, 26)), inset: 8pt, width: 100%)[
  #text(weight: "bold", fill: rgb(112, 28, 26))[🔬 L'Œil de la Molécule : Le Rubicon des 82°C] \
  À 82°C, la lipovitelline du jaune déploie ses bras hydrophiles pour piéger l'eau dans un réseau onctueux. À 85°C, les ponts disulfures se nouent de façon irréversible : l'eau est expulsée, la crème tourne en œufs brouillés.
]

#pagebreak()

// --- PAGE 4 (Style 1) : Infographie Technique ---
#heading(level: 2)[Analyse Visuelle : Les Transferts Thermiques en Cuisine]
#v(6pt)
Comprendre la cinétique de l'énergie dans les fluides et les solides permet d'éliminer toute incertitude :

#v(10pt)
#align(center)[
  #image("figures/livre_1/fig_02_thermodynamique_transferts.svg", width: 85%)
  #v(4pt)
  #text(size: 8.5pt, style: "italic", fill: rgb(92, 85, 73))[Figure 1.2 : Conduction, convection et rayonnement au service du geste culinaire.]
]

#v(10pt)
L'épaisseur du métal dicte l'inertie : la fonte emmagasine l'énergie pour la restituer sans faiblir, tandis que le cuivre propage instantanément les variations de la flamme.

#pagebreak()

// --- PAGE 5 (Style 1) : Tableau Guide Référence ---
#heading(level: 2)[Annexe Technique : Barème des Températures Critiques]
#v(6pt)
#table(
  columns: (25%, 35%, 40%),
  stroke: 0.5pt + rgb(212, 163, 115),
  fill: (x, y) => if y == 0 { rgb(242, 236, 225) } else if calc.odd(y) { rgb(250, 247, 242) } else { none },
  inset: 7pt,
  table.header([*Température*], [*Phénomène Moléculaire*], [*Conséquence en Bouche & Geste*]),
  [60°C à 65°C], [Dénaturation myosine & gélatinisation amidon], [La viande rosit, les grains de riz s'imbibent d'eau.],
  [68°C], [Dénaturation brutale de l'actine animale], [Resserrement élastique violent : expulsion de l'eau cellulaire.],
  [82°C], [Coagulation optimale des protéines du jaune], [Nappage parfait de la crème anglaise et du sabayon.],
  [140°C à 165°C], [Réactions de Maillard (sucres + acides aminés)], [Genèse des arômes complexes de croûte dorée et grillé.],
  [190°C], [Point de fumée de l'huile d'olive extra-vierge], [Décomposition thermique des lipides en acroléine toxique.]
)

#pagebreak()

// ------------------------------------------------------------------------------
// STYLE 2 : MAGAZINE BISTRONOMIQUE (PAGES 6 À 10)
// ------------------------------------------------------------------------------
#set text(font: "Liberation Sans", size: 9.5pt, fill: rgb(30, 41, 59))
#set par(justify: true, leading: 0.7em)

// --- PAGE 6 (Style 2) : Ouverture ---
#v(0.5cm)
#text(size: 10pt, weight: "bold", fill: rgb(163, 67, 43), tracking: 0.15em)[STYLE 2 — MAGAZINE BISTRONOMIQUE CONTEMPORAIN]
#v(4pt)
#text(size: 26pt, weight: "bold", fill: rgb(15, 23, 42))[L'Art du Feu et le Sens de la Matière]
#v(10pt)
#text(size: 11pt, fill: rgb(100, 116, 139))[Pourquoi abandonner les dogmes poussiéreux pour comprendre la thermodynamique pure.]

#v(15pt)
#grid(
  columns: (68%, 32%),
  gutter: 15pt,
  [
    La cuisine moderne ne commence pas par une liste de courses, mais par la maîtrise des flux d'énergie. En saisissant une viande dans une poêle en fonte surchauffée, vous n'obéissez pas à un rituel : vous déclenchez une cascade de réactions biochimiques orchestrées au degré près.

    Comprendre le comportement de l'eau intracellulaire permet de bannir à tout jamais les viandes sèches et bouillies.
  ],
  [
    #rect(fill: rgb(254, 243, 199), stroke: 1pt + rgb(245, 158, 11), inset: 8pt, radius: 4pt, width: 100%)[
      #text(size: 8pt, weight: "bold", fill: rgb(180, 83, 9))[REPÈRE CHEF]\
      #text(size: 7.5pt, fill: rgb(120, 53, 15))[La fonte ne pardonne pas l'approximation : chauffez toujours 5 min à sec avant d'huiler.]
    ]
  ]
)

#v(15pt)
#align(center)[
  #image("figures/nourriture/poireaux_frais.jpg", width: 60%)
  #v(4pt)
  #text(size: 8pt, style: "italic", fill: rgb(100, 116, 139))[Légumes de pleine terre : la fraîcheur cellulaire avant transformation thermique.]
]

#pagebreak()

// --- PAGE 7 (Style 2) : Théorie ---
#heading(level: 2)[Thermodynamique : La Poêle en Fonte face à l'Inox]
#v(6pt)
#grid(
  columns: (68%, 32%),
  gutter: 15pt,
  [
    Pourquoi les viandes attachent-elles au fond d'une poêle trop froide ? Lorsque la température de surface est inférieure à 140°C, les protéines forment des liaisons covalentes avec les atomes de fer du métal. À 180°C, la dessiccation instantanée crée un coussin de vapeur qui détache spontanément la pièce.
  ],
  [
    #rect(fill: rgb(241, 245, 249), stroke: 0.5pt + rgb(148, 163, 184), inset: 8pt, radius: 4pt, width: 100%)[
      #text(size: 8pt, weight: "bold", fill: rgb(51, 65, 85))[LEIDENFROST]\
      #text(size: 7.5pt, fill: rgb(71, 85, 105))[À 190°C, une goutte d'eau roule sans s'évaporer : signal de saisie parfait.]
    ]
  ]
)

#v(12pt)
#table(
  columns: (35%, 35%, 30%),
  stroke: 0.5pt + rgb(203, 213, 225),
  fill: (x, y) => if y == 0 { rgb(226, 232, 240) } else { rgb(255, 255, 255) },
  inset: 7pt,
  table.header([*Matériau*], [*Avantage Clé*], [*Usage Idéal*]),
  [Fonte Brute], [Inertie thermique colossale], [Saisir steaks, smash burgers],
  [Inox 18/10 3-ply], [Neutralité chimique absolue], [Déglaçages acides, sauces],
  [Cuivre Étamé], [Réactivité instantanée], [Sucres, confiseries fines]
)

#pagebreak()

// --- PAGE 8 (Style 2) : Fiche Recette ---
#heading(level: 2)[Recette Express : Le Dahl Velouté aux Lentilles Corail]
#v(4pt)
#grid(
  columns: (68%, 32%),
  gutter: 15pt,
  [
    - *Préparation :* 5 min | *Cuisson :* 15 min | *Coût :* moins de 1,50 €/pers
    - *Ingrédients :* 250 g lentilles corail, 400 ml lait de coco, 1 oignon, cumin, curcuma, citron vert.

    #v(6pt)
    *1. Torréfaction à sec (0 à 2 min) :* Jeter le cumin dans la casserole sans matière grasse. Dès que le parfum de noisette embaume, ajouter l'huile et l'oignon émincé.\
    *2. Imperméabilisation lipidique (2 à 5 min) :* Verser les lentilles rincées et le curcuma. Remuer vivement pour enrober chaque grain de gras parfumé.\
    *3. Mijotage onctueux (5 à 20 min) :* Ajouter l'eau et le coco. Cuire à feu doux. Saler et citronner uniquement hors du feu.
  ],
  [
    #rect(fill: rgb(236, 253, 245), stroke: 1pt + rgb(16, 185, 129), inset: 8pt, radius: 4pt, width: 100%)[
      #text(size: 8pt, weight: "bold", fill: rgb(4, 120, 87))[CHRONO 20 MIN]\
      #text(size: 7.5pt, fill: rgb(6, 95, 70))[Zéro trempage : la cuticule cellulosique externe a été retirée à la meule.]
    ]
  ]
)

#pagebreak()

// --- PAGE 9 (Style 2) : Infographie ---
#heading(level: 2)[L'Europe des Trois Graisses et la Mécanique du Goût]
#v(6pt)
#align(center)[
  #image("figures/livre_4/fig_carte_trois_graisses_terroirs.svg", width: 92%)
  #v(4pt)
  #text(size: 8pt, style: "italic", fill: rgb(100, 116, 139))[Figure 2.1 : Beurre du Nord, graisse de canard du Sud-Ouest et huile d'olive du Midi.]
]

#pagebreak()

// --- PAGE 10 (Style 2) : Guide Culottage ---
#heading(level: 2)[Guide d'Entretien : Culotter sa Fonte en 3 Étapes]
#v(6pt)
1. *Lavage et décapage initial :* Frotter à l'eau très chaude sans détergent agressif.
2. *Le film d'huile ultra-fin :* Essuyer avec un chiffon imbibé d'huile de lin ou de tournesol (0,5 ml suffisent).
3. *La polymérisation au four :* Enfourner 1 heure à 230°C. Les chaînes d'acides gras insaturés se réticulent en un émail noir naturel inusable.

#pagebreak()

// ------------------------------------------------------------------------------
-- STYLE 3 : LE LABORATOIRE CULINAIRE (PAGES 11 À 15)
// ------------------------------------------------------------------------------
#set text(font: "Liberation Sans", size: 9.5pt, fill: rgb(15, 23, 42))
#set par(justify: true, leading: 0.68em)

// --- PAGE 11 (Style 3) : Ouverture ---
#v(0.5cm)
#rect(fill: rgb(224, 242, 254), stroke: 1pt + rgb(2, 132, 199), inset: 10pt, radius: 2pt, width: 100%)[
  #text(font: "Liberation Mono", size: 9pt, weight: "bold", fill: rgb(3, 105, 161))[-- STYLE 3 : THE FOOD LAB & MODERNIST PROTOCOLS]\
  #text(size: 20pt, weight: "bold", fill: rgb(15, 23, 42))[Cinétique de Dégradation Macromoléculaire]
]

#v(15pt)
#columns(2, gutter: 15pt)[
  *OBJECTIF :* Quantifier l'énergie d'activation requise pour rompre les ponts peptidiques du tissu collagénique sans provoquer la polymérisation toxique des acides gras libres.

  *MÉTHODOLOGIE :* Mesure par capteur thermocouple à compensation de soudure froide, spectrophotométrie d'absorption des composés néoformés et chromatographie en phase gazeuse des pyrazines volatiles.
]

#v(15pt)
#align(center)[
  #image("figures/science/gouttelettes_emulsion_microscope.jpg", width: 52%)
  #v(4pt)
  #text(font: "Liberation Mono", size: 7.5pt, fill: rgb(100, 116, 139))[Fig 3.1 : Micelles lipidiques en émulsion métastable observées au grossissement x400.]
]

#pagebreak()

// --- PAGE 12 (Style 3) : Formule & Tableau Lab ---
#heading(level: 2)[Modèle Thermique Fractionné de Coagulation]
#v(6pt)
La dénaturation de l'ovalbumine suit une loi d'Arrhenius :
$ k = A dot e^(- E_a / (R T)) $
avec $E_a = 418\ "kJ/mol"$, expliquant pourquoi une élévation de seulement 2°C entre 63°C et 65°C multiplie la vitesse de gélification par dix.

#v(10pt)
#table(
  columns: (25%, 25%, 25%, 25%),
  stroke: 0.5pt + rgb(2, 132, 199),
  fill: (x, y) => if y == 0 { rgb(2, 132, 199) } else { rgb(255, 255, 255) },
  inset: 6pt,
  table.header(
    [#text(fill: white)[*Fraction Protéique*]], 
    [#text(fill: white)[*T° Dénaturation*]], 
    [#text(fill: white)[*État Physique*]], 
    [#text(fill: white)[*Viscosité*]]
  ),
  [Ovotransferrine], [61,5°C], [Gel laiteux fragile], [12 mPa.s],
  [Ovalbumine], [84,5°C], [Réseau rigide opaque], [150 mPa.s],
  [Lipovitelline (Jaune)], [65°C à 70°C], [Pâte crémeuse dense], [85 mPa.s],
  [Actine Musculaire], [66°C], [Rétractation fibrillaire], [Expulsion 30% H2O]
)

#pagebreak()

// --- PAGE 13 (Style 3) : Fiche Expérimentale ---
#heading(level: 2)[Fiche Expérimentale : L'Œuf Mollet Parfait à 64°C]
#v(6pt)
#rect(stroke: 0.5pt + rgb(203, 213, 225), inset: 8pt, width: 100%)[
  *MATÉRIEL CRITIQUE :* Bain thermostaté à circulation d'eau (±0,1°C), chronomètre digital, bol d'eau à 0°C saturé en glaçons.
]
#v(8pt)
1. Régler le bain à 64,0°C stables.
2. Immerger l'œuf intact pendant exactement 45 minutes.
3. Plonger 30 secondes dans le bain d'eau glacée pour figer la membrane coquillière.
4. Écaler délicatement : le blanc est soyeux comme une crème prise, le jaune est chaud et nappant.

#pagebreak()

// --- PAGE 14 (Style 3) : Infographie Lab ---
#heading(level: 2)[Courbe de Coagulation de l'Œuf]
#v(8pt)
#align(center)[
  #image("figures/livre_2/fig_06_courbe_coagulation_oeuf.svg", width: 85%)
  #v(4pt)
  #text(font: "Liberation Mono", size: 7.5pt, fill: rgb(100, 116, 139))[Fig 3.2 : Cinétique comparée de prise du blanc et du jaune selon la température.]
]

#pagebreak()

// --- PAGE 15 (Style 3) : Guide Toxicologie ---
#heading(level: 2)[Contrôle Toxicologique des Additifs E249 à E252]
#v(6pt)
Les nitrites et nitrates industriels réagissent avec les amines secondaires en milieu gastrique acide pour synthétiser des N-nitrosamines cancérigènes :
$ upright(R)_2 upright(N H) + upright(H N O)_2 arrow.r upright(R)_2 upright(N-N=O) + upright(H)_2 upright(O) $
Recommandation sanitaire formelle : privilégier les charcuteries fermières certifiées sans sel nitrité.

#pagebreak()

// ------------------------------------------------------------------------------
// STYLE 4 : LE CARNET D'ATELIER ARTISANAL (PAGES 16 À 20)
// ------------------------------------------------------------------------------
#set text(font: "Linux Libertine", size: 10.5pt, fill: rgb(45, 41, 38))
#set par(justify: true, leading: 0.8em)

// --- PAGE 16 (Style 4) : Ouverture ---
#v(1cm)
#align(center)[
  #text(size: 11pt, fill: rgb(120, 53, 15), font: "Linux Libertine")[STYLE 4 — CARNET D'ATELIER ARTISANAL & TERROIR]\
  #v(8pt)
  #text(size: 22pt, weight: "bold", fill: rgb(45, 41, 38))[La Mémoire du Pain et du Levain]\
  #v(6pt)
  #line(length: 40%, stroke: 0.5pt + rgb(163, 67, 43))
]

#v(1cm)
Rien n'égale l'odeur d'une miche de pain qui sort du four à bois au petit matin. Ce miracle du quotidien ne réclame que trois ingrédients élémentaires : de la farine de meule paysanne, de l'eau de source et une pincée de sel marin. Le reste est l'œuvre silencieuse des levures sauvages et des bactéries lactiques qui dorment dans l'air de notre cuisine.

#v(1cm)
#align(center)[
  #image("figures/nourriture/pain_levain_artisan_dore.jpg", width: 80%)
  #v(4pt)
  #text(size: 8.5pt, style: "italic", fill: rgb(120, 53, 15))[La croûte dorée au levain naturel : alvéoles sauvages et caramélisation lente.]
]

#pagebreak()

// --- PAGE 17 (Style 4) : Théorie ---
#heading(level: 2)[Le Secret du Levain : Symbiose entre Bactéries et Levures]
#v(6pt)
Dans un levain chef rafraîchi, deux micro-organismes collaborent en harmonie parfaite :
- *Les Levures Sauvages (Candida milleri) :* Elles fermentent le maltose sans toucher au saccharose, produisant les bulles de gaz carbonique ($"CO"_2$) qui soulèvent la pâte.
- *Les Bactéries Lactiques (Lactobacillus sanfranciscensis) :* Elles sécrètent de l'acide lactique et de l'acide acétique. Cette acidité abaisse le pH à 4,2, empêchant toute moisissure parasite et prédigérant le gluten pour le rendre digeste.

#v(10pt)
#rect(fill: rgb(252, 251, 247), stroke: 0.5pt + rgb(212, 163, 115), inset: 10pt, radius: 4pt, width: 100%)[
  #text(weight: "bold", fill: rgb(120, 53, 15))[Règle d'or du boulanger :] Jamais d'eau chlorée du robinet pour rafraîchir un levain. Le chlore est un biocide conçu pour éradiquer les bactéries ; il tuerait votre colonie en quelques heures.
]

#pagebreak()

// --- PAGE 18 (Style 4) : Recette ---
#heading(level: 2)[La Boule de Pain de Campagne en Cocotte de Fonte]
#v(6pt)
- *Farine T65 ou T80 de meule :* 500 g
- *Eau tiède non chlorée :* 350 g (Hydratation à 70%)
- *Levain actif mûr :* 100 g
- *Sel fin gris de Guérande :* 10 g

#v(8pt)
1. *Autolyse (45 min) :* Mélanger la farine et l'eau grossièrement. Laisser reposer sous un linge : les enzymes de la farine développent le réseau de gluten sans pétrissage fatiguant.
2. *Ensemencement et Rabats :* Ajouter le levain et le sel. Donner 4 rabats espacés de 30 minutes.
3. *Apprêt au frais :* Laisser lever 12 heures au réfrigérateur dans un banneton fariné.
4. *Cuisson sous cloche en fonte :* Enfourner la cocotte fermée à 240°C pendant 25 min, puis 15 min sans couvercle pour dorer la croûte.

#pagebreak()

// --- PAGE 19 (Style 4) : Image Terroir ---
#heading(level: 2)[Le Plateau de Fromages au Fil des Saisons]
#v(6pt)
#align(center)[
  #image("figures/nourriture/plateau_fromages_terroir.jpg", width: 80%)
  #v(4pt)
  #text(size: 8.5pt, style: "italic", fill: rgb(120, 53, 15))[L'expression du terroir : chaque fromage atteint son apogée selon le cycle des pâturages.]
]

#pagebreak()

// --- PAGE 20 (Style 4) : Tableau Fromages ---
#heading(level: 2)[Calendrier des Fromages à Point]
#v(6pt)
#table(
  columns: (30%, 35%, 35%),
  stroke: 0.5pt + rgb(163, 67, 43),
  fill: (x, y) => if y == 0 { rgb(244, 238, 225) } else { rgb(255, 253, 250) },
  inset: 7pt,
  table.header([*Saison Idéale*], [*Fromages à leur Apogée*], [*Raison Biologique & Pâturage*]),
  [Printemps], [Chèvres frais, Saint-Marcellin], [Montée de lait frais parfumé aux jeunes pousses.],
  [Été], [Beaufort jeune, Reblochon fermier], [Vaches en alpage consommant fleurs et trèfles sauvages.],
  [Automne], [Comtés affinés 18 mois, Fourme], [Lait riche en carotènes des regain d'automne.],
  [Hiver], [Mont d'Or coulant, Raclette], [Lait d'étable riche en lipides, sangles d'épicéa.]
)

#pagebreak()

// ------------------------------------------------------------------------------
// STYLE 5 : LE MINIMALISME ÉDITORIAL NORDIQUE (PAGES 21 À 25)
// ------------------------------------------------------------------------------
#set text(font: "Liberation Sans", size: 9pt, fill: rgb(0, 0, 0))
#set par(justify: true, leading: 0.85em)

// --- PAGE 21 (Style 5) : Ouverture ---
#v(2.5cm)
#text(size: 11pt, tracking: 0.15em, fill: rgb(100, 116, 139))[STYLE 5 — MINIMALISME ÉDITORIAL NORDIQUE]\
#v(1cm)
#text(size: 32pt, weight: "light", fill: rgb(0, 0, 0), tracking: 0.05em)[01\
DE LA MATIÈRE\
BRUTE AU GESTE]

#v(2cm)
#text(size: 11pt, fill: rgb(100, 116, 139), tracking: 0.05em)[
  Rien de trop.\
  Un couteau affûté.\
  Une flamme pure.\
  L'intelligence du temps.
]

#pagebreak()

// --- PAGE 22 (Style 5) : Théorie ---
#v(1cm)
#text(size: 18pt, weight: "regular")[L'Inertie Silencieuse]
#v(1cm)

Le feu ne se combat pas : il s'apprivoise. 

Quand l'acier rencontre la matière, il n'existe aucun compromis possible. Soit la température est exacte, soit la texture est brisée à tout jamais.

#v(1.5cm)
$ Delta E = m dot c_p dot Delta T $

#v(1.5cm)
#text(size: 10pt, fill: rgb(71, 85, 105))[
  Un kilogramme de fonte stocke quatre cent cinquante joules par kelvin.\
  C'est le bouclier qui empêche la chaleur de faiblir.
]

#pagebreak()

// --- PAGE 23 (Style 5) : Recette ---
#v(1cm)
#text(size: 18pt, weight: "regular")[Ceviche de Merlan]
#v(6pt)
#text(size: 10pt, fill: rgb(148, 163, 184))[Quinze minutes sous l'acide.]
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

// --- PAGE 24 (Style 5) : Image ---
#v(1cm)
#align(center)[
  #image("figures/nourriture/ceviche_poisson_frais.jpg", width: 95%)
  #v(8pt)
  #text(size: 8.5pt, fill: rgb(100, 116, 139))[La dénaturation froide par l'acide citrique.]
]

#pagebreak()

// --- PAGE 25 (Style 5) : Tableau ---
#v(2cm)
#text(size: 18pt, weight: "regular")[Précision des Seuils]
#v(1.5cm)

#table(
  columns: (40%, 60%),
  stroke: none,
  fill: none,
  inset: 10pt,
  table.hline(stroke: 1pt + black),
  table.header([*Degré Celsius*], [*État de la Matière*]),
  table.hline(stroke: 0.5pt + black),
  [0°C], [Cristallisation de l'eau pure],
  [52°C], [Bœuf saignant : relaxation parfaite],
  [64°C], [Prise onctueuse de l'albumine],
  [82°C], [Seuil absolu des liaisons lactées],
  [100°C], [Ébullition franche de l'eau],
  [140°C], [Éveil des réactions de Maillard],
  table.hline(stroke: 1pt + black)
)
