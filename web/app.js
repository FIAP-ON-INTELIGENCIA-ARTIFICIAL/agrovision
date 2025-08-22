// Registrar Service Worker (PWA)
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/service-worker.js');
}

async function postJSON(url, obj) {
  const r = await fetch(url, {method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify(obj)});
  return r.json();
}

document.getElementById('btn-area').onclick = async () => {
  const base = Number(document.getElementById('base').value);
  const altura = Number(document.getElementById('altura').value);
  const data = await postJSON('/api/calcular/area', {tipo:'retangulo', base_m: base, altura_m: altura});
  document.getElementById('out-area').textContent = JSON.stringify(data, null, 2);
}

document.getElementById('btn-insumo').onclick = async () => {
  const area_ha = Number(document.getElementById('area_ha').value);
  const taxa = Number(document.getElementById('taxa').value);
  const data = await postJSON('/api/calcular/insumos', {area_ha, taxa_kg_ha: taxa});
  document.getElementById('out-insumo').textContent = JSON.stringify(data, null, 2);
}

document.getElementById('btn-prev').onclick = async () => {
  const area_ha = Number(document.getElementById('p_area').value);
  const insumo_kg = Number(document.getElementById('p_insumo').value);
  const chuva_mm = Number(document.getElementById('p_chuva').value);
  const data = await postJSON('/api/prever/producao', {area_ha, insumo_kg, chuva_mm});
  document.getElementById('out-prev').textContent = JSON.stringify(data, null, 2);
}

document.getElementById('btn-clima').onclick = async () => {
  const lat = Number(document.getElementById('lat').value);
  const lon = Number(document.getElementById('lon').value);
  const days = Number(document.getElementById('days').value);
  const r = await fetch(`/api/clima?lat=${lat}&lon=${lon}&days=${days}`);
  const data = await r.json();
  document.getElementById('out-clima').textContent = JSON.stringify(data.hourly?.precipitation?.slice(0,24), null, 2);
}
