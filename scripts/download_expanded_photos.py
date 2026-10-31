# -*- coding: utf-8 -*-
"""
Script robuste de téléchargement des images haute définition Wikimedia Commons
Mots-clés concis et fiables pour l'API Commons.
"""

import urllib.request
import urllib.parse
import json
import os
import time

HEADERS = {
    'User-Agent': 'LaCuisineExpliqueeBot/4.0 (culinary educational treatise; silvere.martin@gmail.com)'
}

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOURRITURE_DIR = os.path.join(BASE_DIR, "figures", "nourriture")
PATRIMOINE_DIR = os.path.join(BASE_DIR, "figures", "patrimoine")

os.makedirs(NOURRITURE_DIR, exist_ok=True)
os.makedirs(PATRIMOINE_DIR, exist_ok=True)

TARGETS = [
    # --- OUVERTURES DES 6 LIVRES (PAGE PAIRE) ---
    ("Prehistoric fire", PATRIMOINE_DIR, "livre1_ouverture_feu_ancestral.jpg", "Foyer ancestral et découverte du feu"),
    ("Chardin kitchen", PATRIMOINE_DIR, "livre2_ouverture_cuisine_ordre.jpg", "L'arsenal ordonné de cuisine"),
    ("Vegetable market stall", NOURRITURE_DIR, "livre3_ouverture_marche_abondance.jpg", "Grand étal maraîcher d'ingrédients bruts"),
    ("Sourdough bread bakery", NOURRITURE_DIR, "livre4_ouverture_fournil_levain.jpg", "Miches dorées au fournil"),
    ("Banquet table setting", PATRIMOINE_DIR, "livre5_ouverture_banquet_table.jpg", "Table de banquet dressée avec couverts"),
    ("Kitchen garden harvest", NOURRITURE_DIR, "livre6_ouverture_potager_saisons.jpg", "Potager et récolte vivante"),

    # --- RECETTES & COMPLÉMENTS ---
    ("Green salad vinaigrette", NOURRITURE_DIR, "salade_croquante.jpg", "Salade verte croquante"),
    ("Mashed potatoes butter", NOURRITURE_DIR, "puree_pommes_terre.jpg", "Purée de pommes de terre"),
    ("Glazed carrots", NOURRITURE_DIR, "carottes_glacees.jpg", "Carottes glacées au beurre"),
    ("Red wine pan sauce", NOURRITURE_DIR, "deglacage_sauce_vin.jpg", "Sauce réduite au vin"),
    ("Clear consomme soup", NOURRITURE_DIR, "consomme_clarifie.jpg", "Consommé de bœuf clarifié"),
    ("Soft boiled egg", NOURRITURE_DIR, "oeuf_mollet.jpg", "Œuf mollet"),
    ("Poached egg", NOURRITURE_DIR, "oeuf_poche.jpg", "Œuf poché"),
    ("Mayonnaise sauce", NOURRITURE_DIR, "mayonnaise_fouet.jpg", "Mayonnaise"),
    ("Hollandaise sauce", NOURRITURE_DIR, "sauce_hollandaise.jpg", "Sauce hollandaise"),
    ("Bechamel sauce", NOURRITURE_DIR, "sauce_bechamel.jpg", "Sauce béchamel"),
    ("Lentil dal", NOURRITURE_DIR, "dahl_lentilles.jpg", "Dahl de lentilles corail"),
    ("Crispy tofu", NOURRITURE_DIR, "tofu_croustillant.jpg", "Tofu doré croustillant"),
    ("Duck fat potatoes", NOURRITURE_DIR, "pommes_sarladaises.jpg", "Pommes de terre sautées"),
    ("Aioli garlic", NOURRITURE_DIR, "aioli_provencal.jpg", "Grand aïoli"),
    ("Pickled vegetables jars", NOURRITURE_DIR, "pickles_lactofermentes.jpg", "Légumes lactofermentés"),
    ("Creme anglaise", NOURRITURE_DIR, "creme_anglaise.jpg", "Crème anglaise vanille"),
    ("Shortcrust pastry dough", NOURRITURE_DIR, "pate_brisee.jpg", "Pâte brisée sablée"),
    ("Chocolate mousse glass", NOURRITURE_DIR, "mousse_aquafaba.jpg", "Mousse au chocolat"),
    ("Baked Alaska dessert", NOURRITURE_DIR, "omelette_norvegienne.jpg", "Omelette norvégienne"),
    ("Ice cream bowl", NOURRITURE_DIR, "glace_artisanale.jpg", "Crème glacée"),
    ("Beef bone broth", NOURRITURE_DIR, "bouillon_viande_glace.jpg", "Grand bouillon de bœuf"),
    ("Spices mortar pestle", NOURRITURE_DIR, "epices_herbes_mortier.jpg", "Épices au mortier"),
    ("Table setting cutlery", PATRIMOINE_DIR, "art_table_couverts.jpg", "Couverts et arts de la table")
]

def search_commons_file(query):
    params = {
        'action': 'query',
        'list': 'search',
        'srsearch': query,
        'srnamespace': '6',
        'srlimit': '10',
        'format': 'json'
    }
    url = f"https://commons.wikimedia.org/w/api.php?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            results = data.get('query', {}).get('search', [])
            for r in results:
                title = r['title']
                if any(ext in title.lower() for ext in ['.jpg', '.jpeg', '.png']):
                    return title
    except Exception as e:
        print(f"Erreur recherche '{query}': {e}")
    return None

def download_file_by_title(file_title, dest_path):
    params = {
        'action': 'query',
        'titles': file_title,
        'prop': 'imageinfo',
        'iiprop': 'url',
        'iiurlwidth': '1200',
        'format': 'json'
    }
    url = f"https://commons.wikimedia.org/w/api.php?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            pages = data.get('query', {}).get('pages', {})
            for pid, pinfo in pages.items():
                if 'imageinfo' in pinfo:
                    info = pinfo['imageinfo'][0]
                    thumb_url = info.get('thumburl', info.get('url'))
                    img_req = urllib.request.Request(thumb_url, headers=HEADERS)
                    with urllib.request.urlopen(img_req, timeout=25) as img_resp:
                        with open(dest_path, 'wb') as out_f:
                            out_f.write(img_resp.read())
                    print(f"  [OK] Telecharge : {os.path.basename(dest_path)} ({os.path.getsize(dest_path)} octets)")
                    return True
    except Exception as e:
        print(f"  [ERREUR] {file_title}: {e}")
    return False

def main():
    print("=== TELECHARGEMENT DES IMAGES COMMONS ===")
    total = len(TARGETS)
    downloaded = 0
    for i, (query, folder, filename, desc) in enumerate(TARGETS, 1):
        dest_path = os.path.join(folder, filename)
        if os.path.exists(dest_path) and os.path.getsize(dest_path) > 3000:
            print(f"[{i}/{total}] Deja present : {filename}")
            downloaded += 1
            continue
        print(f"[{i}/{total}] Recherche : '{query}'...")
        title = search_commons_file(query)
        if title:
            ok = download_file_by_title(title, dest_path)
            if ok:
                downloaded += 1
        else:
            print(f"  [NON TROUVE] {query}")
        time.sleep(0.3)

    print(f"\nBilan : {downloaded}/{total} images prsentes.")

if __name__ == "__main__":
    main()
