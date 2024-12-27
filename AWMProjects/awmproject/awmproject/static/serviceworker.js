const CACHE_NAME = 'offline-cache-v1';
// const OFFLINE_URL = '/static/offline.html';
const OFFLINE_URL = '/static/offline.html';

const FILES_TO_CACHE = [
    
    '/',
    
    '/map.html',
    '/offline.html',
    '/styles.css',
    '/app.js',
    '/serviceworker.js',
    '/manifest.json',
    '/icons/icon-192x192.png',
    '/icons/icon-512x512.png' // Add other required files, e.g., CSS, JS, images
  ];
// self.addEventListener('install', event => {
//     event.waitUntil(
//         caches.open(CACHE_NAME).then(cache => {
//             return cache.addAll([
//                 OFFLINE_URL,
//                 '/static/css/styles.css', // Include other assets
//             ]);
//         })
//     );
// });

// Install event: Cache files
self.addEventListener('install', (event) => {
    event.waitUntil(
      caches.open(CACHE_NAME).then((cache) => {
        console.log('[Service Worker] Caching offline page');
        return cache.addAll(FILES_TO_CACHE);
      })
    );
    self.skipWaiting();
  });

// self.addEventListener('fetch', event => {
//     if (event.request.mode === 'navigate') {
//         event.respondWith(
//             fetch(event.request).catch(() => {
//                 return caches.match(OFFLINE_URL);
//             })
//         );
//     }
// });
self.addEventListener('fetch', (event) => {
    if (event.request.mode === 'navigate') {
      event.respondWith(
        fetch(event.request).catch(() => {
          return caches.open(CACHE_NAME).then((cache) => {
            return cache.match('/offline.html');
          });
        })
      );
    }
  });