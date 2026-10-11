// Tiny static server for the renderer page, its fonts and the three.js module.
import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const ROOTS = {
  '/three/': path.join(HERE, 'node_modules/three/'),
  '/fonts/': path.join(HERE, '../animation/assets/fonts/'),
  '/data/': path.join(HERE, '../animation/build/'),
  '/': path.join(HERE, 'web/'),
};
const TYPES = { '.js': 'text/javascript', '.html': 'text/html', '.ttf': 'font/ttf', '.json': 'application/json' };

export function serve(port = 0) {
  const server = http.createServer((req, res) => {
    const url = decodeURIComponent(req.url.split('?')[0]);
    const prefix = Object.keys(ROOTS).find((p) => url.startsWith(p));
    const file = path.join(ROOTS[prefix], url.slice(prefix.length) || 'index.html');
    if (!file.startsWith(ROOTS[prefix]) || !fs.existsSync(file) || fs.statSync(file).isDirectory()) {
      res.writeHead(404); res.end(); return;
    }
    res.writeHead(200, { 'Content-Type': TYPES[path.extname(file)] || 'application/octet-stream' });
    fs.createReadStream(file).pipe(res);
  });
  return new Promise((resolve) => server.listen(port, '127.0.0.1', () => resolve(server)));
}
