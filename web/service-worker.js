const CACHE = 'agrovision-v1';
const ASSETS = [
  '/', '/index.html', '/styles.css', '/app.js',
  '/manifest.webmanifest'
];

self.addEventListener('install', (e) => {
  e.waitUntil(caches.open(CACHE).then((c) => c.addAll(ASSETS)));
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys().then(keys => Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k))))
  );
});

self.addEventListener('fetch', (e) => {
  const { request } = e;
  // Estratégia: network first para APIs, cache first para estáticos
  if (request.url.includes('/api/')) {
    e.respondWith(
      fetch(request).then((res) => {
        const clone = res.clone();
        caches.open(CACHE).then((c) => c.put(request, clone));
        return res;
      }).catch(() => caches.match(request))
    );
  } else {
    e.respondWith(caches.match(request).then((c) => c || fetch(request)));
  }
});
