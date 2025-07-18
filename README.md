# 1. Setup project

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
├─ data/                           ← shapefile, CSV...
│  ├─ aoi/
│  │  ├─ aoi_1km7x16_3035.cpg
│  │  ├─ aoi_1km7x16_3035.dbf
│  │  ├─ aoi_1km7x16_3035.prj
│  │  ├─ aoi_1km7x16_3035.qmd
│  │  ├─ aoi_1km7x16_3035.shp
│  │  └─ aoi_1km7x16_3035.shx
│  ├─ csv/
│  └─ raster/
├─ doc/
│  ├─ sar_moisture/
│  │  ├─ 2505.00265v1.pdf
│  │  └─ remotesensing-17-00542.pdf
│  └─ var/
├─ notebook/
│  └─ 1_s1_moisture.ipynb
├─ output/                          ← GeoTIFF, report...                          
│  ├─ s1/
│  │  └─ sar_vv_2024_04_09.tif
│  └─ var/
├─ scripts/
│  ├─ __pycache__/
│  │  ├─ aoi_loader.cpython-312.pyc
│  │  └─ download_s1.cpython-312.pyc
│  ├─ __init__.py
│  ├─ aoi_loader.py
│  ├─ conv_db_sm.py
│  └─ download_s1.py
├─ utils/
│  └─ config.py                      ← common parameters (date, AOI, ecc.)
├─ venv/                             ← .gitignore
├─ .gitignore
├─ README.md
└─ requirements.txt

```

# 2. Reference Documentation

doc path: SAR\doc\sar_moisture\remotesensing-17-00542.pdf
**Reference**: Stanyer et al. (2025), *Remote Sensing*, 17(542), https://doi.org/10.3390/rs17030542  

## Summary

### Title  
**Soil Texture, Soil Moisture, and Sentinel-1 Backscattering: Towards the Retrieval of Field-Scale Soil Hydrological Properties**  
*Stanyer et al., Remote Sens. 2025, 17, 542*

### 1. Introduction

Soil moisture is a key variable for agriculture, climate regulation, and hydrology.  
Radar satellites (such as Sentinel-1) can monitor soil moisture regardless of cloud cover, but their accuracy is limited when **soil texture**—a key factor influencing the radar signal—is not considered.

This study investigates how **Sentinel-1 VV radar backscatter** varies in relation to both **soil moisture (SM)** and **soil texture**, using data from the **COSMOS-UK** monitoring network.

### 2. Materials and Methods

#### 2.1 Study Sites
- 17 agricultural sites in the UK, part of the **COSMOS-UK** network.
- Each site includes a sensor that measures soil moisture using **cosmic-ray neutron probes**.

#### 2.2 Data Sources
- **Soil Moisture (SM)** from COSMOS (0–20 cm depth, ~200 m footprint).
- **VV Backscatter** from Sentinel-1 (C-band, GRD IW mode, 10 m resolution).
- **NDVI** from Sentinel-2, used to detect low-vegetation periods.
- **Soil Texture** from the UK Soil Observatory (UKSO).

#### 2.3 Methodology
- Agricultural **Field Sectors** were defined around each COSMOS sensor.
- **Low Vegetation Periods (L-periods)** were selected where **NDVI < 0.35**.
- Sentinel-1 data were **corrected for orbit-related biases**.
- For each sector and L-period:
  - A **linear regression** was performed between VV and SM.
  - The **slope** (sensitivity: %VWC per dB) was calculated.
- The slopes were then compared with the corresponding **soil texture classes**.

### 3. Results and Discussion

- A **significant linear relationship** was found between SM and VV backscatter under bare-soil conditions.
- The **slope of the regression** varied depending on soil texture:
  - **Sandy soils** showed higher sensitivity (e.g., 1.69% VWC/dB).
  - **Clay soils** showed lower sensitivity (e.g., 4.81% VWC/dB).
- Slopes remained **stable over time** for each site, indicating their dependence on texture.

The results suggest that **VV backscatter can serve as a proxy for soil texture**, especially when combined with rainfall data and hydrological models.

### 4. Conclusions

- The influence of **soil texture** on the Sentinel-1 VV radar response to soil moisture has been confirmed.
- This paves the way for retrieving **soil hydrological properties** (e.g., infiltration potential) **using satellite data alone**.
- The approach can support:
  - Precision agriculture,
  - Field-scale water balance modelling,
  - Irrigation decision support systems.

### Citation

> Stanyer, C., Seco-Rizo, I., Atzberger, C., Marti-Cardona, B.  
> *Soil Texture, Soil Moisture, and Sentinel-1 Backscattering: Towards the Retrieval of Field-Scale Soil Hydrological Properties*.  
> Remote Sens. 2025, 17, 542. https://doi.org/10.3390/rs17030542

---

## Using Sentinel-1 SAR for Soil Moisture and Crop Irrigation Needs

When using **Sentinel-1 SAR imagery** for agricultural applications—especially to estimate **soil moisture (SM)** and calculate **crop irrigation requirements** — you must always **convert the backscatter values (VV in dB) into actual soil moisture (%)**.

### Why?

Sentinel-1 does **not measure soil moisture directly**.  
It returns a **backscatter coefficient** (in dB), which reflects how much of the radar signal bounces off the Earth’s surface.

Backscatter is influenced by:
- Soil moisture
- Soil texture (sand, loam, clay)
- Vegetation cover (NDVI)
- Surface roughness (ploughing, tillage)

Therefore, you need an **empirical formula** to **translate radar signal into real soil moisture**.

---

### Typical Conversion Formula

You can use a **linear regression model** like:

```python
SM (%) = a × VV_dB + b
```

- The **slope `a`** reflects how sensitive backscatter is to moisture.
- The **intercept `b`** varies based on local soil and calibration.

These values depend on the **soil type**:
- **Sandy soil** → lower slope (e.g., −1.7 %/dB)
- **Clay soil** → higher slope (e.g., −4.8 %/dB)

This is exactly what was demonstrated in the paper:  
**"Soil Texture, Soil Moisture, and Sentinel-1 Backscattering" (Stanyer et al., 2025)**

> In general, coefficients vary from -3 to -5 (slope) and -30 to -50 (intercept), depending on:
> - soil type (sandy, clayey, etc.),
> - presence of vegetation,
> - surface roughness.

---

### From Soil Moisture to Irrigation Need

Once you have `SM (%)`, you can estimate irrigation requirements:

```python
water_deficit = ideal_SM - actual_SM
mm_water = (water_deficit / 100) * root_zone_depth_mm
```

Where:
- `ideal_SM` = target soil moisture for the crop (e.g., 30% for maize)
- `root_zone_depth_mm` = depth of active root zone (e.g., 300 mm)

---

- Estimate soil moisture from Sentinel-1 | Convert VV ➜ SM |
- Calculate irrigation demand | Compare SM to crop target |
- Determine water amount | Convert deficit to mm or liters/m² |

---

### What is **VV** in Sentinel-1 SAR?

**VV** stands for **Vertical transmit – Vertical receive** polarization.

#### In more detail:

Sentinel-1 is a **Synthetic Aperture Radar (SAR)** satellite that emits microwave pulses toward the Earth's surface and measures the reflected signal (backscatter).

SAR can transmit and receive radar waves in different **polarizations**:

* **V = Vertical** (the electric field is oriented vertically)
* **H = Horizontal**

So:

* **VV** = Radar signal **transmitted vertically** and **received vertically**
* **VH** = Transmitted vertically, received horizontally

---

### Why is **VV used for soil moisture estimation**?

* **VV backscatter** is more **sensitive to surface moisture** than VH in many bare-soil or low-vegetation conditions.
* It responds strongly to **changes in dielectric properties** of the soil, which are influenced by **water content**.
* VV also has **higher signal-to-noise ratio** over smooth, flat surfaces (e.g., agricultural fields).

> In most studies (including Stanyer et al., 2025), **VV backscatter** is used as the main input to estimate **surface soil moisture** from Sentinel-1.

---

### Units and Usage

* VV backscatter is given in **decibels (dB)**.
* It is a **negative number** (e.g., −5 to −20 dB).
* Lower dB → less reflection (dry soil)
  Higher dB → more reflection (wet soil)

You can convert it to **soil moisture (%)** using empirical formulas like:

```python
soil_moisture = a * vv_dB + b
```

---

# 3. Soil Texture

https://www.isric.org/news/soilgrids-data-now-available-google-earth-engine
