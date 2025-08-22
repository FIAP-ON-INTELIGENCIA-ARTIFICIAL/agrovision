import os, math, datetime as dt
from flask import Flask, send_from_directory, request, jsonify
import requests

USE_R = os.getenv("USE_R", "false").lower() == "true"
R_URL = os.getenv("R_URL", "http://r-analytics:8000")
OPEN_METEO_URL = "https://api.open-meteo.com/v1/forecast"

app = Flask(__name__, static_folder="web", static_url_path="")

# ---- PWA (arquivos estáticos) ----
@app.get("/")
def index():
    return send_from_directory("web", "index.html")

@app.get("/manifest.webmanifest")
def manifest():
    return send_from_directory("web", "manifest.webmanifest")

@app.get("/service-worker.js")
def sw():
    # service worker precisa ser servido na raiz
    return send_from_directory("web", "service-worker.js")


# ---- API ----
@app.get("/api/health")
def health():
    return {"status": "ok", "use_r": USE_R}

@app.post("/api/calcular/area")
def calcular_area():
    """Calcula área retangular ou poligonal simples."""
    body = request.get_json() or {}
    tipo = body.get("tipo", "retangulo")
    if tipo == "retangulo":
        base = float(body.get("base_m", 0))
        altura = float(body.get("altura_m", 0))
        area_m2 = base * altura
    else:
        # polígonos simples (lista de (x,y)) – fórmula do polígono (Shoelace)
        pts = body.get("pontos", [])
        s1 = sum(pts[i][0]*pts[(i+1)%len(pts)][1] for i in range(len(pts)))
        s2 = sum(pts[i][1]*pts[(i+1)%len(pts)][0] for i in range(len(pts)))
        area_m2 = abs(s1 - s2) / 2.0
    return jsonify({"area_m2": area_m2, "area_ha": area_m2/10_000})

@app.post("/api/calcular/insumos")
def calcular_insumos():
    """Recomendação básica: taxa * área (parâmetros didáticos)."""
    body = request.get_json() or {}
    area_ha = float(body.get("area_ha", 0))
    taxa_kg_ha = float(body.get("taxa_kg_ha", 0))
    total_kg = area_ha * taxa_kg_ha
    return jsonify({"total_kg": total_kg})

@app.post("/api/prever/producao")
def prever_producao():
    """Baseline em Python; opcionalmente delega ao R."""
    body = request.get_json() or {}
    area = float(body.get("area_ha", 0))
    insumo = float(body.get("insumo_kg", 0))
    chuva = float(body.get("chuva_mm", 0))

    if not USE_R:
        y = 1.2*area + 0.8*insumo + 0.5*chuva
        return jsonify({"predicao": y, "unidade": "ton", "provider": "python-baseline"})

    r = requests.post(f"{R_URL}/predict_producao",
                      json={"area_ha": area, "insumo_kg": insumo, "chuva_mm": chuva},
                      timeout=15)
    r.raise_for_status()
    data = r.json()
    data["provider"] = "R-plumber"
    return jsonify(data)

@app.get("/api/clima")
def clima():
    """
    Integração simples de clima (Open-Meteo).
    Parâmetros: lat, lon, start (YYYY-MM-DD), days (int)
    """
    lat = float(request.args.get("lat", -16.6869))   # Goiânia por padrão
    lon = float(request.args.get("lon", -49.2648))
    days = int(request.args.get("days", 3))
    start = request.args.get("start")
    if start:
        start_date = dt.date.fromisoformat(start)
    else:
        start_date = dt.date.today()
    end_date = start_date + dt.timedelta(days=days)

    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": "precipitation,temperature_2m,relative_humidity_2m",
        "start_date": start_date.isoformat(),
        "end_date": end_date.isoformat(),
        "timezone": "auto",
    }
    resp = requests.get(OPEN_METEO_URL, params=params, timeout=20)
    resp.raise_for_status()
    return jsonify(resp.json())


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
