## Setup

```bash
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows

pip install -r requirements.txt
```

---
## Project Structure

* `notebook/`: analysis and prototyping
* `scripts/`: reusable Python modules
* `data/`: local shapefiles and input data
* `output/`: generated maps and results

```bash
SAR/
│
├── .gitignore
├── requirements.txt
├── README.md
│
├── venv/                      ← .gitignore
├── data/                      ← shapefile, CSV...
├── output/                    ← GeoTIFF, report...
├── notebook/
│   └── 1_s1_moisture.ipynb
├── scripts/
│
└── utils/
    └── config.py              ← common parameters (date, AOI, ecc.)
```


