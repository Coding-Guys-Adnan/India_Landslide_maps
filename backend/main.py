import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import math

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

data = []

@app.on_event("startup")
def load_data():
    global data
    df = pd.read_excel("../Landslide_Labeled_ResearchGrade.xlsx")
    
    def safe_val(x):
        if pd.isna(x):
            return None
        # Convert pandas/numpy ints and floats so they sequence to JSON correctly
        if isinstance(x, float) and math.isnan(x):
            return None
        return x

    dsrc_mapping = {
        'Below all research thresholds': 'None',
        'Combined-Kanungo2009': 'Combined',
        'USGS-Direct': 'USGS',
        'Seismic-Newmark/Jibson2007': 'Seismic',
        'Rainfall-Guzzetti2008': 'Rainfall'
    }

    # df.columns.tolist() for matching index:
    # 5: Latitude, 6: Longitude, 17: Slope, 19: Steep, 20: Very Steep
    for _, row in df.iterrows():
        item = {
            "year": safe_val(row["Year"]),
            "lat": safe_val(row.iloc[5]),
            "lon": safe_val(row.iloc[6]),
            "place": safe_val(row["Place"]),
            "region": safe_val(row["Region"]),
            "mag": safe_val(row["Magnitude (Mw)"]),
            "depth": safe_val(row["Depth (km)"]),
            "pga": safe_val(row["PGA (g)"]),
            "mmi": safe_val(row["MMI"]),
            "elev": safe_val(row["Elevation (m)"]),
            "slope": safe_val(row.iloc[17]),
            "steep": safe_val(row.iloc[19]),
            "vsteep": safe_val(row.iloc[20]),
            "rain": safe_val(row["Rainfall 30d (mm)"]),
            "prain": safe_val(row["Peak Daily Rain (mm)"]),
            "clay": safe_val(row["Clay (%)"]),
            "sand": safe_val(row["Sand (%)"]),
            "ph": safe_val(row["pH"]),
            "ndvi": safe_val(row["NDVI"]),
            "lc": safe_val(row["Land Cover Class"]),
            "rdist": safe_val(row["River Dist (km)"]),
            "stord": safe_val(row["Stream Order"]),
            "nriver": safe_val(row["Near River"]),
            "locc": 1 if row["Landslide Occurred"] == "YES" else 0 if row["Landslide Occurred"] == "NO" else safe_val(row["Landslide Occurred"]),
            "dsrc": dsrc_mapping.get(row["Detection Source"], safe_val(row["Detection Source"])) if pd.notna(row["Detection Source"]) else None
        }
        # pandas converts integers to numpy datatypes which JSON sometimes hates, standardizing type
        for k, v in item.items():
            if pd.api.types.is_integer(v):
                item[k] = int(v)
            elif pd.api.types.is_float(v) and not math.isnan(v):
                item[k] = float(v)
                
        data.append(item)

@app.get("/api/data")
def get_data():
    return data
