import os
import xml.etree.ElementTree as ET

# Palette chaude officielle (AGENTS.md)
# Fond principal : #FCFBF7 | Bordure cadre : #DFDACF
# Bordeaux : #701C1A | Terracotta : #A3432B | Ambre : #B45309 | Bistre : #6B4423 | Sauge sourde : #5A6E54
# Encre : #242124 | Gris chaud : #5C5549 | Crème carte : #FAF7F2

SVGS = {}

# ==============================================================================
# FIG 10 : figures/livre_1/fig_securite_accidents_frigo_feu.svg
# ==============================================================================
SVGS["figures/livre_1/fig_securite_accidents_frigo_feu.svg"] = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 540" width="100%" height="100%">
  <rect width="880" height="540" rx="14" fill="#FCFBF7" stroke="#DFDACF" stroke-width="2"/>
  <text x="440" y="34" font-family="Liberation Serif, Georgia, serif" font-size="20" font-weight="bold" fill="#701C1A" text-anchor="middle">SÉCURITÉ EN CUISINE : LES 4 ACCIDENTS MAJEURS ET LEURS PARADES</text>
  <text x="440" y="55" font-family="Liberation Sans, Arial, sans-serif" font-size="13.5" fill="#5C5549" text-anchor="middle">Les réflexes immédiats de survie et les gestes dangereux à proscrire absolument.</text>

  <!-- Bloc 1 : Panne de Frigo -->
  <g transform="translate(30, 72)">
    <rect width="395" height="210" rx="8" fill="#FAF7F2" stroke="#966C3B" stroke-width="1.5"/>
    <rect width="395" height="30" rx="8" fill="#6B4423"/>
    <text x="197" y="20" font-family="Liberation Serif, Georgia, serif" font-size="13.5" font-weight="bold" fill="#FCFBF7" text-anchor="middle">1. PANNE DE RÉFRIGÉRATEUR OU CONGÉLATEUR</text>

    <text x="14" y="48" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" font-weight="bold" fill="#5A6E54">✓ CE QU'IL FAUT FAIRE :</text>
    <text x="14" y="66" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">• Garder les portes strictement fermées (4 à 6h d'autonomie).</text>
    <text x="14" y="83" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">• Si T° &gt; 4°C depuis plus de 2h : cuire immédiatement</text>
    <text x="24" y="98" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">à cœur (100°C) les viandes, volailles et poissons.</text>
    <text x="14" y="115" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">• Un aliment cuit à cœur peut ensuite être recongelé.</text>

    <text x="14" y="140" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" font-weight="bold" fill="#701C1A">✗ INTERDICTION ABSOLUE :</text>
    <text x="14" y="158" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" font-weight="bold" fill="#A3432B">• Ne jamais recongeler un aliment décongelé cru !</text>
    <text x="14" y="175" font-family="Liberation Sans, Arial, sans-serif" font-size="11.8" fill="#5C5549">L'exsudat cellulaire libéré multiplie par 100 la croissance</text>
    <text x="14" y="190" font-family="Liberation Sans, Arial, sans-serif" font-size="11.8" fill="#5C5549">bactérienne et la synthèse de toxines thermostables.</text>
  </g>

  <!-- Bloc 2 : Poêle en Feu -->
  <g transform="translate(455, 72)">
    <rect width="395" height="210" rx="8" fill="#FAF7F2" stroke="#A3432B" stroke-width="1.5"/>
    <rect width="395" height="30" rx="8" fill="#701C1A"/>
    <text x="197" y="20" font-family="Liberation Serif, Georgia, serif" font-size="13.5" font-weight="bold" fill="#FCFBF7" text-anchor="middle">2. POÊLE EN FEU (INCENDIE D'HUILE)</text>

    <text x="14" y="48" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" font-weight="bold" fill="#5A6E54">✓ LE GESTE VITAL EN 3 SECONDES :</text>
    <text x="14" y="66" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">• Couper immédiatement la source d'énergie (gaz/plaque).</text>
    <text x="14" y="83" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">• Faire glisser un couvercle métallique ou un linge</text>
    <text x="24" y="98" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">humide essoré sur la poêle pour étouffer l'oxygène.</text>
    <text x="14" y="115" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">• Laisser refroidir 15 min sans soulever le couvercle.</text>

    <text x="14" y="140" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" font-weight="bold" fill="#701C1A">✗ ERREUR MORTELLE :</text>
    <text x="14" y="158" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" font-weight="bold" fill="#A3432B">• Ne jamais jeter d'eau sur de l'huile en flammes !</text>
    <text x="14" y="175" font-family="Liberation Sans, Arial, sans-serif" font-size="11.8" fill="#5C5549">Vaporisation instantanée (volume × 1700) pulvérisant</text>
    <text x="14" y="190" font-family="Liberation Sans, Arial, sans-serif" font-size="11.8" fill="#5C5549">l'huile brûlante en une boule de feu explosive (boilover).</text>
  </g>

  <!-- Bloc 3 : Brûlures Thermiques -->
  <g transform="translate(30, 300)">
    <rect width="395" height="215" rx="8" fill="#FAF7F2" stroke="#B45309" stroke-width="1.5"/>
    <rect width="395" height="30" rx="8" fill="#B45309"/>
    <text x="197" y="20" font-family="Liberation Serif, Georgia, serif" font-size="13.5" font-weight="bold" fill="#FCFBF7" text-anchor="middle">3. BRÛLURES PAR CONTACT OU CARAMEL</text>

    <text x="14" y="48" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" font-weight="bold" fill="#5A6E54">✓ LA RÈGLE MÉDICALE DES « TROIS 15 » :</text>
    <text x="14" y="66" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">• Eau tempérée à <tspan font-weight="bold">15°C</tspan> (jamais d'eau glacée ni glaçon).</text>
    <text x="14" y="83" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">• Pendant <tspan font-weight="bold">15 minutes</tspan> continues pour drainer les calories.</text>
    <text x="14" y="100" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">• À <tspan font-weight="bold">15 cm</tspan> du robinet en filet ruisselant sans pression.</text>

    <text x="14" y="130" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" font-weight="bold" fill="#701C1A">✗ MYTHE DANGEREUX À BANNIR :</text>
    <text x="14" y="148" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" font-weight="bold" fill="#A3432B">• Ne jamais étaler de beurre, d'huile ou de dentifrice !</text>
    <text x="14" y="165" font-family="Liberation Sans, Arial, sans-serif" font-size="11.8" fill="#5C5549">Le corps gras forme un manteau isolant qui emprisonne</text>
    <text x="14" y="180" font-family="Liberation Sans, Arial, sans-serif" font-size="11.8" fill="#5C5549">la chaleur dans le derme et aggrave la brûlure profonde.</text>
  </g>

  <!-- Bloc 4 : Coupures et Lame -->
  <g transform="translate(455, 300)">
    <rect width="395" height="215" rx="8" fill="#FAF7F2" stroke="#5A6E54" stroke-width="1.5"/>
    <rect width="395" height="30" rx="8" fill="#5A6E54"/>
    <text x="197" y="20" font-family="Liberation Serif, Georgia, serif" font-size="13.5" font-weight="bold" fill="#FCFBF7" text-anchor="middle">4. COUPURES FRANCHES ET TENUE DE LAME</text>

    <text x="14" y="48" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" font-weight="bold" fill="#5A6E54">✓ PRÉVENTION BIOMÉCANIQUE :</text>
    <text x="14" y="66" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">• Main guide : doigts repliés en <tspan font-weight="bold">« griffe de chat »</tspan>,</text>
    <text x="24" y="81" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">plat de lame en appui glissant contre la 2e phalange.</text>
    <text x="14" y="98" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">• Main active : pince pouce-index sur le talon d'acier.</text>

    <text x="14" y="130" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" font-weight="bold" fill="#701C1A">✗ EN CAS DE COUPURE SAIGNANTE :</text>
    <text x="14" y="148" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" font-weight="bold" fill="#A3432B">• Ne pas porter à la bouche ni soulever le linge toutes les 30 s.</text>
    <text x="14" y="165" font-family="Liberation Sans, Arial, sans-serif" font-size="11.8" fill="#5C5549">Rincer à l'eau claire et comprimer fermement pendant</text>
    <text x="14" y="180" font-family="Liberation Sans, Arial, sans-serif" font-size="11.8" fill="#5C5549">5 minutes continues pour consolider le caillot de fibrine.</text>
  </g>
</svg>"""

# ==============================================================================
# FIG 12 : figures/livre_1/fig_additifs_bliss_point_courses.svg
# ==============================================================================
SVGS["figures/livre_1/fig_additifs_bliss_point_courses.svg"] = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 510" width="100%" height="100%">
  <rect width="880" height="510" rx="14" fill="#FCFBF7" stroke="#DFDACF" stroke-width="2"/>
  <text x="440" y="34" font-family="Liberation Serif, Georgia, serif" font-size="20" font-weight="bold" fill="#701C1A" text-anchor="middle">L'INGÉNIERIE INDUSTRIELLE : LE BLISS POINT ET LES ADDITIFS E</text>
  <text x="440" y="55" font-family="Liberation Sans, Arial, sans-serif" font-size="13.5" fill="#5C5549" text-anchor="middle">Démystifier les listes d'ingrédients, repérer les vrais toxiques et déjouer le piège des courses.</text>

  <!-- Panneau Gauche : Le Triangle du Bliss Point -->
  <g transform="translate(30, 75)">
    <rect width="395" height="410" rx="10" fill="#FAF7F2" stroke="#A3432B" stroke-width="1.5"/>
    <rect width="395" height="32" rx="10" fill="#701C1A"/>
    <text x="197" y="21" font-family="Liberation Serif, Georgia, serif" font-size="13.5" font-weight="bold" fill="#FCFBF7" text-anchor="middle">1. LE BLISS POINT : COURT-CIRCUITER LA SATIÉTÉ</text>

    <!-- Triangle équilatéral -->
    <polygon points="197,65 85,205 310,205" fill="#F7EFEA" stroke="#A3432B" stroke-width="2"/>

    <circle cx="197" cy="65" r="22" fill="#701C1A"/>
    <text x="197" y="69" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" font-weight="bold" fill="#FCFBF7" text-anchor="middle">SUCRE</text>

    <circle cx="85" cy="205" r="22" fill="#B45309"/>
    <text x="85" y="209" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" font-weight="bold" fill="#FCFBF7" text-anchor="middle">GRAS</text>

    <circle cx="310" cy="205" r="22" fill="#6B4423"/>
    <text x="310" y="209" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" font-weight="bold" fill="#FCFBF7" text-anchor="middle">SEL</text>

    <text x="197" y="150" font-family="Liberation Serif, Georgia, serif" font-size="14" font-weight="bold" fill="#701C1A" text-anchor="middle">PIC DE DOPAMINE</text>
    <text x="197" y="168" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#5C5549" text-anchor="middle">(Inhibition du signal de leptine)</text>

    <text x="16" y="250" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" fill="#242124"><tspan font-weight="bold" fill="#701C1A">• Le ratio d'addiction :</tspan> L'industrie ajuste sel, sucre</text>
    <text x="26" y="268" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#5C5549">et lipides pour désactiver le signal naturel de satiété.</text>

    <text x="16" y="294" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" fill="#242124"><tspan font-weight="bold" fill="#701C1A">• L'illusion acoustique :</tspan> Le croustillant calibré</text>
    <text x="26" y="312" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#5C5549">trompe le cerveau en simulant la fraîcheur végétale.</text>

    <text x="16" y="338" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" fill="#242124"><tspan font-weight="bold" fill="#701C1A">• La rétention d'eau :</tspan> Les polyphosphates piègent</text>
    <text x="26" y="356" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#5C5549">jusqu'à 30 % d'eau vendue au prix de la viande.</text>

    <rect x="16" y="370" width="363" height="28" rx="5" fill="#F2ECE1"/>
    <text x="197" y="388" font-family="Liberation Serif, Georgia, serif" font-size="12.2" font-weight="bold" fill="#701C1A" text-anchor="middle">Bilan : Surconsommation calorique passive.</text>
  </g>

  <!-- Panneau Droit : Additifs E & Courses -->
  <g transform="translate(455, 75)">
    <rect width="395" height="410" rx="10" fill="#FAF7F2" stroke="#966C3B" stroke-width="1.5"/>
    <rect width="395" height="32" rx="10" fill="#6B4423"/>
    <text x="197" y="21" font-family="Liberation Serif, Georgia, serif" font-size="13.5" font-weight="bold" fill="#FCFBF7" text-anchor="middle">2. LE TRI RATIONNEL ET LA RÈGLE DU CADDIE</text>

    <!-- Inoffensifs -->
    <rect x="16" y="46" width="363" height="96" rx="6" fill="#F4F6F4" stroke="#5A6E54" stroke-width="1.2"/>
    <text x="26" y="66" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" font-weight="bold" fill="#5A6E54">✓ MOLÉCULES NATURELLES INOFFENSIVES :</text>
    <text x="26" y="85" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">• <tspan font-weight="bold">E300</tspan> : Acide ascorbique (vitamine C antioxydante).</text>
    <text x="26" y="103" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">• <tspan font-weight="bold">E330</tspan> : Acide citrique naturel du jus de citron.</text>
    <text x="26" y="121" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">• <tspan font-weight="bold">E322</tspan> : Lécithine (œuf/soja) | <tspan font-weight="bold">E440</tspan> : Pectine de fruit.</text>

    <!-- À bannir -->
    <rect x="16" y="154" width="363" height="122" rx="6" fill="#FBF6F5" stroke="#A3432B" stroke-width="1.2"/>
    <text x="26" y="174" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" font-weight="bold" fill="#701C1A">✗ ADDITIFS CRITIQUES À ÉCARTER :</text>
    <text x="26" y="193" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">• <tspan font-weight="bold" fill="#701C1A">E250 (Nitrite de sodium) :</tspan> Forme des nitrosamines</text>
    <text x="36" y="209" font-family="Liberation Sans, Arial, sans-serif" font-size="11.8" fill="#5C5549">cancérogènes dans l'estomac (charcuteries roses).</text>
    <text x="26" y="227" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">• <tspan font-weight="bold" fill="#701C1A">E150d :</tspan> Caramel au sulfite d'ammonium (sodas).</text>
    <text x="26" y="245" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">• <tspan font-weight="bold" fill="#701C1A">E466 / E433 :</tspan> Émulsifiants synthétiques érodant</text>
    <text x="36" y="261" font-family="Liberation Sans, Arial, sans-serif" font-size="11.8" fill="#5C5549">le mucus protecteur du microbiote intestinal.</text>

    <!-- Courses -->
    <rect x="16" y="288" width="363" height="106" rx="6" fill="#F2ECE1" stroke="#B45309" stroke-width="1.2"/>
    <text x="26" y="308" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" font-weight="bold" fill="#B45309">LA PARADE NEUROLOGIQUE DES COURSES :</text>
    <text x="26" y="327" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">• <tspan font-weight="bold">Ventre vide :</tspan> Pic de ghréline court-circuitant</text>
    <text x="36" y="343" font-family="Liberation Sans, Arial, sans-serif" font-size="11.8" fill="#5C5549">le cortex rationnel vers les produits ultra-transformés.</text>
    <text x="26" y="365" font-family="Liberation Serif, Georgia, serif" font-size="12.2" font-weight="bold" fill="#5A6E54">✓ Règle d'or : Courses le ventre plein, liste fermée</text>
    <text x="36" y="381" font-family="Liberation Serif, Georgia, serif" font-size="12.0" font-weight="bold" fill="#5A6E54">et priorité aux produits bruts sans étiquette !</text>
  </g>
</svg>"""

# ==============================================================================
# FIG 15 : figures/livre_1/fig_pates_thermodynamique.svg
# ==============================================================================
SVGS["figures/livre_1/fig_pates_thermodynamique.svg"] = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 500" width="100%" height="100%">
  <rect width="880" height="500" rx="14" fill="#FCFBF7" stroke="#DFDACF" stroke-width="2"/>
  <text x="440" y="34" font-family="Liberation Serif, Georgia, serif" font-size="20" font-weight="bold" fill="#701C1A" text-anchor="middle">THERMODYNAMIQUE DES PÂTES ET ÉMULSION D'OR DE LA CARBONARA</text>
  <text x="440" y="55" font-family="Liberation Sans, Arial, sans-serif" font-size="13.5" fill="#5C5549" text-anchor="middle">Gélatinisation de l'amidon, règle 100 / 10 / 1 et liaison colloïdale sans crème.</text>

  <!-- Panneau Gauche : Règle 100 / 10 / 1 -->
  <g transform="translate(30, 75)">
    <rect width="395" height="400" rx="10" fill="#FAF7F2" stroke="#966C3B" stroke-width="1.5"/>
    <rect width="395" height="32" rx="10" fill="#6B4423"/>
    <text x="197" y="21" font-family="Liberation Serif, Georgia, serif" font-size="13.5" font-weight="bold" fill="#FCFBF7" text-anchor="middle">1. L'ÉQUATION DES PÂTES : 100 g / 10 g / 1 L</text>

    <text x="16" y="54" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" fill="#242124"><tspan font-weight="bold" fill="#6B4423">• Ratio canonique :</tspan> 100 g de pâtes, 10 g de sel, 1 L d'eau.</text>
    <text x="16" y="74" font-family="Liberation Sans, Arial, sans-serif" font-size="12.0" fill="#5C5549">Le grand volume d'eau assure l'inertie thermique à 100°C</text>
    <text x="16" y="90" font-family="Liberation Sans, Arial, sans-serif" font-size="12.0" fill="#5C5549">au plongeon et dilue l'amidon pour éviter l'agglutination.</text>

    <text x="16" y="118" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" font-weight="bold" fill="#5A6E54">✓ LE GESTE VERTUEUX :</text>
    <text x="20" y="138" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">1. Plonger dans l'eau salée à bouillon vif (100°C).</text>
    <text x="20" y="156" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">2. Remuer dès les 30 premières secondes critiques.</text>
    <text x="20" y="174" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">3. Cuire <tspan font-style="italic">al dente</tspan> : cœur de gluten ferme (IG modéré).</text>
    <text x="20" y="192" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" font-weight="bold" fill="#B45309">4. Prélever 1 louche d'eau de cuisson blanchie d'amylose</text>
    <text x="34" y="208" font-family="Liberation Sans, Arial, sans-serif" font-size="12.0" fill="#5C5549">avant d'égoutter pour lier et émulsionner la sauce !</text>

    <text x="16" y="240" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" font-weight="bold" fill="#701C1A">✗ LES TROIS ERREURS À BANNIR :</text>
    <text x="20" y="260" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">• <tspan font-weight="bold" fill="#701C1A">Verser de l'huile dans l'eau :</tspan> elle flotte en surface,</text>
    <text x="30" y="276" font-family="Liberation Sans, Arial, sans-serif" font-size="11.8" fill="#5C5549">puis imperméabilise la pâte à l'égouttage (la sauce glisse).</text>
    <text x="20" y="298" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">• <tspan font-weight="bold" fill="#701C1A">Rincer les pâtes cuites à l'eau :</tspan> élimine le film</text>
    <text x="30" y="314" font-family="Liberation Sans, Arial, sans-serif" font-size="11.8" fill="#5C5549">d'amidon superficiel indispensable à l'accroche du condiment.</text>
    <text x="20" y="336" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">• <tspan font-weight="bold" fill="#701C1A">Surcuire :</tspan> effondre la trame protéique et double</text>
    <text x="30" y="352" font-family="Liberation Sans, Arial, sans-serif" font-size="11.8" fill="#5C5549">la vitesse d'assimilation glycémique (pic d'insuline).</text>
  </g>

  <!-- Panneau Droit : Émulsion Carbonara -->
  <g transform="translate(455, 75)">
    <rect width="395" height="400" rx="10" fill="#FAF7F2" stroke="#B45309" stroke-width="1.5"/>
    <rect width="395" height="32" rx="10" fill="#B45309"/>
    <text x="197" y="21" font-family="Liberation Serif, Georgia, serif" font-size="13.5" font-weight="bold" fill="#FCFBF7" text-anchor="middle">2. LA CARBONARA : FENÊTRE THERMIQUE (62–65°C)</text>

    <rect x="20" y="48" width="355" height="95" rx="6" fill="#F2ECE1" stroke="#B45309" stroke-width="1.2"/>
    <text x="197" y="68" font-family="Liberation Serif, Georgia, serif" font-size="13" font-weight="bold" fill="#701C1A" text-anchor="middle">L'ÉQUATION COLLOÏDALE SANS CRÈME</text>
    <text x="197" y="88" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124" text-anchor="middle">Jaunes d'œufs (Lécithine) + Pecorino râpé fin</text>
    <text x="197" y="106" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124" text-anchor="middle">+ Graisse fondue du Guanciale + Eau amidonnée (64°C)</text>
    <text x="197" y="126" font-family="Liberation Serif, Georgia, serif" font-size="12.5" font-weight="bold" fill="#B45309" text-anchor="middle">= Crème d'or veloutée nappant chaque brin</text>

    <text x="16" y="168" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" font-weight="bold" fill="#5A6E54">✓ LE PROTOCOLE HORS DU FEU :</text>
    <text x="20" y="188" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">1. Rissoler le guanciale à sec jusqu'à transparence ambrée.</text>
    <text x="20" y="206" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">2. Fouetter jaunes + pecorino + poivre noir concassé</text>
    <text x="34" y="222" font-family="Liberation Sans, Arial, sans-serif" font-size="12.0" fill="#5C5549">avec une cuillerée d'eau de cuisson tiédie.</text>
    <text x="20" y="240" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" font-weight="bold" fill="#701C1A">3. Retirer la poêle du feu et attendre 30 secondes</text>
    <text x="34" y="256" font-family="Liberation Sans, Arial, sans-serif" font-size="12.0" fill="#5C5549">que le métal descende sous le seuil critique de 68°C.</text>
    <text x="20" y="274" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">4. Verser l'appareil aux jaunes et vanner énergiquement.</text>

    <rect x="20" y="298" width="355" height="82" rx="6" fill="#FBF6F5" stroke="#A3432B" stroke-width="1"/>
    <text x="197" y="318" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" font-weight="bold" fill="#701C1A" text-anchor="middle">✗ LE PIÈGE DE LA POÊLE SUR LE BRÛLEUR (&gt; 70°C) :</text>
    <text x="197" y="338" font-family="Liberation Sans, Arial, sans-serif" font-size="12.0" fill="#242124" text-anchor="middle">Les protéines du jaune coagulent brutalement en</text>
    <text x="197" y="354" font-family="Liberation Sans, Arial, sans-serif" font-size="12.0" fill="#242124" text-anchor="middle">grumeaux d'omelette sèche au lieu d'émulsionner.</text>
  </g>
</svg>"""

# ==============================================================================
# FIG 22 : figures/livre_3/fig_puree_blumenthal_infusion.svg
# ==============================================================================
SVGS["figures/livre_3/fig_puree_blumenthal_infusion.svg"] = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 460" width="100%" height="100%">
  <rect width="880" height="460" rx="14" fill="#FCFBF7" stroke="#DFDACF" stroke-width="2"/>
  <text x="440" y="34" font-family="Liberation Serif, Georgia, serif" font-size="20" font-weight="bold" fill="#701C1A" text-anchor="middle">LA PURÉE PARFAITE SELON HESTON BLUMENTHAL</text>
  <text x="440" y="55" font-family="Liberation Sans, Arial, sans-serif" font-size="13.5" fill="#5C5549" text-anchor="middle">L'infusion aromatique des épluchures dans le lait et le respect mécanique des cellules d'amidon.</text>

  <!-- Panneau Gauche : Infusion des pelures -->
  <g transform="translate(30, 75)">
    <rect width="395" height="360" rx="10" fill="#FAF7F2" stroke="#B45309" stroke-width="1.5"/>
    <rect width="395" height="32" rx="10" fill="#B45309"/>
    <text x="197" y="21" font-family="Liberation Serif, Georgia, serif" font-size="13.5" font-weight="bold" fill="#FCFBF7" text-anchor="middle">1. LE SECRET MOLÉCULAIRE : LA PEAU</text>

    <ellipse cx="197" cy="110" rx="95" ry="52" fill="#F2ECE1" stroke="#6B4423" stroke-width="3"/>
    <ellipse cx="197" cy="110" rx="85" ry="43" fill="#FAF7F2" stroke="#B45309" stroke-width="1.5" stroke-dasharray="4,2"/>
    <text x="197" y="106" font-family="Liberation Serif, Georgia, serif" font-size="13.5" font-weight="bold" fill="#6B4423" text-anchor="middle">Chair centrale :</text>
    <text x="197" y="124" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" fill="#B45309" text-anchor="middle">Amidon pur (neutre)</text>

    <text x="197" y="186" font-family="Liberation Sans, Arial, sans-serif" font-size="13.0" font-weight="bold" fill="#701C1A" text-anchor="middle">Sous-épiderme (0 à 2 mm sous la peau) :</text>
    <text x="197" y="205" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" fill="#242124" text-anchor="middle">Concentre 85 % des molécules d'arômes volatils</text>
    <text x="197" y="223" font-family="Liberation Sans, Arial, sans-serif" font-size="12.0" fill="#5C5549" font-style="italic" text-anchor="middle">(Méthional et pyrazines au parfum de terre chaude)</text>

    <rect x="20" y="245" width="355" height="95" rx="6" fill="#F2ECE1" stroke="#B45309" stroke-width="1.2"/>
    <text x="197" y="267" font-family="Liberation Serif, Georgia, serif" font-size="13.0" font-weight="bold" fill="#701C1A" text-anchor="middle">✓ Le Protocole d'Infusion Blumenthal :</text>
    <text x="197" y="287" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124" text-anchor="middle">Brosser les tubercules, prélever les épluchures saines</text>
    <text x="197" y="305" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124" text-anchor="middle">et les faire infuser 25 min dans le lait frémissant</text>
    <text x="197" y="323" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" font-weight="bold" fill="#B45309" text-anchor="middle">avant de filtrer au chinois sur la pulpe écrasée !</text>
  </g>

  <!-- Panneau Droit : Presse-purée vs Mixeur -->
  <g transform="translate(455, 75)">
    <rect width="395" height="360" rx="10" fill="#FAF7F2" stroke="#966C3B" stroke-width="1.5"/>
    <rect width="395" height="32" rx="10" fill="#6B4423"/>
    <text x="197" y="21" font-family="Liberation Serif, Georgia, serif" font-size="13.5" font-weight="bold" fill="#FCFBF7" text-anchor="middle">2. MÉCANIQUE CELLULAIRE : PRESSE vs MIXEUR</text>

    <rect x="20" y="48" width="355" height="140" rx="6" fill="#F4F6F4" stroke="#5A6E54" stroke-width="1.2"/>
    <text x="32" y="70" font-family="Liberation Sans, Arial, sans-serif" font-size="13.0" font-weight="bold" fill="#5A6E54">✓ PRESSE-PURÉE OU MOULIN À LÉGUMES</text>
    <text x="32" y="92" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">• Cisaillement lent à basse pression mécanique.</text>
    <text x="32" y="110" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">• Les cellules végétales se dissocient le long</text>
    <text x="42" y="126" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">de leur lamelle pectique sans jamais éclater.</text>
    <text x="32" y="144" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">• L'amylose reste confiné dans son sac cellulaire.</text>
    <text x="32" y="168" font-family="Liberation Serif, Georgia, serif" font-size="12.5" font-weight="bold" fill="#5A6E54">→ Résultat : Texture nuageuse, courte et fondante.</text>

    <rect x="20" y="202" width="355" height="140" rx="6" fill="#FBF6F5" stroke="#A3432B" stroke-width="1.2"/>
    <text x="32" y="224" font-family="Liberation Sans, Arial, sans-serif" font-size="13.0" font-weight="bold" fill="#701C1A">✗ MIXEUR PLONGEANT OU ROBOT À LAME</text>
    <text x="32" y="246" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">• Hélice tournant à 10 000 tours/minute.</text>
    <text x="32" y="264" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">• Éventration mécanique des parois cellulaires.</text>
    <text x="32" y="282" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">• L'amylose libéré dans l'eau s'entrelace en un</text>
    <text x="42" y="298" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">réseau viscoélastique collant irréversible.</text>
    <text x="32" y="322" font-family="Liberation Serif, Georgia, serif" font-size="12.5" font-weight="bold" fill="#701C1A">→ Résultat : Colle à papier peint élastique et gluante.</text>
  </g>
</svg>"""

# ==============================================================================
# FIG 34 : figures/livre_2/fig_05_oeuf_anatomie_barriere.svg
# ==============================================================================
SVGS["figures/livre_2/fig_05_oeuf_anatomie_barriere.svg"] = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 470" width="100%" height="100%">
  <rect width="880" height="470" rx="14" fill="#FCFBF7" stroke="#DFDACF" stroke-width="2"/>
  <text x="440" y="34" font-family="Liberation Serif, Georgia, serif" font-size="20" font-weight="bold" fill="#701C1A" text-anchor="middle">ANATOMIE PHYSICO-CHIMIQUE ET BARRIÈRE CUTICULAIRE DE L'ŒUF</text>
  <text x="440" y="55" font-family="Liberation Sans, Arial, sans-serif" font-size="13.5" fill="#5C5549" text-anchor="middle">Pourquoi l'œuf est un écosystème respirant et pourquoi le lavage détruit sa défense biologique.</text>

  <!-- Coupe de l'œuf à gauche -->
  <g transform="translate(55, 95)">
    <!-- Cuticule externe pointillée -->
    <path d="M 140 12 C 236 12 286 118 286 200 C 286 286 224 328 140 328 C 56 328 -6 286 -6 200 C -6 118 44 12 140 12 Z" fill="none" stroke="#5A6E54" stroke-width="2.2" stroke-dasharray="6,3"/>
    <!-- Coquille -->
    <path d="M 140 20 C 230 20 280 120 280 200 C 280 280 220 320 140 320 C 60 320 0 280 0 200 C 0 120 50 20 140 20 Z" fill="#FAF7F2" stroke="#B45309" stroke-width="3.5"/>
    <!-- Chambre à air -->
    <path d="M 50 294 Q 140 258 230 294 C 205 315 165 320 140 320 C 115 320 75 315 50 294 Z" fill="#F2ECE1" stroke="#966C3B" stroke-width="1.5"/>
    <text x="140" y="304" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" font-weight="bold" fill="#6B4423" text-anchor="middle">Chambre à air</text>

    <!-- Blanc liquide et blanc épais -->
    <path d="M 140 36 C 215 36 260 125 260 195 C 260 255 205 265 140 265 C 75 265 20 255 20 195 C 20 125 65 36 140 36 Z" fill="#FCFBF7" stroke="#D4A373" stroke-width="1.2"/>
    <path d="M 140 62 C 195 62 235 130 235 190 C 235 240 195 245 140 245 C 85 245 45 240 45 190 C 45 130 85 62 140 62 Z" fill="#F5EFE6" stroke="#966C3B" stroke-width="1.5"/>
    <text x="140" y="88" font-family="Liberation Sans, Arial, sans-serif" font-size="11.8" font-weight="bold" fill="#6B4423" text-anchor="middle">Albumen (62°C – 84°C)</text>

    <!-- Jaune -->
    <circle cx="140" cy="168" r="52" fill="#D97706" stroke="#B45309" stroke-width="2.5"/>
    <circle cx="140" cy="168" r="45" fill="#F59E0B"/>
    <text x="140" y="165" font-family="Liberation Serif, Georgia, serif" font-size="13" font-weight="bold" fill="#FCFBF7" text-anchor="middle">Vitellus (Jaune)</text>
    <text x="140" y="182" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" font-weight="bold" fill="#FCFBF7" text-anchor="middle">Seuil : 68°C</text>

    <!-- Chalazes -->
    <path d="M 88 168 C 70 162 65 174 48 168" fill="none" stroke="#6B4423" stroke-width="2.5"/>
    <path d="M 192 168 C 210 162 215 174 232 168" fill="none" stroke="#6B4423" stroke-width="2.5"/>
    <text x="140" y="348" font-family="Liberation Sans, Arial, sans-serif" font-size="12" font-weight="bold" fill="#5A6E54" text-anchor="middle">Pointillés : Cuticule protéique (bouclier contre Salmonella)</text>
  </g>

  <!-- Cartouches explicatifs à droite -->
  <g transform="translate(390, 80)">
    <rect width="460" height="165" rx="8" fill="#FAF7F2" stroke="#5A6E54" stroke-width="1.5"/>
    <rect width="460" height="30" rx="8" fill="#5A6E54"/>
    <text x="230" y="20" font-family="Liberation Serif, Georgia, serif" font-size="13.5" font-weight="bold" fill="#FCFBF7" text-anchor="middle">1. LE DILEMME DU FRIGO : EUROPE vs ÉTATS-UNIS</text>

    <text x="16" y="50" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" fill="#242124">• <tspan font-weight="bold" fill="#5A6E54">La cuticule naturelle :</tspan> vernis protéique obturant les</text>
    <text x="26" y="66" font-family="Liberation Sans, Arial, sans-serif" font-size="12.0" fill="#5C5549">10 000 pores de la coquille calcaire contre les bactéries.</text>
    <text x="16" y="88" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" fill="#242124">• <tspan font-weight="bold" fill="#5A6E54">Europe (non lavé) :</tspan> cuticule intacte → conservation stable</text>
    <text x="26" y="104" font-family="Liberation Sans, Arial, sans-serif" font-size="12.0" fill="#5C5549">hors condensation. Ne jamais laver un œuf avant de le stocker !</text>
    <text x="16" y="126" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" fill="#242124">• <tspan font-weight="bold" fill="#701C1A">États-Unis (lavé au chlore) :</tspan> cuticule détruite → pores</text>
    <text x="26" y="142" font-family="Liberation Sans, Arial, sans-serif" font-size="12.0" fill="#701C1A">ouverts imposant le réfrigérateur continu à 4°C.</text>

    <rect y="182" width="460" height="190" rx="8" fill="#FAF7F2" stroke="#966C3B" stroke-width="1.5"/>
    <rect y="182" width="460" height="30" rx="8" fill="#701C1A"/>
    <text x="230" y="202" font-family="Liberation Serif, Georgia, serif" font-size="13.5" font-weight="bold" fill="#FCFBF7" text-anchor="middle">2. LA MÉCANIQUE DU VIEILLISSEMENT : 3 MARQUEURS</text>

    <text x="16" y="232" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" fill="#242124"><tspan font-weight="bold" fill="#701C1A">1. Évaporation hydrique :</tspan> la chambre à air s'agrandit.</text>
    <text x="26" y="248" font-family="Liberation Sans, Arial, sans-serif" font-size="12.0" fill="#5C5549">L'œuf frais coule à plat ; l'œuf de plus de 28 jours flotte.</text>

    <text x="16" y="272" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" fill="#242124"><tspan font-weight="bold" fill="#701C1A">2. Fuite de CO₂ dissous :</tspan> le pH grimpe de 7,6 à 9,2.</text>
    <text x="26" y="288" font-family="Liberation Sans, Arial, sans-serif" font-size="12.0" fill="#5C5549">Un œuf de 10 jours s'écale bien mieux dur qu'un œuf du jour.</text>

    <text x="16" y="312" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" fill="#242124"><tspan font-weight="bold" fill="#701C1A">3. Relâchement de l'ovomucine :</tspan> le blanc se liquéfie.</text>
    <text x="26" y="328" font-family="Liberation Sans, Arial, sans-serif" font-size="12.0" fill="#5C5549">Seul un œuf extra-frais (&lt; 8 jours) donne un œuf poché compact.</text>
    <text x="16" y="354" font-family="Liberation Serif, Georgia, serif" font-size="12.2" font-weight="bold" fill="#B45309">→ Tempérer l'œuf 30 min à l'air ambiant avant cuisson douce.</text>
  </g>
</svg>"""

# ==============================================================================
# FIG 44 : figures/livre_4/fig_caillage_lait_caseine.svg
# ==============================================================================
SVGS["figures/livre_4/fig_caillage_lait_caseine.svg"] = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 510" width="100%" height="100%">
  <rect width="880" height="510" rx="14" fill="#FCFBF7" stroke="#DFDACF" stroke-width="2"/>
  <text x="440" y="34" font-family="Liberation Serif, Georgia, serif" font-size="20" font-weight="bold" fill="#701C1A" text-anchor="middle">BIOMÉCANIQUE DU CAILLAGE : LES DEUX VOIES DE RUPTURE COLLOÏDALE</text>
  <text x="440" y="55" font-family="Liberation Sans, Arial, sans-serif" font-size="13.5" fill="#5C5549" text-anchor="middle">De la répulsion électrostatique des micelles de caséine à la prise en gel du fromage.</text>

  <!-- Bloc Racine : Lait Entier -->
  <g transform="translate(245, 72)">
    <rect width="390" height="76" rx="8" fill="#FAF7F2" stroke="#966C3B" stroke-width="1.8"/>
    <text x="195" y="26" font-family="Liberation Serif, Georgia, serif" font-size="15" font-weight="bold" fill="#701C1A" text-anchor="middle">LAIT ENTIER FRAIS (pH 6,6)</text>
    <text x="195" y="46" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" fill="#242124" text-anchor="middle">Suspension colloïdale stable de micelles de caséine</text>
    <text x="195" y="64" font-family="Liberation Sans, Arial, sans-serif" font-size="11.8" font-style="italic" fill="#5C5549" text-anchor="middle">Charges négatives de surface = répulsion électrostatique mutuelle</text>
  </g>

  <!-- Lignes de bifurcation -->
  <path d="M 440 148 L 440 175" stroke="#966C3B" stroke-width="2.2"/>
  <path d="M 227 175 L 652 175" stroke="#966C3B" stroke-width="2.2"/>
  <path d="M 227 175 L 227 198" stroke="#5A6E54" stroke-width="2.2"/>
  <polygon points="227,204 222,196 232,196" fill="#5A6E54"/>
  <path d="M 652 175 L 652 198" stroke="#B45309" stroke-width="2.2"/>
  <polygon points="652,204 647,196 657,196" fill="#B45309"/>

  <!-- Voie Gauche : Acide -->
  <g transform="translate(40, 206)">
    <rect width="375" height="92" rx="8" fill="#F4F6F4" stroke="#5A6E54" stroke-width="1.5"/>
    <text x="187" y="25" font-family="Liberation Serif, Georgia, serif" font-size="14" font-weight="bold" fill="#5A6E54" text-anchor="middle">VOIE 1 : COAGULATION ACIDE DIRECTE</text>
    <text x="187" y="45" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" font-weight="bold" fill="#242124" text-anchor="middle">Citron, Vinaigre ou Ferments lactiques (pH 4,6)</text>
    <text x="187" y="64" font-family="Liberation Sans, Arial, sans-serif" font-size="12.0" fill="#5C5549" text-anchor="middle">Point isoélectrique : les protons H⁺ annulent les charges.</text>
    <text x="187" y="81" font-family="Liberation Sans, Arial, sans-serif" font-size="11.8" fill="#5C5549" text-anchor="middle">Les micelles déminéralisées floculent instantanément.</text>
  </g>

  <path d="M 227 298 L 227 325" stroke="#5A6E54" stroke-width="2.2"/>
  <polygon points="227,331 222,323 232,323" fill="#5A6E54"/>

  <g transform="translate(40, 333)">
    <rect width="375" height="150" rx="8" fill="#FAF7F2" stroke="#5A6E54" stroke-width="1.5"/>
    <rect width="375" height="30" rx="8" fill="#5A6E54"/>
    <text x="187" y="20" font-family="Liberation Serif, Georgia, serif" font-size="13" font-weight="bold" fill="#FCFBF7" text-anchor="middle">CAILLÉ LACTIQUE : PÂTE FRAÎCHE FRIABLE</text>
    <text x="18" y="52" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" font-weight="bold" fill="#5A6E54">• Architecture microscopique :</text>
    <text x="28" y="70" font-family="Liberation Sans, Arial, sans-serif" font-size="12.0" fill="#242124">Réseau poreux court, fragile et très humide.</text>
    <text x="18" y="94" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" font-weight="bold" fill="#5A6E54">• Applications au foyer :</text>
    <text x="28" y="112" font-family="Liberation Sans, Arial, sans-serif" font-size="12.0" fill="#242124">Fromage frais en 15 min, Faisselle, Paneer, Ricotta.</text>
    <text x="18" y="135" font-family="Liberation Sans, Arial, sans-serif" font-size="11.8" font-style="italic" fill="#5C5549">Égouttage doux par gravité dans une étamine de coton.</text>
  </g>

  <!-- Voie Droite : Présure -->
  <g transform="translate(465, 206)">
    <rect width="375" height="92" rx="8" fill="#F2ECE1" stroke="#B45309" stroke-width="1.5"/>
    <text x="187" y="25" font-family="Liberation Serif, Georgia, serif" font-size="14" font-weight="bold" fill="#B45309" text-anchor="middle">VOIE 2 : COAGULATION ENZYMATIQUE</text>
    <text x="187" y="45" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" font-weight="bold" fill="#242124" text-anchor="middle">Présure / Chymosine à tiédeur animale (32–35°C)</text>
    <text x="187" y="64" font-family="Liberation Sans, Arial, sans-serif" font-size="12.0" fill="#5C5549" text-anchor="middle">Cisaillement sélectif des poils de caséine kappa.</text>
    <text x="187" y="81" font-family="Liberation Sans, Arial, sans-serif" font-size="11.8" fill="#5C5549" text-anchor="middle">Soudure tridimensionnelle par ponts de calcium (Ca²⁺).</text>
  </g>

  <path d="M 652 298 L 652 325" stroke="#B45309" stroke-width="2.2"/>
  <polygon points="652,331 647,323 657,323" fill="#B45309"/>

  <g transform="translate(465, 333)">
    <rect width="375" height="150" rx="8" fill="#FAF7F2" stroke="#B45309" stroke-width="1.5"/>
    <rect width="375" height="30" rx="8" fill="#B45309"/>
    <text x="187" y="20" font-family="Liberation Serif, Georgia, serif" font-size="13" font-weight="bold" fill="#FCFBF7" text-anchor="middle">GEL PRÉSURE : CAILLÉ SOUPLE DE GARDE</text>
    <text x="18" y="52" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" font-weight="bold" fill="#B45309">• Architecture microscopique :</text>
    <text x="28" y="70" font-family="Liberation Sans, Arial, sans-serif" font-size="12.0" fill="#242124">Gel élastique et imperméable à forte synérèse.</text>
    <text x="18" y="94" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" font-weight="bold" fill="#B45309">• Fromages d'affinage :</text>
    <text x="28" y="112" font-family="Liberation Sans, Arial, sans-serif" font-size="12.0" fill="#242124">Comté, Beaufort, Tomme de montagne, Camembert.</text>
    <text x="18" y="135" font-family="Liberation Sans, Arial, sans-serif" font-size="11.8" font-style="italic" fill="#5C5549">Autorise le décaillage au sabre, le chauffage et le pressage.</text>
  </g>
</svg>"""

# ==============================================================================
# FIG 46 : figures/livre_3/fig_gateau_chocolat_matrice.svg
# ==============================================================================
SVGS["figures/livre_3/fig_gateau_chocolat_matrice.svg"] = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 520" width="100%" height="100%">
  <rect width="880" height="520" rx="14" fill="#FCFBF7" stroke="#DFDACF" stroke-width="2"/>
  <text x="440" y="34" font-family="Liberation Serif, Georgia, serif" font-size="20" font-weight="bold" fill="#701C1A" text-anchor="middle">LA MATRICE UNIVERSELLE DU GÂTEAU ET LA RIGUEUR DU FOUR</text>
  <text x="440" y="55" font-family="Liberation Sans, Arial, sans-serif" font-size="13.5" fill="#5C5549" text-anchor="middle">L'équation fonctionnelle de la pâtisserie et la loi physique du préchauffage.</text>

  <!-- Bandeau supérieur : Équation matricielle -->
  <g transform="translate(30, 72)">
    <rect width="820" height="62" rx="8" fill="#F2ECE1" stroke="#B45309" stroke-width="1.5"/>
    <text x="410" y="25" font-family="Liberation Serif, Georgia, serif" font-size="14" font-weight="bold" fill="#701C1A" text-anchor="middle">L'ÉQUATION D'ÉTAT : LA RECETTE COMME SYSTÈME MODULAIRE</text>
    <text x="410" y="47" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#6B4423" text-anchor="middle">Corps Gras (Beurre/Huile) + Agent Sucrant + Féculent (Farine/Riz) + Liant (Œuf/Aquafaba) + Chaleur = GÂTEAU</text>
  </g>

  <!-- Méthode 1 : Tout-en-un -->
  <g transform="translate(30, 148)">
    <rect width="395" height="175" rx="8" fill="#FAF7F2" stroke="#966C3B" stroke-width="1.5"/>
    <rect width="395" height="30" rx="8" fill="#6B4423"/>
    <text x="197" y="20" font-family="Liberation Serif, Georgia, serif" font-size="13.5" font-weight="bold" fill="#FCFBF7" text-anchor="middle">MÉTHODE 1 : ÉMULSION DIRECTE (RAPIDE)</text>
    <text x="16" y="50" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">• Mélange direct : œufs entiers + sucre + chocolat</text>
    <text x="26" y="66" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">et beurre fondus + farine tamisée en pluie.</text>
    <text x="16" y="88" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">• Temps actif : 4 minutes. Une seule jatte à laver.</text>
    <text x="16" y="110" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#5A6E54" font-weight="bold">✓ Texture obtenue : Fondant dense et humide,</text>
    <text x="26" y="126" font-family="Liberation Sans, Arial, sans-serif" font-size="12.0" fill="#5C5549">idéal pour moelleux coulant, brownie et financier.</text>
    <text x="16" y="150" font-family="Liberation Sans, Arial, sans-serif" font-size="12.0" font-weight="bold" fill="#701C1A">Règle : Ne jamais trop fouetter après ajout de la farine.</text>
  </g>

  <!-- Méthode 2 : Blancs montés -->
  <g transform="translate(455, 148)">
    <rect width="395" height="175" rx="8" fill="#FAF7F2" stroke="#B45309" stroke-width="1.5"/>
    <rect width="395" height="30" rx="8" fill="#B45309"/>
    <text x="197" y="20" font-family="Liberation Serif, Georgia, serif" font-size="13.5" font-weight="bold" fill="#FCFBF7" text-anchor="middle">MÉTHODE 2 : BLANCS MONTÉS EN NEIGE</text>
    <text x="16" y="50" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">• Incorporation délicate de la mousse d'albumine</text>
    <text x="26" y="66" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">à la maryse dans l'appareil chocolaté dense.</text>
    <text x="16" y="88" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">• Dilatation thermique des microbulles d'air au four.</text>
    <text x="16" y="110" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#6B4423" font-weight="bold">✓ Texture obtenue : Mie souple, aérienne et</text>
    <text x="26" y="126" font-family="Liberation Sans, Arial, sans-serif" font-size="12.0" fill="#5C5549">alvéolée (biscuit de Savoie, génoise, soufflé).</text>
    <text x="16" y="150" font-family="Liberation Sans, Arial, sans-serif" font-size="12.0" font-weight="bold" fill="#B45309">Substitut végétal : Aquafaba (eau de pois chiches).</text>
  </g>

  <!-- Bandeau inférieur : Pourquoi préchauffer le four -->
  <g transform="translate(30, 340)">
    <rect width="820" height="156" rx="8" fill="#FAF7F2" stroke="#701C1A" stroke-width="1.5"/>
    <rect width="820" height="30" rx="8" fill="#701C1A"/>
    <text x="410" y="20" font-family="Liberation Serif, Georgia, serif" font-size="13.5" font-weight="bold" fill="#FCFBF7" text-anchor="middle">POURQUOI ENFOURNER DANS UN FOUR PRÉCHAUFFÉ (180°C) PLUTÔT QUE FROID ?</text>

    <text x="18" y="52" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" fill="#242124"><tspan font-weight="bold" fill="#5A6E54">1. L'Oven Spring (Poussée gazeuse synchronisée) :</tspan> Dans un four chaud à 180°C, la vapeur d'eau</text>
    <text x="34" y="69" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#5C5549">et le CO₂ se dilatent brutalement dès l'enfournement, soulevant la pâte avant que la croûte ne fige.</text>

    <text x="18" y="93" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" fill="#242124"><tspan font-weight="bold" fill="#5A6E54">2. La fixation de la charpente :</tspan> Les protéines de l'œuf coagulent (68–84°C) et l'amidon gélatinise</text>
    <text x="34" y="110" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#5C5549">exactement au sommet de l'expansion gazeuse, verrouillant la structure spongieuse du gâteau.</text>

    <text x="18" y="136" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" fill="#701C1A"><tspan font-weight="bold">✗ En départ four froid :</tspan> Le beurre fond dès 32°C, l'émulsion se brise et le gaz fuit avant coagulation → gâteau plat.</text>
  </g>
</svg>"""

# ==============================================================================
# FIG 50 : figures/livre_3/fig_omelette_norvegienne_bouclier.svg
# ==============================================================================
SVGS["figures/livre_3/fig_omelette_norvegienne_bouclier.svg"] = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 390" width="100%" height="100%">
  <rect width="880" height="390" rx="14" fill="#FCFBF7" stroke="#DFDACF" stroke-width="2"/>
  <text x="440" y="34" font-family="Liberation Serif, Georgia, serif" font-size="20" font-weight="bold" fill="#701C1A" text-anchor="middle">LE BOUCLIER THERMIQUE DE LA MERINGUE : L'OMELETTE NORVÉGIENNE</text>
  <text x="440" y="55" font-family="Liberation Sans, Arial, sans-serif" font-size="13.5" fill="#5C5549" text-anchor="middle">Comment dorer un dôme à 240°C sans faire fondre le cœur de glace à -18°C.</text>

  <!-- Coupe architecturale à gauche -->
  <g transform="translate(45, 78)">
    <text x="200" y="14" font-family="Liberation Serif, Georgia, serif" font-size="13.0" font-weight="bold" fill="#A3432B" text-anchor="middle">CHALEUR DU FOUR (240°C) OU FLAMBAGE (800°C)</text>
    <line x1="75" y1="22" x2="75" y2="54" stroke="#A3432B" stroke-width="2"/>
    <polygon points="75,59 71,51 79,51" fill="#A3432B"/>
    <line x1="200" y1="22" x2="200" y2="44" stroke="#A3432B" stroke-width="2"/>
    <polygon points="200,49 196,41 204,41" fill="#A3432B"/>
    <line x1="325" y1="22" x2="325" y2="54" stroke="#A3432B" stroke-width="2"/>
    <polygon points="325,59 321,51 329,51" fill="#A3432B"/>

    <path d="M 25 244 C 25 14 375 14 375 244 Z" fill="#FAF7F0" stroke="#92400E" stroke-width="2.5"/>
    <path d="M 33 242 C 33 23 367 23 367 242" fill="none" stroke="#D4A373" stroke-width="2" stroke-dasharray="5,3"/>

    <text x="200" y="112" font-family="Liberation Serif, Georgia, serif" font-size="13.5" font-weight="bold" fill="#92400E" text-anchor="middle">MANTEAU DE MERINGUE (2 cm)</text>
    <text x="200" y="130" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" fill="#5C5549" text-anchor="middle">90 % de microbulles d'air immobile</text>

    <path d="M 95 244 C 95 148 305 148 305 244 Z" fill="#F2ECE1" stroke="#8C7355" stroke-width="2"/>
    <text x="200" y="204" font-family="Liberation Serif, Georgia, serif" font-size="13.5" font-weight="bold" fill="#242124" text-anchor="middle">CŒUR DE GLACE (-18°C)</text>
    <text x="200" y="222" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#5A6E54" font-weight="bold" text-anchor="middle">Intact : zéro fusion thermique</text>

    <rect x="18" y="244" width="364" height="26" rx="4" fill="#E6C49A" stroke="#92400E" stroke-width="1.5"/>
    <text x="200" y="261" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" font-weight="bold" fill="#451A03" text-anchor="middle">SOCLE DE GÉNOISE : Isolant thermique inférieur</text>
  </g>

  <!-- Cartouche explicatif à droite -->
  <g transform="translate(475, 82)">
    <rect width="375" height="275" rx="8" fill="#FAF7F2" stroke="#DFDACF" stroke-width="1.5"/>
    <rect width="375" height="32" rx="8" fill="#701C1A"/>
    <text x="187" y="21" font-family="Liberation Serif, Georgia, serif" font-size="13.5" font-weight="bold" fill="#FCFBF7" text-anchor="middle">LES 3 SECRETS PHYSIQUES DU MIRACLE</text>

    <text x="16" y="54" font-family="Liberation Serif, Georgia, serif" font-size="13.5" font-weight="bold" fill="#A3432B">1. L'air prisonnier est un mur thermique</text>
    <text x="16" y="72" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">La mousse de blancs d'œufs bloque la chaleur</text>
    <text x="16" y="88" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#5C5549">comme un double vitrage isolant parfait.</text>

    <text x="16" y="118" font-family="Liberation Serif, Georgia, serif" font-size="13.5" font-weight="bold" fill="#A3432B">2. Le socle biscuité coupe la conduction</text>
    <text x="16" y="136" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">La génoise aérée empêche le plat chaud de</text>
    <text x="16" y="152" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#5C5549">faire fondre la crème glacée par le dessous.</text>

    <text x="16" y="182" font-family="Liberation Serif, Georgia, serif" font-size="13.5" font-weight="bold" fill="#701C1A">3. Étanchéité hermétique exigée</text>
    <text x="16" y="200" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">La meringue doit sceller le socle sans la moindre</text>
    <text x="16" y="216" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#5C5549">fissure (coloration éclair : 3 à 4 min au gril).</text>

    <rect x="16" y="232" width="343" height="28" rx="4" fill="#F4F6F4" stroke="#5A6E54" stroke-width="1"/>
    <text x="187" y="250" font-family="Liberation Serif, Georgia, serif" font-size="12.5" font-weight="bold" fill="#5A6E54" text-anchor="middle">Contraste : +240°C dehors / -18°C dedans</text>
  </g>
</svg>"""

# ==============================================================================
# FIG 51 : figures/livre_5/fig_fromage_glace_cryoscopie.svg
# ==============================================================================
SVGS["figures/livre_5/fig_fromage_glace_cryoscopie.svg"] = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 510" width="100%" height="100%">
  <rect width="880" height="510" rx="14" fill="#FCFBF7" stroke="#DFDACF" stroke-width="2"/>
  <text x="440" y="34" font-family="Liberation Serif, Georgia, serif" font-size="20" font-weight="bold" fill="#701C1A" text-anchor="middle">DEUX PRODIGES DOMESTIQUES PAR LES PRINCIPES PREMIERS</text>
  <text x="440" y="55" font-family="Liberation Sans, Arial, sans-serif" font-size="13.5" fill="#5C5549" text-anchor="middle">Fabriquer du fromage frais en 15 minutes et turbiner une glace onctueuse sans machine.</text>

  <!-- Volet Gauche : Fromage frais -->
  <g transform="translate(30, 75)">
    <rect width="395" height="410" rx="10" fill="#FAF7F2" stroke="#5A6E54" stroke-width="1.5"/>
    <rect width="395" height="32" rx="10" fill="#5A6E54"/>
    <text x="197" y="21" font-family="Liberation Serif, Georgia, serif" font-size="13.5" font-weight="bold" fill="#FCFBF7" text-anchor="middle">1. LE FROMAGE FRAIS EN 15 MIN (SANS PRÉSURE)</text>

    <!-- Schéma Caséines -->
    <rect x="20" y="46" width="355" height="86" rx="6" fill="#F4F6F4" stroke="#5A6E54" stroke-width="1"/>
    <circle cx="70" cy="89" r="24" fill="#FCFBF7" stroke="#6B4423" stroke-width="2"/>
    <text x="70" y="93" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" font-weight="bold" fill="#6B4423" text-anchor="middle">Caséines</text>

    <path d="M 105 89 L 155 89" stroke="#5A6E54" stroke-width="2.5"/>
    <polygon points="160,89 152,85 152,93" fill="#5A6E54"/>
    <text x="132" y="79" font-family="Liberation Sans, Arial, sans-serif" font-size="11.8" font-weight="bold" fill="#5A6E54" text-anchor="middle">+ Citron (H⁺)</text>

    <path d="M 175 74 L 195 102 L 215 74 L 235 102 L 255 74" fill="none" stroke="#6B4423" stroke-width="2.5"/>
    <text x="310" y="84" font-family="Liberation Serif, Georgia, serif" font-size="12.5" font-weight="bold" fill="#5A6E54" text-anchor="middle">Caillé blanc</text>
    <text x="310" y="102" font-family="Liberation Sans, Arial, sans-serif" font-size="11.8" fill="#5C5549" text-anchor="middle">+ Lactosérum</text>

    <text x="18" y="158" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" font-weight="bold" fill="#701C1A">Proportions canoniques :</text>
    <text x="18" y="176" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">1 L de lait entier frais + 3 c. à soupe de jus de citron</text>
    <text x="18" y="192" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#5C5549">(ou vinaigre de cidre) + 1 pincée de fleur de sel.</text>

    <text x="18" y="220" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" font-weight="bold" fill="#5A6E54">Protocole thermique et colloïdal :</text>
    <text x="18" y="240" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">1. Porter le lait à <tspan font-weight="bold">82–85°C</tspan> (frémissement, sans bouillir).</text>
    <text x="18" y="258" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">2. Couper le feu, verser l'acide et remuer doucement.</text>
    <text x="18" y="276" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">3. Couvrir 10 min : le caillé flocule dans le petit-lait.</text>
    <text x="18" y="294" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">4. Égoutter en passoire tapissée d'un linge propre.</text>

    <rect x="18" y="316" width="359" height="76" rx="6" fill="#F2ECE1"/>
    <text x="197" y="338" font-family="Liberation Serif, Georgia, serif" font-size="12.5" font-weight="bold" fill="#5A6E54" text-anchor="middle">✓ Deux textures selon le temps d'égouttage :</text>
    <text x="197" y="358" font-family="Liberation Sans, Arial, sans-serif" font-size="12.0" fill="#242124" text-anchor="middle">• 15 min : Ricotta / Fromage frais crémeux à tartiner.</text>
    <text x="197" y="376" font-family="Liberation Sans, Arial, sans-serif" font-size="12.0" fill="#242124" text-anchor="middle">• 1 h sous poids : Paneer ferme à dorer à la poêle.</text>
  </g>

  <!-- Volet Droit : Glace cryoscopique -->
  <g transform="translate(455, 75)">
    <rect width="395" height="410" rx="10" fill="#FAF7F2" stroke="#B45309" stroke-width="1.5"/>
    <rect width="395" height="32" rx="10" fill="#701C1A"/>
    <text x="197" y="21" font-family="Liberation Serif, Georgia, serif" font-size="13.5" font-weight="bold" fill="#FCFBF7" text-anchor="middle">2. LA GLACE SANS SORBETIÈRE PAR LE SEL (-18°C)</text>

    <!-- Schéma Bain Cryoscopique -->
    <rect x="20" y="46" width="355" height="86" rx="6" fill="#F2ECE1" stroke="#B45309" stroke-width="1"/>
    <circle cx="115" cy="89" r="34" fill="#FAF7F2" stroke="#701C1A" stroke-width="2"/>
    <circle cx="115" cy="89" r="18" fill="#F59E0B" stroke="#B45309" stroke-width="1.5"/>
    <text x="115" y="93" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" font-weight="bold" fill="#242124" text-anchor="middle">Crème</text>
    <text x="260" y="78" font-family="Liberation Serif, Georgia, serif" font-size="12.5" font-weight="bold" fill="#701C1A" text-anchor="middle">Bain cryoscopique externe :</text>
    <text x="260" y="96" font-family="Liberation Sans, Arial, sans-serif" font-size="12.0" fill="#242124" text-anchor="middle">3 parts de glace + 1 part de gros sel</text>
    <text x="260" y="114" font-family="Liberation Sans, Arial, sans-serif" font-size="12.0" font-weight="bold" fill="#A3432B" text-anchor="middle">Chute thermique à -18°C !</text>

    <text x="18" y="158" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" font-weight="bold" fill="#701C1A">Principe de l'abaissement cryoscopique :</text>
    <text x="18" y="176" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">Fondre la glace pour dissoudre le sel consomme une</text>
    <text x="18" y="192" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">énergie endothermique massive pompée au bol central.</text>

    <text x="18" y="220" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" font-weight="bold" fill="#B45309">Protocole de turbinage manuel :</text>
    <text x="18" y="240" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">1. Grand saladier : 1 kg de glaçons + 300 g de gros sel.</text>
    <text x="18" y="258" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">2. Y niché un cul-de-poule inox contenant la crème.</text>
    <text x="18" y="276" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">3. Fouetter et racler les parois durant 8 à 10 minutes.</text>
    <text x="18" y="294" font-family="Liberation Sans, Arial, sans-serif" font-size="12.2" fill="#242124">4. L'agitation brise les germes de glace (&lt; 20 microns).</text>

    <rect x="18" y="316" width="359" height="76" rx="6" fill="#F2ECE1"/>
    <text x="197" y="338" font-family="Liberation Serif, Georgia, serif" font-size="12.5" font-weight="bold" fill="#701C1A" text-anchor="middle">✓ Pourquoi la glace prise sans fouetter est dure :</text>
    <text x="197" y="358" font-family="Liberation Sans, Arial, sans-serif" font-size="12.0" fill="#242124" text-anchor="middle">Sans agitation ni air foisonné, l'eau gèle en aiguilles</text>
    <text x="197" y="376" font-family="Liberation Sans, Arial, sans-serif" font-size="12.0" fill="#242124" text-anchor="middle">grossières. Le fouet crée l'onctuosité d'un glacier.</text>
  </g>
</svg>"""

# ==============================================================================
# FIG 55 : figures/livre_5/fig_retroplanning_reception.svg
# ==============================================================================
SVGS["figures/livre_5/fig_retroplanning_reception.svg"] = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 360" width="100%" height="100%">
  <rect width="960" height="360" rx="12" fill="#FCFBF7" stroke="#DFDACF" stroke-width="2"/>
  <text x="480" y="36" font-family="Liberation Serif, Georgia, serif" font-size="20" font-weight="bold" fill="#701C1A" text-anchor="middle">LE RÉTROPLANNING DE RÉCEPTION : CHRONOGRAMME DU CUISINIER SEREIN</text>
  <text x="480" y="58" font-family="Liberation Sans, Arial, sans-serif" font-size="13" fill="#5C5549" text-anchor="middle">La dissociation temporelle entre la préparation technique et le plaisir partagé à table.</text>

  <!-- Étape 1 : J-2 / J-1 -->
  <g transform="translate(30, 85)">
    <rect width="205" height="235" rx="8" fill="#FAF7F2" stroke="#966C3B" stroke-width="1.5"/>
    <rect width="205" height="36" rx="8" fill="#701C1A"/>
    <text x="102" y="23" font-family="Liberation Serif, Georgia, serif" font-size="13" font-weight="bold" fill="#FCFBF7" text-anchor="middle">J - 2 / J - 1 : ANTICIPER</text>
    <text x="15" y="65" font-family="Liberation Sans, Arial, sans-serif" font-size="12" font-weight="bold" fill="#701C1A">• Courses complètes</text>
    <text x="25" y="82" font-family="Liberation Sans, Arial, sans-serif" font-size="11" fill="#5C5549">Vérifier épices et sel</text>
    <text x="15" y="108" font-family="Liberation Sans, Arial, sans-serif" font-size="12" font-weight="bold" fill="#701C1A">• Pâtes &amp; Desserts</text>
    <text x="25" y="125" font-family="Liberation Sans, Arial, sans-serif" font-size="11" fill="#5C5549">Fonds de tarte, biscuits</text>
    <text x="15" y="151" font-family="Liberation Sans, Arial, sans-serif" font-size="12" font-weight="bold" fill="#701C1A">• Bouillons &amp; Glaces</text>
    <text x="25" y="168" font-family="Liberation Sans, Arial, sans-serif" font-size="11" fill="#5C5549">Réductions collagéniques</text>
    <text x="15" y="194" font-family="Liberation Sans, Arial, sans-serif" font-size="12" font-weight="bold" fill="#701C1A">• Marinades &amp; Mijotés</text>
    <text x="25" y="211" font-family="Liberation Sans, Arial, sans-serif" font-size="11" fill="#5C5549">Meilleurs réchauffés J+1</text>
  </g>

  <path d="M 238 200 L 265 200" stroke="#A3432B" stroke-width="2.5"/>
  <polygon points="269,200 261,196 261,204" fill="#A3432B"/>

  <!-- Étape 2 : Matin J -->
  <g transform="translate(270, 85)">
    <rect width="205" height="235" rx="8" fill="#FAF7F2" stroke="#966C3B" stroke-width="1.5"/>
    <rect width="205" height="36" rx="8" fill="#A3432B"/>
    <text x="102" y="23" font-family="Liberation Serif, Georgia, serif" font-size="13" font-weight="bold" fill="#FCFBF7" text-anchor="middle">MATIN J : STRUCTURER</text>
    <text x="15" y="65" font-family="Liberation Sans, Arial, sans-serif" font-size="12" font-weight="bold" fill="#A3432B">• Taillages végétaux</text>
    <text x="25" y="82" font-family="Liberation Sans, Arial, sans-serif" font-size="11" fill="#5C5549">Éplucher, ciseler, parer</text>
    <text x="15" y="108" font-family="Liberation Sans, Arial, sans-serif" font-size="12" font-weight="bold" fill="#A3432B">• Pesées précises</text>
    <text x="25" y="125" font-family="Liberation Sans, Arial, sans-serif" font-size="11" fill="#5C5549">Mise en place en bols</text>
    <text x="15" y="151" font-family="Liberation Sans, Arial, sans-serif" font-size="12" font-weight="bold" fill="#A3432B">• Dresser la table</text>
    <text x="25" y="168" font-family="Liberation Sans, Arial, sans-serif" font-size="11" fill="#5C5549">Verres, couverts, carafes</text>
    <text x="15" y="194" font-family="Liberation Sans, Arial, sans-serif" font-size="12" font-weight="bold" fill="#A3432B">• Cuisine immaculée</text>
    <text x="25" y="211" font-family="Liberation Sans, Arial, sans-serif" font-size="11" fill="#5C5549">Évier vide, plonge faite</text>
  </g>

  <path d="M 478 200 L 505 200" stroke="#B45309" stroke-width="2.5"/>
  <polygon points="509,200 501,196 501,204" fill="#B45309"/>

  <!-- Étape 3 : H - 2 heures -->
  <g transform="translate(510, 85)">
    <rect width="205" height="235" rx="8" fill="#FAF7F2" stroke="#966C3B" stroke-width="1.5"/>
    <rect width="205" height="36" rx="8" fill="#B45309"/>
    <text x="102" y="23" font-family="Liberation Serif, Georgia, serif" font-size="13" font-weight="bold" fill="#FCFBF7" text-anchor="middle">H - 2 H : CONDITIONNER</text>
    <text x="15" y="65" font-family="Liberation Sans, Arial, sans-serif" font-size="12" font-weight="bold" fill="#B45309">• Sortir les viandes</text>
    <text x="25" y="82" font-family="Liberation Sans, Arial, sans-serif" font-size="11" fill="#5C5549">Tempérer à 20°C ambiant</text>
    <text x="15" y="108" font-family="Liberation Sans, Arial, sans-serif" font-size="12" font-weight="bold" fill="#B45309">• Chauffer les assiettes</text>
    <text x="25" y="125" font-family="Liberation Sans, Arial, sans-serif" font-size="11" fill="#5C5549">Four doux à 55°C</text>
    <text x="15" y="151" font-family="Liberation Sans, Arial, sans-serif" font-size="12" font-weight="bold" fill="#B45309">• Ouvrir &amp; Aérer les vins</text>
    <text x="25" y="168" font-family="Liberation Sans, Arial, sans-serif" font-size="11" fill="#5C5549">Oxygénation des arômes</text>
    <text x="15" y="194" font-family="Liberation Sans, Arial, sans-serif" font-size="12" font-weight="bold" fill="#B45309">• Pause de l'hôte</text>
    <text x="25" y="211" font-family="Liberation Sans, Arial, sans-serif" font-size="11" fill="#5C5549">Disponibilité d'esprit</text>
  </g>

  <path d="M 718 200 L 745 200" stroke="#5A6E54" stroke-width="2.5"/>
  <polygon points="749,200 741,196 741,204" fill="#5A6E54"/>

  <!-- Étape 4 : À l'arrivée -->
  <g transform="translate(750, 85)">
    <rect width="185" height="235" rx="8" fill="#F4F6F4" stroke="#5A6E54" stroke-width="2"/>
    <rect width="185" height="36" rx="8" fill="#5A6E54"/>
    <text x="92" y="23" font-family="Liberation Serif, Georgia, serif" font-size="13" font-weight="bold" fill="#FCFBF7" text-anchor="middle">L'ARRIVÉE : SAVOURER</text>
    <text x="12" y="65" font-family="Liberation Sans, Arial, sans-serif" font-size="12" font-weight="bold" fill="#5A6E54">✓ Hôte disponible</text>
    <text x="22" y="82" font-family="Liberation Sans, Arial, sans-serif" font-size="11" fill="#5C5549">Accueil chaleureux</text>
    <text x="12" y="108" font-family="Liberation Sans, Arial, sans-serif" font-size="12" font-weight="bold" fill="#5A6E54">✓ Zéro précipitation</text>
    <text x="22" y="125" font-family="Liberation Sans, Arial, sans-serif" font-size="11" fill="#5C5549">Tout est prêt et pesé</text>
    <text x="12" y="151" font-family="Liberation Sans, Arial, sans-serif" font-size="12" font-weight="bold" fill="#5A6E54">✓ Cuissons minute</text>
    <text x="22" y="168" font-family="Liberation Sans, Arial, sans-serif" font-size="11" fill="#5C5549">Saisie rapide en fonte</text>
    <text x="12" y="194" font-family="Liberation Sans, Arial, sans-serif" font-size="12" font-weight="bold" fill="#5A6E54">✓ Partage intégral</text>
    <text x="22" y="211" font-family="Liberation Sans, Arial, sans-serif" font-size="11" fill="#5C5549">Présence avec les convives</text>
  </g>
</svg>"""

for path, content in SVGS.items():
    ET.fromstring(content)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[OK VALID WARM SVG] {path}")
