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

sar/
│
├── .gitignore
├── requirements.txt
├── README.md
├── LICENSE (opzionale)
│
├── venv/                      ← .gitignore
├── data/                      ← shapefile, CSV...
├── output/                    ← GeoTIFF, report...
├── notebook/
│   └── 1_s1_moisture.ipynb
├── scripts/
│   ├── download_s1.py         ← functions download
│   └── soil_moisture.py
└── utils/
    └── config.py              ← common parameters (date, AOI, ecc.)


