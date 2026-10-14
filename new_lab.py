#!/usr/bin/env python3
"""Create a starter lab: python3 new_lab.py my-lab "My Lab Title" [Category]"""
import os, re, sys
if len(sys.argv) < 3:
    raise SystemExit('Usage: python3 new_lab.py <folder-id> "Lab Title" [Category]')
lab_id, title = sys.argv[1], sys.argv[2]
cat = sys.argv[3] if len(sys.argv) > 3 else "Physics"
if not re.fullmatch(r"[a-z0-9-]+", lab_id):
    raise SystemExit("Folder id must use lowercase letters, numbers, and hyphens.")
folder = os.path.join("labs", lab_id)
os.makedirs(folder, exist_ok=False)
html = """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>__TITLE__</title><link rel="stylesheet" href="../../assets/style.css"></head><body><header class="site"><a href="../../index.html">← Virtual Lab</a></header><main><h1>__TITLE__</h1><section class="panel"><h2>Aim</h2><p>Describe what this simulation investigates.</p><h2>Theory</h2><p>Explain the scientific principle and equations.</p></section><section class="panel"><canvas id="sim" width="640" height="360"></canvas><div id="result" class="result">Add your simulation here.</div></section><section class="panel"><h2>Observations</h2><table id="tbl"></table><button id="csv">Download CSV</button></section></main><script src="../../assets/lab.js"></script><script>document.getElementById('csv').onclick=()=>downloadCSV(['Variable','Value'],[], '__ID__-observations.csv');</script></body></html>"""
html = html.replace("__TITLE__", title.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")).replace("__ID__", lab_id)
with open(os.path.join(folder, "index.html"), "w", encoding="utf-8") as f: f.write(html)
print(f"Created {folder}/index.html")
print("Add this entry to assets/main.js LABS array (JSON-style object):")
print(f"  {{id:'{lab_id}',title:{title!r},cat:{cat!r},icon:'🔬',desc:'Short description.'}},")
