# Virtual Lab
Free online science experiments, built with plain HTML/CSS/JS and hosted on GitHub Pages.

## Run locally
```bash
python3 serve.py
```
Open http://localhost:8000.

## Add a lab
```bash
python3 new_lab.py my-lab "My Lab Title" Physics
```
Then add the printed entry to the `LABS` array in `assets/main.js`. The script creates a starter page; you must implement its simulation logic.

## Deploy
1. Create a GitHub repository named `virtual-lab` (or any name).
2. Upload/push the contents of this folder to the repository's `main` branch.
3. Open Settings → Pages → Build and deployment, and choose **GitHub Actions**.
4. The workflow in `.github/workflows/pages.yml` deploys the static website.

## Included experiments
Physics, electricity, optics, magnetism, chemistry, biology/health education, mathematics, computer science, and the custom Your Lab builder. Simulations are educational models, not laboratory-grade tools.
