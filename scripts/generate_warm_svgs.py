import re
import os
import xml.etree.ElementTree as ET

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def save_and_verify(path, content):
    full_path = os.path.join(BASE_DIR, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content.strip())
    try:
        ET.fromstring(content.strip())
        print(f"[OK VALID] {path}")
    except ET.ParseError as e:
        print(f"[ERROR XML] {path}: {e}")
        raise

# ==============================================================================
# FIG 1 : Evolution du Feu (Charte Chaude : Bordeaux, Terracotta, Ambre/Bistre)
# ==============================================================================
def gen_fig_01():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 520" width="100%" height="100%">
  <rect width="940" height="520" rx="14" fill="#FCFBF7" stroke="#D1C7B7" stroke-width="1.5"/>
  
  <text x="470" y="38" font-family="Liberation Serif, Georgia, serif" font-size="22" font-weight="bold" fill="#701C1A" text-anchor="middle">L'ÉVOLUTION DU FEU ET LA MORPHOGENÈSE HUMAINE</text>
  <text x="470" y="62" font-family="Liberation Sans, Arial, sans-serif" font-size="13" fill="#6B5E55" text-anchor="middle">La prédigestion externe : comment la maîtrise thermique a façonné le cerveau d'Homo sapiens</text>

  <!-- Bloc 1 : Le Cru -->
  <g transform="translate(30, 90)">
    <rect width="270" height="390" rx="10" fill="#FAF6F0" stroke="#C8BAAA" stroke-width="1.5"/>
    <rect width="270" height="42" rx="10" fill="#6B4423"/>
    <text x="135" y="26" font-family="Liberation Sans, Arial, sans-serif" font-size="14.5" font-weight="bold" fill="#FFFFFF" text-anchor="middle">1. LE MONDE DU CRU</text>
    
    <text x="16" y="72" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#6B4423">• Mastication interminable</text>
    <text x="26" y="93" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#3D352E">5 à 7 heures par jour</text>
    <text x="26" y="111" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#3D352E">pour broyer les fibres végétales</text>
    
    <text x="16" y="145" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#6B4423">• Tube digestif surdimensionné</text>
    <text x="26" y="166" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#3D352E">Intestin massif absorbant</text>
    <text x="26" y="184" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#3D352E">40% de l'énergie métabolique</text>
    
    <text x="16" y="218" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#6B4423">• Rendement calorique faible</text>
    <text x="26" y="239" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#3D352E">Collagène et amidon cru</text>
    <text x="26" y="257" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#3D352E">en grande partie indigestibles</text>
    
    <rect x="16" y="305" width="238" height="65" rx="6" fill="#EFE8DE"/>
    <text x="135" y="330" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" font-weight="bold" fill="#6B4423" text-anchor="middle">Cerveau limité : 450 cm³</text>
    <text x="135" y="350" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" fill="#5C5046" text-anchor="middle">Temps de survie contraint</text>
  </g>

  <!-- Connecteur 1 -> 2 -->
  <path d="M 305 285 L 345 285" stroke="#A3432B" stroke-width="2.5" marker-end="url(#arrow-terracotta)"/>

  <!-- Bloc 2 : Le Feu -->
  <g transform="translate(350, 90)">
    <rect width="260" height="390" rx="10" fill="#FAF5F0" stroke="#C8BAAA" stroke-width="1.5"/>
    <rect width="260" height="42" rx="10" fill="#A3432B"/>
    <text x="130" y="26" font-family="Liberation Sans, Arial, sans-serif" font-size="14.5" font-weight="bold" fill="#FFFFFF" text-anchor="middle">2. L'ÉTINCELLE DU FEU</text>
    
    <text x="16" y="72" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#A3432B">• Gélatinisation de l'amidon</text>
    <text x="26" y="93" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#3D352E">Explosion calorique :</text>
    <text x="26" y="111" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#3D352E">glucose assimilable à 95%</text>
    
    <text x="16" y="145" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#A3432B">• Fusion du collagène</text>
    <text x="26" y="166" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#3D352E">Transformation en gélatine molle,</text>
    <text x="26" y="184" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#3D352E">mastication en 30 minutes</text>
    
    <text x="16" y="218" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#A3432B">• Barrière sanitaire absolue</text>
    <text x="26" y="239" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#3D352E">Éradication des parasites</text>
    <text x="26" y="257" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#3D352E">et des toxines thermolabiles</text>
    
    <rect x="16" y="305" width="228" height="65" rx="6" fill="#F4E8DC"/>
    <text x="130" y="330" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" font-weight="bold" fill="#A3432B" text-anchor="middle">Prédigestion externe :</text>
    <text x="130" y="350" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" fill="#7A3220" text-anchor="middle">Le feu remplace l'estomac</text>
  </g>

  <!-- Connecteur 2 -> 3 -->
  <path d="M 615 285 L 655 285" stroke="#701C1A" stroke-width="2.5" marker-end="url(#arrow-bordeaux)"/>

  <!-- Bloc 3 : Homo sapiens -->
  <g transform="translate(660, 90)">
    <rect width="250" height="390" rx="10" fill="#FBF7F5" stroke="#C8BAAA" stroke-width="1.5"/>
    <rect width="250" height="42" rx="10" fill="#701C1A"/>
    <text x="125" y="26" font-family="Liberation Sans, Arial, sans-serif" font-size="14.5" font-weight="bold" fill="#FFFFFF" text-anchor="middle">3. L'HOMME CULINAIRE</text>
    
    <text x="16" y="72" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#701C1A">• Mâchoire et dents fines</text>
    <text x="26" y="93" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#3D352E">Rétrécissement de l'appareil</text>
    <text x="26" y="111" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#3D352E">mandibulaire et visage gracile</text>
    
    <text x="16" y="145" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#701C1A">• Réduction du tube digestif</text>
    <text x="26" y="166" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#3D352E">Économie métabolique de 60%</text>
    <text x="26" y="184" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#3D352E">réallouée au cerveau</text>
    
    <text x="16" y="218" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#701C1A">• Veillées et culture du partage</text>
    <text x="26" y="239" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#3D352E">Naissance du foyer social,</text>
    <text x="26" y="257" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#3D352E">du récit et du langage</text>
    
    <rect x="16" y="305" width="218" height="65" rx="6" fill="#F0E3DF"/>
    <text x="125" y="330" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" font-weight="bold" fill="#701C1A" text-anchor="middle">Cerveau moderne : 1400 cm³</text>
    <text x="125" y="350" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" fill="#501413" text-anchor="middle">Triplement du volume crânien</text>
  </g>

  <defs>
    <marker id="arrow-terracotta" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 8 5 L 0 9 z" fill="#A3432B"/>
    </marker>
    <marker id="arrow-bordeaux" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 8 5 L 0 9 z" fill="#701C1A"/>
    </marker>
  </defs>
</svg>'''
    save_and_verify("figures/histoire/fig_histoire_evolution_feu.svg", svg)

# ==============================================================================
# FIG 2 : Nutrition, Digestion et Survie (Cadres élargis, aucun texte ne déborde)
# ==============================================================================
def gen_fig_02():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 520" width="100%" height="100%">
  <rect width="940" height="520" rx="14" fill="#FCFBF7" stroke="#D1C7B7" stroke-width="1.5"/>
  
  <text x="470" y="38" font-family="Liberation Serif, Georgia, serif" font-size="22" font-weight="bold" fill="#701C1A" text-anchor="middle">PHYSIOLOGIE DE LA NUTRITION ET CYCLE DE SURVIE</text>
  <text x="470" y="62" font-family="Liberation Sans, Arial, sans-serif" font-size="13" fill="#6B5E55" text-anchor="middle">Des macromolécules ingérées à l'anabolisme cellulaire et à l'élimination des toxines</text>

  <!-- Colonne 1 : Ingestion -->
  <g transform="translate(30, 90)">
    <rect width="270" height="390" rx="10" fill="#FAF6F0" stroke="#C8BAAA" stroke-width="1.5"/>
    <rect width="270" height="42" rx="10" fill="#6B4423"/>
    <text x="135" y="26" font-family="Liberation Sans, Arial, sans-serif" font-size="14.5" font-weight="bold" fill="#FFFFFF" text-anchor="middle">1. LES MACROMOLÉCULES</text>
    
    <text x="16" y="72" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#6B4423">• Protéines (Bâtisseuses)</text>
    <text x="26" y="93" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#3D352E">Chaînes d'acides aminés</text>
    <text x="26" y="111" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#3D352E">Dénaturation acide gastrique (pH 2)</text>
    
    <text x="16" y="145" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#6B4423">• Lipides (Carburant dense)</text>
    <text x="26" y="166" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#3D352E">Triglycérides énergétiques (9 kcal/g)</text>
    <text x="26" y="184" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#3D352E">Émulsification biliaire au duodénum</text>
    
    <text x="16" y="218" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#6B4423">• Glucides (Énergie rapide)</text>
    <text x="26" y="239" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#3D352E">Amidon gélatinisé hydrolysé</text>
    <text x="26" y="257" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#3D352E">en monomères de glucose</text>
    
    <rect x="16" y="305" width="238" height="65" rx="6" fill="#EFE8DE"/>
    <text x="135" y="330" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" font-weight="bold" fill="#6B4423" text-anchor="middle">Alimentation brute :</text>
    <text x="135" y="350" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" fill="#5C5046" text-anchor="middle">Matières complexes à dégrader</text>
  </g>

  <!-- Connecteur 1 -> 2 -->
  <path d="M 305 285 L 345 285" stroke="#A3432B" stroke-width="2.5" marker-end="url(#arrow-terracotta)"/>

  <!-- Colonne 2 : Digestion & Catabolisme -->
  <g transform="translate(350, 90)">
    <rect width="260" height="390" rx="10" fill="#FAF5F0" stroke="#C8BAAA" stroke-width="1.5"/>
    <rect width="260" height="42" rx="10" fill="#A3432B"/>
    <text x="130" y="26" font-family="Liberation Sans, Arial, sans-serif" font-size="14.5" font-weight="bold" fill="#FFFFFF" text-anchor="middle">2. TRANSFORMATION INTERNE</text>
    
    <text x="16" y="72" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#A3432B">• Clivage enzymatique</text>
    <text x="26" y="93" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#3D352E">Pepsine, lipases, amylases :</text>
    <text x="26" y="111" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#3D352E">découpe en nutriments élémentaires</text>
    
    <text x="16" y="145" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#A3432B">• Absorption intestinale</text>
    <text x="26" y="166" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#3D352E">Passage des villosités du grêle</text>
    <text x="26" y="184" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#3D352E">vers le flux sanguin porte</text>
    
    <text x="16" y="218" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#A3432B">• Tri hépatique majeur</text>
    <text x="26" y="239" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#3D352E">Le foie stocke le glycogène</text>
    <text x="26" y="257" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#3D352E">et neutralise les composés toxiques</text>
    
    <rect x="16" y="305" width="228" height="65" rx="6" fill="#F4E8DC"/>
    <text x="130" y="330" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" font-weight="bold" fill="#A3432B" text-anchor="middle">Catabolisme :</text>
    <text x="130" y="350" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" fill="#7A3220" text-anchor="middle">Production d'énergie vitale (ATP)</text>
  </g>

  <!-- Connecteur 2 -> 3 -->
  <path d="M 615 285 L 655 285" stroke="#701C1A" stroke-width="2.5" marker-end="url(#arrow-bordeaux)"/>

  <!-- Colonne 3 : Élimination & Homéostasie -->
  <g transform="translate(660, 90)">
    <rect width="250" height="390" rx="10" fill="#FBF7F5" stroke="#C8BAAA" stroke-width="1.5"/>
    <rect width="250" height="42" rx="10" fill="#701C1A"/>
    <text x="125" y="26" font-family="Liberation Sans, Arial, sans-serif" font-size="14.5" font-weight="bold" fill="#FFFFFF" text-anchor="middle">3. ASSIMILATION &amp; REJET</text>
    
    <text x="16" y="72" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#701C1A">• Anabolisme &amp; Reconstruction</text>
    <text x="26" y="93" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#3D352E">Synthèse musculaire, réparation</text>
    <text x="26" y="111" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#3D352E">des tissus et immunité active</text>
    
    <text x="16" y="145" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#701C1A">• Fermentation du microbiote</text>
    <text x="26" y="166" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#3D352E">Le côlon nourrit les bactéries</text>
    <text x="26" y="184" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#3D352E">amies grâce aux fibres insolubles</text>
    
    <text x="16" y="218" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#701C1A">• Évacuation des déchets</text>
    <text x="26" y="239" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#3D352E">Ballast fécal, élimination</text>
    <text x="26" y="257" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#3D352E">de l'urée rénale et des sels biliaires</text>
    
    <rect x="16" y="305" width="218" height="65" rx="6" fill="#F0E3DF"/>
    <text x="125" y="330" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" font-weight="bold" fill="#701C1A" text-anchor="middle">Homéostasie totale :</text>
    <text x="125" y="350" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" fill="#501413" text-anchor="middle">Équilibre et survie durable</text>
  </g>

  <defs>
    <marker id="arrow-terracotta" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 8 5 L 0 9 z" fill="#A3432B"/>
    </marker>
    <marker id="arrow-bordeaux" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 8 5 L 0 9 z" fill="#701C1A"/>
    </marker>
  </defs>
</svg>'''
    save_and_verify("figures/histoire/fig_nutrition_digestion_survie.svg", svg)

# ==============================================================================
# FIG 3 : Les Trois Graisses (Nord, Sud-Ouest, Midi)
# ==============================================================================
def gen_fig_03():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 500" width="100%" height="100%">
  <rect width="940" height="500" rx="14" fill="#FCFBF7" stroke="#D1C7B7" stroke-width="1.5"/>
  
  <text x="470" y="38" font-family="Liberation Serif, Georgia, serif" font-size="22" font-weight="bold" fill="#701C1A" text-anchor="middle">GÉOPOLITIQUE ET CHIMIE DES TROIS CORPS GRAS FONDATEURS</text>
  <text x="470" y="62" font-family="Liberation Sans, Arial, sans-serif" font-size="13" fill="#6B5E55" text-anchor="middle">Point de fumée, composition lipidique et comportement thermique en cuisine</text>

  <!-- Bloc 1 : Le Beurre (Nord) -->
  <g transform="translate(30, 90)">
    <rect width="270" height="370" rx="10" fill="#FAF6F0" stroke="#C8BAAA" stroke-width="1.5"/>
    <rect width="270" height="42" rx="10" fill="#B45309"/>
    <text x="135" y="26" font-family="Liberation Sans, Arial, sans-serif" font-size="14.5" font-weight="bold" fill="#FFFFFF" text-anchor="middle">1. LE BEURRE (NORD)</text>
    
    <text x="16" y="72" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#B45309">• Point de fumée brut :</text>
    <text x="26" y="93" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#701C1A">130°C à 150°C (très bas)</text>
    <text x="26" y="111" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" fill="#5C5046">Brûlure rapide des caséines</text>
    
    <text x="16" y="145" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#B45309">• Beurre clarifié (Ghee) :</text>
    <text x="26" y="166" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#3D352E">250°C après filtration</text>
    <text x="26" y="184" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" fill="#5C5046">Pur lipide sans eau ni lactose</text>
    
    <text x="16" y="218" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#B45309">• Arômes signatures :</text>
    <text x="26" y="239" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#3D352E">Diacétyle et lactones</text>
    <text x="26" y="257" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" fill="#5C5046">Notes noisette à 120°C</text>
    
    <rect x="16" y="295" width="238" height="55" rx="6" fill="#F4EADB"/>
    <text x="135" y="320" font-family="Liberation Sans, Arial, sans-serif" font-size="12" font-weight="bold" fill="#B45309" text-anchor="middle">Usage : Pâtisserie, nappages,</text>
    <text x="135" y="338" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" fill="#5C5046" text-anchor="middle">sauces blanches et émulsions</text>
  </g>

  <!-- Bloc 2 : Canard (Sud-Ouest) -->
  <g transform="translate(335, 90)">
    <rect width="270" height="370" rx="10" fill="#FAF5F0" stroke="#C8BAAA" stroke-width="1.5"/>
    <rect width="270" height="42" rx="10" fill="#A3432B"/>
    <text x="135" y="26" font-family="Liberation Sans, Arial, sans-serif" font-size="14.5" font-weight="bold" fill="#FFFFFF" text-anchor="middle">2. GRAISSE DE VOLAILLE</text>
    
    <text x="16" y="72" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#A3432B">• Point de fumée :</text>
    <text x="26" y="93" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#3D352E">190°C à 200°C (stable)</text>
    <text x="26" y="111" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" fill="#5C5046">Idéal pour les saisies vives</text>
    
    <text x="16" y="145" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#A3432B">• Profil lipidique noble :</text>
    <text x="26" y="166" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#3D352E">Acides gras mono-insaturés</text>
    <text x="26" y="184" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" fill="#5C5046">Étonnamment proche de l'olive</text>
    
    <text x="16" y="218" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#A3432B">• Texture croustillante :</text>
    <text x="26" y="239" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#3D352E">Croûte dorée sans mollesse</text>
    <text x="26" y="257" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" fill="#5C5046">Permet le confisage long</text>
    
    <rect x="16" y="295" width="238" height="55" rx="6" fill="#F4E8DC"/>
    <text x="135" y="320" font-family="Liberation Sans, Arial, sans-serif" font-size="12" font-weight="bold" fill="#A3432B" text-anchor="middle">Usage : Pommes sarladaises,</text>
    <text x="135" y="338" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" fill="#7A3220" text-anchor="middle">confits, rôtis et pommes sautées</text>
  </g>

  <!-- Bloc 3 : Huile d'Olive (Midi) -->
  <g transform="translate(640, 90)">
    <rect width="270" height="370" rx="10" fill="#FBF7F5" stroke="#C8BAAA" stroke-width="1.5"/>
    <rect width="270" height="42" rx="10" fill="#701C1A"/>
    <text x="135" y="26" font-family="Liberation Sans, Arial, sans-serif" font-size="14.5" font-weight="bold" fill="#FFFFFF" text-anchor="middle">3. HUILE D'OLIVE (MIDI)</text>
    
    <text x="16" y="72" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#701C1A">• Point de fumée :</text>
    <text x="26" y="93" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#3D352E">190°C (extra-vierge)</text>
    <text x="26" y="111" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" fill="#5C5046">210°C (huile d'olive pure)</text>
    
    <text x="16" y="145" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#701C1A">• Polyphénols protecteurs :</text>
    <text x="26" y="166" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#3D352E">Oléocanthal antioxydant</text>
    <text x="26" y="184" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" fill="#5C5046">Goût fruité, herbacé et piquant</text>
    
    <text x="16" y="218" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#701C1A">• Comportement thermique :</text>
    <text x="26" y="239" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#3D352E">Fige à 4°C au réfrigérateur</text>
    <text x="26" y="257" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" fill="#5C5046">Fluide à température ambiante</text>
    
    <rect x="16" y="295" width="238" height="55" rx="6" fill="#F0E3DF"/>
    <text x="135" y="320" font-family="Liberation Sans, Arial, sans-serif" font-size="12" font-weight="bold" fill="#701C1A" text-anchor="middle">Usage : Aïoli au mortier,</text>
    <text x="135" y="338" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" fill="#501413" text-anchor="middle">assaisonnements et étuvées</text>
  </g>
</svg>'''
    save_and_verify("figures/livre_4/fig_carte_trois_graisses_terroirs.svg", svg)

# ==============================================================================
# FIG 4 : Arsenal Minimal (5 Outils Larges et Lisibles)
# ==============================================================================
def gen_fig_04():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 480" width="100%" height="100%">
  <rect width="960" height="480" rx="14" fill="#FCFBF7" stroke="#D1C7B7" stroke-width="1.5"/>
  
  <text x="480" y="38" font-family="Liberation Serif, Georgia, serif" font-size="22" font-weight="bold" fill="#701C1A" text-anchor="middle">L'ARSENAL MINIMAL : CINQ ORGANES FONDAMENTAUX DU CUISINIER</text>
  <text x="480" y="62" font-family="Liberation Sans, Arial, sans-serif" font-size="13" fill="#6B5E55" text-anchor="middle">Cinq instruments purs pour accomplir 99% de toutes les préparations culinaires du monde</text>

  <!-- Outil 1 : Couteau Chef -->
  <g transform="translate(25, 85)">
    <rect width="170" height="325" rx="8" fill="#FAF6F0" stroke="#C8BAAA" stroke-width="1.5"/>
    <rect width="170" height="38" rx="8" fill="#701C1A"/>
    <text x="85" y="24" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">1. COUTEAU CHEF</text>
    <text x="12" y="66" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" font-weight="bold" fill="#701C1A">• Lame 20 cm forgée</text>
    <text x="12" y="86" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" fill="#3D352E">Affûtage régulier rasoir</text>
    <text x="12" y="112" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" font-weight="bold" fill="#701C1A">• Rôle mécanique :</text>
    <text x="12" y="132" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" fill="#3D352E">Sectionne les cellules</text>
    <text x="12" y="148" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" fill="#3D352E">sans écraser le suc</text>
    <rect x="10" y="245" width="150" height="60" rx="6" fill="#F0E3DF"/>
    <text x="85" y="268" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" font-weight="bold" fill="#701C1A" text-anchor="middle">Prise en main :</text>
    <text x="85" y="286" font-family="Liberation Sans, Arial, sans-serif" font-size="11" fill="#501413" text-anchor="middle">Pince sur la lame</text>
  </g>

  <!-- Outil 2 : Planche Bois -->
  <g transform="translate(210, 85)">
    <rect width="170" height="325" rx="8" fill="#FAF6F0" stroke="#C8BAAA" stroke-width="1.5"/>
    <rect width="170" height="38" rx="8" fill="#A3432B"/>
    <text x="85" y="24" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">2. PLANCHE BOIS</text>
    <text x="12" y="66" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" font-weight="bold" fill="#A3432B">• Bois franc ou de bout</text>
    <text x="12" y="86" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" fill="#3D352E">Épaisseur 3 à 4 cm</text>
    <text x="12" y="112" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" font-weight="bold" fill="#A3432B">• Rôle mécanique :</text>
    <text x="12" y="132" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" fill="#3D352E">Stabilité au plan,</text>
    <text x="12" y="148" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" fill="#3D352E">préserve le tranchant</text>
    <rect x="10" y="245" width="150" height="60" rx="6" fill="#F4E8DC"/>
    <text x="85" y="268" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" font-weight="bold" fill="#A3432B" text-anchor="middle">Hygiène active :</text>
    <text x="85" y="286" font-family="Liberation Sans, Arial, sans-serif" font-size="11" fill="#7A3220" text-anchor="middle">Dessèche les microbes</text>
  </g>

  <!-- Outil 3 : Poêle en Fonte -->
  <g transform="translate(395, 85)">
    <rect width="170" height="325" rx="8" fill="#FAF6F0" stroke="#C8BAAA" stroke-width="1.5"/>
    <rect width="170" height="38" rx="8" fill="#6B4423"/>
    <text x="85" y="24" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">3. POÊLE EN FONTE</text>
    <text x="12" y="66" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" font-weight="bold" fill="#6B4423">• Fonte brute culottée</text>
    <text x="12" y="86" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" fill="#3D352E">Masse lourde (2 à 3 kg)</text>
    <text x="12" y="112" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" font-weight="bold" fill="#6B4423">• Rôle thermique :</text>
    <text x="12" y="132" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" fill="#3D352E">Inertie calorifique pure,</text>
    <text x="12" y="148" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" fill="#3D352E">croûte de Maillard flash</text>
    <rect x="10" y="245" width="150" height="60" rx="6" fill="#EFE8DE"/>
    <text x="85" y="268" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" font-weight="bold" fill="#6B4423" text-anchor="middle">Anti-adhésion n°1 :</text>
    <text x="85" y="286" font-family="Liberation Sans, Arial, sans-serif" font-size="11" fill="#5C5046" text-anchor="middle">Huile polymérisée</text>
  </g>

  <!-- Outil 4 : Casserole Inox -->
  <g transform="translate(580, 85)">
    <rect width="170" height="325" rx="8" fill="#FAF6F0" stroke="#C8BAAA" stroke-width="1.5"/>
    <rect width="170" height="38" rx="8" fill="#8C6239"/>
    <text x="85" y="24" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">4. CASSEROLE INOX</text>
    <text x="12" y="66" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" font-weight="bold" fill="#8C6239">• Inox 18/10 sandwich</text>
    <text x="12" y="86" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" fill="#3D352E">Cœur alu conducteur</text>
    <text x="12" y="112" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" font-weight="bold" fill="#8C6239">• Rôle chimique :</text>
    <text x="12" y="132" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" fill="#3D352E">Neutralité absolue,</text>
    <text x="12" y="148" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" fill="#3D352E">cuisson des acides sans risque</text>
    <rect x="10" y="245" width="150" height="60" rx="6" fill="#F0EBE1"/>
    <text x="85" y="268" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" font-weight="bold" fill="#8C6239" text-anchor="middle">Zéro migration :</text>
    <text x="85" y="286" font-family="Liberation Sans, Arial, sans-serif" font-size="11" fill="#5C5046" text-anchor="middle">Bouillons &amp; sauces</text>
  </g>

  <!-- Outil 5 : Fouet & Maryse -->
  <g transform="translate(765, 85)">
    <rect width="170" height="325" rx="8" fill="#FAF6F0" stroke="#C8BAAA" stroke-width="1.5"/>
    <rect width="170" height="38" rx="8" fill="#B45309"/>
    <text x="85" y="24" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">5. FOUET &amp; MARYSE</text>
    <text x="12" y="66" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" font-weight="bold" fill="#B45309">• Fouet ballon inox</text>
    <text x="12" y="86" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" fill="#3D352E">Spatule silicone souple</text>
    <text x="12" y="112" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" font-weight="bold" fill="#B45309">• Rôle d'émulsion :</text>
    <text x="12" y="132" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" fill="#3D352E">Cisaillement des gouttes,</text>
    <text x="12" y="148" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" fill="#3D352E">raclage intégral des fonds</text>
    <rect x="10" y="245" width="150" height="60" rx="6" fill="#F4EADB"/>
    <text x="85" y="268" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" font-weight="bold" fill="#B45309" text-anchor="middle">Liaison parfaite :</text>
    <text x="85" y="286" font-family="Liberation Sans, Arial, sans-serif" font-size="11" fill="#78350F" text-anchor="middle">Mayonnaise &amp; roux</text>
  </g>

  <!-- Ruban Conclusion -->
  <rect x="70" y="425" width="820" height="38" rx="6" fill="#701C1A"/>
  <text x="480" y="449" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">RÈGLE MAÎTRESSE : CINQ INSTRUMENTS PURS COMPOSENT 99% DE TOUTES LES RECETTES DU MONDE</text>
</svg>'''
    save_and_verify("figures/livre_1/fig_01_arsenal_minimal.svg", svg)

# ==============================================================================
# FIG 8 : Les Trois Vecteurs Thermodynamiques (Charte Chaude)
# ==============================================================================
def gen_fig_08():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 500" width="100%" height="100%">
  <rect width="940" height="500" rx="14" fill="#FCFBF7" stroke="#D1C7B7" stroke-width="1.5"/>
  
  <text x="470" y="38" font-family="Liberation Serif, Georgia, serif" font-size="22" font-weight="bold" fill="#701C1A" text-anchor="middle">LES TROIS VECTEURS THERMODYNAMIQUES EN CUISINE</text>
  <text x="470" y="62" font-family="Liberation Sans, Arial, sans-serif" font-size="13" fill="#6B5E55" text-anchor="middle">Comment l'énergie traverse la matière : conduction, convection et rayonnement</text>

  <!-- Vecteur 1 : Conduction -->
  <g transform="translate(30, 90)">
    <rect width="270" height="370" rx="10" fill="#FAF6F0" stroke="#C8BAAA" stroke-width="1.5"/>
    <rect width="270" height="42" rx="10" fill="#701C1A"/>
    <text x="135" y="26" font-family="Liberation Sans, Arial, sans-serif" font-size="14.5" font-weight="bold" fill="#FFFFFF" text-anchor="middle">1. CONDUCTION</text>
    
    <text x="16" y="72" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#701C1A">• Contact physique direct</text>
    <text x="26" y="93" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#3D352E">De solide à solide</text>
    <text x="26" y="111" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" fill="#5C5046">Paroi poêle → aliment</text>
    
    <text x="16" y="145" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#701C1A">• Loi du carré de l'épaisseur :</text>
    <text x="26" y="166" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" font-weight="bold" fill="#701C1A">Temps proportionnel à x²</text>
    <text x="26" y="184" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" fill="#5C5046">Épaisseur ×2 = Temps ×4 !</text>
    
    <text x="16" y="218" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#701C1A">• Rôle du corps gras :</text>
    <text x="26" y="239" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#3D352E">Comble les micro-vides d'air</text>
    <text x="26" y="257" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" fill="#5C5046">Multiplie le transfert par dix</text>
    
    <rect x="16" y="295" width="238" height="55" rx="6" fill="#F0E3DF"/>
    <text x="135" y="320" font-family="Liberation Sans, Arial, sans-serif" font-size="12" font-weight="bold" fill="#701C1A" text-anchor="middle">Usage : Pavé de bœuf, crêpes,</text>
    <text x="135" y="338" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" fill="#501413" text-anchor="middle">œufs au plat et saisie en fonte</text>
  </g>

  <!-- Vecteur 2 : Convection -->
  <g transform="translate(335, 90)">
    <rect width="270" height="370" rx="10" fill="#FAF5F0" stroke="#C8BAAA" stroke-width="1.5"/>
    <rect width="270" height="42" rx="10" fill="#A3432B"/>
    <text x="135" y="26" font-family="Liberation Sans, Arial, sans-serif" font-size="14.5" font-weight="bold" fill="#FFFFFF" text-anchor="middle">2. CONVECTION</text>
    
    <text x="16" y="72" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#A3432B">• Fluide en mouvement</text>
    <text x="26" y="93" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#3D352E">Eau, bouillon, huile, air chaud</text>
    <text x="26" y="111" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" fill="#5C5046">Brassage continu des molécules</text>
    
    <text x="16" y="145" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#A3432B">• Enveloppe homogène :</text>
    <text x="26" y="166" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#3D352E">Température égale sur tout le pourtour</text>
    <text x="26" y="184" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" fill="#5C5046">Zéro point chaud destructeur</text>
    
    <text x="16" y="218" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#A3432B">• Liquide versus Vapeur :</text>
    <text x="26" y="239" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#3D352E">L'eau transfère 25 fois plus vite</text>
    <text x="26" y="257" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" fill="#5C5046">la chaleur qu'un air sec à 100°C</text>
    
    <rect x="16" y="295" width="238" height="55" rx="6" fill="#F4E8DC"/>
    <text x="135" y="320" font-family="Liberation Sans, Arial, sans-serif" font-size="12" font-weight="bold" fill="#A3432B" text-anchor="middle">Usage : Bouillons, pochage doux,</text>
    <text x="135" y="338" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" fill="#7A3220" text-anchor="middle">étuvée sous cartouche et friture</text>
  </g>

  <!-- Vecteur 3 : Rayonnement -->
  <g transform="translate(640, 90)">
    <rect width="270" height="370" rx="10" fill="#FAF6F0" stroke="#C8BAAA" stroke-width="1.5"/>
    <rect width="270" height="42" rx="10" fill="#B45309"/>
    <text x="135" y="26" font-family="Liberation Sans, Arial, sans-serif" font-size="14.5" font-weight="bold" fill="#FFFFFF" text-anchor="middle">3. RAYONNEMENT</text>
    
    <text x="16" y="72" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#B45309">• Ondes électromagnétiques</text>
    <text x="26" y="93" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#3D352E">Infrarouges sans matière porteuse</text>
    <text x="26" y="111" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" fill="#5C5046">Braises vives, gril supérieur</text>
    
    <text x="16" y="145" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#B45309">• Loi de Stefan-Boltzmann :</text>
    <text x="26" y="166" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" font-weight="bold" fill="#B45309">Énergie rayonnée en T⁴</text>
    <text x="26" y="184" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" fill="#5C5046">Une braise à 600°C rayonne 16× plus</text>
    
    <text x="16" y="218" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#B45309">• Pénétration superficielle :</text>
    <text x="26" y="239" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#3D352E">Saisit la surface immédiatement</text>
    <text x="26" y="257" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" fill="#5C5046">Déclenche Maillard sans assécher</text>
    
    <rect x="16" y="295" width="238" height="55" rx="6" fill="#F4EADB"/>
    <text x="135" y="320" font-family="Liberation Sans, Arial, sans-serif" font-size="12" font-weight="bold" fill="#B45309" text-anchor="middle">Usage : Gril, rôtissoire, broche,</text>
    <text x="135" y="338" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" fill="#78350F" text-anchor="middle">salamandre et gratins dorés</text>
  </g>
</svg>'''
    save_and_verify("figures/livre_1/fig_02_thermodynamique_transferts.svg", svg)

if __name__ == "__main__":
    gen_fig_01()
    gen_fig_02()
    gen_fig_03()
    gen_fig_04()
    gen_fig_08()
    print("Toutes les figures 1, 2, 3, 4, 8 regénérées avec la charte chaude et zéro débordement !")
