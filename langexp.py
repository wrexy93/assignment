"""Serve the Australian Aboriginal Language Explorer in a browser."""  # Documents the app entry point.

import base64  # Decodes the bundled dataset payload.
import csv  # Reads dataset rows.
import gzip  # Decompresses the bundled dataset payload.
import json  # Encodes rows for the browser API.
import webbrowser  # Opens the running app in the user's browser.
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer  # Serves the local app and its data.
from io import StringIO  # Exposes the embedded CSV text to the CSV reader.
from pathlib import Path  # Locates optional files and the README beside this script.

from embedded_data import DATASET_GZIP_BASE64  # Bundles the catalogue with the application.

README_PATH = Path(__file__).resolve().parent / "README.md"  # Stores the project instructions for browser download.
REQUIRED_COLUMNS = {"austlang_code", "primary_name", "lat", "lon", "state_territory", "status"}  # Defines the CSV fields used by the app.

PAGE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Australian Aboriginal Language Explorer</title>
<style>
:root{color-scheme:light;--ink:#183b35;--green:#286451;--coral:#c45e43;--paper:#f6f7f2;--line:#dce4dc;--muted:#5e7069;--white:#fff}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);font:16px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}
button,input{font:inherit}
.topbar{display:flex;align-items:center;justify-content:space-between;gap:20px;padding:16px max(22px,calc((100vw - 1180px)/2));background:var(--ink);color:white}
.brand{font-size:14px;font-weight:750;letter-spacing:.04em}
.nav{display:flex;gap:8px}
.nav button,.action{border:0;border-radius:4px;padding:10px 14px;background:transparent;color:white;cursor:pointer}
.nav button[aria-current="page"],.nav button:hover{background:#ffffff20}
main{max-width:1180px;margin:auto;padding:42px 24px 64px}
.eyebrow{margin:0 0 8px;color:var(--coral);font-size:12px;font-weight:750;text-transform:uppercase}
h1,h2,h3,p{margin-top:0}
h1{max-width:760px;margin-bottom:12px;font:600 38px/1.13 Georgia,serif}
.intro{max-width:700px;color:var(--muted)}
.hero{margin:28px 0;padding:26px;background:var(--green);color:white}
.hero h2{margin:0 0 8px;font:600 25px/1.2 Georgia,serif}
.hero p{margin:0;color:#eef5ed}
.actions{display:flex;flex-wrap:wrap;gap:10px;margin-top:20px}
.action{background:var(--coral);font-weight:700}
.action.secondary{background:white;color:var(--ink);border:1px solid var(--line)}
.note{max-width:900px;border-left:3px solid var(--coral);padding:10px 14px;color:var(--muted);background:#fff}
.page[hidden]{display:none}
.searchbar{display:flex;align-items:center;gap:12px;margin:22px 0 12px}
.searchbar input{width:100%;min-width:0;padding:13px 14px;border:1px solid #aebdb4;border-radius:4px;background:white;color:var(--ink)}
.result-count{flex:none;color:var(--muted);font-size:14px}
.table-wrap{overflow:auto;border:1px solid var(--line);background:white}
table{width:100%;border-collapse:collapse;text-align:left}
th,td{padding:11px 13px;border-bottom:1px solid var(--line);vertical-align:top}
th{position:sticky;top:0;background:#e9efea;color:var(--ink);font-size:12px;text-transform:uppercase}
td:first-child{font-weight:650}
.empty{padding:18px;color:var(--muted)}
.metrics{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin:22px 0 28px}
.metric{padding:17px;background:white;border:1px solid var(--line)}
.metric strong{display:block;color:var(--green);font:600 30px Georgia,serif}
.metric span{color:var(--muted);font-size:12px;font-weight:700}
.data-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:28px}
.data-section{padding-top:17px;border-top:2px solid var(--green)}
.data-section h2{margin:0 0 4px;font:600 21px Georgia,serif}
.section-note{margin-bottom:14px;color:var(--muted);font-size:14px}
.count-row{display:grid;grid-template-columns:minmax(130px,190px) 1fr 44px;align-items:center;gap:10px;margin:9px 0;font-size:14px}
.count-label{overflow-wrap:anywhere}
.bar-track{height:10px;background:#e4eae4}
.bar{height:100%;background:var(--coral)}
.count-value{text-align:right;font-variant-numeric:tabular-nums;font-weight:700}
.unavailable{padding:14px;background:white;border:1px dashed #aebdb4;color:var(--muted)}
footer{max-width:1180px;margin:auto;padding:0 24px 26px;color:var(--muted);font-size:13px}
@media(max-width:680px){.topbar{align-items:flex-start;flex-direction:column;gap:10px}.nav{width:100%}.nav button{flex:1;padding:9px 5px;font-size:14px}main{padding:30px 16px 42px}h1{font-size:31px}.data-grid{grid-template-columns:1fr;gap:24px}.count-row{grid-template-columns:minmax(110px,145px) 1fr 38px;gap:7px}.metrics{gap:8px}.metric{padding:13px}.metric strong{font-size:25px}.searchbar{align-items:stretch;flex-direction:column}.result-count{align-self:flex-end}}
</style>
</head>
<body>
<header class="topbar">
<div class="brand">AUSTRALIAN ABORIGINAL LANGUAGE EXPLORER</div>
<nav class="nav" aria-label="Main navigation">
<button type="button" data-page="home" aria-current="page">Home</button>
<button type="button" data-page="explore">Explore Languages</button>
<button type="button" data-page="data">Data</button>
</nav>
</header>
<main>
<section class="page" id="home">
<p class="eyebrow">Language catalogue</p>
<h1>Australian Aboriginal Language Explorer</h1>
<p class="intro">Search the supplied language records and explore how this catalogue is distributed across the listed states and territories.</p>
<div class="hero">
<h2>Explore the collection</h2>
<p>Browse language names and catalogue details, or review the available counts.</p>
<div class="actions">
<button class="action" type="button" data-page="explore">Explore Languages</button>
<button class="action secondary" type="button" data-page="data">View Data</button>
</div>
</div>
<p class="note">Catalogue status is not a measure of whether a language is actively spoken. This dataset does not include speaker vitality or community-defined regional classifications.</p>
</section>
<section class="page" id="explore" hidden>
<p class="eyebrow">Browse the records</p>
<h1>Explore Languages</h1>
<p class="intro">Search language names, codes, catalogue status, states or territories, and coordinates.</p>
<label class="searchbar"><input id="search" type="search" placeholder="Search language, region, etc." autocomplete="off"><span class="result-count" id="result-count"></span></label>
<div class="table-wrap"><table><thead><tr><th>Language</th><th>Austlang code</th><th>State / territory</th><th>Catalogue status</th></tr></thead><tbody id="results"></tbody></table><p class="empty" id="empty" hidden>No matching records. Try a different search.</p></div>
</section>
<section class="page" id="data" hidden>
<p class="eyebrow">Dataset summary</p>
<h1>Data</h1>
<p class="intro">Counts are calculated from the supplied CSV. A catalogue record is not necessarily a distinct language or evidence of current speaker vitality.</p>
<div class="actions" style="margin-top: 12px; margin-bottom: 20px;">
<button class="action secondary" id="download-readme" type="button">Download README.md</button>
</div>
<div class="metrics"><div class="metric"><strong id="record-total">—</strong><span>CATALOGUE RECORDS</span></div><div class="metric"><strong id="name-total">—</strong><span>DISTINCT PRIMARY NAMES</span></div></div>
<div class="data-grid">
<section class="data-section"><h2>Records by language status</h2><p class="section-note">These are the CSV's record-status labels, not active / inactive vitality ratings.</p><div id="status-counts"></div></section>
<section class="data-section"><h2>Most represented geographic areas</h2><p class="section-note">Distinct primary names by state or territory. Names linked to multiple jurisdictions appear in each.</p><div id="place-counts"></div><p class="section-note" id="missing-places"></p></section>
<section class="data-section"><h2>Distribution across major regions</h2><p class="unavailable">Unavailable: the CSV has no region or major-region field. No regional values have been inferred.</p></section>
<section class="data-section"><h2>Language vitality</h2><p class="unavailable">Unavailable: the CSV's status field describes catalogue records, not whether a language is active or inactive.</p></section>
</div>
</section>
</main>
<footer>Counts describe this dataset only. Verify source, permissions, names, and community-preferred information with the relevant data provider and communities.</footer>
<script>
const stateNames={ACT:"Australian Capital Territory",NSW:"New South Wales",NT:"Northern Territory",QLD:"Queensland",SA:"South Australia",TAS:"Tasmania",TSI:"Torres Strait Islands",VIC:"Victoria",WA:"Western Australia"};
let records=[];
const byId=id=>document.getElementById(id);
function showPage(name){document.querySelectorAll(".page").forEach(page=>{page.hidden=page.id!==name});document.querySelectorAll("[data-page]").forEach(button=>{if(button.tagName==="BUTTON"&&button.closest("nav")){if(button.dataset.page===name){button.setAttribute("aria-current","page")}else{button.removeAttribute("aria-current")}}});window.scrollTo(0,0)}
function addCountRows(target,counts,labels={}){const container=byId(target);container.replaceChildren();const maximum=Math.max(1,...Object.values(counts));Object.entries(counts).sort((a,b)=>b[1]-a[1]||a[0].localeCompare(b[0])).forEach(([key,count])=>{const row=document.createElement("div");row.className="count-row";const label=document.createElement("span");label.className="count-label";label.textContent=labels[key]||key;const track=document.createElement("div");track.className="bar-track";const bar=document.createElement("div");bar.className="bar";bar.style.width=`${count/maximum*100}%`;track.append(bar);const value=document.createElement("span");value.className="count-value";value.textContent=count.toLocaleString();row.append(label,track,value);container.append(row)})}
function renderData(){const uniqueNames=new Set(records.map(row=>row.primary_name.trim().toLocaleLowerCase()).filter(Boolean));byId("record-total").textContent=records.length.toLocaleString();byId("name-total").textContent=uniqueNames.size.toLocaleString();const statusCounts={};const placeNames={};let missingPlaces=0;records.forEach(row=>{const status=row.status||"Unspecified";statusCounts[status]=(statusCounts[status]||0)+1;const places=row.state_territory.split(",").map(place=>place.trim()).filter(Boolean);if(!places.length){missingPlaces+=1}places.forEach(place=>{if(!placeNames[place]){placeNames[place]=new Set()}if(row.primary_name.trim()){placeNames[place].add(row.primary_name.trim().toLocaleLowerCase())}})});addCountRows("status-counts",statusCounts);const placeCounts=Object.fromEntries(Object.entries(placeNames).map(([place,names])=>[place,names.size]));addCountRows("place-counts",placeCounts,stateNames);byId("missing-places").textContent=`${missingPlaces.toLocaleString()} records have no state or territory value.`}
function renderResults(query=""){const term=query.trim().toLocaleLowerCase();const matches=records.filter(row=>!term||Object.values(row).some(value=>value.toLocaleLowerCase().includes(term)));const body=byId("results");body.replaceChildren();matches.forEach(row=>{const tr=document.createElement("tr");[row.primary_name||"Unnamed",row.austlang_code,row.state_territory.replaceAll(",",", ")||"Not recorded",row.status||"Unspecified"].forEach(value=>{const cell=document.createElement("td");cell.textContent=value;tr.append(cell)});body.append(tr)});byId("result-count").textContent=`${matches.length.toLocaleString()} records`;byId("empty").hidden=matches.length!==0}
document.querySelectorAll("[data-page]").forEach(button=>button.addEventListener("click",()=>showPage(button.dataset.page)));
byId("download-readme").addEventListener("click",()=>{window.location.href="/download/readme";});
byId("search").addEventListener("input",event=>renderResults(event.target.value));
async function start(){try{const response=await fetch("/api/records");if(!response.ok){throw new Error(`Dataset request failed (${response.status})`)}records=await response.json();renderData();renderResults()}catch(error){document.querySelector("main").innerHTML=`<h1>Dataset could not be loaded</h1><p>${error.message}</p>`}}
start();
</script>
</body>
</html>"""  # Contains the browser pages, responsive design, search, and visual summaries.


def load_records(file_path=None):  # Reads and validates the bundled CSV or an optional replacement file.
	if file_path is None:  # Uses embedded data by default so no separate CSV download is needed.
		csv_text = gzip.decompress(base64.b64decode(DATASET_GZIP_BASE64)).decode("utf-8-sig")
		source = StringIO(csv_text)
	else:  # Allows a replacement CSV for testing or customized catalogues.
		source = Path(file_path).open("r", encoding="utf-8-sig", newline="")
	with source:  # Supports UTF-8 names and CSV line endings.
		reader = csv.DictReader(source)  # Reads rows using the CSV header names.
		if not reader.fieldnames:  # Checks that the CSV has a header row.
			raise ValueError("The dataset has no header row.")  # Reports an invalid or empty CSV.
		missing = REQUIRED_COLUMNS - set(reader.fieldnames)  # Finds fields required by the app but absent from the file.
		if missing:  # Stops startup if this is not the expected dataset.
			raise ValueError("Dataset is missing columns: " + ", ".join(sorted(missing)))  # Lists the unavailable fields.
		records = [{key: (value or "").strip() for key, value in row.items()} for row in reader]  # Normalizes each CSV value for searching and display.
	if not records:  # Ensures pages have records to display.
		raise ValueError("The dataset contains no records.")  # Explains why the app cannot continue.
	return records  # Supplies validated records to the web server.


class AppHandler(BaseHTTPRequestHandler):  # Routes browser page and dataset requests.
	records = []  # Holds the validated dataset shared by request handlers.

	def do_GET(self):  # Responds to browser GET requests.
		if self.path == "/":  # Serves the main application page.
			content = PAGE.encode("utf-8")  # Encodes the HTML document for HTTP.
			content_type = "text/html; charset=utf-8"  # Labels the response as a UTF-8 webpage.
		elif self.path == "/api/records":  # Serves actual CSV rows to the browser.
			content = json.dumps(self.records, ensure_ascii=False).encode("utf-8")  # Encodes names and records as JSON.
			content_type = "application/json; charset=utf-8"  # Labels the response as JSON.
		elif self.path == "/download/readme":  # Downloads the project README for the user.
			if not README_PATH.exists():
				self.send_error(404, "README not found")
				return
			content = README_PATH.read_bytes()  # Reads the markdown file for download.
			content_type = "text/markdown; charset=utf-8"  # Labels the response as markdown text.
			self.send_response(200)
			self.send_header("Content-Type", content_type)
			self.send_header("Content-Length", str(len(content)))
			self.send_header("Content-Disposition", "attachment; filename=README.md")
			self.send_header("Cache-Control", "no-store")
			self.end_headers()
			self.wfile.write(content)
			return
		else:  # Rejects routes the app does not provide.
			self.send_error(404, "Not found")  # Returns a standard not-found response.
			return  # Stops handling the unknown route.
		self.send_response(200)  # Marks the requested resource as successful.
		self.send_header("Content-Type", content_type)  # Tells the browser how to interpret the response.
		self.send_header("Content-Length", str(len(content)))  # Supplies the response size.
		self.send_header("Cache-Control", "no-store")  # Ensures refreshed dataset responses are not stale.
		self.end_headers()  # Finishes the HTTP response headers.
		self.wfile.write(content)  # Sends the page or dataset to the browser.

	def log_message(self, format, *args):  # Keeps routine HTTP requests out of the terminal.
		return  # Leaves the terminal free for the app URL and shutdown message.


def create_server(port=0):  # Creates a local server on an available port by default.
	AppHandler.records = load_records()  # Loads bundled data before accepting requests.
	return ThreadingHTTPServer(("127.0.0.1", port), AppHandler)  # Serves only on this computer.


def main():  # Opens the local site and runs its HTTP server.
	server = create_server()  # Binds an available local port and loads the CSV.
	url = "http://{}:{}/".format(*server.server_address)  # Builds the browser URL for the running server.
	print("Australian Aboriginal Language Explorer is running at " + url)  # Shows the URL in the terminal.
	print("Press Ctrl+C in this terminal to stop the app.")  # Explains how to shut down the local server.
	webbrowser.open(url)  # Opens the app in the default browser.
	try:  # Keeps serving until the user stops the app.
		server.serve_forever()  # Handles page and dataset requests.
	except KeyboardInterrupt:  # Handles the normal Ctrl+C shutdown.
		print("\nExplorer stopped.")  # Confirms the server has stopped.
	finally:  # Releases the local port on every exit path.
		server.server_close()  # Closes the listening socket.


if __name__ == "__main__":  # Starts the app only when this script is run directly.
	main()  # Launches the browser-based explorer.
