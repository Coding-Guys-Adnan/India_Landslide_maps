# India Seismic & Landslide Risk Atlas — Research Grade

![License](https://img.shields.io/badge/license-MIT-blue.svg?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Leaflet](https://img.shields.io/badge/Leaflet-199900?style=for-the-badge&logo=leaflet&logoColor=white)
![OpenStreetMap](https://img.shields.io/badge/OpenStreetMap-7EC0EE?style=for-the-badge&logo=openstreetmap&logoColor=white)

> A high-performance, full-stack geospatial platform designed for **disaster analysis, geospatial research, hazard visualization, and academic use**.

---

## 📖 Overview
The **India Seismic & Landslide Risk Atlas** is an advanced interactive dashboard engineered to analyze and visualize over 15,000 seismic events and consequential landslide triggers across the Indian subcontinent (2000–2026). 

Built to handle research-grade analytical datasets, the platform dynamically analyzes earthquakes mapped directly against pivotal spatial infrastructure—such as focal depth, rainfall buffers, terrain slope, NDVI (vegetation density), and soil properties—to actively contextualize mass-movement vulnerability. 

## ✨ Key Features
- **Interactive Seismic Visualization**: Dynamically map points cleanly segmented by precise Magnitude (Mw), Peak Ground Acceleration (PGA), or Focal Depth constraints.
- **Landslide Risk Mapping**: Overlay known confirmed landslide occurrences natively on top of the seismic data map to draw geological correlations gracefully onto the UI.
- **Regional Comparison**: Compare seismic profiles and average triggers across distinct geographic zones (e.g., Himalayan Belt vs. Peninsular India) using deep statistical layouts.
- **Multi-Source Detection**: Visualize detection methodologies powered by combined academic thresholds, USGS arrays, and established Seismic algorithms.
- **Advanced Filtering**: Live, stateless DOM filtration by Region, Temporal range (Year), and Confirmed occurrence status for instantaneous dataset isolation across all map overlays. 
- **Research-Grade Analytics**: Extract real-time sub-layer averages parsing critical metrics mapping components like intersecting soil compositions (sand/clay pH) and vegetation densities directly into sidebar analytics.

---

## 📸 Screenshots

<img width="1906" height="908" alt="image" src="https://github.com/user-attachments/assets/0c7b876e-50e6-4645-bae4-b5e8ae281eea" />
*Detailed interactive mapping of earthquake magnitudes using Leaflet clusters & UI Panels.*

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/97ac53ad-79b2-47e7-bad3-36889518df86" />
*Granular analytics parsing 30-day cumulative rainfall and slope topography models.*

---

## 🛠️ Tech Stack
This application leverages a decoupled, asynchronous architecture maximizing data streaming performance when dealing with large datasets:

- **Backend**: Python 3, FastAPI, Pandas, Uvicorn
- **Frontend**: Vanilla JavaScript (Async Fetch API), HTML5, CSS3 Variables
- **Mapping & Geospatial**: Leaflet.js, OpenStreetMap tileset

---

## 📁 Project Structure
```text
📦 India-Seismic-Risk-Atlas
├── 📂 backend
│   ├── main.py                 # FastAPI server & dataset injection logic
│   └── requirements.txt        # Python dependency lists
├── 📂 frontend
│   ├── index.html              # Core application scaffold & UI elements
│   ├── script.js               # Async operations, Leaflet bindings, and filtering routines
│   └── style.css               # Dynamic dark theme aesthetics
├── Landslide_Labeled_ResearchGrade.xlsx   # Sourced Dataset
└── README.md
```

## 🚀 Installation 

### Prerequisites
- Python 3.8+
- Modern Web Browser

### 1. Setup Backend
Navigate into the backend directory and install the required Python packages.
```bash
cd backend
pip install -r requirements.txt
```

Launch the FastAPI application:
```bash
python -m uvicorn main:app --port 8000
```

### 2. Setup Frontend
In a new terminal window, spin up a basic HTTP server to serve the frontend client cleanly from the local directory:
```bash
cd frontend
python -m http.server 8001
```

## 💻 Usage
1. Ensure the Python backend parses the datasets and logs: `Application startup complete`.
2. Open your browser and navigate to `http://localhost:8001`.
3. Use the **horizontal navigation bar** to hot-swap map data visualizations instantly.
4. Interact with the **Left Sidebar** to trigger cascading filters to isolate geospatial and temporal occurrences.
5. Click on any mapped marker node to spawn detailed localized metrics inside a popup!

## 📊 Data Sources
This system ingests data compiled under the `Landslide_Labeled_ResearchGrade.xlsx` schema. Information is actively corroborated and harmonized across global registries including:
- USGS FDSNWS
- Newmark/Jibson seismic threshold models
- Combined regional rainfall methodologies.

## 🔭 Future Improvements
- **Predictive AI Layer**: Implement Scikit-Learn Random Forests into the Python backend to algorithmically forecast expected mass movements on raw forecasted seismic data.
- **Pagination & Vector Chunking**: Shift processing to GeoJSON chunk-based mapping systems for infinitely scaling datasets beyond 100k+ global events.
- **Dockerization**: Containerize both the FastAPI backend and web server frontend using Docker Compose for streamlined 1-click deployments.

## 📜 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
