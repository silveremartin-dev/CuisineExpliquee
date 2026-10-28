# -*- coding: utf-8 -*-
"""
Générateur de figures vectorielles SVG pour LA CUISINE EXPLIQUÉE
Respecte la charte graphique chromatique officielle :
- Rouge / Énergie / Danger : #dc2626
- Bleu / Eau / Fluide : #2563eb
- Cyan / Froid / Cryoscopie : #0284c7
- Ambre / Gras / Goût : #d97706
- Vert / Acide / Équilibre / Santé : #16a34a
- Ardoise / Encre / Métal : #0f172a
- Gris / Neutre : #64748b, #cbd5e1, #f8fafc
"""

import os
import xml.etree.ElementTree as ET

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG_DIR = os.path.join(BASE_DIR, "figures")

def save_and_verify_svg(filepath, svg_content):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(svg_content.strip())
    # Validation XML
    try:
        ET.fromstring(svg_content.strip())
        print(f"[OK] Figure validée : {filepath}")
    except ET.ParseError as e:
        print(f"[ERREUR XML] {filepath} : {e}")
        raise

# ------------------------------------------------------------------------------
# 1. Fig 01 - Arsenal Minimal
# ------------------------------------------------------------------------------
def gen_fig_01():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" rx="16" fill="#f8fafc" stroke="#e2e8f0" stroke-width="2"/>
  <text x="400" y="42" font-family="Liberation Sans, Arial, sans-serif" font-size="20" font-weight="bold" fill="#0f172a" text-anchor="middle">L'ARSENAL MINIMAL : CINQ ORGANES FONDAMENTAUX DU CUISINIER</text>
  <text x="400" y="68" font-family="Liberation Sans, Arial, sans-serif" font-size="13" fill="#64748b" text-anchor="middle">La connaissance des lois physico-chimiques remplace l'amoncellement des gadgets.</text>

  <!-- Outil 1 : Le Couteau de Chef -->
  <g transform="translate(40, 100)">
    <rect width="130" height="280" rx="12" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="0" y="0" width="130" height="32" rx="12" fill="#0f172a"/>
    <text x="65" y="21" font-family="Liberation Sans, Arial, sans-serif" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">1. LE TRANCHANT</text>
    <path d="M 25 70 Q 75 75 105 130 L 35 130 Z" fill="#94a3b8" stroke="#334155" stroke-width="2"/>
    <rect x="25" y="130" width="16" height="75" rx="3" fill="#475569"/>
    <circle cx="33" cy="145" r="2.5" fill="#cbd5e1"/>
    <circle cx="33" cy="165" r="2.5" fill="#cbd5e1"/>
    <circle cx="33" cy="185" r="2.5" fill="#cbd5e1"/>
    <text x="65" y="225" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Couteau de chef</text>
    <text x="65" y="245" font-family="Liberation Sans, Arial, sans-serif" font-size="11" fill="#475569" text-anchor="middle">Lame forgée 20 cm</text>
    <text x="65" y="263" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#64748b" text-anchor="middle">Section cellulaire nette,</text>
    <text x="65" y="277" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#64748b" text-anchor="middle">zéro écrasement des jus.</text>
  </g>

  <!-- Outil 2 : Poêle Fonte Épaisse -->
  <g transform="translate(190, 100)">
    <rect width="130" height="280" rx="12" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="0" y="0" width="130" height="32" rx="12" fill="#dc2626"/>
    <text x="65" y="21" font-family="Liberation Sans, Arial, sans-serif" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">2. L'INERTIE</text>
    <ellipse cx="65" cy="115" rx="42" ry="24" fill="#334155" stroke="#0f172a" stroke-width="3"/>
    <ellipse cx="65" cy="112" rx="36" ry="19" fill="#1e293b"/>
    <path d="M 95 125 L 122 155" stroke="#0f172a" stroke-width="7" stroke-linecap="round"/>
    <text x="65" y="225" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Poêle lourde</text>
    <text x="65" y="245" font-family="Liberation Sans, Arial, sans-serif" font-size="11" fill="#475569" text-anchor="middle">Fonte ou Inox 5 plis</text>
    <text x="65" y="263" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#dc2626" text-anchor="middle">Tampon calorifique,</text>
    <text x="65" y="277" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#dc2626" text-anchor="middle">chaleur de Maillard constante.</text>
  </g>

  <!-- Outil 3 : Casserole Moyenne Fond Épais -->
  <g transform="translate(340, 100)">
    <rect width="130" height="280" rx="12" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="0" y="0" width="130" height="32" rx="12" fill="#2563eb"/>
    <text x="65" y="21" font-family="Liberation Sans, Arial, sans-serif" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">3. LE FLUIDE</text>
    <rect x="25" y="90" width="60" height="42" rx="4" fill="#cbd5e1" stroke="#475569" stroke-width="2"/>
    <ellipse cx="55" cy="90" rx="30" ry="10" fill="#93c5fd" stroke="#475569" stroke-width="2"/>
    <path d="M 85 96 L 120 90" stroke="#334155" stroke-width="5" stroke-linecap="round"/>
    <rect x="25" y="128" width="60" height="7" fill="#64748b"/>
    <text x="65" y="225" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Casserole 2-3 L</text>
    <text x="65" y="245" font-family="Liberation Sans, Arial, sans-serif" font-size="11" fill="#475569" text-anchor="middle">Fond sandwich épais</text>
    <text x="65" y="263" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#2563eb" text-anchor="middle">Convection liquide,</text>
    <text x="65" y="277" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#2563eb" text-anchor="middle">régulation frémissante.</text>
  </g>

  <!-- Outil 4 : Cul-de-poule et Fouet -->
  <g transform="translate(490, 100)">
    <rect width="130" height="280" rx="12" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="0" y="0" width="130" height="32" rx="12" fill="#d97706"/>
    <text x="65" y="21" font-family="Liberation Sans, Arial, sans-serif" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">4. LA CINÉTIQUE</text>
    <path d="M 20 90 A 45 45 0 0 0 110 90 Z" fill="#e2e8f0" stroke="#475569" stroke-width="2"/>
    <path d="M 75 60 L 55 110" stroke="#94a3b8" stroke-width="3"/>
    <ellipse cx="50" cy="100" rx="10" ry="16" fill="none" stroke="#d97706" stroke-width="1.8" transform="rotate(-25 50 100)"/>
    <text x="65" y="225" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Cul-de-poule inox</text>
    <text x="65" y="245" font-family="Liberation Sans, Arial, sans-serif" font-size="11" fill="#475569" text-anchor="middle">+ Fouet manuel ballon</text>
    <text x="65" y="263" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#d97706" text-anchor="middle">Émulsion moléculaire,</text>
    <text x="65" y="277" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#d97706" text-anchor="middle">foisonnement d'air.</text>
  </g>

  <!-- Outil 5 : Planche Bois Franc -->
  <g transform="translate(640, 100)">
    <rect width="120" height="280" rx="12" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="0" y="0" width="120" height="32" rx="12" fill="#16a34a"/>
    <text x="60" y="21" font-family="Liberation Sans, Arial, sans-serif" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">5. LE TERRAIN</text>
    <rect x="18" y="75" width="84" height="60" rx="4" fill="#fed7aa" stroke="#c2410c" stroke-width="2"/>
    <line x1="28" y1="85" x2="92" y2="85" stroke="#f97316" stroke-width="1"/>
    <line x1="28" y1="105" x2="92" y2="105" stroke="#f97316" stroke-width="1"/>
    <line x1="28" y1="125" x2="92" y2="125" stroke="#f97316" stroke-width="1"/>
    <text x="60" y="225" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Planche en bois</text>
    <text x="60" y="245" font-family="Liberation Sans, Arial, sans-serif" font-size="11" fill="#475569" text-anchor="middle">Bois de bout ou hêtre</text>
    <text x="60" y="263" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#16a34a" text-anchor="middle">Hygiène par dessiccation,</text>
    <text x="60" y="277" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#16a34a" text-anchor="middle">préservation du fil.</text>
  </g>

  <rect x="40" y="395" width="720" height="35" rx="8" fill="#eff6ff" stroke="#bfdbfe" stroke-width="1"/>
  <text x="400" y="417" font-family="Liberation Sans, Arial, sans-serif" font-size="12" fill="#1e40af" text-anchor="middle" font-weight="bold">Règle d'or : Maîtriser le gradient thermique et le contact physique surpasse tout investissement machine.</text>
</svg>"""
    save_and_verify_svg(os.path.join(FIG_DIR, "livre_1", "fig_01_arsenal_minimal.svg"), svg)

# ------------------------------------------------------------------------------
# 2. Fig Sécurité & Accidents : Frigo qui dégèle, Feu, Coupures, Brûlures
# ------------------------------------------------------------------------------
def gen_fig_securite():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" rx="16" fill="#f8fafc" stroke="#e2e8f0" stroke-width="2"/>
  <text x="400" y="36" font-family="Liberation Sans, Arial, sans-serif" font-size="19" font-weight="bold" fill="#0f172a" text-anchor="middle">SÉCURITÉ EN CUISINE : LES 4 ACCIDENTS MAJEURS ET LEURS PARADES</text>
  <text x="400" y="58" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" fill="#64748b" text-anchor="middle">Ce qu'il faut faire immédiatement et ce qu'il faut absolument proscrire.</text>

  <!-- Bloc 1 : Panne de Frigo / Congélateur -->
  <g transform="translate(30, 75)">
    <rect width="360" height="165" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="0" y="0" width="360" height="28" rx="10" fill="#0284c7"/>
    <text x="180" y="19" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">1. FRIGO / CONGÉLATEUR EN PANNE (DÉGEL)</text>
    
    <text x="12" y="46" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#15803d"><tspan font-weight="bold">✓ CE QU'IL FAUT FAIRE :</tspan></text>
    <text x="12" y="62" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#166534">• Laisser les portes fermées (maintien du froid pendant 4 à 6 heures).</text>
    <text x="12" y="77" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#166534">• Si température &gt; 4°C depuis &gt; 2h : cuire à cœur immédiatement viandes/poissons.</text>
    <text x="12" y="92" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#166534">• Les aliments cuits à cœur peuvent alors être recongelés sans risque.</text>
    
    <text x="12" y="112" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#dc2626"><tspan font-weight="bold">✗ INTERDICTION ABSOLUE :</tspan></text>
    <text x="12" y="128" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#b91c1c" font-weight="bold">• NE JAMAIS RECONGELER UN ALIMENT CRU DÉCONGELÉ !</text>
    <text x="12" y="143" font-family="Liberation Sans, Arial, sans-serif" font-size="9.5" fill="#7f1d1d">Les bactéries prolifèrent à vitesse x100 dans l'eau cellulaire libérée.</text>
  </g>

  <!-- Bloc 2 : Poêle en Feu (Huile embrasée) -->
  <g transform="translate(410, 75)">
    <rect width="360" height="165" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="0" y="0" width="360" height="28" rx="10" fill="#dc2626"/>
    <text x="180" y="19" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">2. POÊLE EN FEU (INCENDIE DE CORPS GRAS)</text>
    
    <text x="12" y="46" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#15803d"><tspan font-weight="bold">✓ CE QU'IL FAUT FAIRE (3 SECONDES) :</tspan></text>
    <text x="12" y="62" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#166534">• Couper immédiatement la source de chaleur (gaz/plaque).</text>
    <text x="12" y="77" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#166534">• Glisser un couvercle métallique ou plaque pour étouffer l'oxygène (O₂).</text>
    <text x="12" y="92" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#166534">• Laisser en place 15 min sans soulever pour éviter la ré-inflammation.</text>
    
    <text x="12" y="112" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#dc2626"><tspan font-weight="bold">✗ ERREUR MORTELLE :</tspan></text>
    <text x="12" y="128" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#b91c1c" font-weight="bold">• NE JAMAIS JETER D'EAU SUR L'HUILE EN FLAMMES !</text>
    <text x="12" y="143" font-family="Liberation Sans, Arial, sans-serif" font-size="9.5" fill="#7f1d1d">Vaporisation explosive (x1700) créant une boule de feu de 2 mètres.</text>
  </g>

  <!-- Bloc 3 : Brûlures Thermiques -->
  <g transform="translate(30, 255)">
    <rect width="360" height="175" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="0" y="0" width="360" height="28" rx="10" fill="#d97706"/>
    <text x="180" y="19" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">3. BRÛLURES PAR CONTACT OU CARAMEL</text>
    
    <text x="12" y="46" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#15803d"><tspan font-weight="bold">✓ LA RÈGLE DES « TROIS 15 » :</tspan></text>
    <text x="12" y="64" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#166534">• Eau tempérée à <tspan font-weight="bold">15°C</tspan> (pas d'eau glacée qui aggrave l'ischémie).</text>
    <text x="12" y="80" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#166534">• Pendant <tspan font-weight="bold">15 minutes</tspan> continues sans interruption.</text>
    <text x="12" y="96" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#166534">• À <tspan font-weight="bold">15 cm</tspan> sous le jet doux du robinet pour stopper la chaleur résiduelle.</text>
    
    <text x="12" y="120" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#dc2626"><tspan font-weight="bold">✗ GESTE ABSURDE À BANNIR :</tspan></text>
    <text x="12" y="138" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#b91c1c">• Mettre du beurre, de l'huile ou de la farine sur une brûlure !</text>
    <text x="12" y="153" font-family="Liberation Sans, Arial, sans-serif" font-size="9.5" fill="#7f1d1d">Le gras isole thermiquement et cuit les tissus profonds en retenant la chaleur.</text>
  </g>

  <!-- Bloc 4 : Coupures et Fil de Lame -->
  <g transform="translate(410, 255)">
    <rect width="360" height="175" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="0" y="0" width="360" height="28" rx="10" fill="#334155"/>
    <text x="180" y="19" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">4. GESTION DES COUPURES ET TENUE DE LAME</text>
    
    <text x="12" y="46" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#15803d"><tspan font-weight="bold">✓ PRÉVENTION PAR LA POSTURE :</tspan></text>
    <text x="12" y="64" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#166534">• Main guide : <tspan font-weight="bold">doigts repliés en « griffe de chat »</tspan>.</text>
    <text x="22" y="79" font-family="Liberation Sans, Arial, sans-serif" font-size="9.5" fill="#166534">La face plate de la lame glisse contre les phalanges sans toucher le fil.</text>
    <text x="12" y="96" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#166534">• Main active : pouce et index pincent la base de la lame (contrôle direct).</text>
    
    <text x="12" y="120" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#dc2626"><tspan font-weight="bold">✗ EN CAS DE COUPURE :</tspan></text>
    <text x="12" y="138" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#b91c1c">• Ne pas sucer la plaie (bouche remplie de bactéries pathogènes).</text>
    <text x="12" y="153" font-family="Liberation Sans, Arial, sans-serif" font-size="9.5" fill="#7f1d1d">Laver à l'eau courante, désinfecter et comprimer fort 5 min avec un linge propre.</text>
  </g>
</svg>"""
    save_and_verify_svg(os.path.join(FIG_DIR, "livre_1", "fig_securite_accidents_frigo_feu.svg"), svg)

# ------------------------------------------------------------------------------
# 3. Fig Les Secrets de l'Assiette 3 Étoiles
# ------------------------------------------------------------------------------
def gen_fig_3_etoiles():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" rx="16" fill="#f8fafc" stroke="#e2e8f0" stroke-width="2"/>
  <text x="400" y="36" font-family="Liberation Sans, Arial, sans-serif" font-size="19" font-weight="bold" fill="#0f172a" text-anchor="middle">L'ANATOMIE D'UNE ASSIETTE TROIS ÉTOILES</text>
  <text x="400" y="58" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" fill="#64748b" text-anchor="middle">Où sont les vraies astuces au-delà du cérémonial et du décor : ce qu'il y a dans l'assiette.</text>

  <!-- Assiette Centrale stylisée -->
  <g transform="translate(140, 240)">
    <circle cx="0" cy="0" r="115" fill="#ffffff" stroke="#cbd5e1" stroke-width="4"/>
    <circle cx="0" cy="0" r="85" fill="#fffbeb" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="4,3"/>
    
    <!-- Cordon de Sauce Glacée (Ambre) -->
    <path d="M -50 35 C -20 65 30 55 55 20 C 65 -15 25 -45 -15 -35 C -45 -25 -65 10 -50 35 Z" fill="#d97706" opacity="0.3"/>
    
    <!-- Pièce principale dorée (Maillard) -->
    <rect x="-35" y="-20" width="70" height="40" rx="6" fill="#fde68a" stroke="#d97706" stroke-width="2"/>
    <line x1="-30" y1="-10" x2="30" y2="-10" stroke="#b45309" stroke-width="1.5"/>
    <line x1="-30" y1="0" x2="30" y2="0" stroke="#b45309" stroke-width="1.5"/>
    <line x1="-30" y1="10" x2="30" y2="10" stroke="#b45309" stroke-width="1.5"/>
    
    <!-- Éléments texturaux (croustillant et herbe fraîche) -->
    <circle cx="-15" cy="-28" r="4" fill="#16a34a"/>
    <circle cx="15" cy="-28" r="4" fill="#16a34a"/>
    <polygon points="0,-32 -4,-22 4,-22" fill="#ef4444"/>

    <text x="0" y="5" font-family="Liberation Sans, Arial, sans-serif" font-size="11" font-weight="bold" fill="#78350f" text-anchor="middle">BOUCHÉE</text>
    <text x="0" y="19" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#92400e" text-anchor="middle">PARFAITE</text>
  </g>

  <!-- Les 5 Vérités Physiques du Grand Restaurant -->
  <g transform="translate(300, 85)">
    <!-- Vérité 1 : Le Sel Multi-Strate -->
    <rect width="470" height="60" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1"/>
    <rect x="0" y="0" width="8" height="60" rx="4" fill="#2563eb"/>
    <text x="20" y="22" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" font-weight="bold" fill="#1e40af">1. LE SEL MULTI-STRATE (DYNAMIQUE OSMOTIQUE)</text>
    <text x="20" y="38" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#334155">L'amateur sale à la fin dans l'assiette. Le 3 étoiles sale à chaque transformation :</text>
    <text x="20" y="52" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#64748b">dans l'eau de pochage, dans la marinade, dans la réduction et en fleur de sel croustillante.</text>

    <!-- Vérité 2 : L'Acide Invisible -->
    <rect y="70" width="470" height="60" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1"/>
    <rect y="70" x="0" width="8" height="60" rx="4" fill="#16a34a"/>
    <text x="20" y="92" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" font-weight="bold" fill="#166534">2. L'ACIDE INVISIBLE (« LE COUP DE CISEAU »)</text>
    <text x="20" y="108" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#334155">Un filet de vinaigre vieux, de jus d'agrume ou de vin réduit dans les sauces riches :</text>
    <text x="20" y="122" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#15803d">il ne donne aucun goût aigre, mais neutralise la lourdeur du gras et excite la salivation.</text>

    <!-- Vérité 3 : La Glace de Viande & l'Umami Pur -->
    <rect y="140" width="470" height="60" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1"/>
    <rect y="140" x="0" width="8" height="60" rx="4" fill="#d97706"/>
    <text x="20" y="162" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" font-weight="bold" fill="#92400e">3. LA CONCENTRATION DES SUCS &amp; COLLAGÈNE HYDROLYSÉ</text>
    <text x="20" y="178" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#334155">Des carcasses rôties mijotées 12h puis réduites par dix : le collagène devient</text>
    <text x="20" y="192" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#b45309">une gélatine naturelle brillante qui tapisse les récepteurs umami du palais sans farine.</text>

    <!-- Vérité 4 : Le Tamisage au Chinois Étamine -->
    <rect y="210" width="470" height="60" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1"/>
    <rect y="210" x="0" width="8" height="60" rx="4" fill="#64748b"/>
    <text x="20" y="232" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" font-weight="bold" fill="#334155">4. LA SUPPRESSION DES ASPÉRITÉS (TOUCHER VELOURS)</text>
    <text x="20" y="248" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#334155">Chaque purée, coulis ou jus est passé à travers une maille métallique serrée :</text>
    <text x="20" y="262" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#475569">zéro fibre, zéro grumeau. La langue glisse sur une nappe hydrodynamique parfaite.</text>

    <!-- Vérité 5 : L'Architecture Poly-Texturale -->
    <rect y="280" width="470" height="60" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1"/>
    <rect y="280" x="0" width="8" height="60" rx="4" fill="#dc2626"/>
    <text x="20" y="302" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" font-weight="bold" fill="#991b1b">5. LE QUATUOR TEXTURAL DANS UNE SEULE BOUCHÉE</text>
    <text x="20" y="318" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#334155">Jamais de plat monotone : <tspan font-weight="bold">Croustillant</tspan> (croûte) + <tspan font-weight="bold">Fondant</tspan> (cœur cuit à cœur)</text>
    <text x="20" y="332" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#dc2626">+ <tspan font-weight="bold">Soyeux</tspan> (sauce montée au beurre) + <tspan font-weight="bold">Croquant</tspan> (élément végétal vif cru/al dente).</text>
  </g>
</svg>"""
    save_and_verify_svg(os.path.join(FIG_DIR, "livre_1", "fig_secrets_assiette_3_etoiles.svg"), svg)

# ------------------------------------------------------------------------------
# 4. Fig Additifs Industriels, Bliss Point et Psychologie des Courses
# ------------------------------------------------------------------------------
def gen_fig_additifs_courses():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" rx="16" fill="#f8fafc" stroke="#e2e8f0" stroke-width="2"/>
  <text x="400" y="36" font-family="Liberation Sans, Arial, sans-serif" font-size="19" font-weight="bold" fill="#0f172a" text-anchor="middle">L'INGÉNIERIE INDUSTRIELLE : LE BLISS POINT ET LES ADDITIFS E</text>
  <text x="400" y="58" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" fill="#64748b" text-anchor="middle">Démystifier les listes d'ingrédients, repérer les vrais poisons et déjouer le piège des courses.</text>

  <!-- Panneau Gauche : Le Triangle du Bliss Point -->
  <g transform="translate(40, 75)">
    <rect width="345" height="345" rx="12" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="0" y="0" width="345" height="30" rx="12" fill="#dc2626"/>
    <text x="172" y="20" font-family="Liberation Sans, Arial, sans-serif" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">1. LE BLISS POINT : COURT-CIRCUITER LA SATIÉTÉ</text>

    <!-- Triangle équilatéral central -->
    <polygon points="172,60 70,195 275,195" fill="#fef2f2" stroke="#dc2626" stroke-width="2"/>
    
    <!-- Sommets -->
    <circle cx="172" cy="60" r="14" fill="#dc2626"/>
    <text x="172" y="64" font-family="Liberation Sans, Arial, sans-serif" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">SUCRE</text>

    <circle cx="70" cy="195" r="14" fill="#d97706"/>
    <text x="70" y="199" font-family="Liberation Sans, Arial, sans-serif" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">GRAS</text>

    <circle cx="275" cy="195" r="14" fill="#2563eb"/>
    <text x="275" y="199" font-family="Liberation Sans, Arial, sans-serif" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">SEL</text>

    <text x="172" y="140" font-family="Liberation Sans, Arial, sans-serif" font-size="11" font-weight="bold" fill="#991b1b" text-anchor="middle">DOPAMINE</text>
    <text x="172" y="155" font-family="Liberation Sans, Arial, sans-serif" font-size="9" fill="#7f1d1d" text-anchor="middle">(Addiction sensorielle)</text>

    <text x="20" y="235" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#334155"><tspan font-weight="bold">• L'illusion du craquant :</tspan> Les industriels calibrent</text>
    <text x="30" y="250" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#334155">la résistance mécanique (son acoustique de rupture à 300 Hz)</text>
    <text x="30" y="265" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#334155">pour déclencher une fausse sensation de fraîcheur.</text>
    <text x="20" y="288" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#334155"><tspan font-weight="bold">• Rétention d'eau :</tspan> Les polyphosphates retiennent jusqu'à</text>
    <text x="30" y="303" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#334155">30% d'eau ajoutée dans les jambons bas de gamme.</text>
    <text x="20" y="325" font-family="Liberation Sans, Arial, sans-serif" font-size="10" font-weight="bold" fill="#b91c1c">Résultat : Vous payez de l'eau au prix de la viande.</text>
  </g>

  <!-- Panneau Droit : Le Vrai/Faux des Additifs E et les Courses -->
  <g transform="translate(415, 75)">
    <rect width="345" height="345" rx="12" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="0" y="0" width="345" height="30" rx="12" fill="#2563eb"/>
    <text x="172" y="20" font-family="Liberation Sans, Arial, sans-serif" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">2. ADDITIFS E : NATURELS vs RISQUES RÉELS</text>

    <!-- Inoffensifs -->
    <rect x="15" y="45" width="315" height="85" rx="6" fill="#f0fdf4" stroke="#86efac" stroke-width="1"/>
    <text x="25" y="63" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" font-weight="bold" fill="#166534">✓ TOTALEMENT NATURELS &amp; INOFFENSIFS :</text>
    <text x="25" y="80" font-family="Liberation Sans, Arial, sans-serif" font-size="9.5" fill="#14532d">• <tspan font-weight="bold">E300</tspan> : Vitamine C (acide ascorbique, antioxydant).</text>
    <text x="25" y="95" font-family="Liberation Sans, Arial, sans-serif" font-size="9.5" fill="#14532d">• <tspan font-weight="bold">E330</tspan> : Acide citrique (présent dans le citron).</text>
    <text x="25" y="110" font-family="Liberation Sans, Arial, sans-serif" font-size="9.5" fill="#14532d">• <tspan font-weight="bold">E322</tspan> (Lécithine de soja/œuf) | <tspan font-weight="bold">E440</tspan> (Pectine de pomme).</text>

    <!-- Dangereux -->
    <rect x="15" y="140" width="315" height="100" rx="6" fill="#fef2f2" stroke="#fca5a5" stroke-width="1"/>
    <text x="25" y="158" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" font-weight="bold" fill="#991b1b">✗ LES VRAIS RISQUES À ÉVITER :</text>
    <text x="25" y="175" font-family="Liberation Sans, Arial, sans-serif" font-size="9.5" fill="#7f1d1d">• <tspan font-weight="bold">E250 (Nitrite de sodium) :</tspan> Forme des nitrosamines</text>
    <text x="35" y="188" font-family="Liberation Sans, Arial, sans-serif" font-size="9" fill="#7f1d1d">cancérogènes dans l'estomac (charcuteries roses industrielles).</text>
    <text x="25" y="203" font-family="Liberation Sans, Arial, sans-serif" font-size="9.5" fill="#7f1d1d">• <tspan font-weight="bold">E150d :</tspan> Caramel au sulfite d'ammonium (présence de 4-MEI).</text>
    <text x="25" y="218" font-family="Liberation Sans, Arial, sans-serif" font-size="9.5" fill="#7f1d1d">• <tspan font-weight="bold">E466 / E433 :</tspan> Émulsifiants synthétiques qui dégradent</text>
    <text x="35" y="231" font-family="Liberation Sans, Arial, sans-serif" font-size="9" fill="#7f1d1d">le mucus intestinal et favorisent l'inflammation colique.</text>

    <!-- La règle d'or des courses -->
    <rect x="15" y="250" width="315" height="80" rx="6" fill="#fffbeb" stroke="#fcd34d" stroke-width="1"/>
    <text x="25" y="268" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" font-weight="bold" fill="#92400e">LE PIÈGE NEUROLOGIQUE DES COURSES :</text>
    <text x="25" y="285" font-family="Liberation Sans, Arial, sans-serif" font-size="9.5" fill="#78350f">• <tspan font-weight="bold">Courses le ventre vide :</tspan> Pic de ghréline qui pousse</text>
    <text x="35" y="298" font-family="Liberation Sans, Arial, sans-serif" font-size="9" fill="#78350f">le cerveau vers les produits ultra-transformés et les fringales.</text>
    <text x="25" y="315" font-family="Liberation Sans, Arial, sans-serif" font-size="9.5" fill="#15803d" font-weight="bold">Règle d'or : Faire ses courses le ventre plein avec une liste fermée !</text>
  </g>
</svg>"""
    save_and_verify_svg(os.path.join(FIG_DIR, "livre_1", "fig_additifs_bliss_point_courses.svg"), svg)

# ------------------------------------------------------------------------------
# 5. Fig Recettes Fondatrices : Fromage Maison & Glace Cryoscopique
# ------------------------------------------------------------------------------
def gen_fig_fromage_glace():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" rx="16" fill="#f8fafc" stroke="#e2e8f0" stroke-width="2"/>
  <text x="400" y="36" font-family="Liberation Sans, Arial, sans-serif" font-size="19" font-weight="bold" fill="#0f172a" text-anchor="middle">DEUX RECETTES FONDATRICES PAR LES PRINCIPES PREMIERS</text>
  <text x="400" y="58" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" fill="#64748b" text-anchor="middle">Fabriquer du fromage frais et de la glace onctueuse avec zéro machine sophistiquée.</text>

  <!-- Volet Gauche : Le Fromage Frais Maison (Précipitation Acide) -->
  <g transform="translate(40, 80)">
    <rect width="345" height="340" rx="12" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="0" y="0" width="345" height="30" rx="12" fill="#16a34a"/>
    <text x="172" y="20" font-family="Liberation Sans, Arial, sans-serif" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">LE FROMAGE FRAIS EN 15 MINUTES (SANS PRÉSURE)</text>

    <!-- Schéma Caséines qui s'agrègent -->
    <rect x="25" y="45" width="295" height="85" rx="6" fill="#f0fdf4" stroke="#86efac" stroke-width="1"/>
    <circle cx="70" cy="85" r="22" fill="#ffffff" stroke="#3b82f6" stroke-width="2"/>
    <text x="70" y="89" font-family="Liberation Sans, Arial, sans-serif" font-size="9" fill="#1e40af" text-anchor="middle">Caséines</text>
    
    <path d="M 105 85 L 140 85" stroke="#16a34a" stroke-width="2.5" stroke-linecap="round"/>
    <polygon points="145,85 137,81 137,89" fill="#16a34a"/>
    <text x="122" y="77" font-family="Liberation Sans, Arial, sans-serif" font-size="9.5" fill="#15803d" font-weight="bold" text-anchor="middle">+ H⁺ (Citron)</text>

    <path d="M 160 70 L 180 95 L 200 70 L 220 95 L 240 70" fill="none" stroke="#15803d" stroke-width="2.5"/>
    <text x="265" y="82" font-family="Liberation Sans, Arial, sans-serif" font-size="9.5" font-weight="bold" fill="#14532d">Caillé dense</text>
    <text x="265" y="96" font-family="Liberation Sans, Arial, sans-serif" font-size="9" fill="#15803d">+ Petit-lait</text>

    <text x="20" y="150" font-family="Liberation Sans, Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a">Ingrédients :</text>
    <text x="20" y="168" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#334155">1 litre de lait entier (cru ou frais pasteurisé) + 3 c.à.s de citron ou vinaigre.</text>

    <text x="20" y="194" font-family="Liberation Sans, Arial, sans-serif" font-size="11" font-weight="bold" fill="#166534">Protocole physique :</text>
    <text x="20" y="212" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#14532d">1. Chauffer le lait à <tspan font-weight="bold">82°C</tspan> (vapeur dense sans gros bouillons).</text>
    <text x="20" y="228" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#14532d">2. Couper le feu, verser le jus de citron, remuer une fois.</text>
    <text x="20" y="244" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#14532d">3. Laisser reposer 10 min : le caillé blanc floconne dans un liquide jaune.</text>
    <text x="20" y="260" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#14532d">4. Verser dans une passoire garnie d'un torchon propre (étamine).</text>
    <text x="20" y="278" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#15803d" font-weight="bold">Résultat : Faisselle soyeuse (20 min d'égouttage) ou Paneer ferme (pressé 1h).</text>
  </g>

  <!-- Volet Droit : La Glace Cryoscopique Sel / Glaçons -->
  <g transform="translate(415, 80)">
    <rect width="345" height="340" rx="12" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="0" y="0" width="345" height="30" rx="12" fill="#0284c7"/>
    <text x="172" y="20" font-family="Liberation Sans, Arial, sans-serif" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">LA GLACE SANS MACHINE PAR LE SEL (-18°C)</text>

    <!-- Schéma Bain de Sel Cryoscopique -->
    <rect x="25" y="45" width="295" height="85" rx="6" fill="#f0f9ff" stroke="#7dd3fc" stroke-width="1"/>
    <circle cx="172" cy="88" r="32" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>
    <text x="172" y="85" font-family="Liberation Sans, Arial, sans-serif" font-size="9.5" fill="#0369a1" text-anchor="middle">Grand bol :</text>
    <text x="172" y="98" font-family="Liberation Sans, Arial, sans-serif" font-size="9" fill="#0284c7" font-weight="bold" text-anchor="middle">Glace + Sel (-18°C)</text>
    
    <circle cx="172" cy="88" r="16" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
    <text x="172" y="91" font-family="Liberation Sans, Arial, sans-serif" font-size="7.5" fill="#92400e" text-anchor="middle">Crème</text>

    <text x="20" y="150" font-family="Liberation Sans, Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a">Principe de l'Abaissement Cryoscopique :</text>
    <text x="20" y="168" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#334155">La dissolution du sel marin dans la glace brise les liaisons cristallines,</text>
    <text x="20" y="182" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#334155">pompant la chaleur ambiante et faisant chuter le bain liquide à <tspan font-weight="bold">-18°C</tspan> !</text>

    <text x="20" y="205" font-family="Liberation Sans, Arial, sans-serif" font-size="11" font-weight="bold" fill="#0284c7">Protocole sans sorbetière :</text>
    <text x="20" y="222" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#0369a1">1. Dans un grand cul-de-poule : 1 kg de glaçons pilés + 250 g de gros sel.</text>
    <text x="20" y="238" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#0369a1">2. Poser un petit cul-de-poule inox au centre contenant la crème anglaise.</text>
    <text x="20" y="254" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#0369a1">3. Fouetter énergiquement à la main pendant 8 à 10 minutes.</text>
    <text x="20" y="270" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#0369a1">4. Le raclage permanent empêche les gros cristaux de se souder.</text>
    <text x="20" y="290" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#0284c7" font-weight="bold">Résultat : Une glace minute au velouté digne d'une turbine professionnelle.</text>
  </g>
</svg>"""
    save_and_verify_svg(os.path.join(FIG_DIR, "livre_5", "fig_fromage_glace_cryoscopie.svg"), svg)

# ------------------------------------------------------------------------------
# 5. Autres figures existantes
# ------------------------------------------------------------------------------
def gen_fig_02():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 420" width="100%" height="100%">
  <rect width="800" height="420" rx="16" fill="#f8fafc" stroke="#e2e8f0" stroke-width="2"/>
  <text x="400" y="38" font-family="Liberation Sans, Arial, sans-serif" font-size="20" font-weight="bold" fill="#0f172a" text-anchor="middle">LES TROIS VECTEURS THERMODYNAMIQUES EN CUISINE</text>
  <text x="400" y="62" font-family="Liberation Sans, Arial, sans-serif" font-size="13" fill="#64748b" text-anchor="middle">Comment l'énergie cinétique microscopique pénètre la matière alimentaire.</text>
  <g transform="translate(30, 85)">
    <rect width="230" height="300" rx="12" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="0" y="0" width="230" height="32" rx="12" fill="#dc2626"/>
    <text x="115" y="21" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">1. LA CONDUCTION SOLIDE</text>
    <rect x="25" y="160" width="180" height="18" fill="#334155" rx="3"/>
    <text x="115" y="174" font-family="Liberation Sans, Arial, sans-serif" font-size="11" fill="#ffffff" text-anchor="middle">Paroi métallique (Fonte / Inox)</text>
    <rect x="45" y="85" width="140" height="75" fill="#fca5a5" stroke="#ef4444" stroke-width="2" rx="4"/>
    <rect x="45" y="145" width="140" height="15" fill="#991b1b" rx="2"/>
    <text x="115" y="156" font-family="Liberation Sans, Arial, sans-serif" font-size="9" fill="#fef2f2" text-anchor="middle">Zone Maillard déshydratée (&gt;140°C)</text>
    <text x="115" y="125" font-family="Liberation Sans, Arial, sans-serif" font-size="11" fill="#7f1d1d" text-anchor="middle" font-weight="bold">Cœur cru (20°C)</text>
    <path d="M 60 215 L 60 185" stroke="#dc2626" stroke-width="3" stroke-linecap="round"/>
    <polygon points="60,180 56,188 64,188" fill="#dc2626"/>
    <path d="M 115 215 L 115 185" stroke="#dc2626" stroke-width="3" stroke-linecap="round"/>
    <polygon points="115,180 111,188 119,188" fill="#dc2626"/>
    <path d="M 170 215 L 170 185" stroke="#dc2626" stroke-width="3" stroke-linecap="round"/>
    <polygon points="170,180 166,188 174,188" fill="#dc2626"/>
    <text x="115" y="232" font-family="Liberation Sans, Arial, sans-serif" font-size="11" fill="#dc2626" font-weight="bold" text-anchor="middle">Flux de Fourier q = -k · ∇T</text>
    <text x="115" y="260" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#334155" text-anchor="middle">• Contact direct d'atome à atome</text>
    <text x="115" y="276" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#334155" text-anchor="middle">• Dépend de la diffusivité α</text>
    <text x="115" y="292" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#b91c1c" text-anchor="middle" font-weight="bold">Application : Saisir, poêler</text>
  </g>
  <g transform="translate(285, 85)">
    <rect width="230" height="300" rx="12" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="0" y="0" width="230" height="32" rx="12" fill="#2563eb"/>
    <text x="115" y="21" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">2. LA CONVECTION FLUIDE</text>
    <rect x="35" y="65" width="160" height="110" rx="4" fill="#eff6ff" stroke="#3b82f6" stroke-width="2"/>
    <path d="M 65 145 C 50 115 55 85 85 85 C 105 85 105 130 85 145" fill="none" stroke="#2563eb" stroke-width="2.5" stroke-dasharray="4,3"/>
    <polygon points="85,148 80,140 88,140" fill="#2563eb"/>
    <path d="M 165 145 C 180 115 175 85 145 85 C 125 85 125 130 145 145" fill="none" stroke="#dc2626" stroke-width="2.5" stroke-dasharray="4,3"/>
    <polygon points="145,148 140,140 148,140" fill="#dc2626"/>
    <ellipse cx="115" cy="115" rx="22" ry="16" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
    <text x="115" y="119" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#92400e" text-anchor="middle">Œuf / Légume</text>
    <text x="115" y="200" font-family="Liberation Sans, Arial, sans-serif" font-size="11" fill="#2563eb" font-weight="bold" text-anchor="middle">Loi de Newton : q = h · ΔT</text>
    <text x="115" y="222" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#334155" text-anchor="middle">• Déplacement macroscopique</text>
    <text x="115" y="238" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#334155" text-anchor="middle">• Eau : transfert x25 vs air calme</text>
    <text x="115" y="254" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#334155" text-anchor="middle">• Température uniforme 100°C</text>
    <text x="115" y="292" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#1d4ed8" text-anchor="middle" font-weight="bold">Application : Bouillir, pocher, vapeur</text>
  </g>
  <g transform="translate(540, 85)">
    <rect width="230" height="300" rx="12" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="0" y="0" width="230" height="32" rx="12" fill="#d97706"/>
    <text x="115" y="21" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">3. LE RAYONNEMENT IR</text>
    <rect x="30" y="55" width="170" height="15" rx="3" fill="#dc2626"/>
    <text x="115" y="67" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#ffffff" text-anchor="middle">Résistance / Braise rouge (800°C)</text>
    <path d="M 60 75 Q 65 95 60 115" fill="none" stroke="#f59e0b" stroke-width="2"/>
    <polygon points="60,118 57,110 63,110" fill="#f59e0b"/>
    <path d="M 115 75 Q 120 95 115 115" fill="none" stroke="#f59e0b" stroke-width="2"/>
    <polygon points="115,118 112,110 118,110" fill="#f59e0b"/>
    <path d="M 170 75 Q 175 95 170 115" fill="none" stroke="#f59e0b" stroke-width="2"/>
    <polygon points="170,118 167,110 173,110" fill="#f59e0b"/>
    <rect x="50" y="125" width="130" height="40" rx="4" fill="#fed7aa" stroke="#c2410c" stroke-width="2"/>
    <text x="115" y="149" font-family="Liberation Sans, Arial, sans-serif" font-size="11" fill="#7c2d12" text-anchor="middle" font-weight="bold">Surface rôtie à sec</text>
    <text x="115" y="200" font-family="Liberation Sans, Arial, sans-serif" font-size="11" fill="#d97706" font-weight="bold" text-anchor="middle">Stefan-Boltzmann : q ∝ T⁴</text>
    <text x="115" y="222" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#334155" text-anchor="middle">• Aucun milieu matériel requis</text>
    <text x="115" y="238" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#334155" text-anchor="middle">• Pénétration superficielle (&lt;1 mm)</text>
    <text x="115" y="254" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#334155" text-anchor="middle">• Dessiccation éclair de croûte</text>
    <text x="115" y="292" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#b45309" text-anchor="middle" font-weight="bold">Application : Rôtir, griller, salamandre</text>
  </g>
</svg>"""
    save_and_verify_svg(os.path.join(FIG_DIR, "livre_1", "fig_02_thermodynamique_transferts.svg"), svg)

def gen_fig_histoire_feu():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 440" width="100%" height="100%">
  <rect width="800" height="440" rx="16" fill="#f8fafc" stroke="#e2e8f0" stroke-width="2"/>
  <text x="400" y="38" font-family="Liberation Sans, Arial, sans-serif" font-size="19" font-weight="bold" fill="#0f172a" text-anchor="middle">L'ÉVOLUTION DU FEU ET LA MORPHOGENÈSE HUMAINE</text>
  <text x="400" y="62" font-family="Liberation Sans, Arial, sans-serif" font-size="13" fill="#64748b" text-anchor="middle">La cuisson comme prédigestion externe : l'hypothèse de Wrangham et la conquête des nutriments.</text>
  <g transform="translate(50, 95)">
    <line x1="20" y1="50" x2="680" y2="50" stroke="#94a3b8" stroke-width="4"/>
    <polygon points="695,50 680,44 680,56" fill="#94a3b8"/>
    <circle cx="60" cy="50" r="10" fill="#dc2626"/>
    <text x="60" y="30" font-family="Liberation Sans, Arial, sans-serif" font-size="11" font-weight="bold" fill="#b91c1c" text-anchor="middle">-1,8 Ma : Le Feu</text>
    <rect x="5" y="70" width="110" height="105" rx="6" fill="#fef2f2" stroke="#fca5a5" stroke-width="1"/>
    <text x="60" y="88" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" font-weight="bold" fill="#991b1b" text-anchor="middle">Prédigestion</text>
    <text x="60" y="104" font-family="Liberation Sans, Arial, sans-serif" font-size="9" fill="#7f1d1d" text-anchor="middle">• Intestin réduit (-60%)</text>
    <text x="60" y="118" font-family="Liberation Sans, Arial, sans-serif" font-size="9" fill="#7f1d1d" text-anchor="middle">• Cerveau x3 (+calories)</text>
    <text x="60" y="132" font-family="Liberation Sans, Arial, sans-serif" font-size="9" fill="#7f1d1d" text-anchor="middle">• Mort des ténias</text>
    <text x="60" y="146" font-family="Liberation Sans, Arial, sans-serif" font-size="9" fill="#7f1d1d" text-anchor="middle">• Neutralise toxines</text>
    <circle cx="230" cy="50" r="10" fill="#d97706"/>
    <text x="230" y="30" font-family="Liberation Sans, Arial, sans-serif" font-size="11" font-weight="bold" fill="#b45309" text-anchor="middle">-10 000 : Céramique</text>
    <rect x="175" y="70" width="110" height="105" rx="6" fill="#fffbeb" stroke="#fcd34d" stroke-width="1"/>
    <text x="230" y="88" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" font-weight="bold" fill="#92400e" text-anchor="middle">Le Bouilli &amp; Sel</text>
    <text x="230" y="104" font-family="Liberation Sans, Arial, sans-serif" font-size="9" fill="#78350f" text-anchor="middle">• Eau bouillante</text>
    <text x="230" y="118" font-family="Liberation Sans, Arial, sans-serif" font-size="9" fill="#78350f" text-anchor="middle">• Gélatinise amidon</text>
    <text x="230" y="132" font-family="Liberation Sans, Arial, sans-serif" font-size="9" fill="#78350f" text-anchor="middle">• Pains &amp; bouillies</text>
    <text x="230" y="146" font-family="Liberation Sans, Arial, sans-serif" font-size="9" fill="#78350f" text-anchor="middle">• Fermentation lactique</text>
    <circle cx="400" cy="50" r="10" fill="#2563eb"/>
    <text x="400" y="30" font-family="Liberation Sans, Arial, sans-serif" font-size="11" font-weight="bold" fill="#1d4ed8" text-anchor="middle">XIVe s. : Épices</text>
    <rect x="345" y="70" width="110" height="105" rx="6" fill="#eff6ff" stroke="#bfdbfe" stroke-width="1"/>
    <text x="400" y="88" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" font-weight="bold" fill="#1e40af" text-anchor="middle">Taillevent / Scappi</text>
    <text x="400" y="104" font-family="Liberation Sans, Arial, sans-serif" font-size="9" fill="#1e3a8a" text-anchor="middle">• Sauces acides (verjus)</text>
    <text x="400" y="118" font-family="Liberation Sans, Arial, sans-serif" font-size="9" fill="#1e3a8a" text-anchor="middle">• Épices bactéricides</text>
    <text x="400" y="132" font-family="Liberation Sans, Arial, sans-serif" font-size="9" fill="#1e3a8a" text-anchor="middle">• Viandes rôties au feu</text>
    <text x="400" y="146" font-family="Liberation Sans, Arial, sans-serif" font-size="9" fill="#1e3a8a" text-anchor="middle">• Masquage olfactif</text>
    <circle cx="560" cy="50" r="10" fill="#16a34a"/>
    <text x="560" y="30" font-family="Liberation Sans, Arial, sans-serif" font-size="11" font-weight="bold" fill="#15803d" text-anchor="middle">1810 : Appertisation</text>
    <rect x="505" y="70" width="110" height="105" rx="6" fill="#f0fdf4" stroke="#86efac" stroke-width="1"/>
    <text x="560" y="88" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" font-weight="bold" fill="#166534" text-anchor="middle">Stérilisation</text>
    <text x="560" y="104" font-family="Liberation Sans, Arial, sans-serif" font-size="9" fill="#14532d">• Conserve sous verre</text>
    <text x="560" y="118" font-family="Liberation Sans, Arial, sans-serif" font-size="9" fill="#14532d">• Pasteur prouve microbe</text>
    <text x="560" y="132" font-family="Liberation Sans, Arial, sans-serif" font-size="9" fill="#14532d">• Mort des spores</text>
    <text x="560" y="146" font-family="Liberation Sans, Arial, sans-serif" font-size="9" fill="#14532d">• Fin du scorbut en mer</text>
  </g>
  <g transform="translate(50, 290)">
    <rect width="335" height="120" rx="8" fill="#f0fdf4" stroke="#22c55e" stroke-width="1.5"/>
    <text x="167" y="24" font-family="Liberation Sans, Arial, sans-serif" font-size="12" font-weight="bold" fill="#15803d" text-anchor="middle">✓ BÉNÉFICES DU CUIT (POURQUOI LE FEU)</text>
    <text x="15" y="46" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#166534">• <tspan font-weight="bold">Rendement énergétique :</tspan> +300% de calories nettes extraites.</text>
    <text x="15" y="64" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#166534">• <tspan font-weight="bold">Éradication parasitaire :</tspan> destruction des kystes et vers.</text>
    <text x="15" y="82" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#166534">• <tspan font-weight="bold">Neutralisation chimique :</tspan> inhibiteurs de trypsine détruits.</text>
    <text x="15" y="100" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#166534">• <tspan font-weight="bold">Biodisponibilité :</tspan> lycopène et minéraux libérés des parois.</text>
    <rect x="365" y="0" width="335" height="120" rx="8" fill="#fef2f2" stroke="#ef4444" stroke-width="1.5"/>
    <text x="532" y="24" font-family="Liberation Sans, Arial, sans-serif" font-size="12" font-weight="bold" fill="#b91c1c" text-anchor="middle">✗ DÉBORDEMENTS DU FEU (CE QU'IL FAUT ÉVITER)</text>
    <text x="380" y="46" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#991b1b">• <tspan font-weight="bold">Pyrolyse carbonée :</tspan> hydrocarbures aromatiques polycycliques (HAP).</text>
    <text x="380" y="64" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#991b1b">• <tspan font-weight="bold">Acrylamide (&gt;120°C friture) :</tspan> mutagène sur féculents brûlés.</text>
    <text x="380" y="82" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#991b1b">• <tspan font-weight="bold">Destruction vitaminique :</tspan> vitamine C oxydée à 60°C en eau.</text>
    <text x="380" y="100" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#991b1b">• <tspan font-weight="bold">Amines hétérocycliques :</tspan> formées sur viandes brûlées au grill.</text>
  </g>
</svg>"""
    save_and_verify_svg(os.path.join(FIG_DIR, "histoire", "fig_histoire_evolution_feu.svg"), svg)

def gen_fig_nutrition():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 440" width="100%" height="100%">
  <rect width="800" height="440" rx="16" fill="#f8fafc" stroke="#e2e8f0" stroke-width="2"/>
  <text x="400" y="38" font-family="Liberation Sans, Arial, sans-serif" font-size="19" font-weight="bold" fill="#0f172a" text-anchor="middle">PHYSIOLOGIE DE LA NUTRITION ET CYCLE DE SURVIE</text>
  <text x="400" y="62" font-family="Liberation Sans, Arial, sans-serif" font-size="13" fill="#64748b" text-anchor="middle">Du signal sensoriel (goût/odorat) à l'excrétion : comment le corps trie la vie et le poison.</text>
  <g transform="translate(40, 85)">
    <rect width="215" height="150" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="0" y="0" width="215" height="28" rx="10" fill="#d97706"/>
    <text x="107" y="19" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">1. LES SIGNAUX D'ALERTE</text>
    <text x="15" y="48" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#0f172a"><tspan font-weight="bold">• Sucré :</tspan> signal calorie/énergie</text>
    <text x="15" y="68" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#0f172a"><tspan font-weight="bold">• Salé :</tspan> régulation osmotique Na⁺</text>
    <text x="15" y="88" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#dc2626"><tspan font-weight="bold">• Amer :</tspan> alerte alcaloïde/poison</text>
    <text x="15" y="108" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#16a34a"><tspan font-weight="bold">• Acide :</tspan> décomposition ou vit. C</text>
    <text x="15" y="128" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#2563eb"><tspan font-weight="bold">• Umami :</tspan> acides aminés/protéines</text>
  </g>
  <g transform="translate(290, 85)">
    <rect width="220" height="150" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="0" y="0" width="220" height="28" rx="10" fill="#2563eb"/>
    <text x="110" y="19" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">2. BESOINS NUTRITIONNELS</text>
    <text x="15" y="48" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#1e3a8a"><tspan font-weight="bold">• 0-20 ans :</tspan> myélinisation lipides,</text>
    <text x="25" y="63" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#475569">Ca²⁺ squelette, acides aminés x2.</text>
    <text x="15" y="83" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#1e3a8a"><tspan font-weight="bold">• Adulte actif :</tspan> équilibre glucides lents,</text>
    <text x="25" y="98" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#475569">acides gras essentiels (oméga 3/6).</text>
    <text x="15" y="118" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#1e3a8a"><tspan font-weight="bold">• Eau vitale :</tspan> 2 à 2,5 L/j (liquide + fruits),</text>
    <text x="25" y="133" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#475569">rôle de l'eau gazeuse (bicarbonates).</text>
  </g>
  <g transform="translate(545, 85)">
    <rect width="215" height="150" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="0" y="0" width="215" height="28" rx="10" fill="#16a34a"/>
    <text x="107" y="19" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">3. DIGESTION &amp; ÉPURATION</text>
    <text x="15" y="48" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#14532d"><tspan font-weight="bold">• Estomac (pH 1.5) :</tspan> tue microbes.</text>
    <text x="15" y="68" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#14532d"><tspan font-weight="bold">• Intestin grêle :</tspan> absorption nutriments.</text>
    <text x="15" y="88" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#14532d"><tspan font-weight="bold">• Côlon &amp; Fibres :</tspan> lest fécal mécanique,</text>
    <text x="25" y="103" font-family="Liberation Sans, Arial, sans-serif" font-size="9.5" fill="#475569">évacuation toxines &amp; acides biliaires.</text>
    <text x="15" y="123" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#991b1b"><tspan font-weight="bold">• Rejets toxiques :</tspan> urée (reins),</text>
    <text x="25" y="138" font-family="Liberation Sans, Arial, sans-serif" font-size="9.5" fill="#b91c1c">matières fécales impropres à l'ingestion.</text>
  </g>
  <g transform="translate(40, 255)">
    <rect width="720" height="165" rx="10" fill="#fffbeb" stroke="#fcd34d" stroke-width="1.5"/>
    <text x="360" y="26" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#92400e" text-anchor="middle">MATURATION SAINE vs PUTRÉFACTION &amp; POISONS</text>
    <text x="25" y="55" font-family="Liberation Sans, Arial, sans-serif" font-size="11" fill="#78350f"><tspan font-weight="bold">1. La Maturation Contrôlée :</tspan> Enzymes endogènes (calpaïnes/cathepsines) coupant les fibres sans bactéries nocives (viande rassie, fromage affiné, koji).</text>
    <text x="25" y="85" font-family="Liberation Sans, Arial, sans-serif" font-size="11" fill="#991b1b"><tspan font-weight="bold">2. La Putréfaction Bactérienne :</tspan> Bactéries d'altération dégradant les protéines en cadavérine, putrescine et amines biogènes hautement toxiques. Odeur fétide = alerte biologique.</text>
    <text x="25" y="115" font-family="Liberation Sans, Arial, sans-serif" font-size="11" fill="#b91c1c"><tspan font-weight="bold">3. Les Toxines Invisibles (Danger Mortel) :</tspan> Clostridium botulinum produit la toxine botulique (inodore, incolore, mortelle à dose nanogramme) en milieu anaérobie sans sel/acide.</text>
    <text x="25" y="145" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#15803d" font-weight="bold">Règle de survie : En cas de doute d'odeur, de boîte bombée ou de moisissure non contrôlée : ON NE GOÛTE PAS, ON JETTE.</text>
  </g>
</svg>"""
    save_and_verify_svg(os.path.join(FIG_DIR, "histoire", "fig_nutrition_digestion_survie.svg"), svg)

def gen_fig_pates_incendie():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 440" width="100%" height="100%">
  <rect width="800" height="440" rx="16" fill="#f8fafc" stroke="#e2e8f0" stroke-width="2"/>
  <text x="400" y="38" font-family="Liberation Sans, Arial, sans-serif" font-size="19" font-weight="bold" fill="#0f172a" text-anchor="middle">LE GESTE AU MICROSCOPE : LES PÂTES ET L'INCENDIE D'HUILE</text>
  <text x="400" y="62" font-family="Liberation Sans, Arial, sans-serif" font-size="13" fill="#64748b" text-anchor="middle">La physique du quotidien : gélatinisation de l'amidon et réaction d'urgence au feu gras.</text>
  <g transform="translate(40, 85)">
    <rect width="345" height="325" rx="12" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="0" y="0" width="345" height="30" rx="12" fill="#2563eb"/>
    <text x="172" y="20" font-family="Liberation Sans, Arial, sans-serif" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">L'ÉQUATION DES PÂTES : 100 / 10 / 1</text>
    <text x="20" y="55" font-family="Liberation Sans, Arial, sans-serif" font-size="11" fill="#1e3a8a"><tspan font-weight="bold">• Proportions :</tspan> 100 g de pâtes, 10 g de sel, 1 L d'eau.</text>
    <text x="20" y="75" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#334155"><tspan font-weight="bold">• Pourquoi tant d'eau ?</tspan> Éviter la saturation en amidon dissous</text>
    <text x="32" y="90" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#334155">qui rend l'eau collante et effondre la température au plongeon.</text>
    <text x="20" y="115" font-family="Liberation Sans, Arial, sans-serif" font-size="11" fill="#15803d"><tspan font-weight="bold">✓ CE QU'IL FAUT FAIRE :</tspan></text>
    <text x="25" y="132" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#166534">1. Jeter dans une eau à bouillon VIF (100°C).</text>
    <text x="25" y="148" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#166534">2. Couvrir 30 secondes pour relancer l'ébullition puis ôter.</text>
    <text x="25" y="164" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#166534">3. Cuire <tspan font-style="italic">al dente</tspan> (cœur légèrement résistant, index glycémique bas).</text>
    <text x="25" y="180" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#166534">4. <tspan font-weight="bold">Garder 1 louche d'eau de cuisson</tspan> riche en amylose dissous !</text>
    <text x="25" y="196" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#166534">5. Émulsionner la sauce directement avec l'eau des pâtes.</text>
    <text x="20" y="224" font-family="Liberation Sans, Arial, sans-serif" font-size="11" fill="#b91c1c"><tspan font-weight="bold">✗ CE QU'IL FAUT ABSOLUMENT ÉVITER :</tspan></text>
    <text x="25" y="242" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#991b1b">• <tspan font-weight="bold">Mettre de l'huile dans l'eau :</tspan> l'huile flotte en surface (inutile),</text>
    <text x="35" y="256" font-family="Liberation Sans, Arial, sans-serif" font-size="9.5" fill="#7f1d1d">puis enrobe les pâtes à l'égouttage, empêchant la sauce d'adhérer !</text>
    <text x="25" y="274" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#991b1b">• <tspan font-weight="bold">Rincer les pâtes cuites sous l'eau :</tspan> rince l'amidon de surface,</text>
    <text x="35" y="288" font-family="Liberation Sans, Arial, sans-serif" font-size="9.5" fill="#7f1d1d">glace les pâtes et détruit toute liaison avec le condiment.</text>
    <text x="25" y="306" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#991b1b">• <tspan font-weight="bold">Surcuire en pâte molle :</tspan> double l'index glycémique (pic d'insuline).</text>
  </g>
  <g transform="translate(415, 85)">
    <rect width="345" height="325" rx="12" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="0" y="0" width="345" height="30" rx="12" fill="#dc2626"/>
    <text x="172" y="20" font-family="Liberation Sans, Arial, sans-serif" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">URGENCE : L'HUILE EN FLAMMES DANS LA POÊLE</text>
    <rect x="25" y="45" width="295" height="95" rx="6" fill="#fef2f2" stroke="#fca5a5" stroke-width="1"/>
    <text x="172" y="65" font-family="Liberation Sans, Arial, sans-serif" font-size="11" font-weight="bold" fill="#991b1b" text-anchor="middle">LE PIÈGE MORTEL DU VERRE D'EAU</text>
    <text x="35" y="85" font-family="Liberation Sans, Arial, sans-serif" font-size="9.5" fill="#7f1d1d">1. L'eau (d=1,0) coule sous l'huile brûlante (d=0,92 à 300°C).</text>
    <text x="35" y="100" font-family="Liberation Sans, Arial, sans-serif" font-size="9.5" fill="#7f1d1d">2. L'eau se vaporise instantanément : <tspan font-weight="bold">expansion x 1 700</tspan> !</text>
    <text x="35" y="115" font-family="Liberation Sans, Arial, sans-serif" font-size="9.5" fill="#b91c1c" font-weight="bold">3. L'explosion pulvérise l'huile en aérosol : boule de feu de 2 mètres.</text>
    <text x="20" y="160" font-family="Liberation Sans, Arial, sans-serif" font-size="11" fill="#15803d"><tspan font-weight="bold">✓ LE SEUL GESTE CORRECT (EN 3 SECONDES) :</tspan></text>
    <text x="25" y="180" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#166534">1. <tspan font-weight="bold">Couper la source de chaleur</tspan> (gaz ou plaque immédiatement).</text>
    <text x="25" y="198" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#166534">2. <tspan font-weight="bold">Faire glisser un couvercle métallique</tspan> ou une plaque sur la poêle.</text>
    <text x="35" y="213" font-family="Liberation Sans, Arial, sans-serif" font-size="9.5" fill="#15803d">(À défaut : poser un torchon mouillé et TRÈS FORTEMENT essoré).</text>
    <text x="25" y="231" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#166534">3. <tspan font-weight="bold">Ne plus toucher</tspan> et attendre 10 minutes que la température</text>
    <text x="35" y="246" font-family="Liberation Sans, Arial, sans-serif" font-size="9.5" fill="#15803d">redescende sous le point d'auto-inflammation (360°C).</text>
    <rect x="25" y="265" width="295" height="45" rx="6" fill="#fef3c7" stroke="#f59e0b" stroke-width="1"/>
    <text x="172" y="283" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" font-weight="bold" fill="#92400e" text-anchor="middle">Principe physique de neutralisation :</text>
    <text x="172" y="299" font-family="Liberation Sans, Arial, sans-serif" font-size="9.5" fill="#78350f" text-anchor="middle">Supprimer le comburant (O₂) sans disperser le combustible (huile).</text>
  </g>
</svg>"""
    save_and_verify_svg(os.path.join(FIG_DIR, "livre_1", "fig_pates_thermodynamique.svg"), svg)

def gen_fig_gateau_matrice():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" rx="16" fill="#f8fafc" stroke="#e2e8f0" stroke-width="2"/>
  <text x="400" y="38" font-family="Liberation Sans, Arial, sans-serif" font-size="19" font-weight="bold" fill="#0f172a" text-anchor="middle">LA MATRICE UNIVERSELLE DU GÂTEAU ET LA RIGUEUR DU FOUR</text>
  <text x="400" y="62" font-family="Liberation Sans, Arial, sans-serif" font-size="13" fill="#64748b" text-anchor="middle">L'équation fonctionnelle : Gras + Sucre + Féculent + Protéine liante + Énergie.</text>
  <g transform="translate(40, 85)">
    <rect width="720" height="60" rx="8" fill="#fffbeb" stroke="#d97706" stroke-width="1.5"/>
    <text x="360" y="26" font-family="Liberation Sans, Arial, sans-serif" font-size="12" font-weight="bold" fill="#92400e" text-anchor="middle">L'ÉQUATION D'ÉTAT : SUBSTANCE = COMBINAISON MODULAIRE</text>
    <text x="360" y="47" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" fill="#78350f" text-anchor="middle">Gras (90g) + Sucre (100g) + Féculent (75g) + Liant Protéique (3 œufs) + Goût (200g choco) + Chaleur = GÂTEAU</text>
  </g>
  <g transform="translate(40, 160)">
    <rect width="345" height="155" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="0" y="0" width="345" height="28" rx="10" fill="#64748b"/>
    <text x="172" y="19" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">MÉTHODE 1 : TOUT-EN-UN (RAPIDE)</text>
    <text x="15" y="46" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#334155">• Mélange brut : Sucre + Œufs entiers + Farine + Beurre/Choco fondus.</text>
    <text x="15" y="66" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#334155">• Temps de préparation : 3 minutes. Zéro vaisselle superflue.</text>
    <text x="15" y="86" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#334155">• <tspan font-weight="bold">Résultat cuit :</tspan> Moelleux dense, fondant au cœur, peu aéré.</text>
    <text x="15" y="106" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#15803d">Parfait pour brownies, fondants denses et gâteaux de voyage.</text>
    <text x="15" y="126" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#dc2626">Attention : ne pas trop mélanger après la farine pour éviter le gluten dur.</text>
  </g>
  <g transform="translate(415, 160)">
    <rect width="345" height="155" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="0" y="0" width="345" height="28" rx="10" fill="#d97706"/>
    <text x="172" y="19" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" font-weight="bold" fill="#ffffff" text-anchor="middle">MÉTHODE 2 : SÉPARATION DES BLANCS EN NEIGE</text>
    <text x="15" y="46" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#334155">• Jaunes blanchis + sucre, puis choco/beurre/farine, puis blancs montés.</text>
    <text x="15" y="66" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#334155">• <tspan font-weight="bold">La réalité sensorielle :</tspan> En théorie plus alvéolé ; en pratique, le poids</text>
    <text x="25" y="80" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#334155">du chocolat dense et du beurre effondre une partie des bulles !</text>
    <text x="15" y="102" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#1e40af"><tspan font-weight="bold">Verdict expérimental :</tspan> Différence minime en bouche pour 2x plus</text>
    <text x="25" y="117" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#1e40af">de temps et de vaisselle. Justifié seulement pour biscuits soufflés légers.</text>
  </g>
  <g transform="translate(40, 330)">
    <rect width="720" height="100" rx="10" fill="#eff6ff" stroke="#93c5fd" stroke-width="1.5"/>
    <text x="360" y="24" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" font-weight="bold" fill="#1e40af" text-anchor="middle">POURQUOI DÉMARRER DANS UN FOUR CHAUD (180°C) PLUTÔT QUE FROID ?</text>
    <text x="20" y="48" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#1e3a8a"><tspan font-weight="bold">1. La poussée gazeuse synchronisée :</tspan> Le CO₂ de la levure et la vapeur d'eau se dilatent violemment à chaud. Dans un four chaud, les bulles gonflent AVANT que la pâte ne fige.</text>
    <text x="20" y="68" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#1e3a8a"><tspan font-weight="bold">2. La fixation des cloisons :</tspan> À 180°C, les protéines de l'œuf coagulent et l'amidon gélatinise en périphérie, rigidifiant les alvéoles au pic de dilatation.</text>
    <text x="20" y="88" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#b91c1c"><tspan font-weight="bold">Dans un four froid :</tspan> Le beurre fond trop tôt, la pâte s'étale liquide, le gaz s'échappe lentement sans pousser : gâteau lourd et tassé.</text>
  </g>
</svg>"""
    save_and_verify_svg(os.path.join(FIG_DIR, "livre_3", "fig_gateau_chocolat_matrice.svg"), svg)

def gen_fig_puree_blumenthal():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 420" width="100%" height="100%">
  <rect width="800" height="420" rx="16" fill="#f8fafc" stroke="#e2e8f0" stroke-width="2"/>
  <text x="400" y="38" font-family="Liberation Sans, Arial, sans-serif" font-size="19" font-weight="bold" fill="#0f172a" text-anchor="middle">LA PURÉE PARFAITE SELON HESTON BLUMENTHAL</text>
  <text x="400" y="62" font-family="Liberation Sans, Arial, sans-serif" font-size="13" fill="#64748b" text-anchor="middle">L'infusion aromatique des épluchures dans le lait et le respect mécanique des cellules d'amidon.</text>
  <g transform="translate(40, 85)">
    <rect width="345" height="300" rx="12" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="0" y="0" width="345" height="30" rx="12" fill="#d97706"/>
    <text x="172" y="20" font-family="Liberation Sans, Arial, sans-serif" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">LE SECRET MOLÉCULAIRE : LA PEAU</text>
    <ellipse cx="172" cy="105" rx="80" ry="50" fill="#fef3c7" stroke="#b45309" stroke-width="3"/>
    <ellipse cx="172" cy="105" rx="72" ry="42" fill="#fffbeb" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="4,2"/>
    <text x="172" y="105" font-family="Liberation Sans, Arial, sans-serif" font-size="11" fill="#92400e" text-anchor="middle">Chair centrale :</text>
    <text x="172" y="119" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#b45309" text-anchor="middle">Amidon pur (neutre)</text>
    <text x="172" y="180" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" font-weight="bold" fill="#78350f" text-anchor="middle">Sous-épiderme (0-2 mm) :</text>
    <text x="172" y="196" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#78350f" text-anchor="middle">85% des molécules d'arômes volatils</text>
    <text x="172" y="210" font-family="Liberation Sans, Arial, sans-serif" font-size="9.5" fill="#475569" font-style="italic">(Méthional, alkylpyrazines à goût de pomme de terre)</text>
    <rect x="20" y="230" width="305" height="55" rx="6" fill="#fef3c7" stroke="#fcd34d" stroke-width="1"/>
    <text x="172" y="248" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" font-weight="bold" fill="#92400e" text-anchor="middle">Le Geste Blumenthal :</text>
    <text x="172" y="264" font-family="Liberation Sans, Arial, sans-serif" font-size="9.5" fill="#78350f" text-anchor="middle">Laver impeccablement les pelures et les faire infuser 30 min</text>
    <text x="172" y="278" font-family="Liberation Sans, Arial, sans-serif" font-size="9.5" fill="#78350f" text-anchor="middle">dans le lait chaud avant de filtrer et monter la purée !</text>
  </g>
  <g transform="translate(415, 85)">
    <rect width="345" height="300" rx="12" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="0" y="0" width="345" height="30" rx="12" fill="#16a34a"/>
    <text x="172" y="20" font-family="Liberation Sans, Arial, sans-serif" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">MÉCANIQUE CELLULAIRE : PRESSE vs MIXEUR</text>
    <rect x="20" y="45" width="305" height="110" rx="6" fill="#f0fdf4" stroke="#86efac" stroke-width="1"/>
    <text x="35" y="65" font-family="Liberation Sans, Arial, sans-serif" font-size="11" font-weight="bold" fill="#166534">✓ PRESSE-PURÉE / MOULIN À LÉGUMES</text>
    <text x="35" y="85" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#14532d">• Pression mécanique douce.</text>
    <text x="35" y="100" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#14532d">• Les cellules végétales se séparent sans éclater.</text>
    <text x="35" y="115" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#14532d">• L'amylose reste piégé à l'intérieur des cellules.</text>
    <text x="35" y="135" font-family="Liberation Sans, Arial, sans-serif" font-size="10" font-weight="bold" fill="#15803d">Résultat : Texture légère, soyeuse et fondante.</text>
    <rect x="20" y="170" width="305" height="110" rx="6" fill="#fef2f2" stroke="#fca5a5" stroke-width="1"/>
    <text x="35" y="190" font-family="Liberation Sans, Arial, sans-serif" font-size="11" font-weight="bold" fill="#991b1b">✗ MIXEUR PLONGEANT / ROBOT À LAME</text>
    <text x="35" y="210" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#7f1d1d">• Rotation à 10 000 tours/min cisaillant les parois.</text>
    <text x="35" y="225" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#7f1d1d">• Éventration massive des cellules de pomme de terre.</text>
    <text x="35" y="240" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#7f1d1d">• L'amylose libre se polymérise en colle d'amidon.</text>
    <text x="35" y="260" font-family="Liberation Sans, Arial, sans-serif" font-size="10" font-weight="bold" fill="#b91c1c">Résultat : Purée gluante, élastique comme du mastic.</text>
  </g>
</svg>"""
    save_and_verify_svg(os.path.join(FIG_DIR, "livre_3", "fig_puree_blumenthal_infusion.svg"), svg)

def gen_fig_05():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450" width="100%" height="100%">
  <rect width="800" height="450" rx="16" fill="#f8fafc" stroke="#e2e8f0" stroke-width="2"/>
  <text x="400" y="38" font-family="Liberation Sans, Arial, sans-serif" font-size="20" font-weight="bold" fill="#0f172a" text-anchor="middle">ANATOMIE PHYSICO-CHIMIQUE ET BARRIÈRE CUTICULAIRE DE L'ŒUF</text>
  <text x="400" y="62" font-family="Liberation Sans, Arial, sans-serif" font-size="13" fill="#64748b" text-anchor="middle">Pourquoi l'œuf est un écosystème respirant et pourquoi le lavage détruit sa défense biologique.</text>
  <g transform="translate(60, 95)">
    <path d="M 140 20 C 230 20 280 120 280 200 C 280 280 220 320 140 320 C 60 320 0 280 0 200 C 0 120 50 20 140 20 Z" fill="#fffbeb" stroke="#d97706" stroke-width="4"/>
    <path d="M 140 14 C 236 14 286 118 286 200 C 286 286 224 326 140 326 C 56 326 -6 286 -6 200 C -6 118 44 14 140 14 Z" fill="none" stroke="#16a34a" stroke-width="2" stroke-dasharray="5,3"/>
    <path d="M 50 295 Q 140 260 230 295 C 205 315 165 320 140 320 C 115 320 75 315 50 295 Z" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.5"/>
    <text x="140" y="303" font-family="Liberation Sans, Arial, sans-serif" font-size="11" font-weight="bold" fill="#0369a1" text-anchor="middle">Chambre à air</text>
    <path d="M 140 35 C 215 35 260 125 260 195 C 260 255 205 265 140 265 C 75 265 20 255 20 195 C 20 125 65 35 140 35 Z" fill="#eff6ff" stroke="#93c5fd" stroke-width="1"/>
    <path d="M 140 60 C 195 60 235 130 235 190 C 235 240 195 245 140 245 C 85 245 45 240 45 190 C 45 130 85 60 140 60 Z" fill="#dbeafe" stroke="#3b82f6" stroke-width="1.8"/>
    <circle cx="140" cy="165" r="52" fill="#fbbf24" stroke="#d97706" stroke-width="2.5"/>
    <circle cx="140" cy="165" r="46" fill="#f59e0b"/>
    <circle cx="120" cy="145" r="5" fill="#fef3c7"/>
    <path d="M 88 165 C 70 160 65 170 48 165" fill="none" stroke="#ffffff" stroke-width="3"/>
    <path d="M 192 165 C 210 160 215 170 232 165" fill="none" stroke="#ffffff" stroke-width="3"/>
  </g>
  <g transform="translate(390, 95)">
    <rect width="370" height="135" rx="8" fill="#f0fdf4" stroke="#86efac" stroke-width="1.5"/>
    <text x="15" y="24" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#166534">LE DILEMME DU FRIGO : EUROPE vs ÉTATS-UNIS</text>
    <text x="15" y="46" font-family="Liberation Sans, Arial, sans-serif" font-size="11" fill="#14532d">• <tspan font-weight="bold">La cuticule protectrice :</tspan> fine pellicule protéique naturelle</text>
    <text x="25" y="62" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#15803d">qui colmate les 10 000 pores de calcite contre les microbes.</text>
    <text x="15" y="82" font-family="Liberation Sans, Arial, sans-serif" font-size="11" fill="#14532d">• <tspan font-weight="bold">Europe (Pas de lavage obligatoire) :</tspan> cuticule intacte.</text>
    <text x="25" y="98" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#15803d">Stockage tempéré possible (évite condensation favorisant bactéries).</text>
    <text x="15" y="118" font-family="Liberation Sans, Arial, sans-serif" font-size="11" fill="#991b1b">• <tspan font-weight="bold">USA (Lavage désinfectant) :</tspan> cuticule détruite $\to$ frigo vital (4°C).</text>
    <rect y="150" width="370" height="170" rx="8" fill="#eff6ff" stroke="#bfdbfe" stroke-width="1.5"/>
    <text x="15" y="174" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#1e40af">LA MÉCANIQUE DU TEMPS : 3 TRANSFORMATIONS</text>
    <text x="15" y="196" font-family="Liberation Sans, Arial, sans-serif" font-size="11" fill="#1e3a8a"><tspan font-weight="bold">1. Évaporation hydrique :</tspan> la chambre à air grossit.</text>
    <text x="25" y="211" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#3b82f6">Œuf frais coule horizontalement ; œuf vieux flotte verticalement.</text>
    <text x="15" y="233" font-family="Liberation Sans, Arial, sans-serif" font-size="11" fill="#1e3a8a"><tspan font-weight="bold">2. Fuite de CO₂ dissous :</tspan> le pH monte de 7.6 à 9.2.</text>
    <text x="25" y="248" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#3b82f6">L'albumen s'alcalinise spontanément et perd sa turbidité laiteuse.</text>
    <text x="15" y="270" font-family="Liberation Sans, Arial, sans-serif" font-size="11" fill="#1e3a8a"><tspan font-weight="bold">3. Liquéfaction de l'albumen :</tspan> dégradation de l'ovomucine.</text>
    <text x="25" y="285" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#3b82f6">L'œuf frais reste compact en dôme ; l'œuf âgé s'étale comme de l'eau.</text>
    <text x="25" y="305" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#b91c1c" font-weight="bold">Conséquence : seul l'œuf extra-frais permet un œuf poché parfait.</text>
  </g>
</svg>"""
    save_and_verify_svg(os.path.join(FIG_DIR, "livre_2", "fig_05_oeuf_anatomie_barriere.svg"), svg)

def gen_fig_06():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 420" width="100%" height="100%">
  <rect width="800" height="420" rx="16" fill="#f8fafc" stroke="#e2e8f0" stroke-width="2"/>
  <text x="400" y="36" font-family="Liberation Sans, Arial, sans-serif" font-size="20" font-weight="bold" fill="#0f172a" text-anchor="middle">LE SPECTRE DE COAGULATION THERMIQUE DE L'ŒUF</text>
  <text x="400" y="60" font-family="Liberation Sans, Arial, sans-serif" font-size="13" fill="#64748b" text-anchor="middle">Seuils de dénaturation des fractions protéiques et pilotage millimétrique des textures.</text>
  <g transform="translate(60, 100)">
    <rect x="0" y="100" width="680" height="24" rx="12" fill="#e2e8f0"/>
    <rect x="136" y="100" width="136" height="24" fill="#fef08a"/>
    <rect x="272" y="100" width="136" height="24" fill="#fed7aa"/>
    <rect x="408" y="100" width="136" height="24" fill="#fca5a5"/>
    <rect x="544" y="100" width="136" height="24" rx="12" fill="#ef4444"/>
    <line x1="0" y1="95" x2="0" y2="130" stroke="#64748b" stroke-width="2"/>
    <text x="0" y="148" font-family="Liberation Sans, Arial, sans-serif" font-size="12" font-weight="bold" fill="#475569" text-anchor="middle">50°C</text>
    <line x1="136" y1="95" x2="136" y2="130" stroke="#64748b" stroke-width="2"/>
    <text x="136" y="148" font-family="Liberation Sans, Arial, sans-serif" font-size="12" font-weight="bold" fill="#475569" text-anchor="middle">60°C</text>
    <line x1="163" y1="60" x2="163" y2="125" stroke="#2563eb" stroke-width="2" stroke-dasharray="3,2"/>
    <rect x="100" y="25" width="126" height="35" rx="5" fill="#eff6ff" stroke="#3b82f6" stroke-width="1"/>
    <text x="163" y="40" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" font-weight="bold" fill="#1e40af" text-anchor="middle">62°C : Ovotransferrine</text>
    <text x="163" y="53" font-family="Liberation Sans, Arial, sans-serif" font-size="9.5" fill="#2563eb" text-anchor="middle">Blanc prend en gelée douce</text>
    <line x1="190" y1="95" x2="190" y2="185" stroke="#16a34a" stroke-width="3"/>
    <rect x="120" y="195" width="140" height="42" rx="6" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.5"/>
    <text x="190" y="212" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" font-weight="bold" fill="#166534" text-anchor="middle">64°C : ŒUF PARFAIT</text>
    <text x="190" y="228" font-family="Liberation Sans, Arial, sans-serif" font-size="9.5" fill="#15803d" text-anchor="middle">Blanc crémeux tremblotant</text>
    <text x="190" y="240" font-family="Liberation Sans, Arial, sans-serif" font-size="9.5" fill="#15803d" text-anchor="middle">Jaune pâteux soyeux</text>
    <line x1="245" y1="60" x2="245" y2="125" stroke="#d97706" stroke-width="2" stroke-dasharray="3,2"/>
    <rect x="185" y="25" width="120" height="35" rx="5" fill="#fffbeb" stroke="#d97706" stroke-width="1"/>
    <text x="245" y="40" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" font-weight="bold" fill="#92400e" text-anchor="middle">68°C : Jaune ferme</text>
    <text x="245" y="53" font-family="Liberation Sans, Arial, sans-serif" font-size="9.5" fill="#b45309" text-anchor="middle">Lipovitellines figées</text>
    <line x1="272" y1="95" x2="272" y2="130" stroke="#64748b" stroke-width="2"/>
    <text x="272" y="148" font-family="Liberation Sans, Arial, sans-serif" font-size="12" font-weight="bold" fill="#475569" text-anchor="middle">70°C</text>
    <line x1="408" y1="95" x2="408" y2="130" stroke="#64748b" stroke-width="2"/>
    <text x="408" y="148" font-family="Liberation Sans, Arial, sans-serif" font-size="12" font-weight="bold" fill="#475569" text-anchor="middle">80°C</text>
    <line x1="462" y1="60" x2="462" y2="125" stroke="#dc2626" stroke-width="2" stroke-dasharray="3,2"/>
    <rect x="402" y="25" width="120" height="35" rx="5" fill="#fef2f2" stroke="#dc2626" stroke-width="1"/>
    <text x="462" y="40" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" font-weight="bold" fill="#991b1b" text-anchor="middle">84°C : Ovalbumine</text>
    <text x="462" y="53" font-family="Liberation Sans, Arial, sans-serif" font-size="9.5" fill="#b91c1c" text-anchor="middle">54% du blanc, ferme solide</text>
    <line x1="680" y1="95" x2="680" y2="130" stroke="#64748b" stroke-width="2"/>
    <text x="680" y="148" font-family="Liberation Sans, Arial, sans-serif" font-size="12" font-weight="bold" fill="#475569" text-anchor="middle">100°C</text>
    <rect x="480" y="195" width="200" height="48" rx="6" fill="#fef2f2" stroke="#b91c1c" stroke-width="1.5"/>
    <text x="580" y="212" font-family="Liberation Sans, Arial, sans-serif" font-size="11" font-weight="bold" fill="#991b1b" text-anchor="middle">ZONE DANGER : ANNEAU VERT</text>
    <text x="580" y="227" font-family="Liberation Sans, Arial, sans-serif" font-size="9.5" fill="#7f1d1d" text-anchor="middle">H₂S (blanc) + Fe²⁺ (jaune) → FeS</text>
    <text x="580" y="239" font-family="Liberation Sans, Arial, sans-serif" font-size="9.5" fill="#7f1d1d" text-anchor="middle">Précipité de sulfure de fer grisâtre</text>
  </g>
  <rect x="50" y="370" width="700" height="32" rx="6" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1"/>
  <text x="400" y="391" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" fill="#334155" text-anchor="middle"><tspan font-weight="bold">Règle de maîtrise :</tspan> Cuire un œuf dur sans anneau vert exige une eau frémissante (90°C max) et un bain glacé immédiat pour stopper la diffusion du fer.</text>
</svg>"""
    save_and_verify_svg(os.path.join(FIG_DIR, "livre_2", "fig_06_courbe_coagulation_oeuf.svg"), svg)

def gen_fig_07():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 420" width="100%" height="100%">
  <rect width="800" height="420" rx="16" fill="#f8fafc" stroke="#e2e8f0" stroke-width="2"/>
  <text x="400" y="38" font-family="Liberation Sans, Arial, sans-serif" font-size="20" font-weight="bold" fill="#0f172a" text-anchor="middle">MÉCANIQUE D'UNE ÉMULSION : ARCHITECTURE DE LA GOUTTELETTE</text>
  <text x="400" y="62" font-family="Liberation Sans, Arial, sans-serif" font-size="13" fill="#64748b" text-anchor="middle">Comment les lécithines et lipoprotéines empêchent la coalescence de l'huile dans l'eau.</text>
  <g transform="translate(180, 230)">
    <rect x="-140" y="-140" width="280" height="280" rx="140" fill="#eff6ff" stroke="#93c5fd" stroke-width="1.5"/>
    <text x="0" y="-115" font-family="Liberation Sans, Arial, sans-serif" font-size="11.5" font-weight="bold" fill="#1d4ed8" text-anchor="middle">PHASE CONTINUE : EAU (Jaune + Vinaigre)</text>
    <circle cx="0" cy="0" r="70" fill="#fef3c7" stroke="#f59e0b" stroke-width="2"/>
    <text x="0" y="-10" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#92400e" text-anchor="middle">GOUTTELETTE</text>
    <text x="0" y="8" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#92400e" text-anchor="middle">D'HUILE</text>
    <text x="0" y="25" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#b45309" text-anchor="middle">(Phase dispersée)</text>
    <circle cx="0" cy="-78" r="6" fill="#2563eb"/>
    <line x1="0" y1="-72" x2="0" y2="-55" stroke="#d97706" stroke-width="2.5"/>
    <circle cx="0" cy="78" r="6" fill="#2563eb"/>
    <line x1="0" y1="72" x2="0" y2="55" stroke="#d97706" stroke-width="2.5"/>
    <circle cx="-78" cy="0" r="6" fill="#2563eb"/>
    <line x1="-72" y1="0" x2="-55" y2="0" stroke="#d97706" stroke-width="2.5"/>
    <circle cx="78" cy="0" r="6" fill="#2563eb"/>
    <line x1="72" y1="0" x2="55" y2="0" stroke="#d97706" stroke-width="2.5"/>
    <circle cx="55" cy="-55" r="6" fill="#2563eb"/>
    <line x1="51" y1="-51" x2="38" y2="-38" stroke="#d97706" stroke-width="2.5"/>
    <circle cx="-55" cy="-55" r="6" fill="#2563eb"/>
    <line x1="-51" y1="-51" x2="-38" y2="-38" stroke="#d97706" stroke-width="2.5"/>
    <circle cx="55" cy="55" r="6" fill="#2563eb"/>
    <line x1="51" y1="51" x2="38" y2="38" stroke="#d97706" stroke-width="2.5"/>
    <circle cx="-55" cy="55" r="6" fill="#2563eb"/>
    <line x1="-51" y1="51" x2="-38" y2="38" stroke="#d97706" stroke-width="2.5"/>
  </g>
  <g transform="translate(380, 95)">
    <rect width="380" height="135" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="20" y="26" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#0f172a">ZOOM : MOLÉCULE AMPHIPHILE (LÉCITHINE)</text>
    <circle cx="55" cy="70" r="16" fill="#2563eb" stroke="#1d4ed8" stroke-width="2"/>
    <text x="55" y="75" font-family="Liberation Sans, Arial, sans-serif" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">+</text>
    <text x="90" y="65" font-family="Liberation Sans, Arial, sans-serif" font-size="11" font-weight="bold" fill="#1d4ed8">Tête polaire hydrophile</text>
    <text x="90" y="80" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#475569">Liaisons hydrogène avec l'eau libre</text>
    <path d="M 55 86 C 45 105 60 115 50 125" fill="none" stroke="#d97706" stroke-width="3"/>
    <path d="M 60 86 C 70 105 55 115 65 125" fill="none" stroke="#d97706" stroke-width="3"/>
    <text x="90" y="105" font-family="Liberation Sans, Arial, sans-serif" font-size="11" font-weight="bold" fill="#b45309">Queues d'acides gras lipophiles</text>
    <text x="90" y="120" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#475569">Plongent au cœur de la gouttelette d'huile</text>
  </g>
  <g transform="translate(380, 245)">
    <rect width="380" height="145" rx="8" fill="#fffbeb" stroke="#fcd34d" stroke-width="1.5"/>
    <text x="20" y="24" font-family="Liberation Sans, Arial, sans-serif" font-size="12.5" font-weight="bold" fill="#92400e">🛠️ CAS LIMITE : L'ÉMULSION TRANCHÉE</text>
    <text x="20" y="44" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#78350f"><tspan font-weight="bold">Cause physique :</tspan> Trop d'huile ajoutée trop vite. Les gouttelettes</text>
    <text x="20" y="59" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#78350f">se touchent, coalescent et expulsent l'eau : inversion de phase.</text>
    <text x="20" y="82" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" font-weight="bold" fill="#b91c1c">Protocole de Sauvetage en 60 secondes :</text>
    <text x="20" y="98" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#334155">1. Verser 1 cuillère à café d'eau tiède (5 ml) dans un bol propre.</text>
    <text x="20" y="113" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#334155">2. Fouetter en incorporant la sauce tranchée goutte par goutte.</text>
    <text x="20" y="128" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#15803d" font-weight="bold">Résultat : L'eau recrée la phase continue ; les micelles se reforment.</text>
  </g>
</svg>"""
    save_and_verify_svg(os.path.join(FIG_DIR, "livre_2", "fig_07_micelle_emulsion.svg"), svg)

def gen_fig_16():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 420" width="100%" height="100%">
  <rect width="800" height="420" rx="16" fill="#f8fafc" stroke="#e2e8f0" stroke-width="2"/>
  <text x="400" y="38" font-family="Liberation Sans, Arial, sans-serif" font-size="20" font-weight="bold" fill="#0f172a" text-anchor="middle">LES TRANSFORMATIONS SANS FEU : OSMOSE SALINE ET DÉNATURATION ACIDE</text>
  <text x="400" y="62" font-family="Liberation Sans, Arial, sans-serif" font-size="13" fill="#64748b" text-anchor="middle">Comment le sel et les ions H⁺ modifient la matière vivante sans aucun apport calorique.</text>
  <g transform="translate(40, 85)">
    <rect width="345" height="305" rx="12" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="0" y="0" width="345" height="32" rx="12" fill="#2563eb"/>
    <text x="172" y="21" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">L'OSMOSE DU SEL (NaCl)</text>
    <rect x="40" y="55" width="265" height="130" rx="6" fill="#eff6ff" stroke="#93c5fd" stroke-width="1"/>
    <line x1="172" y1="55" x2="172" y2="185" stroke="#3b82f6" stroke-width="2" stroke-dasharray="6,4"/>
    <text x="105" y="75" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#1e40af" text-anchor="middle">Milieu Intracellulaire</text>
    <text x="105" y="90" font-family="Liberation Sans, Arial, sans-serif" font-size="9.5" fill="#3b82f6" text-anchor="middle">(Hypotonique en sel)</text>
    <text x="240" y="75" font-family="Liberation Sans, Arial, sans-serif" font-size="10.5" fill="#1e40af" text-anchor="middle">Milieu Extérieur</text>
    <text x="240" y="90" font-family="Liberation Sans, Arial, sans-serif" font-size="9.5" fill="#3b82f6" text-anchor="middle">(Hypertonique : Sel massif)</text>
    <rect x="210" y="105" width="10" height="10" fill="#ffffff" stroke="#1e40af" stroke-width="1.5"/>
    <rect x="235" y="125" width="10" height="10" fill="#ffffff" stroke="#1e40af" stroke-width="1.5"/>
    <rect x="260" y="110" width="10" height="10" fill="#ffffff" stroke="#1e40af" stroke-width="1.5"/>
    <rect x="225" y="150" width="10" height="10" fill="#ffffff" stroke="#1e40af" stroke-width="1.5"/>
    <path d="M 120 120 L 160 120" stroke="#2563eb" stroke-width="3" stroke-linecap="round"/>
    <polygon points="166,120 158,116 158,124" fill="#2563eb"/>
    <path d="M 120 145 L 160 145" stroke="#2563eb" stroke-width="3" stroke-linecap="round"/>
    <polygon points="166,145 158,141 158,149" fill="#2563eb"/>
    <text x="140" y="137" font-family="Liberation Sans, Arial, sans-serif" font-size="10" font-weight="bold" fill="#1d4ed8" text-anchor="middle">Flux H₂O</text>
    <text x="172" y="208" font-family="Liberation Sans, Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Cinétique en 2 temps du saumurage sec :</text>
    <text x="20" y="228" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#334155">1. <tspan font-weight="bold">Phase 1 (0-15 min) :</tspan> L'eau sort pour diluer le sel en surface.</text>
    <text x="20" y="244" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#334155">2. <tspan font-weight="bold">Phase 2 (&gt;30 min) :</tspan> La saumure formée dissout les protéines</text>
    <text x="32" y="259" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#334155">myofibrillaires et est réabsorbée à l'intérieur du muscle.</text>
    <text x="20" y="282" font-family="Liberation Sans, Arial, sans-serif" font-size="10" font-weight="bold" fill="#15803d">Gain : +15% de rétention d'eau à la cuisson chaude ultérieure !</text>
  </g>
  <g transform="translate(415, 85)">
    <rect width="345" height="305" rx="12" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
    <rect x="0" y="0" width="345" height="32" rx="12" fill="#16a34a"/>
    <text x="172" y="21" font-family="Liberation Sans, Arial, sans-serif" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">LA CUISSON ACIDE (CEVICHE / MARINADE)</text>
    <rect x="25" y="55" width="295" height="130" rx="6" fill="#f0fdf4" stroke="#bbf7d0" stroke-width="1"/>
    <path d="M 45 120 C 45 90 85 90 85 120 C 85 140 55 140 65 110" fill="none" stroke="#64748b" stroke-width="3"/>
    <text x="65" y="165" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#475569" text-anchor="middle">Protéine repliée</text>
    <text x="65" y="177" font-family="Liberation Sans, Arial, sans-serif" font-size="9" fill="#64748b" text-anchor="middle">(Poisson cru translucide)</text>
    <path d="M 125 120 L 165 120" stroke="#16a34a" stroke-width="3" stroke-linecap="round"/>
    <polygon points="171,120 163,116 163,124" fill="#16a34a"/>
    <text x="145" y="112" font-family="Liberation Sans, Arial, sans-serif" font-size="11" font-weight="bold" fill="#15803d" text-anchor="middle">+ H⁺ (pH &lt; 4)</text>
    <path d="M 205 100 L 235 140 L 270 105 L 295 135" fill="none" stroke="#16a34a" stroke-width="2.5"/>
    <path d="M 215 135 L 250 100 L 285 140" fill="none" stroke="#16a34a" stroke-width="2.5"/>
    <text x="250" y="165" font-family="Liberation Sans, Arial, sans-serif" font-size="10" font-weight="bold" fill="#166534" text-anchor="middle">Réseau dénaturé</text>
    <text x="250" y="177" font-family="Liberation Sans, Arial, sans-serif" font-size="9" fill="#15803d" text-anchor="middle">(Chair opaque et raffermie)</text>
    <text x="172" y="208" font-family="Liberation Sans, Arial, sans-serif" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Différences capitales avec la chaleur :</text>
    <text x="20" y="228" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#334155">• <tspan font-weight="bold">Zéro stérilisation bactériologique :</tspan> l'acide ne détruit</text>
    <text x="32" y="244" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#b91c1c" font-weight="bold">ni les parasites (anisakis) ni toutes les bactéries.</text>
    <text x="20" y="262" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#334155">• <tspan font-weight="bold">Fenêtre d'action critique :</tspan> 5 à 15 min max. Au-delà,</text>
    <text x="32" y="278" font-family="Liberation Sans, Arial, sans-serif" font-size="10" fill="#334155">la contraction excessive expulse l'eau : chair cotonneuse.</text>
    <text x="20" y="297" font-family="Liberation Sans, Arial, sans-serif" font-size="9.5" fill="#475569" font-style="italic">Impératif de sécurité : Congélation préalable (-20°C / 24h).</text>
  </g>
</svg>"""
    save_and_verify_svg(os.path.join(FIG_DIR, "livre_5", "fig_16_osmose_sel_ceviche.svg"), svg)

if __name__ == "__main__":
    print("Génération de l'ensemble complet des figures vectorielles SVG (13 figures)...")
    gen_fig_01()
    gen_fig_02()
    gen_fig_securite()
    gen_fig_3_etoiles()
    gen_fig_additifs_courses()
    gen_fig_histoire_feu()
    gen_fig_nutrition()
    gen_fig_pates_incendie()
    gen_fig_gateau_matrice()
    gen_fig_puree_blumenthal()
    gen_fig_fromage_glace()
    gen_fig_05()
    gen_fig_06()
    gen_fig_07()
    gen_fig_16()
    print("Succès : Toutes les 13 figures vectorielles ont été générées et validées.")
