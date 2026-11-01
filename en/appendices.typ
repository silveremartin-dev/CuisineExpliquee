#import "../styles.typ": *

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

// =========================================================================
// BOOK OPENING PORTAL: APPENDICES AND REFERENCE COMPENDIUM
// =========================================================================

#pagebreak(weak: false, to: "even")
#set page(margin: 0pt, header: none, footer: none)
#portail_livre_verso("/figures/patrimoine/diderot_encyclopedie_fournil.jpg", "Plate from Diderot and d'Alembert's Encyclopédie (1762): brick oven, proofing chamber, and kitchen instruments (Pl. II).")

#pagebreak(weak: false, to: "odd")
#set page(paper: "a4", margin: (top: 2.5cm, bottom: 2.5cm, left: 2.2cm, right: 2.2cm), header: none, footer: none, fill: rgb(255, 253, 250))
#portail_livre_recto("APPENDICES AND REFERENCE COMPENDIUM", "TABLES, GLOSSARY, AND CRITICAL DIRECTORY", [#text(size: 11.5pt, style: "italic")[— Appendix A --- Absolute Dial of Critical Temperatures in the Kitchen] \
#v(0.38cm)
#text(size: 11.5pt, style: "italic")[— Appendix B --- Comprehensive Physicochemical and Culinary Glossary] \
#v(0.38cm)
#text(size: 11.5pt, style: "italic")[— Appendix C --- Critical and Evaluated Bibliography] \
#v(0.38cm)
#text(size: 11.5pt, style: "italic")[— Appendix D --- Buyer's Guide to the Minimal Arsenal, Energy Costs, and Cooking Durations] \
#v(0.38cm)
#text(size: 11.5pt, style: "italic")[— Appendix E --- Cold Preservation, Refrigerator Bio-Zones, and Food Safety Limits] \
#v(0.38cm)
#text(size: 11.5pt, style: "italic")[— Appendix F --- Prep Cutlery, Consumables, Dry Matrix Pantry & Clean Grocery Template] \
#v(0.38cm)
#text(size: 11.5pt, style: "italic")[— Appendix G --- Iconographic Catalog, Archival Sources, and Image Credits]])

#pagebreak(weak: false, to: "odd")
#set page(header: entete-livre, footer: pied-livre)

// =========================================================================
// APPENDIX A: CRITICAL CULINARY TEMPERATURE DIAL
// =========================================================================

= APPENDIX A --- The Absolute Dial of Critical Temperatures in the Kitchen
<annexe-a-le-cadran-absolu-des-températures-critiques-en-cuisine>
#quote(block: true)[
This compendium synthesizes all the thermodynamic thresholds essential for mastering the transformations of matter at the core and on the surface.
]

#divider()

== 1. ANIMAL PROTEIN DENATURATION THRESHOLDS
<les-seuils-de-dénaturation-des-protéines-animales>
#figure(
  align(center)[#table(
  stroke: 0.5pt + rgb("#dcd6ca"),
  fill: (x, y) => if y == 0 { rgb("#f2ece1") } else if calc.odd(y) { rgb("#faf7f2") } else { none },
  inset: 8pt,

    columns: (33.33%, 33.33%, 33.33%),
    align: (left,left,left,),
    table.header([Core Temperature], [Physicochemical Phenomenon], [Culinary Result & Sensory Aspect],),
    table.hline(),
    [#strong[45°C - 50°C (113°F - 122°F)]], [Denaturation of myosin. Muscle fibers turn opaque.], [Blue-rare red meat; silky semi-cooked salmon.],
    [#strong[52°C - 55°C (126°F - 131°F)]], [Transverse retraction of sarcomeres.], [Rare meat (*saignant*). Maximum tenderness, abundant free juices.],
    [#strong[56°C - 60°C (133°F - 140°F)]], [Denaturation of myoglobin (shift to rose pink).], [Medium meat (*à point*). Onset of moderate moisture loss.],
    [#strong[62°C (144°F)]], [Coagulation of ovotransferrin in egg white.], [Egg white sets into a soft, creamy, delicate gel.],
    [#strong[65°C - 68°C (149°F - 154°F)]], [Sudden denaturation of actin and axial fiber contraction.], [Well-done meat (*bien cuit*). Cells violently expel intracellular moisture. Firm coagulation of egg yolk.],
    [#strong[68°C - 72°C (154°F - 162°F)]], [Onset of hydrogen bond cleavage in connective collagen.], [Ideal thermodynamic zone to initiate slow gelatinization of stewing cuts.],
    [#strong[80°C - 84°C (176°F - 183°F)]], [Coagulation of ovalbumin (54% of total egg white).], [Rigid, firm, fully opaque white.],
    [#strong[> 85°C (185°F) prolonged]], [Release of $upright(H)_2 upright(S)$ gas and precipitation with $upright(F e)^(2+)$.], [Formation of iron sulfide ($upright(F e S)$): unsightly greenish-grey ring around hard-boiled egg yolk.],
  )],
  caption: [Critical denaturation and coagulation thresholds of animal muscle and egg proteins.],
  kind: table
)

#divider()

== 2. STARCH AND SUGAR TRANSFORMATION THRESHOLDS
<les-seuils-de-lamidon-et-des-sucres>
#figure(
  align(center)[#table(
  stroke: 0.5pt + rgb("#dcd6ca"),
  fill: (x, y) => if y == 0 { rgb("#f2ece1") } else if calc.odd(y) { rgb("#faf7f2") } else { none },
  inset: 8pt,

    columns: (33.33%, 33.33%, 33.33%),
    align: (left,left,left,),
    table.header([Temperature], [Phenomenon], [Practical Kitchen Consequence],),
    table.hline(),
    [#strong[60°C - 70°C (140°F - 158°F)]], [Gelatinization of wheat and potato starch.], [Starch granules swell and absorb free water (sauce thickening, bread baking crumb structure).],
    [#strong[100°C (212°F)]], [Boiling of pure water at sea level.], [Absolute thermal plateau that cannot be exceeded as long as liquid water remains present.],
    [#strong[104°C - 105°C (219°F - 221°F)]], [Jam setting point (65% sugar concentration).], [Osmotic equilibrium and natural pectin network gelling.],
    [#strong[110°C - 115°C (230°F - 239°F)]], [Thread stage (*filet*) / sugar concentration.], [Initial sugar concentration for Italian meringues and marzipan paste.],
    [#strong[140°C - 165°C (284°F - 329°F)]], [#strong[Maillard Reaction.]], [Carbonyl-amine condensation: birth of roasted pyrazine aromas and crisp golden crusts.],
    [#strong[160°C - 180°C (320°F - 356°F)]], [#strong[Sucrose Caramelization.]], [Pure carbohydrate thermolysis without nitrogen: buttery hazelnut aromas and rich amber color.],
    [#strong[> 190°C (374°F)]], [Carbonaceous Pyrolysis.], [Burnt acrid bitterness and formation of undesirable harmful compounds (acrolein, PAHs).],
  )],
  caption: [Transformation and degradation thresholds of starches and carbohydrate sugars.],
  kind: table
)

#divider()

== 3. SMOKE POINTS OF COOKING FATS
<les-points-de-fumée-des-matières-grasses>
#figure(
  align(center)[#table(
  stroke: 0.5pt + rgb("#dcd6ca"),
  fill: (x, y) => if y == 0 { rgb("#f2ece1") } else if calc.odd(y) { rgb("#faf7f2") } else { none },
  inset: 8pt,

    columns: (25%, 25%, 25%, 25%),
    align: (left,left,left,left,),
    table.header([Cooking Fat], [Smoke Point], [Recommended Usage], [Precautions],),
    table.hline(),
    [#strong[Raw Unsalted Butter]], [150°C (302°F)], [Finishing, mounting, delicate low-heat pastry], [Do not overheat: whey milk proteins burn quickly into acrid black particles.],
    [#strong[Extra-Virgin Olive Oil]], [190°C (374°F)], [Cold dressing, gentle to medium sautéing], [Avoid intense repeated deep-frying to preserve delicate polyphenols.],
    [#strong[Duck / Goose Fat]], [190°C (374°F)], [Sarladaise potatoes, roasted root vegetables], [Outstanding culinary flavor, high thermal stability.],
    [#strong[Peanut Oil]], [220°C (428°F)], [Deep-frying, high-heat pan searing], [Neutral flavor profile, strong resistance to thermal oxidation.],
    [#strong[Clarified Butter (Ghee)]], [#strong[250°C (482°F)]], [Extreme high-heat searing, emulsified warm sauces], [Proteins and water fully eliminated: 100% pure lipid phase.],
  )],
  caption: [Smoke points and culinary operating zones of foundational culinary fats.],
  kind: table
)

#divider()

// =========================================================================
// APPENDIX B: COMPREHENSIVE GLOSSARY
// =========================================================================

= APPENDIX B --- Comprehensive Physicochemical & Culinary Glossary
<annexe-b-glossaire-physico-chimique-et-culinaire-exhaustif>
#quote(block: true)[
"Cooking is the art of transforming raw molecules into biological delight through heat, water, and mechanical force."
]

#divider()

=== Water Activity ($a_w$)
Dimensionless thermodynamic ratio between the vapor pressure of water in a food system ($p$) and the vapor pressure of pure water ($p_0$) at the identical temperature ($a_w = p / p_0$). Scales from 0 to 1.0. Fresh raw meat and produce have $a_w approx 0.99$. Microorganisms require free water to thrive: pathogenous bacteria halt proliferation below $a_w = 0.85$, while halophilic yeasts and osmophilic molds cease below $a_w = 0.60$. Salting, sugar concentration, and dehydration mechanically lock free water.

=== Actin & Myosin
The two primary contractile myofibrillar proteins composing skeletal muscle tissue. Myosin thick filaments denature and aggregate at 50°C (122°F), turning translucent pink flesh into opaque tender meat. Actin thin filaments contract axially at 65°C - 68°C (149°F - 154°F), wringing muscle sarcomeres like a sponge and expelling intracellular water into the pan fond.

=== Essential Amino Acids
The 9 amino acids that the human body cannot synthesize endogenously (leucine, isoleucine, valine, lysine, methionine, phenylalanine, threonine, tryptophan, histidine) and which must be acquired through diet. While animal muscle, eggs, and dairy provide all 9 in complete ratios, combining legumes (rich in lysine, deficient in methionine) with cereals (rich in methionine, deficient in lysine) yields an equivalent complete protein profile.

=== Alkylpyrazines
Heterocyclic aromatic compounds containing two nitrogen atoms in a six-membered carbon ring, synthesized during the advanced Maillard reaction between reducing sugars and free amino acids above 140°C (284°F). Responsible for the distinctive, mouth-watering roasted, nutty, popcorn, and crust notes found in seared steaks, roasted coffee, toasted bread, and roasted peanuts.

=== Starch (Amylose & Amylopectin)
The primary storage polysaccharide in plant grains and tubers. Composed of linear, tightly packed alpha-(1,4) chains of #strong[amylose] and highly branched alpha-(1,4) and alpha-(1,6) chains of #strong[amylopectin]. Amylose leaches into aqueous media at 60°C - 70°C (140°F - 158°F) to form firm gels; branched amylopectin produces glossy, elastic, creamy textures (as seen in risotto rice or mashed potatoes).

=== Appertization
Thermal sterilization process invented by Nicolas Appert in 1810: sealing foods inside hermetic containers (glass jars or metal tins) and subjecting them to sustained boiling water ($100^compose upright("C")$) or autoclaving ($121^compose upright("C")$) to destroy all vegetative pathogens and bacterial spores (*Clostridium botulinum*), enabling perpetual room-temperature shelf life without refrigeration.

=== Aquafaba
The viscous viscous cooking broth of chickpeas or other legumes. Rich in dissolved saponins, albuminous plant proteins, and soluble carbohydrates, aquafaba mimics the precise surface-tension reducing and film-forming properties of egg whites. When whipped with a whisk, it incorporates air into voluminous, stable molecular foams suitable for vegan chocolate mousses and meringues.

=== Botulism (_Clostridium botulinum_)
A lethal neurotoxic foodborne intoxication caused by ingestion of botulinum neurotoxin produced by the obligate anaerobic, spore-forming bacterium *Clostridium botulinum*. Its spores survive ordinary boiling at 100°C (212°F) and germinate in oxygen-deprived environments (oil preserves, canned vegetables, vacuum bags) where pH exceeds 4.6. Spores are destroyed only by pressurized autoclaving at 121°C (250°F) for 30 minutes, or the active neurotoxin is denatured by boiling above 85°C (185°F) for 10 minutes.

=== Volumetric Heat Capacity
The amount of thermal energy required to raise the temperature of $1 upright(" m")^3$ of a substance by $1^compose upright("C")$ ($upright("J")/(upright("m")^3 dot upright("K"))$). Pure water possesses an exceptionally high volumetric heat capacity ($4.18 upright(" MJ")/(upright("m")^3 dot upright("K"))$), making broths and water baths immense thermal buffers. In contrast, dry air possesses a minuscule heat capacity ($0.0012 upright(" MJ")/(upright("m")^3 dot upright("K"))$), explaining why human skin can endure 100°C dry sauna air without scorching, but is instantly scalded by 100°C liquid water.

=== Casein
The principal family of phosphoproteins representing 80% of total milk proteins. Grouped into sub-micellar spherical clusters held together by colloidal calcium phosphate. The protruding hydrophobic and negatively charged hairy layer of $kappa$-casein prevents micelle aggregation. When milk pH drops to 4.6 (acid curdling) or when chymosin cleaves $kappa$-casein (rennet curdling), electrostatic repulsion vanishes and caseins aggregate into curd.

=== Coalescence
The spontaneous thermodynamic collapse and fusion of two or more dispersed emulsion droplets (such as oil droplets in water) into a single larger droplet, driven by the drive to minimize interfacial free surface energy. If unchecked by surface-active emulsifiers (lecithin, proteins), continuous coalescence causes full phase separation (a broken mayonnaise or hollandaise).

=== Collagen & Gelatin
Collagen is the primary structural protein of connective tissue (tendons, epimysium, skin, bones), composed of an insoluble, tightly wound triple-helix of tropocollagen fibers rich in glycine, proline, and hydroxyproline. Between 68°C and 80°C (154°F - 176°F), heat and water disrupt hydrogen bonds, unraveling the triple-helix into water-soluble, succulent #strong[gelatin], which dissolves into cooking broths and sets into a wobble gel upon cooling below 15°C (59°F).

=== Conduction, Convection, Radiation
The 3 fundamental modes of thermodynamic heat transfer in the kitchen:
- #strong[Conduction:] Kinetic energy transfer through direct molecular contact (pan base touching a steak), governed by Fourier's law. Diffusion time scales quadratically with thickness ($t prop x^2$).
- #strong[Convection:] Macroscopic fluid transport of heat via liquid or gas currents (simmering stock, forced-air convection oven).
- #strong[Radiation:] Electromagnetic emission of infrared photons, scaling with absolute temperature to the fourth power according to the Stefan-Boltzmann law ($E prop T^4$). Found in glowing charcoal grills and overhead broilers.

=== Denaturation
The structural unraveling of a protein's native three-dimensional conformation (quaternary, tertiary, secondary structures) caused by thermal energy, mechanical shearing, high salinity, or acidic pH, without cleaving primary covalent peptide bonds. Once unraveled, exposed hydrophobic amino acid side-chains cross-link with neighboring chains to form a rigid or tender cohesive protein gel (coagulation).

=== Leidenfrost Effect
A physical phenomenon occurring when a liquid droplet comes into contact with a solid surface heated significantly above the liquid's boiling point ($> 190^compose upright("C")$ for water). The droplet's bottom vaporizes instantaneously, creating a micro-layer of insulating steam ($0.1 upright(" mm")$) that suspends the droplet and prevents direct conduction. In cooking, water droplets skittering cleanly across a pan confirm that the steel has reached the optimal Maillard searing zone.

=== Emulsion
A thermodynamically unstable colloidal dispersion of two immiscible liquid phases, where one liquid is broken into microscopic droplets (dispersed phase) throughout the volume of the other (continuous phase). Examples include oil-in-water emulsions (mayonnaise, milk, hollandaise, vinaigrette) and water-in-oil emulsions (butter). Stability requires an amphiphilic surfactant.

=== Starch Gelatinization
The irreversible swelling, hydration, and disruption of semicrystalline starch granules placed in excess water above 60°C - 70°C (140°F - 158°F). Water penetrates the amorphous regions of the granule, hydrogen bonds with hydroxyl groups, and causes amylose chains to leach out into the continuous liquid phase, resulting in a thick, velvety viscous sauce.

=== Lecithin (Phosphatidylcholine)
An amphiphilic phospholipid naturally abundant in egg yolks, soybeans, and sunflower seeds. Features a hydrophilic (water-loving) polar head containing a negatively charged phosphate group and positively charged choline, attached to two long hydrophobic (fat-loving) fatty acid hydrocarbon tails. Forms micellar monolayers around oil droplets, preventing coalescence and stabilizing oil-in-water emulsions.

=== Lysozyme
A 14.3 kDa antibacterial enzyme naturally present in egg whites (3.5% of total protein) and human tears. Hydrolyzes the $beta$-(1,4)-glycosidic bonds between N-acetylmuramic acid and N-acetylglucosamine in the peptidoglycan cell walls of Gram-positive bacteria, protecting the embryonic yolk from bacterial invasion during incubation.

=== Osmosis
The spontaneous net migration of water molecules across a semipermeable membrane from a region of lower solute concentration (hypotonic) toward a region of higher solute concentration (hypertonic), driven by the gradient in chemical potential. In culinary practice, salting draws intracellular moisture to the surface of aubergines and raw meats, while dense sugar brines pull liquid out of fruit cells during maceration.

=== Pectin
A structural heteropolysaccharide found in the primary cell walls and middle lamella of fruits and terrestrial plants, rich in alpha-(1,4)-linked D-galacturonic acid units. In acidic media ($upright("pH") < 3.5$) and in the presence of concentrated sucrose ($> 60 %$), electrostatic carboxyl charges are neutralized and water is bound, allowing pectin chains to cross-link into a solid three-dimensional jam jelly.

=== Smoke Point
The exact temperature at which a heated culinary fat or oil begins to break down into visible bluish smoke, pungent volatile acrolein, and free fatty acids. Operating a fat beyond its smoke point denatures its flavor, degrades antioxidants, and generates carcinogenic polycyclic aromatic hydrocarbons (PAHs).

=== Protein
A complex biological macromolecule assembled from linear chains of amino acids linked by covalent peptide bonds, folded into a unique three-dimensional conformation determined by hydrogen bonds, ionic salt bridges, disulfide bonds, and hydrophobic interactions. Denaturation and structural cross-linking of food proteins dictate the texture of roasted meats, set eggs, and curdled cheeses.

=== Maillard Reaction
A non-enzymatic cascade of chemical condensations between the carbonyl group of a reducing sugar and the free nucleophilic amino group of an amino acid or protein, initiated between 140°C and 165°C (284°F - 329°F). Produces glycosylamines, Amadori rearrangement intermediates, and ultimately hundreds of volatile aroma compounds (alkylpyrazines, furans, thiols) accompanied by high-molecular-weight brown pigments called #strong[melanoidins].

=== This (Hervé) & Kurti (Nicholas)
Co-founders of Molecular and Physical Gastronomy in 1988 at Oxford and Paris. Nicholas Kurti (1908–1998), Oxford cryophysicist, and Hervé This (born 1955), physical chemist at AgroParisTech/INRAE, introduced scientific rigor, precision temperature measurement, and chemical deconstruction to classical culinary folklore.

=== Umami
The fifth basic human taste modality, identified in 1908 by Japanese chemist Kikunae Ikeda. Triggered primarily by the presence of free monosodium L-glutamate (MSG) and synergistically magnified tenfold by purine ribonucleotides (disodium 5'-inosinate and 5'-guanylate). Found in cured ham, aged Parmesan cheese, ripe tomatoes, dried shiitake mushrooms, kombu kelp, and slowly reduced meat glazes.

#divider()

// =========================================================================
// APPENDIX C: EVALUATED BIBLIOGRAPHY
// =========================================================================

= APPENDIX C --- Critical & Evaluated Bibliography
<annexe-c-bibliographie-raisonnée-et-répertoire-critique>
#quote(block: true)[
"The discovery of a new dish confers more happiness on humanity than the discovery of a new star." \ --- Jean Anthelme Brillat-Savarin, #emph[Physiology of Taste] (1825)
]

#divider()

== 1. FOUNDATIONAL, HERITAGE & HISTORICAL TREATISES
<traités-fondamentaux-patrimoniaux-et-historiques>
- #strong[Marcus Gavius Apicius] --- #emph[De re coquinaria] (1st - 4th century AD). \ #emph[Critical Latin-English edition established and translated by J. André / C. Grocock & S. Grainger.] \ #emph[Critical Notice:] #strong[[Foundational Historical Treatise]] \ The founding written corpus of Imperial Roman dining. Documents the mastery of enzymatic autolysis through *garum* (the Roman predecessor to Southeast Asian fish sauce), food preservation through raw honey and vinegars, and heavy peppery seasoning anticipating modern umami.

- #strong[Guillaume Tirel dit Taillevent] --- #emph[Le Viandier] (c. 1380). \ #emph[Master reference edition based on the Bibliothèque Nationale de France manuscript.] \ #emph[Critical Notice:] #strong[[Foundational Historical Treatise]] \ The zenith of European medieval court cuisine. Codifies two-stage thermal cooking (initial water poaching followed by coal spit-roasting) and vibrant, fat-free sauces thickened with soaked stale bread and sharpened with tart grape verjuice.

- #strong[Anonymous Bourgeois Parisian] --- #emph[Le Ménagier de Paris] (1393). \ #emph[Critical Notice:] #strong[[Domestic Kitchen Autonomy & Pantry Storage]] \ A remarkable medieval household guide written by an elder merchant for his young wife. Provides comprehensive instructions for running a home pantry, salt-curing whole meats, clarifying spoiled wines, and stocking food long before artificial refrigeration.

- #strong[Bartolomeo Scappi] --- #emph[Opera dell'arte del cucinare] (Venice, 1570). \ #emph[Critical Notice:] #strong[[Pioneer of Kitchen Knife Biomechanics & Arsenal Minimalism]] \ Private chef to Renaissance Popes Pius IV and Pius V in Rome. The first culinary treatise extensively illustrated with copperplate engravings of chef's knives, turnspits, and copper pots. Codified the double-boiler (*bain-marie*) for yolk-thickened sauces and distinguished cuts by muscle grain.

- #strong[François Pierre de La Varenne] --- #emph[Le Cuisinier François] (1651). \ #emph[Critical Notice:] #strong[[The Birth of Classical French Cooking]] \ The decisive historical break from heavy medieval spices in favor of fresh sweet dairy butter, native aromatic herbs (tarragon, chervil, bay leaf), and the revolutionary invention of flour roux to thicken gravies.

- #strong[Jean Anthelme Brillat-Savarin] --- #emph[The Physiology of Taste, or Meditations on Transcendental Gastronomy] (1825). \ #emph[Critical Notice:] #strong[[The Master Philosophical & Sensory Reference]] \ The most witty, profound, and lyrical volume ever written on the act of human eating. A pioneering exploration of oral physiology, retro-nasal olfaction, the thermodynamics of frying oil, and the social philosophy of the meal.

- #strong[Auguste Escoffier] --- #emph[Le Guide Culinaire] (1903, with Philéas Gilbert and Émile Fétu). \ #emph[Critical Notice:] #strong[[The Bible of Kitchen Codification & Brigade Order]] \ The definitive legislative architecture of classical French cuisine. Established the military precision of the kitchen brigade, codified the five mother sauces (Espagnole, Velouté, Béchamel, Tomate, Hollandaise), and distilled culinary technique to pure essentials.

- #strong[Domus Editorial Collective] --- #emph[The Silver Spoon] (#emph[Il Cucchiaio d'Argento], Editoriale Domus, Milan, 1950; Phaidon). \ #emph[Critical Notice:] #strong[[Universal Classic of Italian Domestic Cooking]] \ The timeless treasure of Italian home kitchens. Teaches the nobility of humble gestures, the art of hand-rolled egg pasta, pan-searing truth, and the raw beauty of unadorned seasonal produce.

#divider()

== 2. EVOLUTIONARY ANTHROPOLOGY & NUTRITIONAL BIOLOGY
<anthropologie-évolutive-et-biologie-de-la-nutrition>
- #strong[Richard Wrangham] --- #emph[Catching Fire: How Cooking Made Us Human] (Basic Books). \ #emph[Critical Notice:] #strong[[Revolutionary Anthropological Treatise]] \ Proves that the thermal mastery of fire preceded and drove the speciation of *Homo sapiens*: externalizing digestion through cooking drastically reduced the energy cost of the gut, freeing metabolic calories to fuel the tripling of human brain volume.

- #strong[Claude Lévi-Strauss] --- #emph[The Raw and the Cooked] (#emph[Mythologiques], Vol. 1, Plon / University of Chicago Press, 1964). \ #emph[Critical Notice:] #strong[[Structural Anthropology of Human Diet]] \ The profound structural analysis of the universal culinary triangle (the Raw, the Cooked, and the Rotted). Illuminates how passing food through the domestic hearth transforms raw biology into human culture, kinship, and civilization.

#divider()

== 3. MOLECULAR GASTRONOMY & KITCHEN SCIENCE
<gastronomie-moléculaire-et-science-de-la-casserole>
- #strong[Harold McGee] --- #emph[On Food and Cooking: The Science and Lore of the Kitchen] (Scribner). \ #emph[Critical Notice:] #strong[[The Indispensable Global Scientific Masterwork]] \ The exhaustive bedside encyclopedia of modern chefs. Deconstructs atom by atom the physics and chemistry of emulsions, foams, animal myofibrillar proteins, plant cell walls, and fermentation dynamics.

- #strong[Nicholas Kurti & Hervé This] --- #emph[Les Secrets de la casserole] (Belin, 1993); #emph[Molecular Gastronomy: Exploring the Science of Flavor] (Columbia University Press, 2006). \ #emph[Critical Notice:] #strong[[Founding Molecular Gastronomy Corpus]] \ The originators of the discipline in 1988. Rigorous experimental deconstruction of grandmotherly culinary myths, discovery of fractional 64°C egg coagulation, and structural modeling of sauce emulsions.

- #strong[Heston Blumenthal] --- #emph[The Fat Duck Cookbook] (Bloomsbury); #emph[In Search of Perfection] (Bloomsbury). \ #emph[Critical Notice:] #strong[[Three-Star Sensory Excellence via Pure Scientific Method]] \ Relentless pursuit of aromatic volatile extraction (potato peel infusion for mashed potatoes), triple-cooked french fries, and multi-sensory flavor perception.

- #strong[Nathan Myhrvold, Chris Young & Maxime Bilet] --- #emph[Modernist Cuisine: The Art and Science of Cooking] (The Cooking Lab, 6 volumes). \ #emph[Critical Notice:] #strong[[The Monumental Technical Compendium of the 21st Century]] \ Cutaway macro-photography of vessels inside living fire, ultra-precision thermodynamics, rotary evaporation, and industrial hydrocolloids applied to culinary creativity.

- #strong[J. Kenji López-Alt] --- #emph[The Food Lab: Better Home Cooking Through Science] (W. W. Norton). \ #emph[Critical Notice:] #strong[[The Best Contemporary Practical Kitchen Manual]] \ Brilliant application of the empirical experimental method to everyday home cooking: 45-minute advance dry brining of steaks, heavy cast-iron searing physics, and the ultimate smashed burger.

- #strong[Samin Nosrat] --- #emph[Salt, Fat, Acid, Heat: Mastering the Elements of Good Cooking] (Simon & Schuster). \ #emph[Critical Notice:] #strong[[Global Best-Selling Intuitive Primer]] \ Luminous and universal synthesis of the 4 foundational pillars of cooking, enabling home cooks to season instinctively without being held captive by recipes.

#divider()

// =========================================================================
// APPENDIX D: BUYER'S GUIDE, POWER & COOKING TIMES
// =========================================================================

= APPENDIX D --- Buyer's Guide to the Minimal Arsenal, Energy Costs & Cooking Time Dial
<annexe-d-guide-dachat-de-larsenal-minimal-coûts-et-durées>
#quote(block: true)[
"A true cook needs few tools, but requires those tools to be indestructible, thermodynamically dense, and balanced in the hand."
]

#divider()

== 1. THE PRACTITIONER'S MINIMAL ARSENAL: BUYER'S GUIDE & QUALITY DETECTION
<larsenal-minimal-du-praticien-guide-dachat-détection-du-bon-matériel>

Selecting kitchen tools is an investment for life. A poor pan warps under heat, creates scorching hotspots, and wastes energy; an authentic instrument improves with age:

#figure(
  align(center)[#table(
    stroke: 0.5pt + rgb("#dcd6ca"),
    fill: (x, y) => if y == 0 { rgb("#f2ece1") } else if calc.odd(y) { rgb("#faf7f2") } else { none },
    inset: 8pt,
    columns: (22%, 22%, 28%, 28%),
    align: (left, left, left, left),
    table.header([Instrument], [Recommended Material], [Physical Hallmark of Quality], [Pitfalls to Reject]),
    table.hline(),
    [#strong[1. Chef's Knife (20 cm / 8 in)]], [High-carbon steel or AUS-10 / VG-10 stainless], [Full-tang blade forged from a single billet; neutral balance point right at bolster.], [Welded bolster, thin stamped sheet metal, hollow plastic handle.],
    [#strong[2. Cast-Iron Skillet (26 cm / 10 in)]], [Raw cast iron or heavy carbon steel (2.5 - 3 mm)], [Heavy weight ($> 2 upright(" kg")$ / 4.4 lb), thick thermal bottom for immense heat retention.], [Thin non-stick coatings (PTFE) that blister and degrade above 200°C (392°F).],
    [#strong[3. Dutch Oven (5.5 L / 6 qt)]], [Heavy enameled cast iron], [Dense tight-fitting lid with moisture-recirculating interior spikes; thick flat base.], [Lightweight stamped aluminum, plastic lid knobs that melt in hot ovens.],
    [#strong[4. Stainless Sauté Pan (24 cm)]], [Tri-ply stainless steel (18/10 stainless + aluminum core)], [Aluminum core encapsulated continuously up the entire sidewalls (full clad).], [Thin disc-bottom bonded only to base with thermal discontinuity at edges.],
    [#strong[5. Large Stockpot (8 - 10 L)]], [18/10 surgical stainless steel], [Sturdy riveted handles, wide diameter for evaporation, thick base.], [Thin walls that dent easily; spot-welded hollow handles that snap.],
    [#strong[6. End-Grain Cutting Board]], [Hardwood (Rock Maple, Walnut, Beech)], [Thick end-grain wood fibers ($4 - 5 upright(" cm")$ / 1.5 - 2 in) that absorb knife impact without dulling blade.], [Glass, granite, or bamboo boards that chip steel cutting edges instantly.],
    [#strong[7. Digital Thermometer]], [Fast-response thermocouple needle], [Reading speed $< 2 upright(" seconds")$, millimetric thin probe, accuracy $plus.minus 0.5^compose upright("C")$.], [Slow dial bi-metal gauges with wide thermal hysteresis and uncalibrated readings.],
    [#strong[8. Fine Mesh Chinois]], [Conical woven stainless mesh], [Fine woven wire cone with welded protective outer ribs and sturdy hanging loop.], [Coarse perforated sheet metal strainers that let sediment and fiber through.]
  )],
  caption: [Buyer's guide and quality evaluation criteria for the Minimal Eight Arsenal.],
  kind: table
)

#divider()

== 2. COMPARATIVE THERMODYNAMICS OF COOKING MODES: EFFICIENCY, POWER & ENERGY COST
<thermodynamique-comparée-des-modes-de-cuisson-rendement-puissance-coût-en-énergie>

The primary function of a kitchen heat source is the transfer of thermodynamic energy into the food mass. However, each cooking medium exhibits vastly different energetic efficiencies:

#figure(
  align(center)[#table(
    stroke: 0.5pt + rgb("#dcd6ca"),
    fill: (x, y) => if y == 0 { rgb("#f2ece1") } else if calc.odd(y) { rgb("#faf7f2") } else { none },
    inset: 8pt,
    columns: (22%, 22%, 28%, 28%),
    align: (left, center, center, left),
    table.header([Heat Source / Appliance], [Nominal Power (Watts)], [Energetic Efficiency (%)], [Physical Vector & Heat Loss]),
    table.hline(),
    [#strong[Induction Cooktop]], [1,800 to 3,500 W], [#strong[85% to 90%]], [Direct magnetic eddy current generation inside pan steel. Almost zero ambient heat loss.],
    [#strong[Microwave Oven]], [800 to 1,000 W], [#strong[65% to 70%]], [Direct 2.45 GHz dielectric rotation of polar water molecules. Very efficient for small reheating volumes.],
    [#strong[Ceramic / Radiant Hob]], [1,500 to 2,200 W], [60% to 65%], [Slow conduction through glass-ceramic surface. Substantial residual heat loss.],
    [#strong[Forced-Air Convection Oven]], [2,000 to 2,500 W], [15% to 20%], [Heats an entire cavity of low-density air ($0.0012 upright(" J/(cm")^3 upright("·K)")$) with high wall losses.],
    [#strong[Standard Domestic Gas Burner]], [1,500 to 3,500 W], [35% to 40%], [Open methane combustion flame: 60% of thermal heat escapes laterally into kitchen air.]
  )],
  caption: [Comparative energetic efficiency and power consumption across kitchen heating vectors.],
  kind: table
)

==== 🔬 The Physics of Induction Efficiency: Eddy Currents & Joule Heating
Induction cooktops do not generate heat. A high-frequency alternating electrical current (20 to 50 kHz) flows through a copper coil beneath the glass-ceramic plate, generating a fluctuating magnetic field. When a ferromagnetic vessel (cast iron, 18/10 stainless steel) is placed within this field, the magnetic flux induces circular electrical currents—#strong[Foucault eddy currents]—inside the pan's metallic base. Heat is synthesized directly within the metal itself via resistance (Joule heating: $P = R dot I^2$). Because the cooktop surface remains cool except for contact feedback, energetic losses are virtually non-existent.

#divider()

== 3. SYNOPTIC MASTER COOKING TIMES BY METHOD & FOOD
<tableau-synoptique-des-durées-de-cuisson-standard-par-méthode-aliment>

Cooking times cannot be calculated purely by weight; they depend fundamentally on the food's geometry, water content, and heat transfer method (conduction through metal, water convection, or air radiation):

#figure(
  align(center)[#table(
    stroke: 0.5pt + rgb("#dcd6ca"),
    fill: (x, y) => if y == 0 { rgb("#f2ece1") } else if calc.odd(y) { rgb("#faf7f2") } else { none },
    inset: 7pt,
    columns: (22%, 24%, 26%, 28%),
    align: (left, left, left, left),
    table.header([Food Category], [Ideal Thermal Threshold], [Standard Cooking Mode], [Calibrated Duration & Landmark Sensory Test]),
    table.hline(),
    [#strong[Thick Beef Steak (3.5 cm / 1.5 in)]], [54°C (129°F) core (rare)], [Very hot cast-iron skillet ($> 200^compose upright("C")$)], [2 min per side + 5 min basting with foaming butter. Firm thumb-spring bounce.],
    [#strong[Whole Chicken (1.5 kg / 3.3 lb)]], [74°C (165°F) thigh joint], [Convection oven at 190°C (374°F)], [1 hr to 1 hr 15 min. Clear juices running from cavity, crisp crackling skin.],
    [#strong[Collagen Beef Shank / Stew]], [85°C to 90°C (185°F - 194°F) liquid], [Gentle simmer in Dutch oven], [3 to 4 hours under tight lid. Meat yields under fork with zero resistance.],
    [#strong[White Fish Fillet (Cod, 150 g)]], [50°C to 52°C (122°F - 126°F) core], [Gentle water poaching or parchment packet], [6 to 8 minutes at 80°C (176°F). Myotome flakes separate under slight blade pressure.],
    [#strong[Large Whole Egg (60 g)]], [63°C white / 65°C yolk], [Rolling boiling water ($100^compose upright("C")$)], [#strong[Soft-Boiled (*mollet*):] exactly 6 min; #strong[Hard-Boiled:] 9 min in cold water plunge.],
    [#strong[Potatoes (medium whole)]], [88°C to 90°C (190°F - 194°F) core], [Cold water start, gentle simmer], [20 to 25 minutes. Paring knife blade slides in and out without lifting tuber.],
    [#strong[Dried Legumes (soaked)]], [Full starch swelling ($> 95^compose upright("C")$)], [Slow steady simmer in stockpot], [45 min (Lentils) to 1 hr 30 min (Chickpeas). Butter-soft core, intact outer skins.]
  )],
  caption: [Synoptic master cooking durations, internal temperatures, and sensory readiness tests.],
  kind: table
)

#divider()

// =========================================================================
// APPENDIX E: REFRIGERATION & FOOD PRESERVATION
// =========================================================================

= APPENDIX E --- Cold Chain Storage, Refrigerator Zones & Food Safety Limits
<annexe-e-conservation-au-froid-zones-du-réfrigérateur-durées-limites-sanitaires>
#quote(block: true)[
"Cold does not kill bacteria: it slows their enzymatic metabolism. Mastering the cold chain is the invisible frontier of kitchen survival."
]

#divider()

== 1. REFRIGERATOR THERMAL MAPPING: A BIO-ZONE ON EVERY SHELF
<cartographie-thermique-du-réfrigérateur-à-chaque-étage-sa-bio-zone>

A domestic refrigerator is not a thermally uniform volume. Because cold air is denser than warm air ($rho prop 1/T$), air naturally settles downward via natural convection. In static refrigerators, vertical temperature deltas can reach $6^compose upright("C")$. Each shelf corresponds to a distinct ecological biological niche:

#figure(
  align(center)[#table(
    stroke: 0.5pt + rgb("#dcd6ca"),
    fill: (x, y) => if y == 0 { rgb("#f2ece1") } else if calc.odd(y) { rgb("#faf7f2") } else { none },
    inset: 8pt,
    columns: (22%, 22%, 28%, 28%),
    align: (left, center, left, left),
    table.header([Refrigerator Level / Compartment], [Internal Temperature], [Foods to Store Exclusively], [Physical & Biological Rationale]),
    table.hline(),
    [#strong[Extra-Cold Zone (Lower Shelf above crisper)]], [#strong[0°C to 2°C (32°F to 36°F)]], [Raw meats, ground beef, fresh fish, shellfish, thawed raw poultry.], [Halts proliferation of psychrotrophic pathogens (*Listeria monocytogenes*). Keeps moisture from weeping.],
    [#strong[Intermediate Cold Zone (Middle Shelves)]], [#strong[3°C to 4°C (37°F to 39°F)]], [Cooked leftovers, homemade broths, artisan dairy, farm cheeses, open preserves.], [Stable cold environment. Minimizes enzymatic degradation of cooked proteins and dairy.],
    [#strong[Upper Shelf (Top Level)]], [#strong[5°C to 6°C (41°F to 43°F)]], [Pastries, packaged cooked ham, commercial yogurts, fermented butter.], [Gentle cold preserving delicate emulsified fats without hardening butter excessively.],
    [#strong[Vegetable Crisper Drawer]], [#strong[6°C to 8°C (43°F to 46°F)]], [Fresh leafy greens, crucifers, root vegetables, ripe stone fruits.], [Higher relative humidity (85 - 90%) prevents cellular transpirational wilting; prevents cold-burn.],
    [#strong[Refrigerator Door Racks]], [#strong[6°C to 9°C (43°F to 48°F)]], [Condiments, Dijon mustard, natural vinegars, pasteurized milk bottles, eggs in shell.], [Most thermally vulnerable zone: subjected to repetitive room-air thermal shocks on opening.]
  )],
  caption: [Refrigerator thermal bio-zones and calibrated ingredient positioning.],
  kind: table
)

==== ⚠️ Critical Food Safety Error: Never Store Raw Meat Above Cooked Dishes
Never place raw meats, poultry, or draining seafood on upper shelves above ready-to-eat cooked leftovers or fresh greens. Raw protein weeping contains high microbial loads (*Salmonella enterica*, *Campylobacter jejuni*, *E. coli*). A single drop falling into a cooked dish consumed without subsequent high-heat re-boiling causes instant acute food intoxication.

#divider()

== 2. COMPREHENSIVE SANITARY STORAGE DURATIONS: REFRIGERATOR VS. FREEZER
<tableau-exhaustif-des-durées-de-conservation-sanitaires-frigo-vs-congélateur>

#figure(
  align(center)[#table(
    stroke: 0.5pt + rgb("#dcd6ca"),
    fill: (x, y) => if y == 0 { rgb("#f2ece1") } else if calc.odd(y) { rgb("#faf7f2") } else { none },
    inset: 7pt,
    columns: (28%, 24%, 24%, 24%),
    align: (left, center, center, left),
    table.header([Ingredient / Food System], [Refrigerator (0°C to 4°C / 32°F to 39°F)], [Freezer (-18°C / 0°F)], [Key Spoilage Marker & Safety Reflex]),
    table.hline(),
    [#strong[Ground Beef / Raw Steak Tartare]], [#strong[12 to 24 hours max]], [3 to 4 months], [Extreme bacterial surface area. Consume same day as ground.],
    [#strong[Fresh White Fish & Raw Shrimp]], [#strong[24 to 48 hours max]], [3 to 6 months], [Fast enzymatic proteolysis. Flesh softens, sweet ammonia smell emerges.],
    [#strong[Whole Chicken / Poultry Cuts]], [2 to 3 days], [9 to 12 months], [Surface slime, sulfur odor. Wrap tightly in airtight containers.],
    [#strong[Thick Beef Steaks / Roasts]], [3 to 4 days], [8 to 12 months], [Deep red oxidation is harmless; discard if sticky or foul-smelling.],
    [#strong[Cooked Dishes, Soups & Broths]], [3 to 4 days], [3 months], [Reheat thoroughly to boiling ($> 85^compose upright("C")$) before serving.],
    [#strong[Raw Shell Eggs in Carton]], [28 to 30 days], [Do not freeze in shell], [Washed shells lose cuticle; float test reveals internal air expansion.],
    [#strong[Open Pasteurized Milk / Cream]], [4 to 5 days], [Not recommended], [Lactic souring; fat globules separate upon thawing.]
  )],
  caption: [Microbiological food safety storage limits: Refrigerator vs. Deep Freezer.],
  kind: table
)

#divider()

== 3. RAPID SAFE THAWING PROTOCOL WITHOUT BACTERIAL RISK
<protocole-expéditif-de-décongélation-sans-risque-bactérien>

==== ✓ The Only Safe Thawing Methods:
1. #strong[Slow Refrigerator Thawing (Safest Gold Standard):] Place frozen meat on a rimmed plate in the coldest zone ($0^compose upright(" to ") 2^compose upright("C")$) for 12 to 24 hours. The food remains entirely outside the danger zone ($4^compose upright(" to ") 60^compose upright("C")$).
2. #strong[Submerged Cold Water Bath (Fast & Safe):] Seal food tightly inside an airtight leakproof bag and submerge completely in a bowl of cold tap water ($< 15^compose upright("C")$), changing the water every 30 minutes. Water's high thermal conductivity thaws food within 45 to 60 minutes.
3. #strong[Direct-to-Pan Cooking for Thin Cuts:] Steaks under $2 upright(" cm")$ can be seared directly from frozen in a screaming-hot cast-iron pan, then finished under gentle oven heat.

==== ✗ The Fatal Mistake: Ambient Countertop Thawing
Leaving raw poultry or meat to thaw at room temperature on the kitchen counter is a dangerous biohazard. While the core remains frozen solid for hours, the outer surface reaches $20^compose upright("C")$ within 45 minutes, creating explosive exponential bacterial growth ($2^n$ doubling every 20 minutes) across the exterior tissue.

#divider()

// =========================================================================
// APPENDIX F: PREP CUTLERY, CONSUMABLES & GROCERY TEMPLATE
// =========================================================================

= APPENDIX F --- Prep Cutlery, Household Consumables, Matrix Pantry & Clean Grocery Template
<larsenal-doffice-consommables-domestiques-fond-de-placard-gabarit-matriciel-de-courses-saines>
#quote(block: true)[
"The kitchen is a laboratory of sovereign autonomy: equip it with essentials, banish disposable plastics, and govern your pantry with order."
]

#divider()

== 1. DAILY PREP CUTLERY & KITCHEN UTENSILS (BEYOND THE MINIMAL EIGHT)
<léquipement-doffice-coutellerie-du-quotidien-au-delà-des-huit-grands-instruments>

While the Minimal Eight tools manage 90% of culinary transformations, secondary prep utensils provide mechanical precision and speed:

#figure(
  align(center)[#table(
    stroke: 0.5pt + rgb("#dcd6ca"),
    fill: (x, y) => if y == 0 { rgb("#f2ece1") } else if calc.odd(y) { rgb("#faf7f2") } else { none },
    inset: 7pt,
    columns: (22%, 22%, 28%, 28%),
    align: (left, left, left, left),
    table.header([Utensil], [Recommended Material], [Culinary Role & Physics], [Quality Hallmark]),
    table.hline(),
    [#strong[Short Paring Knife (8 - 10 cm)]], [Carbon or stainless steel], [Precision peeling, coring, trimming, garlic mincing.], [Rigid blade, fine sharp tip, comfortable pinch grip.],
    [#strong[Y-Peeler (Razor Peeler)]], [Carbon steel blade], [Removes sub-millimetric vegetable skins without wasting flesh.], [Swiveling carbon blade, far sharper than dull stainless.],
    [#strong[Serrated Bread Knife (22 cm)]], [Stiff stainless steel], [Slices through crackling crusts without crushing crumb.], [Deep scalloped serrations, zero lateral blade flex.],
    [#strong[Solid Stainless Spoon]], [18/10 stainless steel], [Basting steaks with foaming butter; stirring pan sauces.], [Deep bowl, long rigid handle that does not heat up.],
    [#strong[Solid Beech Wooden Spoon]], [Solid untreated beechwood], [Stirring roux, deglazing pan fond without scratching iron.], [Flat-edged spatula corner to scrape pan corners clean.],
    [#strong[Offset Metal Spatula]], [Spring stainless steel], [Deglazing, flipping burgers, scraping searing fond.], [Beveled ground front edge, firm spring resistance.],
    [#strong[Silicone Spatula (Maryse)]], [High-heat silicone (250°C)], [Zero-waste scraping of bowls; gentle foam folding.], [Seamless one-piece silicone molding, flexible tip.],
    [#strong[Precision Chef's Tongs (30 cm)]], [18/10 stainless steel], [Delicate placement, turning meats without piercing fibers.], [Firm spring tension, scalloped gripping tips.],
    [#strong[Two-Prong Meat Carving Fork]], [Forged stainless steel], [Anchoring roasts during carving; testing braised doneness.], [Long tapered rigid prongs, forged bolster.],
    [#strong[Stainless Wire Spider Skimmer]], [Crossed stainless wire], [Retrieving gnocchi, deep-fried foods, blanching greens.], [Open woven wire mesh that drains liquid instantaneously.],
    [#strong[One-Piece Soup Ladle]], [Seamless stamped stainless], [Serving broths, transferring stocks without drips.], [Zero welded seams between handle and bowl.],
    [#strong[12-Wire Balloon Whisk]], [Spring stainless steel], [Beating egg whites, emulsifying mayonnaise, silky sauces.], [Flexible wires anchored in sealed resin handle.],
    [#strong[Microplane Fine Grater]], [Photo-etched stainless steel], [Zesting citrus without white bitter pith, grating Parmigiano.], [Razor-sharp etched teeth that slice instead of tearing.],
    [#strong[Heavy Kitchen Shears]], [Take-apart stainless steel], [Snipping poultry bones, trimming herb stems, fish fins.], [Center joint uncouples completely for thorough sanitization.]
  )],
  caption: [Comprehensive guide to secondary prep cutlery and kitchen utensils.],
  kind: table
)

#divider()

== 2. HOUSEHOLD TECHNICAL CONSUMABLES: SAFETY AND CONTACT
<les-consommables-techniques-du-foyer-thermodynamique-contact-et-sécurité>

Household consumables are not passive packaging: they participate directly in thermodynamic heat exchange and chemical surface contact:

#figure(
  align(center)[#table(
    stroke: 0.5pt + rgb("#dcd6ca"),
    fill: (x, y) => if y == 0 { rgb("#f2ece1") } else if calc.odd(y) { rgb("#faf7f2") } else { none },
    inset: 7pt,
    columns: (22%, 22%, 28%, 28%),
    align: (left, left, left, left),
    table.header([Technical Consumable], [Material & Limits], [Virtuous Operating Gesture], [Dangerous Misuse to Reject]),
    table.hline(),
    [#strong[Unbleached Parchment Paper]], [Siliconized cellulose (heat safe to 220°C / 428°F)], [Baking pan lining, parchment cartouche lids for glazed vegetables, en papillote packets.], [Never expose to open broiler element ($> 250^compose upright("C")$); paper chars and catches fire.],
    [#strong[Heavy Aluminum Foil]], [Pure metal alloy ($18 - 25 upright(" µm")$ thickness)], [Heat-shield wrapping for resting roasts; tight lid seal for long oven braises.], [#strong[Strictly avoid contact with acidic foods] (tomatoes, lemon, vinegars); acid leaches ionic aluminum into food.],
    [#strong[100% Cotton Kitchen Twine]], [Pure unbleached natural cotton], [Trussing whole chickens for uniform roasting; binding rolled roasts and herb bouquets garni.], [Never use synthetic nylon cords: plastics melt and decompose into toxic compounds under heat.],
    [#strong[Cheesecloth & Fine Linen]], [Fine unbleached cotton mesh], [Draining fresh farm curd in 15 min; straining broths and consommés to mirror clarity.], [Wash exclusively with unscented neutral soap; scented detergents ruin food flavors.],
    [#strong[Heavy Paper Towels & Clean Cloths]], [High-absorption pure cellulose], [#strong[The absolute golden rule of surface drying:] drying steaks before pan searing.], [Never attempt to sear damp meat: surface moisture wastes $2,260 upright(" J/g")$ in steam, halting Maillard reaction.]
  )],
  caption: [Household technical consumables, thermodynamic contact rules, and safety boundaries.],
  kind: table
)

#point_attention[
#strong[The Golden Physical Rule of Surface Drying:]
A single droplet of water on the surface of raw meat absorbs $2,260 upright(" J/g")$ of heat through latent heat of vaporization. As long as liquid moisture is present, the surface remains trapped at the 100°C (212°F) boiling plateau. The Maillard reaction ($140^compose upright(" to ") 165^compose upright("C")$) can never ignite: the meat boils in its own sweat instead of crisping. A clean paper towel is the physical guarantee of golden crust.
]

#divider()

== 3. THE MATRIX DRY PANTRY: HEALTHY SHELF-STABLE STAPLES
<le-fond-de-placard-matriciel-lépicerie-de-survie-saine-hors-frigo>

=== A. Stable Cooking Fats & Culinary Acids
- #strong[Extra-virgin olive oil:] first cold pressed, high polyphenol count for salads and gentle cooking.
- #strong[Neutral high-heat oil:] refined peanut oil or high-oleic sunflower oil for high-heat searing.
- #strong[Rendered animal fat:] pure duck or goose fat preserved in glass jars for roasting potatoes.
- #strong[Traditional wine vinegar:] aged red or white wine vinegar for deglazing pan sauces.
- #strong[Raw apple cider vinegar:] unfiltered with active bacterial mother for vinaigrettes and pickles.

=== B. Essential Minerals & Whole Spices
- #strong[Coarse gray sea salt:] unrefined Atlantic sea salt for salting pasta and blanching water.
- #strong[Fleur de sel:] delicate finishing sea salt crystals for seasoned meats and salads.
- #strong[Black peppercorns in mill:] whole tellicherry black peppercorns ground fresh at service.
- #strong[Whole spices:] cumin seeds, coriander seeds, cardamom pods, cinnamon sticks, whole cloves.

=== C. Grains, Flours & Protein Legumes
- #strong[Organic wheat flour (T65 / Bread Flour):] unbleached stone-ground flour for bread and doughs.
- #strong[Bronze-die dry pasta:] durum wheat semolina with rough matte surface for sauce mantecatura.
- #strong[Long-grain rice (Basmati / Jasmine):] fragrant dry grains for steaming and pilafs.
- #strong[Round risotto rice (Carnaroli / Arborio):] rich in surface amylopectin for creamy binding.
- #strong[Red coral lentils:] cook tender in 12 minutes without advance soaking for instant dahl.
- #strong[Green or brown lentils:] French Puy lentils holding firm shape for salads and stews.
- #strong[Dried chickpeas & white beans:] dense source of complex starches and plant proteins.
- #strong[Rolled whole oats:] rich in soluble beta-glucan fibers for breakfasts and crumbs.

=== D. High-Value Canned Goods & Raw Nuts
- #strong[Whole canned San Marzano tomatoes:] picked ripe in juice, far superior to pale winter hothouse tomatoes.
- #strong[Double-concentrated tomato paste in tube:] deep umami base for braises and pan sauces.
- #strong[Canned chickpeas & white beans:] quick cooked legumes; chickpea liquid provides aquafaba.
- #strong[Solid canned tuna / sardines:] preserved in pure extra-virgin olive oil for emergency protein.
- #strong[Raw nuts & seeds:] whole walnuts, raw almonds, pumpkin seeds, golden flaxseeds, sesame seeds.

=== E. Cellar Alliums & Storage Roots (Cool, Dark Storage)
- #strong[Yellow storage onions:] foundational aromatic base for mirepoix, stocks, and sauces.
- #strong[Dry garlic bulbs:] firm purple or white garlic stored in breathable basket.
- #strong[Traditional shallots:] refined sulfurous aromatic nuances for pan sauces and dressings.
- #strong[Storage potatoes:] firm waxy tubers (Charlotte) and starchy baking tubers (Bintje/Russet).

#divider()

== 4. PERMANENT REFRIGERATOR FRESH ESSENTIALS (THE NINE COLD SENTINELS)
<le-frais-permanent-du-réfrigérateur-le-fond-de-frigo-toujours-disponible>

#figure(
  align(center)[#table(
    stroke: 0.5pt + rgb("#dcd6ca"),
    fill: (x, y) => if y == 0 { rgb("#f2ece1") } else if calc.odd(y) { rgb("#faf7f2") } else { none },
    inset: 7pt,
    columns: (22%, 22%, 28%, 28%),
    align: (left, left, left, left),
    table.header([Cold Sentinel], [Recommended Type], [Preservation Life], [Culinary Transformation Role]),
    table.hline(),
    [#strong[1. Fresh Organic Eggs]], [Free-range (Grade A)], [28 to 30 days], [Emulsions (mayo), structure (cakes), standalone poached/soft-boiled proteins.],
    [#strong[2. European Butter]], [Unsalted (82% fat minimum)], [30 to 45 days], [Mounting sauces, pastry laminations, pan fond basting.],
    [#strong[3. Parmigiano Reggiano]], [AOP aged 24 to 30 months], [2 to 3 months (in wax paper)], [Concentrated glutamate umami, sauce binding, finishing salads.],
    [#strong[4. Plain Whole Yogurt]], [Greek whole milk with live cultures], [15 to 20 days], [Acid marinades (tenderizes chicken), sauces, dressings, digestive health.],
    [#strong[5. Whole Heavy Cream]], [Pasteurized liquid (30 - 35% fat)], [7 to 10 days], [Sauce velvet coats, whipped foams, pastry ganache.],
    [#strong[6. Fresh Lemons]], [Organic untreated lemons], [15 to 21 days], [Culinary acid balance: drops cut fat and brighten meat jus instantaneously.],
    [#strong[7. Dijon Mustard]], [Traditional sharp seed mustard], [6 months (refrigerated)], [Emulsifying agent for vinaigrettes, crust seasoning for roasted poultry.],
    [#strong[8. Celery & Carrots]], [Unwashed fresh bunches], [14 to 21 days (crisper)], [Mirepoix aromatic trio (onion-carrot-celery), broths, crisp crudités.],
    [#strong[9. Fresh Flat-Leaf Parsley]], [Fresh bunches in water glass], [7 to 10 days], [Fresh finishing chlorophyll, herb stems for bouquet garni.]
  )],
  caption: [The Nine Permanent Refrigerator Sentinels for instant culinary autonomy.],
  kind: table
)

#divider()

== 5. THE RATIONAL CLEAN GROCERY TEMPLATE (THREE STANDALONE FULL PAGES)
<le-gabarit-matriciel-de-courses-saines-avec-cases-à-cocher>

Shopping with enlightenment is not about roaming aisles reacting to industrial packaging. This protocol implements the #strong[four cardinal rules of sovereign food provisioning]:

1. #strong[The Full-Stomach Rule:] Never enter a market or grocery store hungry. Dropping leptin and surging ghrelin trigger primitive impulses to seek refined fast sugars and saturated industrial fats.
2. #strong[The 80/20 Perimeter Rule:] In any supermarket, allocate 80% of your budget and cart to the outer perimeter (fresh produce, butchers, fishmongers, raw dairy, bulk whole grains). Avoid the center aisles packed with ultra-processed foods.
3. #strong[The Five-Ingredient Rule:] If a packaged item lists more than five components or includes additives not found in a domestic kitchen (modified starches, hydrogenated fats, synthetic flavor enhancers), it has no place in your body.
4. #strong[The Weekly 30-Plant Rule:] Protect gut microbiome biodiversity by checking off a wide variety of root vegetables, leafy greens, bulk seeds, fresh herbs, and protein legumes every week.

The following template has been engineered to occupy #strong[three complete standalone pages], designed to be detached, photocopied, or photographed on a smartphone without text breaks across page boundaries:

#pagebreak()

// =========================================================================
// GROCERY TEMPLATE — STANDALONE FULL PAGE 1 / 3: THE PLANT KINGDOM
// =========================================================================

#align(center)[
  #text(size: 13pt, weight: "bold", fill: c-bordeaux)[RATIONAL CLEAN GROCERY TEMPLATE — SHEET 1 / 3] \
  #v(1pt)
  #text(size: 8.8pt, style: "italic", fill: c-slate)[The Plant Kingdom: Fresh Greens, Roots, Cereals & Bulk Whole Grains — Standalone Page to Detach]
]

#v(0.2cm)

#grid(
  columns: (1fr, 1fr),
  gutter: 12pt,
  [
    #block(
      fill: rgb("#faf7f0"),
      stroke: 0.5pt + rgb("#dfdacf"),
      inset: 8pt,
      radius: 4pt,
      width: 100%,
      spacing: 0.65em
    )[
      #text(weight: "bold", size: 9.8pt, fill: c-bordeaux)[1. FRESH GREENS, ROOTS & HERBAL PANTRY]
      #v(1pt)
      #line(length: 100%, stroke: 0.5pt + c-bronze)
      #v(3pt)
      #set text(size: 8.8pt)
      #set par(leading: 0.65em)
      #case_cocher Storage Carrots (unwashed soil) \
      #case_cocher Celery stalk or celeriac root \
      #case_cocher Yellow storage onions & red onions \
      #case_cocher Dry garlic bulbs & gray shallots \
      #case_cocher Leeks or head cabbage (green / red) \
      #case_cocher Crisp market salad greens / baby shoots \
      #case_cocher Organic unwaxed lemons \
      #case_cocher Waxy firm potatoes (Charlotte / Yukon Gold) \
      #case_cocher Starchy baking potatoes (Bintje / Russet) \
      #case_cocher Fresh flat-leaf parsley or fresh cilantro \
      #case_cocher Seasonal leafy greens (spinach, chard) \
      #case_cocher Seasonal fruit-vegetables (zucchini, tomatoes) \
      #case_cocher Raw seasonal fruits (apples, pears) \
      #case_cocher Fresh button or wild mushrooms \
      #case_cocher Fresh ginger root \
      #case_cocher #line(length: 82%, stroke: 0.4pt + rgb("#a8a29e")) \
      #case_cocher #line(length: 82%, stroke: 0.4pt + rgb("#a8a29e")) \
      #case_cocher #line(length: 82%, stroke: 0.4pt + rgb("#a8a29e")) \
      #case_cocher #line(length: 82%, stroke: 0.4pt + rgb("#a8a29e")) \
    ]
  ],
  [
    #block(
      fill: rgb("#faf7f0"),
      stroke: 0.5pt + rgb("#dfdacf"),
      inset: 8pt,
      radius: 4pt,
      width: 100%,
      spacing: 0.65em
    )[
      #text(weight: "bold", size: 9.8pt, fill: c-bordeaux)[2. DRY PANTRY & BULK WHOLE GRAINS]
      #v(1pt)
      #line(length: 100%, stroke: 0.5pt + c-bronze)
      #v(3pt)
      #set text(size: 8.8pt)
      #set par(leading: 0.65em)
      #case_cocher Organic stone-ground wheat flour (T65 / Bread) \
      #case_cocher Bronze-cut durum wheat pasta \
      #case_cocher Long-grain Basmati or Jasmine rice \
      #case_cocher Risotto rice (Carnaroli / Arborio) \
      #case_cocher Red coral lentils (12-min quick cook) \
      #case_cocher French green Puy lentils or brown lentils \
      #case_cocher Dried farm chickpeas \
      #case_cocher Dried white beans (cannellini / navy) \
      #case_cocher Rolled whole oats (beta-glucans) \
      #case_cocher Cornstarch (Maizena) or potato starch \
      #case_cocher Brown flaxseeds & raw pumpkin seeds \
      #case_cocher Whole golden sesame seeds \
      #case_cocher Raw walnut halves & raw unroasted almonds \
      #case_cocher Whole unrefined cane sugar (Muscovado) \
      #case_cocher Raw artisanal beekeeper honey \
      #case_cocher #line(length: 82%, stroke: 0.4pt + rgb("#a8a29e")) \
      #case_cocher #line(length: 82%, stroke: 0.4pt + rgb("#a8a29e")) \
      #case_cocher #line(length: 82%, stroke: 0.4pt + rgb("#a8a29e")) \
      #case_cocher #line(length: 82%, stroke: 0.4pt + rgb("#a8a29e")) \
    ]
  ]
)

#v(0.2cm)

#point_attention[
#strong[Microbiome Target: The 30 Weekly Plants:] To feed the diverse bacterial phyla of your colon, vary botanical families and colors. Every box checked across the two columns above (alliums, brassicas, apiaceous roots, legumes, grasses, seeds, and nuts) delivers a unique profile of prebiotic fibers and protective polyphenols.
]

#pagebreak()

// =========================================================================
// GROCERY TEMPLATE — STANDALONE FULL PAGE 2 / 3: FRESH COLD & PROTEINS
// =========================================================================

#align(center)[
  #text(size: 13pt, weight: "bold", fill: c-bordeaux)[RATIONAL CLEAN GROCERY TEMPLATE — SHEET 2 / 3] \
  #v(1pt)
  #text(size: 8.8pt, style: "italic", fill: c-slate)[Living Cold, Butcher, Seafood & Noble Preserves — Standalone Page to Detach]
]

#v(0.2cm)

#grid(
  columns: (1fr, 1fr),
  gutter: 12pt,
  [
    #block(
      fill: rgb("#faf7f0"),
      stroke: 0.5pt + rgb("#dfdacf"),
      inset: 8pt,
      radius: 4pt,
      width: 100%,
      spacing: 0.65em
    )[
      #text(weight: "bold", size: 9.8pt, fill: c-bordeaux)[3. DAIRY, EGGS & LIVING COLD]
      #v(1pt)
      #line(length: 100%, stroke: 0.5pt + c-bronze)
      #v(3pt)
      #set text(size: 8.8pt)
      #set par(leading: 0.65em)
      #case_cocher Organic free-range fresh eggs (Grade A) \
      #case_cocher Unsalted churned butter (82% fat) \
      #case_cocher Parmigiano Reggiano PDO wedge (24-30 mo) \
      #case_cocher Plain whole Greek yogurt (sheep/cow milk) \
      #case_cocher Fresh farm cottage cheese (fromage blanc) \
      #case_cocher Heavy liquid cream (35% fat) \
      #case_cocher Pasteurized whole fresh milk \
      #case_cocher Firm plain organic soy tofu \
      #case_cocher Aged brown or white miso paste \
      #case_cocher Aged raw milk cheese (Comté / Gruyère) \
      #case_cocher #line(length: 82%, stroke: 0.4pt + rgb("#a8a29e")) \
      #case_cocher #line(length: 82%, stroke: 0.4pt + rgb("#a8a29e")) \
    ]

    #v(0.2cm)

    #block(
      fill: rgb("#faf7f0"),
      stroke: 0.5pt + rgb("#dfdacf"),
      inset: 8pt,
      radius: 4pt,
      width: 100%,
      spacing: 0.65em
    )[
      #text(weight: "bold", size: 9.8pt, fill: c-bordeaux)[4. BUTCHER, POULTRY & SEAFOOD]
      #v(1pt)
      #line(length: 100%, stroke: 0.5pt + c-bronze)
      #v(3pt)
      #set text(size: 8.8pt)
      #set par(leading: 0.65em)
      #case_cocher Whole free-range chicken ready to truss \
      #case_cocher Thick beef steak for searing (ribeye, sirloin) \
      #case_cocher Collagen braising cut (chuck, beef cheek) \
      #case_cocher Line-caught fresh white fish (cod, haddock) \
      #case_cocher Fresh oily small fish (sardines, mackerel) \
      #case_cocher Raw shell-on shrimp (shells for broth) \
      #case_cocher #line(length: 82%, stroke: 0.4pt + rgb("#a8a29e")) \
    ]
  ],
  [
    #block(
      fill: rgb("#faf7f0"),
      stroke: 0.5pt + rgb("#dfdacf"),
      inset: 8pt,
      radius: 4pt,
      width: 100%,
      spacing: 0.65em
    )[
      #text(weight: "bold", size: 9.8pt, fill: c-bordeaux)[5. NOBLE PRESERVES & CELLAR STAPLES]
      #v(1pt)
      #line(length: 100%, stroke: 0.5pt + c-bronze)
      #v(3pt)
      #set text(size: 8.8pt)
      #set par(leading: 0.65em)
      #case_cocher Whole canned peeled San Marzano tomatoes \
      #case_cocher Double-concentrated tomato paste in tube \
      #case_cocher Canned chickpeas (water for aquafaba) \
      #case_cocher Canned white beans in water \
      #case_cocher Solid white tuna in extra-virgin olive oil \
      #case_cocher Sardines in extra-virgin olive oil \
      #case_cocher Salted anchovies in olive oil \
      #case_cocher Canned unsweetened pure coconut milk \
      #case_cocher Dark baking chocolate ($> 70 %$ cocoa) \
      #case_cocher Pure cocoa powder (unsweetened) \
      #case_cocher Traditional active dry baker's yeast \
      #case_cocher Glass jars of cooked chestnuts \
      #case_cocher Pure roasted nut paste (tahini, peanut) \
      #case_cocher #line(length: 82%, stroke: 0.4pt + rgb("#a8a29e")) \
      #case_cocher #line(length: 82%, stroke: 0.4pt + rgb("#a8a29e")) \
      #case_cocher #line(length: 82%, stroke: 0.4pt + rgb("#a8a29e")) \
      #case_cocher #line(length: 82%, stroke: 0.4pt + rgb("#a8a29e")) \
      #case_cocher #line(length: 82%, stroke: 0.4pt + rgb("#a8a29e")) \
    ]
  ]
)

#v(0.2cm)

#danger[
#strong[Cold Chain & Food Safety Reflex:] Always purchase categories 3 and 4 (dairy, poultry, meat, fish) at the very end of your shopping trip. Place them immediately inside an insulated cooler bag. Once home, unpack straight into calibrated refrigerator bio-zones (0°C to 2°C / 32°F to 36°F).
]

#pagebreak()

// =========================================================================
// GROCERY TEMPLATE — STANDALONE FULL PAGE 3 / 3: CONDIMENTS & CUTLERY
// =========================================================================

#align(center)[
  #text(size: 13pt, weight: "bold", fill: c-bordeaux)[RATIONAL CLEAN GROCERY TEMPLATE — SHEET 3 / 3] \
  #v(1pt)
  #text(size: 8.8pt, style: "italic", fill: c-slate)[Seasoning Pillars, Household Consumables & Cutlery — Standalone Page to Detach]
]

#v(0.2cm)

#grid(
  columns: (1fr, 1fr),
  gutter: 12pt,
  [
    #block(
      fill: rgb("#faf7f0"),
      stroke: 0.5pt + rgb("#dfdacf"),
      inset: 8pt,
      radius: 4pt,
      width: 100%,
      spacing: 0.65em
    )[
      #text(weight: "bold", size: 9.8pt, fill: c-bordeaux)[6. NOBLE FATS, ACIDS & CONDIMENTS]
      #v(1pt)
      #line(length: 100%, stroke: 0.5pt + c-bronze)
      #v(3pt)
      #set text(size: 8.8pt)
      #set par(leading: 0.65em)
      #case_cocher Extra-virgin cold-pressed olive oil \
      #case_cocher Refined peanut or high-oleic sunflower oil \
      #case_cocher Toasted virgin sesame oil \
      #case_cocher Pure rendered duck or goose fat in jar \
      #case_cocher Traditional red wine vinegar \
      #case_cocher Raw unfiltered apple cider vinegar \
      #case_cocher Traditional sharp Dijon mustard \
      #case_cocher Shoyu or Tamari soy sauce \
      #case_cocher Coarse unrefined gray sea salt \
      #case_cocher Fine finishing sea salt (fleur de sel) \
      #case_cocher Whole black Tellicherry peppercorns \
      #case_cocher Whole spices (cumin, coriander, cardamom) \
      #case_cocher Smoked sweet paprika (pimentón) \
      #case_cocher Dried bay leaves & dried wild thyme \
      #case_cocher Unbleached baking parchment paper roll \
      #case_cocher Heavy aluminum foil (for resting meats) \
      #case_cocher Pure unbleached cotton kitchen twine \
      #case_cocher Heavy-duty absorbent paper towels \
      #case_cocher #line(length: 82%, stroke: 0.4pt + rgb("#a8a29e")) \
      #case_cocher #line(length: 82%, stroke: 0.4pt + rgb("#a8a29e")) \
    ]
  ],
  [
    #block(
      fill: rgb("#faf7f0"),
      stroke: 0.5pt + rgb("#dfdacf"),
      inset: 8pt,
      radius: 4pt,
      width: 100%,
      spacing: 0.65em
    )[
      #text(weight: "bold", size: 9.8pt, fill: c-bordeaux)[7. PREP CUTLERY & KITCHEN UTENSILS]
      #v(1pt)
      #line(length: 100%, stroke: 0.5pt + c-bronze)
      #v(3pt)
      #set text(size: 8.8pt)
      #set par(leading: 0.65em)
      #case_cocher Short paring knife (8 to 10 cm / 3-4 in) \
      #case_cocher Swiveling Y-peeler with carbon steel blade \
      #case_cocher Stiff serrated bread knife (22 cm / 9 in) \
      #case_cocher Solid 18/10 stainless spoon for basting \
      #case_cocher Solid beechwood spatula spoon \
      #case_cocher Beveled offset metal spatula (deglazing) \
      #case_cocher High-heat silicone spatula Maryse (250°C) \
      #case_cocher Precision chef's tongs (30 cm / 12 in) \
      #case_cocher Forged two-prong meat carving fork \
      #case_cocher Crossed-wire stainless spider skimmer \
      #case_cocher Seamless one-piece soup ladle \
      #case_cocher 12-wire spring balloon whisk \
      #case_cocher Fine microplane grater (zests & Parmesan) \
      #case_cocher Heavy take-apart bone kitchen shears \
      #case_cocher #line(length: 82%, stroke: 0.4pt + rgb("#a8a29e")) \
    ]
  ]
)

#v(0.2cm)

#truc_de_chef[
#strong[30-Minute Weekly Grocery Protocol:]
1. #strong[Pantry Audit (Day -1):] Open dry cupboard and crisper; check off on this template only the missing items in categories 1 through 6.
2. #strong[Linear Market Circuit:] Follow strict numerical order (1 Produce $arrow.r$ 2 Bulk Grains $arrow.r$ 3 Dairy $arrow.r$ 4 Butcher/Fish). Cold, fragile proteins enter the insulated cooler bag last.
3. #strong[Direct-Integration (FIFO):] Upon returning, immediately store fresh foods according to the thermal map of Appendix E: raw meats and fish in the coldest zone (0°C to 2°C / 32°F to 36°F), dairy in the middle (4°C / 39°F), vegetables in the crisper (6°C to 8°C / 43°F to 46°F).
]

#divider()

// =========================================================================
// APPENDIX G: ICONOGRAPHIC DIRECTORY & IMAGE SOURCES
// =========================================================================

= APPENDIX G --- Comprehensive Iconographic Directory & Image Sources
<annexe-g-répertoire-des-crédits-iconographiques-et-sources-des-illustrations>
This directory compiles all sources, attributions, historical dates, and open licenses (#emph[Creative Commons] or #emph[Public Domain]) for all artworks, engravings, food photography plates, and vector diagrams in this work.

#divider()

== 1. Major Book Opening Portals (Full-Page Verso Openings)
<grandes-ouvertures-de-livres-pleines-pages-verso>
#figure(
  align(center)[#table(
  stroke: 0.5pt + rgb("#dcd6ca"),
  fill: (x, y) => if y == 0 { rgb("#f2ece1") } else if calc.odd(y) { rgb("#faf7f2") } else { none },
  inset: 8pt,

    columns: (20%, 20%, 20%, 20%, 20%),
    align: (left,left,left,left,left,),
    table.header([Placement], [Subject & Artwork], [Artist / Institution], [Dating], [License & Source],),
    table.hline(),
    [#strong[Book I]], [#emph[Paleolithic Fire Conquest & Externalized Digestion]], [Archaeological Collections], [Paleolithic], [CC BY-SA 4.0 / Wikimedia],
    [#strong[Book II]], [#emph[The Ordered Domestic Hearth: La Pourvoyeuse / L'Écureuse]], [Jean Siméon Chardin / Louvre], [1738], [Public Domain / Wikimedia],
    [#strong[Book III]], [#emph[Market Abundance of Raw Produce Before Cooking]], [Joachim Beuckelaer / Kunsthistorisches Museum], [16th c.], [Public Domain / Wikimedia],
    [#strong[Book IV]], [#emph[Golden Artisan Sourdough Loaves in Hearth Oven]], [Artisanal Bakery Photography], [2024], [CC BY-SA 4.0 / Wikimedia],
    [#strong[Book V]], [#emph[Gala Banquet Table, Silver Flatware & Shared Service]], [Gala Table Service Photography], [Contemporary], [CC BY-SA 3.0 / Wikimedia],
    [#strong[Book VI]], [#emph[The Living Biodiverse Kitchen Garden Across Seasons]], [Agronomic & Horticultural Photography], [Contemporary], [Public Domain / Wikimedia],
    [#strong[Appendices]], [#emph[Confectioner, Proofing Chamber & Oven (Encyclopédie Pl. II)]], [Diderot, d'Alembert, Goussier & Bénard], [1762], [Public Domain / Wikimedia],
  )],
  caption: [Full-page verso opening artworks and historical plates for all major books.],
  kind: table
)

#divider()

== 2. Historical Portraits, Scientific Engravings & Documentary Photographs
<portraits-historiques-gravures-et-photographies-scientifiques>
#figure(
  align(center)[#table(
  stroke: 0.5pt + rgb("#dcd6ca"),
  fill: (x, y) => if y == 0 { rgb("#f2ece1") } else if calc.odd(y) { rgb("#faf7f2") } else { none },
  inset: 8pt,

    columns: (25%, 25%, 25%, 25%),
    align: (left,left,left,left,),
    table.header([Placement], [Subject & Artist], [Institution & Date], [Open License & Source],),
    table.hline(),
    [#strong[Chapter 02]], [#emph[Bread Stall in a Pompeii Bakery] (Roman wall fresco)], [National Archaeological Museum of Naples (1st c. AD)], [Public Domain / Wikimedia],
    [#strong[Chapter 02]], [#emph[Master Renaissance Kitchen Cutlery & Vessels] (Bartolomeo Scappi)], [#emph[Opera dell'arte del cucinare] (1570)], [Public Domain / Wikimedia],
    [#strong[Chapter 02]], [#emph[Portrait of Jean Anthelme Brillat-Savarin]], [Steel engraving (19th Century)], [Public Domain / Wikimedia],
    [#strong[Chapter 02]], [#emph[Portrait of Nicolas Appert] (Inventor of Appertization)], [Official historical portrait (1810)], [Public Domain / Wikimedia],
    [#strong[Chapter 02]], [#emph[Portrait of Auguste Escoffier] (Le Guide Culinaire)], [Historical archival photograph (1903)], [Public Domain / Wikimedia],
    [#strong[Chapter 18]], [#emph[Colloidal Curd and Whey Separation in Cheese Vat]], [Documentary dairy photography], [CC BY-SA 2.0 / Wikimedia],
    [#strong[Chapter 22]], [#emph[Table Arts: Harmonious Flatware Placement]], [Documentary service photography], [CC BY-SA 4.0 / Wikimedia],
    [#strong[Chapter 26]], [#emph[Biodiversity of Dry Legumes & Resistant Starch]], [Agronomic documentary photograph], [Public Domain / Wikimedia],
  )],
  caption: [Historical artworks, engravings, and documentary photography credits.],
  kind: table
)

#divider()

== 3. Culinary Photography of the 26 Foundational Master Recipes
<photographies-culinaires-des-26-recettes-fondatrices>
All photographs illustrating the 26 foundational recipes of this work were sourced from the global open-access repository #strong[Wikimedia Commons] and are distributed under #strong[Creative Commons (CC BY-SA 3.0 / 4.0)] or #strong[Public Domain (CC0)] licenses:

#figure(
  align(center)[#table(
  stroke: 0.5pt + rgb("#dcd6ca"),
  fill: (x, y) => if y == 0 { rgb("#f2ece1") } else if calc.odd(y) { rgb("#faf7f2") } else { none },
  inset: 8pt,

    columns: (50%, 50%),
    align: (left,left,),
    table.header([Recipes 01 to 13 (Book III)], [Recipes 14 to 26 (Books III & IV)],),
    table.hline(),
    [#strong[01.] Traditional Roman Spaghetti alla Carbonara], [#strong[14.] Perfect Soft-Boiled Egg (*Mollet*) with Flowing Yolk],
    [#strong[02.] Comforting Red Lentil Dahl with Coconut Milk], [#strong[15.] Tear-Drop Poached Egg on Golden Toast],
    [#strong[03.] Crispy Pan-Seared Tofu Glazed with Tamari & Sesame], [#strong[16.] Firm Hand-Whisked Cold Mayonnaise Emulsion],
    [#strong[04.] Golden Sarladaise Potatoes Crisped in Duck Fat], [#strong[17.] Velvety Hollandaise Emulsion Mounted Warm],
    [#strong[05.] Grand Provençal Mortar-Crushed Aïoli with Cod], [#strong[18.] Silky Classical Béchamel White Sauce],
    [#strong[06.] Cloud-like Potato Purée Infused with Peel Milk], [#strong[19.] Crackling Dutch-Oven Wild Sourdough Loaf],
    [#strong[07.] Butter-Glazed Carrots Reduced Under Cartouche], [#strong[20.] Crisp Lacto-Fermented Pickled Vegetables in Brine],
    [#strong[08.] Crisp Garden Salad Greens & Dijon Vinaigrette], [#strong[21.] Fresh Farm Cottage Cheese Drained in 15 Minutes],
    [#strong[09.] Simmering Golden Bone Broth Reduced to Glaze], [#strong[22.] Molten Dark Chocolate Lava Cake with Liquid Core],
    [#strong[10.] Mirror-Clear Beef Consommé Clarified with Raft], [#strong[23.] Melt-in-the-Mouth Pure Butter Flaky Shortcrust],
    [#strong[11.] Thick Cast-Iron Seared Beef Ribeye in Butter], [#strong[24.] Airy Dark Chocolate Mousse Leavened with Aquafaba],
    [#strong[12.] Pan Sauce Deglazed with Wine & Mounted with Butter], [#strong[25.] Baked Alaska: Scorched Meringue Shield with Frozen Core],
    [#strong[13.] Vibrant Lime-Cured Cod Ceviche with Red Onion], [#strong[26.] Silky Churnless Vanilla Ice Cream Frozen on Salt-Ice],
  )],
  caption: [Complete photographic index of the 26 foundational master recipes.],
  kind: table
)

#divider()

== 4. Vector SVG Schematics and Technical Figures
<schémas-vectoriels-svg-et-figures-didactiques>
All technical diagrams, thermodynamic timelines, transformation matrices, and anatomical cross-sections (Vector SVG figures) were engineered and authored specifically for this treatise in strict compliance with W3C standards under the #strong[Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)] license:

- #strong[Vector Graphic Authoring:] Editorial & Technical Team of #emph[Cooking Decoded / La Cuisine Expliquée].
- #strong[Embedded Open-Source Typography:] Clean system fonts #emph[Liberation Sans] and #emph[Liberation Serif].
- #strong[Official Semantic Color Palette:]
  - Thermal Energy / Heat: `#dc2626` (Red) / Background `#fef2f2`
  - Water / Hydration / Steam: `#2563eb` (Royal Blue) / Background `#eff6ff`
  - Cold / Sub-Zero / Cryoscopy: `#0284c7` (Cyan Blue) / Background `#f0f9ff`
  - Lipids / Caramelization / Oil: `#d97706` (Amber Gold) / Background `#fffbeb`
  - Acidity / Balance / Success: `#16a34a` (Emerald Green) / Background `#f0fdf4`
  - Metals / Vessels / Coordinate Axes: `#0f172a` (Deep Slate) / Background `#f8fafc`
  - Reference Grids / Baseline Borders: `#94a3b8` (Muted Grey) / Background `#f1f5f9`
