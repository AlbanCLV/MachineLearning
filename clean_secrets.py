import json

notebook_path = '/home/alban/MachineLearning/Workshop1/WS_Exploratory_Data_Analysis_Etudiant.ipynb'
token = "pk.eyJ1Ijoiam9obiIsImEiOiJja2JzdWh3enUwMTUzMndzNmg4YzF1c2FyIn0.Xgpptpghn8u2p8gF5lv5Fg"
placeholder = "your_mapbox_token_here"

try:
    with open(notebook_path, 'r') as f:
        nb = json.load(f)

    changed = False
    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            new_source = []
            for line in cell.get('source', []):
                if token in line:
                    line = line.replace(token, placeholder)
                    changed = True
                new_source.append(line)
            cell['source'] = new_source

    if changed:
        with open(notebook_path, 'w') as f:
            json.dump(nb, f, indent=1)
        print(f"Replaced token in {notebook_path}")
    else:
        print(f"Token not found in {notebook_path}")
except Exception as e:
    print(f"Error processing notebook: {e}")

html_path = '/home/alban/MachineLearning/Workshop1/density_heatmap.html'
try:
    with open(html_path, 'r') as f:
        content = f.read()
    if token in content:
        content = content.replace(token, placeholder)
        with open(html_path, 'w') as f:
            f.write(content)
        print(f"Replaced token in {html_path}")
    else:
        print(f"Token not found in {html_path}")
except FileNotFoundError:
    print(f"File {html_path} not found")
except Exception as e:
    print(f"Error processing HTML: {e}")
