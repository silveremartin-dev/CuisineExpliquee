import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('LA_CUISINE_EXPLIQUEE.typ', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. ASCII Art check
ascii_chars = ['┌', '─', '│', '└', '┐', '┘', '├', '┤', '┬', '┴', '┼', '▲', '▼', '◄', '►']
found_ascii = []
for i, line in enumerate(text.splitlines()):
    if any(c in line for c in ascii_chars):
        found_ascii.append((i+1, line[:60]))

print(f"--- ASCII ART CHECK ---")
if found_ascii:
    print(f"FAILED: Found {len(found_ascii)} ASCII art lines:")
    for lno, l in found_ascii[:10]:
        print(f"  Line {lno}: {l}")
else:
    print("[PASS] ZERO ASCII art found in the entire book!")

# 2. Duplicate Images check
print(f"\n--- DUPLICATE IMAGES CHECK ---")
all_imgs = re.findall(r'image\("([^"]+)"', text)
from collections import Counter
counts = Counter(all_imgs)
dups = {k: v for k, v in counts.items() if v > 1}
if dups:
    print(f"FAILED: Found duplicate images:")
    for k, v in dups.items():
        print(f"  {k}: {v} times")
else:
    print(f"[PASS] ZERO duplicate images found! Total distinct images: {len(all_imgs)}")

# 3. Figures count
figures = re.findall(r'#figure\(image\("([^"]+)"[^)]*\),\s*caption:\s*\[(.*?)\]', text, re.DOTALL)
print(f"\n--- FIGURES COUNT ---")
print(f"Total numbered figures with captions: {len(figures)}")

# 4. Annexe F present
print(f"\n--- ANNEXE F CHECK ---")
print("Has Annexe F:", "ANNEXE F" in text or "Crédits Iconographiques" in text)
