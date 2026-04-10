import json

with open("Projet/Classification.ipynb", "r") as f:
    nb = json.load(f)

cells = nb['cells']

# Identify indices of the misplaced 3D visualization cells
vis_3d_indices = []
for i, cell in enumerate(cells):
    src = "".join(cell.get("source", []))
    if "Visualisation 3D Améliorée #1" in src or \
       "Comment Lire les Visualisations 3D ?" in src or \
       "Visualisation 3D Améliorée #2" in src or \
       "Visualisation 3D Bonus : \"Consensus\"" in src:
        vis_3d_indices.append(i)

print("Found misplaced cells at:", vis_3d_indices)

# We extract them
vis_cells = [cells[i] for i in vis_3d_indices]

# Remove them from their original location (in reverse order to not mess up indices)
for i in sorted(vis_3d_indices, reverse=True):
    del cells[i]

# Find where to insert them. Probably before section 6.
target_idx = -1
for i, cell in enumerate(cells):
    src = "".join(cell.get("source", []))
    if "# 6. Analyse de l'Importance des Facteurs" in src:
        target_idx = i
        break

print("Inserting before section 6 at index:", target_idx)
if target_idx != -1:
    for c in reversed(vis_cells):
        cells.insert(target_idx, c)

with open("Projet/Classification.ipynb", "w") as f:
    json.dump(nb, f, indent=1)

print("SUCCESS")
