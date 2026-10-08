"""A small, dependency-free web app for exploring Australian Aboriginal languages.

Run with: python lang1.py
Then open http://localhost:8000 in a browser.
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


LANGUAGES = [
	{"name": "Warlpiri", "region": "Northern Territory", "family": "Ngarrkic", "speakers": 2300, "status": "Strong", "community": "Yuendumu, Lajamanu"},
	{"name": "Pitjantjatjara", "region": "Central Australia", "family": "Wati", "speakers": 3000, "status": "Strong", "community": "APY Lands"},
	{"name": "Arrernte", "region": "Northern Territory", "family": "Arandic", "speakers": 2500, "status": "Strong", "community": "Alice Springs"},
	{"name": "Noongar", "region": "Western Australia", "family": "Pama-Nyungan", "speakers": 300, "status": "Revitalising", "community": "Southwest WA"},
	{"name": "Yolŋu Matha", "region": "Northern Territory", "family": "Yolŋu", "speakers": 4500, "status": "Strong", "community": "Arnhem Land"},
	{"name": "Wiradjuri", "region": "New South Wales", "family": "Wiradhuric", "speakers": 100, "status": "Reviving", "community": "Central West NSW"},
	{"name": "Boonwurrung", "region": "Victoria", "family": "Kulin", "speakers": 20, "status": "Reviving", "community": "Port Phillip Bay"},
]

PAGE = r'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Ngana — Language Atlas</title><style>
:root{--ink:#19233c;--blue:#405de6;--pink:#f56b91;--cream:#fff9ef;--muted:#6c7186}*{box-sizing:border-box}body{margin:0;background:var(--cream);color:var(--ink);font:16px system-ui,-apple-system,sans-serif}nav{height:76px;padding:0 7%;display:flex;align-items:center;justify-content:space-between;background:#fff;border-bottom:1px solid #eee}.brand{font-weight:800;font-size:22px;color:var(--blue)}.brand span{color:var(--pink)}nav a{margin-left:28px;text-decoration:none;color:var(--ink);font-weight:600;cursor:pointer}.wrap{max-width:1120px;margin:auto;padding:58px 24px}.hero{min-height:calc(100vh - 76px);display:flex;align-items:center;background:radial-gradient(circle at 80% 25%,#ffd2df 0 10%,transparent 11%),radial-gradient(circle at 90% 80%,#dce2ff 0 15%,transparent 16%)}h1{font-size:clamp(42px,7vw,78px);line-height:1.02;margin:15px 0;max-width:720px;letter-spacing:-3px}.eyebrow{color:var(--pink);font-weight:800;letter-spacing:2px;text-transform:uppercase}.lead{font-size:20px;color:var(--muted);max-width:580px;line-height:1.6}.buttons{display:flex;gap:14px;margin-top:34px;flex-wrap:wrap}button,.button{border:0;border-radius:12px;padding:14px 21px;background:var(--blue);color:white;font-weight:700;font-size:15px;cursor:pointer;text-decoration:none}.secondary{background:#fff;color:var(--blue);box-shadow:0 4px 18px #28377116}.page-head{margin-bottom:35px}.page-head h1{font-size:50px;letter-spacing:-2px}.card{background:#fff;border-radius:20px;padding:25px;box-shadow:0 8px 35px #28377112}.search{width:100%;padding:17px;border:2px solid #e5e7f0;border-radius:12px;font-size:17px;margin:10px 0 28px;outline-color:var(--blue)}table{width:100%;border-collapse:collapse;font-size:14px}th{text-align:left;color:var(--muted);font-size:12px;text-transform:uppercase;letter-spacing:.7px}td,th{padding:16px 10px;border-bottom:1px solid #edf0f5}td:first-child{font-weight:750}.tag{background:#e5f7ef;color:#16805c;border-radius:20px;padding:5px 10px;font-size:12px;font-weight:700}.results{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:18px}.result h3{margin:0 0 5px;color:var(--blue)}.result p{color:var(--muted);line-height:1.5;margin:7px 0}.hidden{display:none}@media(max-width:650px){nav{padding:0 20px}nav a{margin-left:10px;font-size:13px}.wrap{padding:35px 18px}h1{letter-spacing:-2px}.card{padding:15px;overflow:auto}table{min-width:720px}}
</style></head><body><nav><a class="brand" onclick="show('home')">ngana<span>.</span></a><div><a onclick="show('data')">Data</a><a onclick="show('search')">Language Search</a></div></nav>
<main id="home" class="hero"><div class="wrap"><div class="eyebrow">A living atlas of Australia</div><h1>Hear the stories in every language.</h1><p class="lead">Explore the richness, resilience and diversity of Aboriginal languages across the continent.</p><div class="buttons"><button onclick="show('data')">Explore the data →</button><button class="secondary" onclick="show('search')">Find a language</button></div></div></main>
<main id="data" class="wrap hidden"><div class="page-head"><div class="eyebrow">Language directory</div><h1>All language data</h1><p class="lead">A snapshot of languages, communities and their current vitality.</p></div><div class="card"><table><thead><tr><th>Language</th><th>Region</th><th>Family</th><th>Speakers</th><th>Status</th><th>Community</th></tr></thead><tbody id="rows"></tbody></table></div></main>
<main id="search" class="wrap hidden"><div class="page-head"><div class="eyebrow">Discover a voice</div><h1>Language search</h1><p class="lead">Search by language, region, family or community.</p></div><div class="card"><input class="search" id="query" placeholder="Try “Northern Territory” or “Warlpiri”" oninput="search()"><div id="results" class="results"></div></div></main>
<script>const data=%DATA%;function show(page){['home','data','search'].forEach(x=>document.getElementById(x).classList.toggle('hidden',x!==page));if(page==='data')renderTable();if(page==='search')search();scrollTo(0,0)}function renderTable(){rows.innerHTML=data.map(x=>`<tr><td>${x.name}</td><td>${x.region}</td><td>${x.family}</td><td>${x.speakers.toLocaleString()}</td><td><span class="tag">${x.status}</span></td><td>${x.community}</td></tr>`).join('')}function search(){let q=(query.value||'').toLowerCase();let found=data.filter(x=>Object.values(x).some(v=>String(v).toLowerCase().includes(q)));results.innerHTML=found.map(x=>`<div class="result"><h3>${x.name}</h3><p>${x.region} · ${x.family}</p><p><b>${x.speakers.toLocaleString()}</b> speakers · <span class="tag">${x.status}</span></p><p>${x.community}</p></div>`).join('')||'<p>No languages found. Try another search.</p>'}</script></body></html>'''


class App(BaseHTTPRequestHandler):
	def do_GET(self):
		if self.path != "/":
			self.send_error(404)
			return
		content = PAGE.replace("%DATA%", json.dumps(LANGUAGES)).encode()
		self.send_response(200)
		self.send_header("Content-Type", "text/html; charset=utf-8")
		self.send_header("Content-Length", str(len(content)))
		self.end_headers()
		self.wfile.write(content)

	def log_message(self, *_):
		pass


if __name__ == "__main__":
	print("Ngana is running at http://localhost:8000")
	HTTPServer(("localhost", 8000), App).serve_forever()
