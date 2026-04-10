import json

with open('Projet/Classification.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Quick fix for headers, we can just rewrite all markdown cells or inject headers.
