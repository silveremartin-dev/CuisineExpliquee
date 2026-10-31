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
# FIG 1 : Evolution du Feu et Morphogenèse Humaine
# ==============================================================================
def gen_fig_01_feu():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 540" width="100%" height="100%">
  <rect width="920" height="540" rx="14" fill="#fcfbf7" stroke="#cbd5e1" stroke-width="2"/>
  
  <text x="460" y="42" font-family="Liberation Sans, Arial, sans-serif" font-size="24" font-weight="bold" fill="#701C1A" text-anchor="middle">L'ÉVOLUTION DU FEU ET LA MORPHOGENÈSE HUMAINE</text>
  <text x="460" y="70" font-family="Liberation Sans, Arial, sans-serif" font-size="15" fill="#64748b" text-anchor="middle">La prédigestion externe : comment la maîtrise thermique a façonné le cerveau d'Homo sapiens</text>

  <!-- Bloc 1 : Avant le Feu -->
  <g transform="translate(35, 100)">
    <rect width="265" height="400" rx="10" fill="#ffffff" stroke="#94a3b8" stroke-width="2"/>
    <rect width="265" height="45" rx="10" fill="#64748b"/>
    <text x="132" y="28" font-family="Liberation Sans, Arial, sans-serif" font-size="17" font-weight="bold" fill="#ffffff" text-anchor="middle">1. LE MONDE DU CRU</text>
    
    <text x="15" y="80" font-family="Liberation Sans, Arial, sans-serif" font-size="16" font-weight="bold" fill="#0f172a">• Mastication interminable</text>
    <text x="25" y="105" font-family="Liberation Sans, Arial, sans-serif" font-size="14" fill="#475569">5 à 7 heures par jour</text>
    <text x="25" y="125" font-family="Liberation Sans, Arial, sans-serif" font-size="14" fill="#475569">pour broyer les fibres dures</text>
    
    <text x="15" y="165" font-family="Liberation Sans, Arial, sans-serif" font-size="16" font-weight="bold" fill="#0f172a">• Métabolisme gastrique lourd</text>
    <text x="25" y="190" font-family="Liberation Sans, Arial, sans-serif" font-size="14" fill="#475569">Tube digestif géant</text>
    <text x="25" y="210" font-family="Liberation Sans, Arial, sans-serif" font-size="14" fill="#475569">absorbant 40% de l'énergie</text>
    
    <text x="15" y="250" font-family="Liberation Sans, Arial, sans-serif" font-size="16" font-weight="bold" fill="#0f172a">• Rendement calorique faible</text>
    <text x="25" y="275" font-family="Liberation Sans, Arial, sans-serif" font-size="14" fill="#475569">Collagène et amidons</text>
    <text x="25" y="295" font-family="Liberation Sans, Arial, sans-serif" font-size="14" fill="#475569">presque indigestibles crus</text>
    
    <rect x="15" y="330" width="235" height="50" rx="6" fill="#f1f5f9"/>
    <text x="132" y="352" font-family="Liberation Sans, Arial, sans-serif" font-size="14" font-weight="bold" fill="#475569" text-anchor="middle">Cerveau limité : 450 cm³</text>
    <text x="132" y="370" font-family="Liberation Sans, Arial, sans-serif" font-size="13" fill="#64748b" text-anchor="middle">(Capacités cognitives restreintes)</text>
  </g>

  <!-- Connecteur 1 -> 2 -->
  <path d="M 305 300 L 335 300" stroke="#dc2626" stroke-width="3" marker-end="url(#arrow-red)"/>

  <!-- Bloc 2 : L'Étincelle du Feu -->
  <g transform="translate(340, 100)">
    <rect width="250" height="400" rx="10" fill="#fff5f5" stroke="#dc2626" stroke-width="2"/>
    <rect width="250" height="45" rx="10" fill="#dc2626"/>
    <text x="125" y="28" font-family="Liberation Sans, Arial, sans-serif" font-size="17" font-weight="bold" fill="#ffffff" text-anchor="middle">2. LA RÉVOLUTION DU FEU</text>
    
    <text x="15" y="80" font-family="Liberation Sans, Arial, sans-serif" font-size="16" font-weight="bold" fill="#991b1b">• Gélatinisation amidon</text>
    <text x="25" y="105" font-family="Liberation Sans, Arial, sans-serif" font-size="14" fill="#7f1d1d">Explosion calorique</text>
    <text x="25" y="125" font-family="Liberation Sans, Arial, sans-serif" font-size="14" fill="#7f1d1d">assimilable à 95%</text>
    
    <text x="15" y="165" font-family="Liberation Sans, Arial, sans-serif" font-size="16" font-weight="bold" fill="#991b1b">• Dénaturation collagène</text>
    <text x="25" y="190" font-family="Liberation Sans, Arial, sans-serif" font-size="14" fill="#7f1d1d">Viande attendrie,</text>
    <text x="25" y="210" font-family="Liberation Sans, Arial, sans-serif" font-size="14" fill="#7f1d1d">mastication en 30 minutes</text>
    
    <text x="15" y="250" font-family="Liberation Sans, Arial, sans-serif" font-size="16" font-weight="bold" fill="#991b1b">• Éradication microbes</text>
    <text x="25" y="275" font-family="Liberation Sans, Arial, sans-serif" font-size="14" fill="#7f1d1d">Sécurité sanitaire totale</text>
    <text x="25" y="295" font-family="Liberation Sans, Arial, sans-serif" font-size="14" fill="#7f1d1d">et conservation accrue</text>
    
    <rect x="15" y="330" width="220" height="50" rx="6" fill="#fecaca"/>
    <text x="125" y="352" font-family="Liberation Sans, Arial, sans-serif" font-size="14" font-weight="bold" fill="#991b1b" text-anchor="middle">Prédigestion externe :</text>
    <text x="125" y="370" font-family="Liberation Sans, Arial, sans-serif" font-size="13" fill="#7f1d1d" text-anchor="middle">La chaleur remplace l'estomac</text>
  </g>

  <!-- Connecteur 2 -> 3 -->
  <path d="M 595 300 L 625 300" stroke="#16a34a" stroke-width="3" marker-end="url(#arrow-green)"/>

  <!-- Bloc 3 : Homo sapiens -->
  <g transform="translate(630, 100)">
    <rect width="255" height="400" rx="10" fill="#f0fdf4" stroke="#16a34a" stroke-width="2"/>
    <rect width="255" height="45" rx="10" fill="#16a34a"/>
    <text x="127" y="28" font-family="Liberation Sans, Arial, sans-serif" font-size="17" font-weight="bold" fill="#ffffff" text-anchor="middle">3. L'HOMME CULINAIRE</text>
    
    <text x="15" y="80" font-family="Liberation Sans, Arial, sans-serif" font-size="16" font-weight="bold" fill="#14532d">• Mâchoire et dents fines</text>
    <text x="25" y="105" font-family="Liberation Sans, Arial, sans-serif" font-size="14" fill="#166534">Rétrécissement de l'appareil</text>
    <text x="25" y="125" font-family="Liberation Sans, Arial, sans-serif" font-size="14" fill="#166534">mandibulaire et visage aplati</text>
    
    <text x="15" y="165" font-family="Liberation Sans, Arial, sans-serif" font-size="16" font-weight="bold" fill="#14532d">• Intestin réduit de 60%</text>
    <text x="25" y="190" font-family="Liberation Sans, Arial, sans-serif" font-size="14" fill="#166534">Économie métabolique</text>
    <text x="25" y="210" font-family="Liberation Sans, Arial, sans-serif" font-size="14" fill="#166534">immense et constante</text>
    
    <text x="15" y="250" font-family="Liberation Sans, Arial, sans-serif" font-size="16" font-weight="bold" fill="#14532d">• Éclosion de la culture</text>
    <text x="25" y="275" font-family="Liberation Sans, Arial, sans-serif" font-size="14" fill="#166534">Foyer, veillées nocturnes,</text>
    <text x="25" y="295" font-family="Liberation Sans, Arial, sans-serif" font-size="14" fill="#166534">partage social et langage</text>
    
    <rect x="15" y="330" width="225" height="50" rx="6" fill="#bbf7d0"/>
    <text x="127" y="352" font-family="Liberation Sans, Arial, sans-serif" font-size="14" font-weight="bold" fill="#14532d" text-anchor="middle">Cerveau moderne : 1400 cm³</text>
    <text x="127" y="370" font-family="Liberation Sans, Arial, sans-serif" font-size="13" fill="#166534" text-anchor="middle">(Triplement du volume crânien)</text>
  </g>

  <defs>
    <marker id="arrow-red" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 8 5 L 0 9 z" fill="#dc2626"/>
    </marker>
    <marker id="arrow-green" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 8 5 L 0 9 z" fill="#16a34a"/>
    </marker>
  </defs>
</svg>'''
    save_and_verify("figures/histoire/fig_histoire_evolution_feu.svg", svg)

# ==============================================================================
# FIG 3 : Carte et Terroirs des Trois Graisses Fondatrices
# ==============================================================================
def gen_fig_03_graisses():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 480" width="100%" height="100%">
  <rect width="920" height="480" rx="14" fill="#fcfbf7" stroke="#cbd5e1" stroke-width="2"/>
  
  <text x="460" y="42" font-family="Liberation Sans, Arial, sans-serif" font-size="24" font-weight="bold" fill="#701C1A" text-anchor="middle">GÉOPOLITIQUE ET CHIMIE DES TROIS CORPS GRAS FONDATEURS</text>
  <text x="460" y="70" font-family="Liberation Sans, Arial, sans-serif" font-size="15" fill="#64748b" text-anchor="middle">Point de fumée, composition lipidique et comportement thermique en cuisine</text>

  <!-- Bloc 1 : Le Beurre (Nord) -->
  <g transform="translate(35, 95)">
    <rect width="265" height="350" rx="10" fill="#fffbeb" stroke="#d97706" stroke-width="2"/>
    <rect width="265" height="45" rx="10" fill="#d97706"/>
    <text x="132" y="28" font-family="Liberation Sans, Arial, sans-serif" font-size="17" font-weight="bold" fill="#ffffff" text-anchor="middle">1. LE BEURRE (NORD)</text>
    
    <text x="15" y="75" font-family="Liberation Sans, Arial, sans-serif" font-size="15" font-weight="bold" fill="#92400e">• Point de fumée brut :</text>
    <text x="25" y="98" font-family="Liberation Sans, Arial, sans-serif" font-size="15" font-weight="bold" fill="#dc2626">130°C à 150°C (très bas)</text>
    <text x="25" y="118" font-family="Liberation Sans, Arial, sans-serif" font-size="13" fill="#64748b">Brûlure rapide des caséines</text>
    
    <text x="15" y="150" font-family="Liberation Sans, Arial, sans-serif" font-size="15" font-weight="bold" fill="#92400e">• Beurre clarifié (Ghee) :</text>
    <text x="25" y="173" font-family="Liberation Sans, Arial, sans-serif" font-size="15" font-weight="bold" fill="#16a34a">250°C (après filtration)</text>
    <text x="25" y="193" font-family="Liberation Sans, Arial, sans-serif" font-size="13" fill="#64748b">Pur lipide sans eau ni lactose</text>
    
    <text x="15" y="225" font-family="Liberation Sans, Arial, sans-serif" font-size="15" font-weight="bold" fill="#92400e">• Arômes signatures :</text>
    <text x="25" y="248" font-family="Liberation Sans, Arial, sans-serif" font-size="14" fill="#78350f">Diacétyle et lactones</text>
    <text x="25" y="268" font-family="Liberation Sans, Arial, sans-serif" font-size="13" fill="#64748b">Notes noisette à 120°C</text>
    
    <rect x="15" y="295" width="235" height="40" rx="6" fill="#fef3c7"/>
    <text x="132" y="320" font-family="Liberation Sans, Arial, sans-serif" font-size="14" font-weight="bold" fill="#92400e" text-anchor="middle">Usage : Pâtisserie, liaison, nappage</text>
  </g>

  <!-- Bloc 2 : Graisse de Canard (Sud-Ouest) -->
  <g transform="translate(325, 95)">
    <rect width="270" height="350" rx="10" fill="#fff7ed" stroke="#ea580c" stroke-width="2"/>
    <rect width="270" height="45" rx="10" fill="#ea580c"/>
    <text x="135" y="28" font-family="Liberation Sans, Arial, sans-serif" font-size="17" font-weight="bold" fill="#ffffff" text-anchor="middle">2. GRAISSE D'OIE / CANARD</text>
    
    <text x="15" y="75" font-family="Liberation Sans, Arial, sans-serif" font-size="15" font-weight="bold" fill="#9a3412">• Point de fumée :</text>
    <text x="25" y="98" font-family="Liberation Sans, Arial, sans-serif" font-size="15" font-weight="bold" fill="#16a34a">190°C à 200°C (stable)</text>
    <text x="25" y="118" font-family="Liberation Sans, Arial, sans-serif" font-size="13" fill="#64748b">Idéal pour saisies vives</text>
    
    <text x="15" y="150" font-family="Liberation Sans, Arial, sans-serif" font-size="15" font-weight="bold" fill="#9a3412">• Profil lipidique :</text>
    <text x="25" y="173" font-family="Liberation Sans, Arial, sans-serif" font-size="14" fill="#7c2d12">Riche en acides gras mono-insaturés</text>
    <text x="25" y="193" font-family="Liberation Sans, Arial, sans-serif" font-size="13" fill="#64748b">Étonnamment proche de l'olive</text>
    
    <text x="15" y="225" font-family="Liberation Sans, Arial, sans-serif" font-size="15" font-weight="bold" fill="#9a3412">• Texture &amp; Flaveur :</text>
    <text x="25" y="248" font-family="Liberation Sans, Arial, sans-serif" font-size="14" fill="#7c2d12">Croustillant inégalable</text>
    <text x="25" y="268" font-family="Liberation Sans, Arial, sans-serif" font-size="13" fill="#64748b">Permet le confisage longue durée</text>
    
    <rect x="15" y="295" width="240" height="40" rx="6" fill="#ffedd5"/>
    <text x="135" y="320" font-family="Liberation Sans, Arial, sans-serif" font-size="14" font-weight="bold" fill="#9a3412" text-anchor="middle">Usage : Sarladaises, confits, rôtis</text>
  </g>

  <!-- Bloc 3 : Huile d'Olive (Midi) -->
  <g transform="translate(620, 95)">
    <rect width="265" height="350" rx="10" fill="#f0fdf4" stroke="#16a34a" stroke-width="2"/>
    <rect width="265" height="45" rx="10" fill="#16a34a"/>
    <text x="132" y="28" font-family="Liberation Sans, Arial, sans-serif" font-size="17" font-weight="bold" fill="#ffffff" text-anchor="middle">3. HUILE D'OLIVE (MIDI)</text>
    
    <text x="15" y="75" font-family="Liberation Sans, Arial, sans-serif" font-size="15" font-weight="bold" fill="#14532d">• Point de fumée :</text>
    <text x="25" y="98" font-family="Liberation Sans, Arial, sans-serif" font-size="15" font-weight="bold" fill="#16a34a">190°C (extra-vierge)</text>
    <text x="25" y="118" font-family="Liberation Sans, Arial, sans-serif" font-size="13" fill="#64748b">210°C (huile d'olive raffinée)</text>
    
    <text x="15" y="150" font-family="Liberation Sans, Arial, sans-serif" font-size="15" font-weight="bold" fill="#14532d">• Richesse polyphénolique :</text>
    <text x="25" y="173" font-family="Liberation Sans, Arial, sans-serif" font-size="14" fill="#166534">Oléocanthal &amp; antioxydants</text>
    <text x="25" y="193" font-family="Liberation Sans, Arial, sans-serif" font-size="13" fill="#64748b">Goût fruité, herbacé et piquant</text>
    
    <text x="15" y="225" font-family="Liberation Sans, Arial, sans-serif" font-size="15" font-weight="bold" fill="#14532d">• Comportement au froid :</text>
    <text x="25" y="248" font-family="Liberation Sans, Arial, sans-serif" font-size="14" fill="#166534">Fige à 4°C au réfrigérateur</text>
    <text x="25" y="268" font-family="Liberation Sans, Arial, sans-serif" font-size="13" fill="#64748b">Reste fluide à température ambiante</text>
    
    <rect x="15" y="295" width="235" height="40" rx="6" fill="#dcfce7"/>
    <text x="132" y="320" font-family="Liberation Sans, Arial, sans-serif" font-size="14" font-weight="bold" fill="#14532d" text-anchor="middle">Usage : Aïoli, assaisonnement, étuvée</text>
  </g>
</svg>'''
    save_and_verify("figures/livre_4/fig_carte_trois_graisses_terroirs.svg", svg)

# ==============================================================================
# FIG 4 : Arsenal Minimal (5 outils)
# ==============================================================================
def gen_fig_04_arsenal():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 940 460" width="100%" height="100%">
  <rect width="940" height="460" rx="14" fill="#fcfbf7" stroke="#cbd5e1" stroke-width="2"/>
  
  <text x="470" y="40" font-family="Liberation Sans, Arial, sans-serif" font-size="24" font-weight="bold" fill="#701C1A" text-anchor="middle">L'ARSENAL MINIMAL : LES CINQ ORGANES FONDAMENTAUX</text>
  <text x="470" y="66" font-family="Liberation Sans, Arial, sans-serif" font-size="15" fill="#64748b" text-anchor="middle">Des outils indestructibles pour maîtriser 99% des transformations culinaires</text>

  <!-- Outil 1 : Couteau de Chef -->
  <g transform="translate(25, 90)">
    <rect width="168" height="300" rx="8" fill="#ffffff" stroke="#94a3b8" stroke-width="1.5"/>
    <rect width="168" height="38" rx="8" fill="#0f172a"/>
    <text x="84" y="25" font-family="Liberation Sans, Arial, sans-serif" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">1. COUTEAU CHEF</text>
    <text x="12" y="68" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#0f172a">• Lame 20 cm acier</text>
    <text x="12" y="90" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#475569">Affûtage rasoir régulier</text>
    <text x="12" y="118" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#0f172a">• Fonction physique :</text>
    <text x="12" y="140" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#475569">Section cellulaire nette</text>
    <text x="12" y="158" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#475569">sans écraser le suc</text>
    <rect x="10" y="235" width="148" height="50" rx="6" fill="#f1f5f9"/>
    <text x="84" y="256" font-family="Liberation Sans, Arial, sans-serif" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">Priorité absolue :</text>
    <text x="84" y="274" font-family="Liberation Sans, Arial, sans-serif" font-size="11" fill="#475569" text-anchor="middle">Prise en pince ferme</text>
  </g>

  <!-- Outil 2 : Planche Bois Massif -->
  <g transform="translate(205, 90)">
    <rect width="168" height="300" rx="8" fill="#ffffff" stroke="#94a3b8" stroke-width="1.5"/>
    <rect width="168" height="38" rx="8" fill="#78350f"/>
    <text x="84" y="25" font-family="Liberation Sans, Arial, sans-serif" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">2. PLANCHE BOIS</text>
    <text x="12" y="68" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#78350f">• Bois de bout / hêtre</text>
    <text x="12" y="90" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#475569">Épaisseur minimum 3 cm</text>
    <text x="12" y="118" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#78350f">• Fonction physique :</text>
    <text x="12" y="140" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#475569">Stabilité au plan de travail,</text>
    <text x="12" y="158" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#475569">préserve le tranchant</text>
    <rect x="10" y="235" width="148" height="50" rx="6" fill="#fef3c7"/>
    <text x="84" y="256" font-family="Liberation Sans, Arial, sans-serif" font-size="12" font-weight="bold" fill="#78350f" text-anchor="middle">Antibactérien naturel :</text>
    <text x="84" y="274" font-family="Liberation Sans, Arial, sans-serif" font-size="11" fill="#92400e" text-anchor="middle">Dessèche les microbes</text>
  </g>

  <!-- Outil 3 : Poêle en Fonte Brute -->
  <g transform="translate(385, 90)">
    <rect width="168" height="300" rx="8" fill="#ffffff" stroke="#94a3b8" stroke-width="1.5"/>
    <rect width="168" height="38" rx="8" fill="#dc2626"/>
    <text x="84" y="25" font-family="Liberation Sans, Arial, sans-serif" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">3. POÊLE FONTE</text>
    <text x="12" y="68" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#991b1b">• Fonte brute culottée</text>
    <text x="12" y="90" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#475569">Masse lourde (2 à 3 kg)</text>
    <text x="12" y="118" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#991b1b">• Fonction physique :</text>
    <text x="12" y="140" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#475569">Inertie thermique immense,</text>
    <text x="12" y="158" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#475569">croûte de Maillard flash</text>
    <rect x="10" y="235" width="148" height="50" rx="6" fill="#fee2e2"/>
    <text x="84" y="256" font-family="Liberation Sans, Arial, sans-serif" font-size="12" font-weight="bold" fill="#991b1b" text-anchor="middle">Anti-adhésion n°1 :</text>
    <text x="84" y="274" font-family="Liberation Sans, Arial, sans-serif" font-size="11" fill="#b91c1c" text-anchor="middle">Polymère d'huile pure</text>
  </g>

  <!-- Outil 4 : Casserole Inox Épaisse -->
  <g transform="translate(565, 90)">
    <rect width="168" height="300" rx="8" fill="#ffffff" stroke="#94a3b8" stroke-width="1.5"/>
    <rect width="168" height="38" rx="8" fill="#2563eb"/>
    <text x="84" y="25" font-family="Liberation Sans, Arial, sans-serif" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">4. CASSEROLE INOX</text>
    <text x="12" y="68" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#1e40af">• Inox 18/10 multicouche</text>
    <text x="12" y="90" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#475569">Fond sandwich aluminium</text>
    <text x="12" y="118" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#1e40af">• Fonction physique :</text>
    <text x="12" y="140" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#475569">Chimiquement inerte,</text>
    <text x="12" y="158" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#475569">cuisson acides sans danger</text>
    <rect x="10" y="235" width="148" height="50" rx="6" fill="#eff6ff"/>
    <text x="84" y="256" font-family="Liberation Sans, Arial, sans-serif" font-size="12" font-weight="bold" fill="#1e40af" text-anchor="middle">Zéro migration :</text>
    <text x="84" y="274" font-family="Liberation Sans, Arial, sans-serif" font-size="11" fill="#3b82f6" text-anchor="middle">Bouillons &amp; réductions</text>
  </g>

  <!-- Outil 5 : Fouet & Spatule Incurvée -->
  <g transform="translate(745, 90)">
    <rect width="168" height="300" rx="8" fill="#ffffff" stroke="#94a3b8" stroke-width="1.5"/>
    <rect width="168" height="38" rx="8" fill="#16a34a"/>
    <text x="84" y="25" font-family="Liberation Sans, Arial, sans-serif" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">5. FOUET &amp; MARYSE</text>
    <text x="12" y="68" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#15803d">• Fouet à fils inox fins</text>
    <text x="12" y="90" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#475569">Spatule souple silicone</text>
    <text x="12" y="118" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#15803d">• Fonction physique :</text>
    <text x="12" y="140" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#475569">Cisaillement des gouttes,</text>
    <text x="12" y="158" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#475569">raclage fond de poêle</text>
    <rect x="10" y="235" width="148" height="50" rx="6" fill="#f0fdf4"/>
    <text x="84" y="256" font-family="Liberation Sans, Arial, sans-serif" font-size="12" font-weight="bold" fill="#15803d" text-anchor="middle">Émulsion parfaite :</text>
    <text x="84" y="274" font-family="Liberation Sans, Arial, sans-serif" font-size="11" fill="#22c55e" text-anchor="middle">Mayonnaise &amp; sauces</text>
  </g>

  <!-- Ruban Conclusion -->
  <rect x="100" y="410" width="740" height="34" rx="6" fill="#701C1A"/>
  <text x="470" y="432" font-family="Liberation Sans, Arial, sans-serif" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">RÈGLE MAÎTRESSE : CINQ INSTRUMENTS PURS COMPOSENT 99% DE TOUTES LES RECETTES DU MONDE</text>
</svg>'''
    save_and_verify("figures/livre_1/fig_01_arsenal_minimal.svg", svg)

# ==============================================================================
# FIG 8 : Thermodynamique des Trois Vecteurs
# ==============================================================================
def gen_fig_08_thermo():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 480" width="100%" height="100%">
  <rect width="920" height="480" rx="14" fill="#fcfbf7" stroke="#cbd5e1" stroke-width="2"/>
  
  <text x="460" y="42" font-family="Liberation Sans, Arial, sans-serif" font-size="24" font-weight="bold" fill="#701C1A" text-anchor="middle">LES TROIS VECTEURS THERMODYNAMIQUES EN CUISINE</text>
  <text x="460" y="70" font-family="Liberation Sans, Arial, sans-serif" font-size="15" fill="#64748b" text-anchor="middle">Comment l'énergie traverse la matière : conduction, convection et rayonnement</text>

  <!-- Vecteur 1 : Conduction -->
  <g transform="translate(35, 95)">
    <rect width="265" height="350" rx="10" fill="#ffffff" stroke="#dc2626" stroke-width="2"/>
    <rect width="265" height="45" rx="10" fill="#dc2626"/>
    <text x="132" y="28" font-family="Liberation Sans, Arial, sans-serif" font-size="17" font-weight="bold" fill="#ffffff" text-anchor="middle">1. CONDUCTION</text>
    
    <text x="15" y="75" font-family="Liberation Sans, Arial, sans-serif" font-size="15" font-weight="bold" fill="#991b1b">• Contact physique direct</text>
    <text x="25" y="98" font-family="Liberation Sans, Arial, sans-serif" font-size="14" fill="#7f1d1d">De solide à solide</text>
    <text x="25" y="118" font-family="Liberation Sans, Arial, sans-serif" font-size="13" fill="#64748b">Paroi poêle → aliment</text>
    
    <text x="15" y="150" font-family="Liberation Sans, Arial, sans-serif" font-size="15" font-weight="bold" fill="#991b1b">• Loi du carré de l'épaisseur :</text>
    <text x="25" y="173" font-family="Liberation Sans, Arial, sans-serif" font-size="14" font-weight="bold" fill="#991b1b">Temps proportionnel à x²</text>
    <text x="25" y="193" font-family="Liberation Sans, Arial, sans-serif" font-size="13" fill="#64748b">Épaisseur ×2 = Temps ×4 !</text>
    
    <text x="15" y="225" font-family="Liberation Sans, Arial, sans-serif" font-size="15" font-weight="bold" fill="#991b1b">• Rôle de la matière grasse :</text>
    <text x="25" y="248" font-family="Liberation Sans, Arial, sans-serif" font-size="14" fill="#7f1d1d">Comble les micropores d'air</text>
    <text x="25" y="268" font-family="Liberation Sans, Arial, sans-serif" font-size="13" fill="#64748b">Multiplie le transfert par 10</text>
    
    <rect x="15" y="295" width="235" height="40" rx="6" fill="#fee2e2"/>
    <text x="132" y="320" font-family="Liberation Sans, Arial, sans-serif" font-size="14" font-weight="bold" fill="#991b1b" text-anchor="middle">Usage : Pavé de bœuf, crêpes, œufs</text>
  </g>

  <!-- Vecteur 2 : Convection -->
  <g transform="translate(325, 95)">
    <rect width="270" height="350" rx="10" fill="#ffffff" stroke="#2563eb" stroke-width="2"/>
    <rect width="270" height="45" rx="10" fill="#2563eb"/>
    <text x="135" y="28" font-family="Liberation Sans, Arial, sans-serif" font-size="17" font-weight="bold" fill="#ffffff" text-anchor="middle">2. CONVECTION</text>
    
    <text x="15" y="75" font-family="Liberation Sans, Arial, sans-serif" font-size="15" font-weight="bold" fill="#1e40af">• Fluide en mouvement</text>
    <text x="25" y="98" font-family="Liberation Sans, Arial, sans-serif" font-size="14" fill="#1e3a8a">Eau, bouillon, huile, air chaud</text>
    <text x="25" y="118" font-family="Liberation Sans, Arial, sans-serif" font-size="13" fill="#64748b">Brassage continu des molécules</text>
    
    <text x="15" y="150" font-family="Liberation Sans, Arial, sans-serif" font-size="15" font-weight="bold" fill="#1e40af">• Enveloppe homogène :</text>
    <text x="25" y="173" font-family="Liberation Sans, Arial, sans-serif" font-size="14" font-weight="bold" fill="#1e40af">Température égale partout</text>
    <text x="25" y="193" font-family="Liberation Sans, Arial, sans-serif" font-size="13" fill="#64748b">Zéro point chaud destructeur</text>
    
    <text x="15" y="225" font-family="Liberation Sans, Arial, sans-serif" font-size="15" font-weight="bold" fill="#1e40af">• Liquide vs Vapeur :</text>
    <text x="25" y="248" font-family="Liberation Sans, Arial, sans-serif" font-size="14" fill="#1e3a8a">L'eau transfère 25 fois plus vite</text>
    <text x="25" y="268" font-family="Liberation Sans, Arial, sans-serif" font-size="13" fill="#64748b">la chaleur qu'un air sec à 100°C</text>
    
    <rect x="15" y="295" width="240" height="40" rx="6" fill="#eff6ff"/>
    <text x="135" y="320" font-family="Liberation Sans, Arial, sans-serif" font-size="14" font-weight="bold" fill="#1e40af" text-anchor="middle">Usage : Bouillons, pochage, étuvée</text>
  </g>

  <!-- Vecteur 3 : Rayonnement -->
  <g transform="translate(620, 95)">
    <rect width="265" height="350" rx="10" fill="#ffffff" stroke="#d97706" stroke-width="2"/>
    <rect width="265" height="45" rx="10" fill="#d97706"/>
    <text x="132" y="28" font-family="Liberation Sans, Arial, sans-serif" font-size="17" font-weight="bold" fill="#ffffff" text-anchor="middle">3. RAYONNEMENT</text>
    
    <text x="15" y="75" font-family="Liberation Sans, Arial, sans-serif" font-size="15" font-weight="bold" fill="#92400e">• Ondes électromagnétiques</text>
    <text x="25" y="98" font-family="Liberation Sans, Arial, sans-serif" font-size="14" fill="#78350f">Infrarouges sans contact</text>
    <text x="25" y="118" font-family="Liberation Sans, Arial, sans-serif" font-size="13" fill="#64748b">Braises, gril supérieur du four</text>
    
    <text x="15" y="150" font-family="Liberation Sans, Arial, sans-serif" font-size="15" font-weight="bold" fill="#92400e">• Loi de Stefan-Boltzmann :</text>
    <text x="25" y="173" font-family="Liberation Sans, Arial, sans-serif" font-size="14" font-weight="bold" fill="#92400e">Énergie émise en T⁴</text>
    <text x="25" y="193" font-family="Liberation Sans, Arial, sans-serif" font-size="13" fill="#64748b">Une braise à 600°C rayonne 16× plus</text>
    
    <text x="15" y="225" font-family="Liberation Sans, Arial, sans-serif" font-size="15" font-weight="bold" fill="#92400e">• Pénétration millimétrique :</text>
    <text x="25" y="248" font-family="Liberation Sans, Arial, sans-serif" font-size="14" fill="#78350f">Saisit la surface immédiatement</text>
    <text x="25" y="268" font-family="Liberation Sans, Arial, sans-serif" font-size="13" fill="#64748b">Déclenche Maillard sans dessécher</text>
    
    <rect x="15" y="295" width="235" height="40" rx="6" fill="#fef3c7"/>
    <text x="132" y="320" font-family="Liberation Sans, Arial, sans-serif" font-size="14" font-weight="bold" fill="#92400e" text-anchor="middle">Usage : Gril, rôtissoire, salamandre</text>
  </g>
</svg>'''
    save_and_verify("figures/livre_1/fig_02_thermodynamique_transferts.svg", svg)

if __name__ == "__main__":
    gen_fig_01_feu()
    gen_fig_03_graisses()
    gen_fig_04_arsenal()
    gen_fig_08_thermo()
    print("Figures 1, 3, 4, 8 regénérées avec de grandes polices lisibles.")
