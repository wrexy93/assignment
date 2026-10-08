"""Desktop explorer for Australian language records. Run: python3 lang3.py"""
import tkinter as tk
from tkinter import ttk

# Illustrative interface data only; consult community-approved sources.
LANGUAGES = [
	{"name": "Arrernte", "region": "Central Australia", "status": "Strong", "family": "Pama-Nyungan", "notes": "Several varieties spoken around Mparntwe and surrounding areas."},
	{"name": "Yolŋu Matha", "region": "Arnhem Land", "status": "Strong", "family": "Pama-Nyungan", "notes": "A term for related languages and varieties of north-east Arnhem Land."},
	{"name": "Pitjantjatjara", "region": "Central Australia", "status": "Strong", "family": "Pama-Nyungan", "notes": "Spoken across parts of the central desert region."},
	{"name": "Kaurna", "region": "South Australia", "status": "Revitalisation", "family": "Pama-Nyungan", "notes": "Language of the Adelaide Plains; active community-led revitalisation."},
	{"name": "Noongar", "region": "South-west Western Australia", "status": "Revitalisation", "family": "Pama-Nyungan", "notes": "Language with regional varieties and ongoing community language work."},
	{"name": "Wiradjuri", "region": "New South Wales", "status": "Revitalisation", "family": "Pama-Nyungan", "notes": "Language of a large area of central New South Wales."},
	{"name": "Palawa kani", "region": "Tasmania", "status": "Revitalisation", "family": "Language revival", "notes": "Contemporary language reclamation project led by the Tasmanian Aboriginal Centre."},
	{"name": "Warlpiri", "region": "Central Australia", "status": "Strong", "family": "Pama-Nyungan", "notes": "Spoken in communities across the Tanami region and surrounding areas."},
]
BG, INK, TEAL, CORAL, MUTED = "#F4F6F1", "#193542", "#187C78", "#E4775E", "#637781"


class Explorer(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title("Language Atlas | Australian Languages")
		self.geometry("1080x740")
		self.minsize(820, 580)
		self.configure(bg=BG)
		style = ttk.Style(self)
		style.theme_use("clam")
		style.configure("Treeview", rowheight=32, font=("Helvetica Neue", 10), background="white", fieldbackground="white", foreground=INK)
		style.configure("Treeview.Heading", font=("Helvetica Neue", 10, "bold"), background="#E5ECE7", foreground=INK)
		self.show_home()

	def reset(self):
		for widget in self.winfo_children():
			widget.destroy()

	def nav(self):
		bar = tk.Frame(self, bg=INK, height=62)
		bar.pack(fill="x")
		bar.pack_propagate(False)
		tk.Label(bar, text="LANGUAGE ATLAS", bg=INK, fg="#A9D7C6", font=("Helvetica Neue", 10, "bold")).pack(side="left", padx=25)
		for label, fn in (("Home", self.show_home), ("Data", self.show_data), ("Language Search", self.show_search)):
			tk.Button(bar, text=label, command=fn, bg=INK, fg="white", activebackground=TEAL, relief="flat", padx=13, cursor="hand2").pack(side="left", pady=12)

	def page_title(self, text, subtitle):
		tk.Label(self, text=text, bg=BG, fg=INK, font=("Helvetica Neue", 27, "bold")).pack(anchor="w", padx=36, pady=(25, 3))
		tk.Label(self, text=subtitle, bg=BG, fg=MUTED, font=("Helvetica Neue", 11)).pack(anchor="w", padx=38, pady=(0, 17))

	def show_home(self):
		self.reset(); self.nav()
		self.page_title("Explore Australia’s languages", "Discover language names, regions and community status.")
		hero = tk.Frame(self, bg=TEAL, padx=35, pady=30)
		hero.pack(fill="x", padx=36, pady=7)
		tk.Label(hero, text="Living knowledge.\nMany languages.", bg=TEAL, fg="white", justify="left", font=("Helvetica Neue", 30, "bold")).pack(anchor="w")
		tk.Label(hero, text="Explore this illustrative collection of Aboriginal and Torres Strait Islander language records.", bg=TEAL, fg="#E1F2E9", font=("Helvetica Neue", 12)).pack(anchor="w", pady=12)
		for label, fn, color in (("Browse data  →", self.show_data, CORAL), ("Search languages  →", self.show_search, INK)):
			tk.Button(hero, text=label, command=fn, bg=color, fg="white", activebackground="#275965", relief="flat", padx=16, pady=10, font=("Helvetica Neue", 11, "bold"), cursor="hand2").pack(side="left", padx=(0, 10))
		cards = tk.Frame(self, bg=BG); cards.pack(fill="x", padx=36, pady=14)
		self.card(cards, str(len(LANGUAGES)), "demo language records", CORAL).pack(side="left", fill="x", expand=True, padx=(0, 8))
		self.card(cards, str(len({x['region'] for x in LANGUAGES})), "regions represented", TEAL).pack(side="left", fill="x", expand=True, padx=8)
		self.card(cards, "Community-led", "knowledge comes first", "#C2942D").pack(side="left", fill="x", expand=True, padx=(8, 0))
		tk.Label(self, text="Language knowledge belongs to its communities. Names, spellings, access and sharing protocols vary; consult community authorities and trusted sources.", bg=BG, fg=MUTED, wraplength=900, justify="left", font=("Helvetica Neue", 10)).pack(anchor="w", padx=38, pady=18)

	@staticmethod
	def card(parent, value, caption, color):
		frame = tk.Frame(parent, bg="white", padx=18, pady=15, highlightthickness=1, highlightbackground="#E1E8E3")
		tk.Label(frame, text=value, bg="white", fg=color, font=("Helvetica Neue", 18, "bold")).pack(anchor="w")
		tk.Label(frame, text=caption, bg="white", fg=MUTED, font=("Helvetica Neue", 10)).pack(anchor="w", pady=(4, 0))
		return frame

	def table(self, parent, records, height=10):
		outer = tk.Frame(parent, bg=BG); outer.pack(fill="both", expand=True, padx=36)
		cols = ("name", "region", "status", "family")
		tree = ttk.Treeview(outer, columns=cols, show="headings", height=height)
		for key, heading, width in (("name", "LANGUAGE", 200), ("region", "REGION", 260), ("status", "STATUS", 170), ("family", "FAMILY / GROUP", 220)):
			tree.heading(key, text=heading); tree.column(key, width=width, anchor="w")
		scroll = ttk.Scrollbar(outer, orient="vertical", command=tree.yview); tree.configure(yscrollcommand=scroll.set)
		tree.pack(side="left", fill="both", expand=True); scroll.pack(side="right", fill="y")
		lookup = {}
		for record in records:
			iid = tree.insert("", "end", values=tuple(record[k] for k in cols)); lookup[iid] = record
		tree.bind("<Double-1>", lambda _e: self.detail(lookup[tree.focus()]) if tree.focus() in lookup else None)
		tree.bind("<Return>", lambda _e: self.detail(lookup[tree.focus()]) if tree.focus() in lookup else None)
		return outer, tree

	def show_data(self):
		self.reset(); self.nav(); self.page_title("Language data", "Select a row and double-click to view the full language record.")
		self.table(self, LANGUAGES, 8)
		panel = tk.Frame(self, bg="white", padx=18, pady=12, highlightthickness=1, highlightbackground="#E1E8E3")
		panel.pack(fill="both", expand=True, padx=36, pady=15)
		tk.Label(panel, text="Demo records by region", bg="white", fg=INK, font=("Helvetica Neue", 13, "bold")).pack(anchor="w")
		canvas = tk.Canvas(panel, height=145, bg="white", highlightthickness=0); canvas.pack(fill="both", expand=True)
		counts = {}
		for item in LANGUAGES: counts[item["region"]] = counts.get(item["region"], 0) + 1
		colors = (TEAL, CORAL, "#D1A63F", "#789B6B", "#897AA4")
		def draw(_event=None):
			canvas.delete("all"); width = max(canvas.winfo_width(), 300); left = min(250, width * .43); maximum = max(counts.values())
			for i, (region, count) in enumerate(sorted(counts.items(), key=lambda item: (-item[1], item[0]))):
				y = 5 + i * 24
				canvas.create_text(0, y + 8, text=region, anchor="w", fill=INK, font=("Helvetica Neue", 9))
				canvas.create_rectangle(left, y, width - 32, y + 15, fill="#EDF1ED", outline="")
				canvas.create_rectangle(left, y, left + (width - left - 32) * count / maximum, y + 15, fill=colors[i % len(colors)], outline="")
				canvas.create_text(width - 7, y + 8, text=str(count), anchor="e", fill=MUTED, font=("Helvetica Neue", 9, "bold"))
		canvas.bind("<Configure>", draw)

	def show_search(self):
		self.reset(); self.nav(); self.page_title("Language search", "Search names, regions, status or family, and filter the results.")
		controls = tk.Frame(self, bg=BG); controls.pack(fill="x", padx=36, pady=(0, 12))
		query = tk.StringVar(); region = tk.StringVar(value="All regions"); status = tk.StringVar(value="All statuses")
		entry = tk.Entry(controls, textvariable=query, font=("Helvetica Neue", 11), relief="flat", highlightthickness=1, highlightbackground="#CDD8D2")
		entry.pack(side="left", fill="x", expand=True, ipady=9, padx=(0, 9))
		entry.insert(0, "Search a language, region, status…")
		ttk.Combobox(controls, textvariable=region, state="readonly", width=25, values=["All regions"] + sorted({x["region"] for x in LANGUAGES})).pack(side="left", padx=5)
		ttk.Combobox(controls, textvariable=status, state="readonly", width=18, values=["All statuses"] + sorted({x["status"] for x in LANGUAGES})).pack(side="left", padx=(5, 0))
		result_label = tk.Label(self, bg=BG, fg=MUTED, font=("Helvetica Neue", 10)); result_label.pack(anchor="w", padx=38, pady=(0, 7))
		holder = tk.Frame(self, bg=BG); holder.pack(fill="both", expand=True)
		current = [None]
		def update(*_):
			if current[0]: current[0].destroy()
			text = query.get().strip().lower()
			if text.startswith("search a language"): text = ""
			found = [x for x in LANGUAGES if (not text or text in " ".join(x.values()).lower()) and (region.get() == "All regions" or x["region"] == region.get()) and (status.get() == "All statuses" or x["status"] == status.get())]
			result_label.config(text=f"{len(found)} result(s) · Double-click a row to open its details")
			current[0], _tree = self.table(holder, found, 14)
		query.trace_add("write", update); region.trace_add("write", update); status.trace_add("write", update)
		entry.bind("<FocusIn>", lambda _e: entry.delete(0, "end") if entry.get().startswith("Search a language") else None)
		update()

	def detail(self, record):
		self.reset(); self.nav(); self.page_title(record["name"], f"Language record · {record['region']}")
		panel = tk.Frame(self, bg="white", padx=26, pady=22, highlightthickness=1, highlightbackground="#E1E8E3")
		panel.pack(fill="x", padx=36, pady=8)
		for label, key in (("REGION", "region"), ("STATUS", "status"), ("FAMILY / GROUP", "family"), ("NOTES", "notes")):
			row = tk.Frame(panel, bg="white"); row.pack(fill="x", pady=10)
			tk.Label(row, text=label, width=20, anchor="nw", bg="white", fg=TEAL, font=("Helvetica Neue", 9, "bold")).pack(side="left")
			tk.Label(row, text=record[key], anchor="w", justify="left", wraplength=650, bg="white", fg=INK, font=("Helvetica Neue", 11)).pack(side="left", fill="x", expand=True)
		tk.Label(self, text="Illustrative demo data, not a definitive linguistic source. Verify with community-approved resources.", bg=BG, fg=MUTED, font=("Helvetica Neue", 10)).pack(anchor="w", padx=38, pady=15)
		tk.Button(self, text="← Back to search", command=self.show_search, bg=TEAL, fg="white", relief="flat", padx=15, pady=9, cursor="hand2").pack(anchor="w", padx=36)


if __name__ == "__main__":
	Explorer().mainloop()
