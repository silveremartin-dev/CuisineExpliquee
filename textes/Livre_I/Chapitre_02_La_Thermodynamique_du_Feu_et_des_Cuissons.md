# CHAPITRE 02 — La Thermodynamique du Feu et des Cuissons

> « Cuire, c'est orchestrer une collision contrôlée entre des photons, des électrons et des molécules d'eau. »

---

## 1. LES TROIS VECTEURS DU TRANSFERT D'ÉNERGIE

La cuisine ne consiste jamais à « chauffer » abstraitement un ingrédient : elle consiste à créer un **gradient thermique** entre l'extérieur et l'intérieur de l'aliment via trois mécanismes physiques distincts.

![Les Trois Vecteurs Thermodynamiques en Cuisine](figures/livre_1/fig_02_thermodynamique_transferts.svg)

### A. La Conduction Solide : La Loi de Fourier
La conduction s'opère par transmission directe de l'agitation thermique d'un atome à son voisin, sans déplacement de matière.
$$\vec{q} = -k \nabla T$$
Où $q$ est la densité de flux thermique, $k$ la conductivité thermique du matériau ($\mathrm{W/(m\cdot K)}$) et $\nabla T$ le gradient de température.
- **La conductivité des ustensiles :**
  - Cuivre pur : $390\,\mathrm{W/(m\cdot K)}$ (réactivité quasi instantanée).
  - Aluminium : $220\,\mathrm{W/(m\cdot K)}$ (excellent conducteur mais faible inertie).
  - Fonte brute : $50\,\mathrm{W/(m\cdot K)}$ (conduction modérée, mais très haute capacité thermique volumique).
  - Inox austénitique : $15\,\mathrm{W/(m\cdot K)}$ (mauvais conducteur seul, d'où la nécessité absolue des fonds multi-plis intégrant une âme d'aluminium ou de cuivre).
- **La diffusivité thermique $\alpha$ des aliments :**
  La chair animale et les végétaux ont une conductivité minuscule ($k \approx 0{,}5\,\mathrm{W/(m\cdot K)}$), proche de celle de l'eau immobile. La chaleur met un temps proportionnel au **carré de l'épaisseur** pour atteindre le centre :
  $$t \propto \frac{x^2}{\alpha}$$
  Doubler l'épaisseur d'une pièce de viande ne double pas son temps de cuisson : cela le **quadruple**.

### B. La Convection Fluide : La Loi de Refroidissement / Réchauffement de Newton
La convection implique le mouvement d'un fluide caloporteur (eau, huile fondue, air pulsé).
$$q = h (T_{\text{fluide}} - T_{\text{surface}})$$
- **Eau liquide vs Air :** L'eau possède une capacité thermique volumique plus de $3000$ fois supérieure à celle de l'air. À $100^\circ\mathrm{C}$, vous pouvez laisser votre main quelques secondes dans un four à air sans vous brûler gravement, alors que plonger la main une demi-seconde dans de l'eau bouillante à $100^\circ\mathrm{C}$ inflige une brûlure au troisième degré.
- **Le rôle capital de l'agitation :** Dans un liquide immobile, une fine pellicule d'eau refroidie s'isole autour de l'aliment (couche limite laminaire). Remuer l'eau ou fouetter une sauce brise cette couche et multiplie par dix le coefficient de transfert thermique $h$.

### C. Le Rayonnement Électromagnétique : La Loi de Stefan-Boltzmann
Le rayonnement thermique ne nécessite aucun intermédiaire matériel : il se propage dans le vide sous forme d'ondes infrarouges émises par les corps incandescents (braises de charbon de bois, résistances de salamandre ou grill, flamme nue).
$$P = \varepsilon \sigma S T^4$$
- La puissance émise croît avec la **puissance quatrième de la température absolue ($T^4$)** ! Une braise rouge à $800^\circ\mathrm{C}$ ($1073\,\mathrm{K}$) rayonne une énergie colossale qui frappe la surface de l'aliment sans chauffer l'air intermédiaire.
- Ce rayonnement est absorbé quasi instantanément sur les premiers micromètres de l'aliment : c'est l'outil par excellence pour déshydrater la croûte et provoquer la réaction de Maillard sans surcuire le cœur.

---

## 2. LES MODES DE CHAUFFE COMPARÉS : GAZ, INDUCTION ET FONTE ÉLECTRIQUE

| Mode de Chauffe | Vecteur Principal | Inertie de Source | Réactivité | Comportement Physique en Pratique |
| :--- | :--- | :--- | :--- | :--- |
| **Gaz vif** | Convection d'air brûlant + Conduction | Nulle | Immédiate | La flamme épouse les parois latérales de la poêle (chauffe 3D enveloppante). Idéal pour le sauté au wok et le flambage. |
| **Induction** | Conduction par courants de Foucault dans le fond | Nulle | Millimétrique | Chauffage direct du métal sans déperdition. Rendement énergétique $>85\,\%$. Attention : ne chauffe que le fond plat, pas les parois. |
| **Plaque Fonte / Radiant** | Conduction de contact + Rayonnement | Très forte | Lente | Met 5 minutes à monter et 15 minutes à descendre. Doit être anticipée en coupant le feu par anticipation pour utiliser l'énergie résiduelle. |
| **Four à Convection naturelle** | Rayonnement des parois + Air chaud lent | Forte | Lente | Cuisson douce et dessèchement mesuré. |
| **Four Chaleur Tournante** | Convection forcée d'air turbulent | Moyenne | Rapide | Évacue la vapeur d'eau protectrice de surface : accélère le croustillant mais peut dessécher prématurément. |

---

## 3. LABORATOIRE DES CAS LIMITES : LA VIANDE QUI BOUT DANS SA POÊLE

### Le Problème
Vous déposez deux gros steaks froids sortis du réfrigérateur dans une poêle moyenne. Au lieu d'entendre un crépitement sec et d'obtenir une croûte brune parfumée, la surface devient grisâtre et une mare de liquide trouble envahit la poêle : la viande est en train de « bouillir dans son jus ».

### L'Explication Thermodynamique
1. **L'effondrement de la capacité thermique :** La quantité de chaleur $Q = m c \Delta T$ stockée dans la poêle était insuffisante pour compenser la masse d'eau froide apportée d'un coup.
2. **Le verrouillage de la chaleur latente de vaporisation :** Pour transformer $1\,\mathrm{g}$ d'eau liquide à $100^\circ\mathrm{C}$ en vapeur, il faut fournir $2257\,\mathrm{joules}$ (alors qu'il ne faut que $4{,}18\,\mathrm{joules}$ pour élever $1\,\mathrm{g}$ d'eau de $1^\circ\mathrm{C}$). 
3. Dès que l'eau cellulaire commence à exsuder, toute l'énergie du feu est engloutie par l'évaporation : la température de la poêle reste bloquée à $100^\circ\mathrm{C}$. Or, la réaction de Maillard exige au minimum $140^\circ\mathrm{C}$. Tant qu'il y a de l'eau liquide libre, le brunissement est physiquement impossible.

### L'Algorithme de Sauvetage et de Prévention
```
              [ DÉSIR DE SAISIR UNE PIÈCE DE VIANDE ]
                                  │
                                  ▼
               [ Tamponner la surface au papier absorbant ]
                    (Élimination du film aqueux libre)
                                  │
                                  ▼
               [ Sortir la pièce 30 min avant à l'avance ]
                     (Réduire le delta T initial)
                                  │
                                  ▼
         [ Préchauffer une poêle LOURDE à feu vif jusqu'au frémissement ]
                                  │
                                  ▼
               [ Ne jamais surcharger la surface : max 50% ]
                ┌─────────────────┴─────────────────┐
                ▼                                   ▼
       [ Crépitement aigu vif ]             [ Présence d'eau liquide ]
         -> Réaction de Maillard             -> Sortir la viande d'urgence,
            croûte immédiate                    jeter le jus, essuyer la poêle,
                                                réchauffer à blanc et réintroduire !
```
