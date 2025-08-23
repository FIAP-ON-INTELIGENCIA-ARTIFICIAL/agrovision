FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app

RUN apt-get update -y && apt-get install -y --no-install-recommends \
    build-essential curl && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt && pip install --no-cache-dir gunicorn

COPY app.py /app/
COPY api /app/api
COPY web /app/web
COPY data /app/data
COPY etl /app/etl
COPY analysis /app/analysis

ENV USE_R=false R_URL=http://r-analytics:8000
EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
  CMD curl -fsS http://localhost:5000/api/health || exit 1

CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "app:app"]
