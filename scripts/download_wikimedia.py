# -*- coding: utf-8 -*-
"""
Téléchargement intelligent depuis Wikimedia Commons via API de recherche
"""

import urllib.request
import urllib.parse
import json
import os
import time

HEADERS = {
    'User-Agent': 'LaCuisineExpliqueeBot/1.0 (educational culinary book; silvere.martin@gmail.com)'
}

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATRIMOINE_DIR = os.path.join(BASE_DIR, "figures", "patrimoine")
SCIENCE_DIR = os.path.join(BASE_DIR, "figures", "science")

os.makedirs(PATRIMOINE_DIR, exist_ok=True)
os.makedirs(SCIENCE_DIR, exist_ok=True)

TARGETS = [
    ("Bartolomeo Scappi cucina", PATRIMOINE_DIR, "scappi_cuisine_renaissance.jpg", "Cuisine de la Renaissance (Scappi)"),
    ("Pompeii bakery fresco", PATRIMOINE_DIR, "pompei_fresque_boulangerie.jpg", "Fresque antique romaine de boulangerie"),
    ("Jean Anthelme Brillat-Savarin", PATRIMOINE_DIR, "brillat_savarin_portrait.jpg", "Portrait de Brillat-Savarin"),
    ("Nicolas Appert portrait", PATRIMOINE_DIR, "nicolas_appert_conserve.jpg", "Portrait de Nicolas Appert"),
    ("Auguste Escoffier", PATRIMOINE_DIR, "auguste_escoffier_portrait.jpg", "Portrait d'Auguste Escoffier"),
    ("Diderot Boulangerie", PATRIMOINE_DIR, "diderot_encyclopedie_fournil.jpg", "Fournil de boulanger (Encyclopédie Diderot)"),
    ("pulses legumes lentils chickpeas", SCIENCE_DIR, "legumineuses_proteines_vegetales.jpg", "Assortiment de légumineuses et protéines végétales"),
    ("oil water emulsion droplet", SCIENCE_DIR, "gouttelettes_emulsion_microscope.jpg", "Émulsion et micelles microscopiques"),
    ("cheese making curd", SCIENCE_DIR, "coagulation_lait_caillage.jpg", "Caillage et fabrication de fromage"),
    ("fire friction primitive", PATRIMOINE_DIR, "homme_feu_friction.jpg", "Production du feu ancestral")
]

def search_commons_file(query):
    params = {
        'action': 'query',
        'list': 'search',
        'srsearch': query,
        'srnamespace': '6',
        'srlimit': '3',
        'format': 'json'
    }
    url = f"https://commons.wikimedia.org/w/api.php?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            results = data.get('query', {}).get('search', [])
            if results:
                return results[0]['title']
    except Exception as e:
        print(f"Erreur recherche '{query}': {e}")
    return None

def download_file_by_title(file_title, dest_path):
    params = {
        'action': 'query',
        'titles': file_title,
        'prop': 'imageinfo',
        'iiprop': 'url',
        'iiurlwidth': '800',
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
                    print(f"Téléchargement {file_title} depuis {thumb_url}...")
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
    print("=== TÉLÉCHARGEMENT RECHERCHE WIKIMEDIA COMMONS ===")
    success = 0
    for query, folder, filename, desc in TARGETS:
        dest_path = os.path.join(folder, filename)
        if os.path.exists(dest_path) and os.path.getsize(dest_path) > 1000:
            print(f"[DÉJÀ PRÉSENT] {filename} ({desc})")
            success += 1
            continue
        
        print(f"Recherche Wikimedia pour : '{query}'...")
        file_title = search_commons_file(query)
        if file_title:
            print(f"-> Trouvé : {file_title}")
            ok = download_file_by_title(file_title, dest_path)
            if ok:
                success += 1
            time.sleep(0.5)
        else:
            print(f"-> Aucun résultat pour '{query}'")
            
    print(f"\nBilan : {success}/{len(TARGETS)} images disponibles.")

if __name__ == "__main__":
    main()
