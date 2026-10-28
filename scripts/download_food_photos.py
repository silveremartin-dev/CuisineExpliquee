# -*- coding: utf-8 -*-
"""
Téléchargement de superbes photographies culinaires réelles et vivantes
(légumes frais, carottes, poireaux, pains dorés, plats cuisinés)
depuis Wikimedia Commons (licences CC / Domaine Public).
"""

import urllib.request
import urllib.parse
import json
import os
import time

HEADERS = {
    'User-Agent': 'LaCuisineExpliqueeBot/2.0 (food photography curation; silvere.martin@gmail.com)'
}

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOURRITURE_DIR = os.path.join(BASE_DIR, "figures", "nourriture")
os.makedirs(NOURRITURE_DIR, exist_ok=True)

TARGETS = [
    # (Recherche Wikimedia, Fichier local, Description)
    ("carrots leeks market fresh vegetables", "couverture_legumes_marche.jpg", "Carottes fanes et poireaux frais du marché pour la couverture"),
    ("sourdough bread loaf crust sliced", "pain_artisan_croute.jpg", "Pain artisanal doré à croûte craquante et mie alvéolée"),
    ("pan seared steak cast iron butter", "steak_poele_fonte.jpg", "Pavé de viande saisi en poêle de fonte avec beurre mousseux"),
    ("spaghetti carbonara pasta dish", "spaghetti_carbonara.jpg", "Spaghetti à la carbonara dorée avec guanciale et pecorino"),
    ("ceviche lime fish red onion", "ceviche_poisson_frais.jpg", "Ceviche de poisson frais mariné au citron vert et oignon rouge"),
    ("chocolate lava cake fondant", "moelleux_chocolat_fondant.jpg", "Moelleux au chocolat noir cœur coulant"),
    ("fresh leeks carrots vegetables wooden board", "legumes_frais_planche.jpg", "Légumes frais de saison (poireaux, carottes) sur planche en bois")
]

def search_commons_file(query):
    params = {
        'action': 'query',
        'list': 'search',
        'srsearch': query,
        'srnamespace': '6',
        'srlimit': '5',
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
                # Éviter les fichiers pdf ou non-images
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
        'iiurlwidth': '1000',
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
                    print(f"Téléchargement {file_title} -> {thumb_url}...")
                    img_req = urllib.request.Request(thumb_url, headers=HEADERS)
                    with urllib.request.urlopen(img_req, timeout=20) as img_resp:
                        with open(dest_path, 'wb') as out_f:
                            out_f.write(img_resp.read())
                    print(f"[OK] {os.path.basename(dest_path)} ({os.path.getsize(dest_path)} octets)")
                    return True
    except Exception as e:
        print(f"Erreur téléchargement {file_title}: {e}")
    return False

def main():
    print("=== TÉLÉCHARGEMENT DE PHOTOGRAPHIES CULINAIRES VIVANTES ===")
    success = 0
    for query, filename, desc in TARGETS:
        dest_path = os.path.join(NOURRITURE_DIR, filename)
        if os.path.exists(dest_path) and os.path.getsize(dest_path) > 1000:
            print(f"[DÉJÀ PRÉSENT] {filename}")
            success += 1
            continue
        print(f"Recherche pour : '{query}'...")
        file_title = search_commons_file(query)
        if file_title:
            ok = download_file_by_title(file_title, dest_path)
            if ok:
                success += 1
            time.sleep(0.5)
        else:
            print(f"-> Rien trouvé pour '{query}'")
    print(f"\nBilan : {success}/{len(TARGETS)} photographies culinaires téléchargées.")

if __name__ == "__main__":
    main()
