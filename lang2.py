"""A colourful three-page explorer for Australian Aboriginal languages.

Run with: streamlit run lang2.py
"""
import tkinter as tk
from tkinter import ttk

st.set_page_config(page_title="Wangka | Language Explorer", page_icon="🪃", layout="wide")

# Illustrative starter records, not a definitive or authoritative catalogue.
LANGUAGES = [
	{"Language": "Noongar", "Region": "Southwest", "Status": "Revitalising", "Speakers": "Growing", "Language family": "Pama–Nyungan", "Traditional Country": "Southwest Western Australia", "Notes": "A language of the Noongar peoples, with active community-led learning and revitalisation."},
	{"Language": "Pitjantjatjara", "Region": "Central Australia", "Status": "Strong", "Speakers": "Thousands", "Language family": "Pama–Nyungan", "Traditional Country": "Central Australia and the western deserts", "Notes": "Spoken across the APY Lands and neighbouring regions; closely related to Yankunytjatjara."},
	{"Language": "Yankunytjatjara", "Region": "Central Australia", "Status": "Strong", "Speakers": "Thousands", "Language family": "Pama–Nyungan", "Traditional Country": "Central Australia", "Notes": "A western desert language with strong community use and connections to Pitjantjatjara."},
	{"Language": "Wiradjuri", "Region": "Southeast", "Status": "Revitalising", "Speakers": "Growing", "Language family": "Pama–Nyungan", "Traditional Country": "Central New South Wales", "Notes": "A major language of New South Wales, supported by substantial revitalisation work."},
	{"Language": "Yolŋu Matha", "Region": "Top End", "Status": "Strong", "Speakers": "Thousands", "Language family": "Multiple language groups", "Traditional Country": "Northeast Arnhem Land", "Notes": "A collective name for related languages spoken across northeast Arnhem Land."},
	{"Language": "Murrinh-Patha", "Region": "Top End", "Status": "Strong", "Speakers": "Thousands", "Language family": "Non-Pama–Nyungan", "Traditional Country": "Port Keats / Wadeye region", "Notes": "A widely spoken language in the Wadeye area of the Northern Territory."},
	{"Language": "Arrernte", "Region": "Central Australia", "Status": "Strong", "Speakers": "Thousands", "Language family": "Pama–Nyungan", "Traditional Country": "Alice Springs and surrounding Country", "Notes": "A group of languages of Central Australia, including Central and Eastern Arrernte."},
	{"Language": "Kaurna", "Region": "Southwest", "Status": "Revitalising", "Speakers": "Growing", "Language family": "Pama–Nyungan", "Traditional Country": "Adelaide Plains, South Australia", "Notes": "The language of the Adelaide Plains, undergoing community-led revitalisation."},
	{"Language": "Palawa kani", "Region": "Tasmania", "Status": "Revitalising", "Speakers": "Growing", "Language family": "Language revival", "Traditional Country": "Tasmania / lutruwita", "Notes": "A contemporary language revival project drawing on records of Tasmanian Aboriginal languages."},
	{"Language": "Kriol", "Region": "Top End", "Status": "Strong", "Speakers": "Thousands", "Language family": "Creole", "Traditional Country": "Northern Australia", "Notes": "A creole language spoken by many Aboriginal communities across northern Australia."},
	{"Language": "Warlpiri", "Region": "Central Australia", "Status": "Strong", "Speakers": "Thousands", "Language family": "Pama–Nyungan", "Traditional Country": "Tanami and Central Australia", "Notes": "A major language of Central Australia with strong intergenerational transmission."},
	{"Language": "Gumbaynggirr", "Region": "Southeast", "Status": "Revitalising", "Speakers": "Growing", "Language family": "Pama–Nyungan", "Traditional Country": "Mid-north coast of New South Wales", "Notes": "A language of the mid-north coast with active teaching and revitalisation programs."},
]
df = pd.DataFrame(LANGUAGES)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');
.stApp{background:#fbf8f1;color:#252d28;font-family:'DM Sans',sans-serif}
[data-testid="stSidebar"]{background:#173d35}[data-testid="stSidebar"] *{color:#fff8e9!important}
h1,h2,h3{font-family:'Playfair Display',serif!important;color:#173d35}
.hero{padding:3rem;border-radius:24px;background:linear-gradient(120deg,#173d35,#246657 65%,#c66c43);color:#fff8e9;margin:1rem 0 1.5rem}
.hero h1{color:#fff8e9!important;font-size:3rem;margin:.2rem 0}.hero p{font-size:1.12rem;max-width:680px;color:#f4e9d5}
.eyebrow{text-transform:uppercase;letter-spacing:.16em;font-size:.75rem;font-weight:700;color:#c66c43}
.note{padding:1rem 1.2rem;border-left:4px solid #c66c43;background:#f2eadb;border-radius:8px}
div[data-testid="stMetric"]{background:white;padding:1rem;border-radius:14px;border:1px solid #eee5d6}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
	st.markdown("## 🪃 Wangka")
	st.caption("Australian language explorer")
	page = st.radio("Explore", ["Home", "Data", "Language Search"], label_visibility="collapsed")
	st.markdown("---")
	st.caption("Language names and status are diverse and community-defined. This sample is illustrative, not a definitive catalogue.")

if page == "Home":
	st.markdown('<div class="hero"><div class="eyebrow" style="color:#e9b979">LANGUAGES · COUNTRY · COMMUNITY</div><h1>Every language carries a world.</h1><p>Explore the remarkable diversity of Aboriginal languages across Australia. Browse the collection, discover regional patterns, and learn about individual languages.</p></div>', unsafe_allow_html=True)
	st.markdown("### Where would you like to begin?")
	left, right = st.columns(2)
	with left:
		st.markdown("#### 📊 Language data")
		st.write("Browse the catalogue and explore its distribution by region and status.")
		if st.button("Explore the data →", use_container_width=True):
			st.session_state["page"] = "Data"
			st.rerun()
	with right:
		st.markdown("#### 🔎 Find a language")
		st.write("Search by language name, region, family, or status and open a language profile.")
		if st.button("Search languages →", use_container_width=True):
			st.session_state["page"] = "Language Search"
			st.rerun()
	st.markdown('<div class="note"><b>A note on respect:</b> Aboriginal and Torres Strait Islander languages belong to their communities. Names, spelling, knowledge, and status can vary; follow community preferences and trusted local sources.</div>', unsafe_allow_html=True)
elif page == "Data":
	st.markdown('<div class="eyebrow">EXPLORE THE COLLECTION</div>', unsafe_allow_html=True)
	st.title("Language data")
	st.write("Browse the available sample records and explore regional patterns.")
	a, b = st.columns(2)
	a.metric("Languages in collection", len(df))
	b.metric("Regions represented", df["Region"].nunique())
	st.markdown("#### Languages by region")
	counts = df.groupby("Region", as_index=False).size().rename(columns={"size": "Languages"}).sort_values("Languages", ascending=False)
	charts = st.columns(2)
	with charts[0]:
		fig = px.bar(counts, x="Region", y="Languages", color="Region", text="Languages", color_discrete_sequence=px.colors.qualitative.Safe)
		fig.update_layout(showlegend=False, plot_bgcolor="#fbf8f1", paper_bgcolor="#fbf8f1", margin=dict(l=10,r=10,t=20,b=10))
		st.plotly_chart(fig, use_container_width=True)
	with charts[1]:
		status_counts = df.groupby("Status", as_index=False).size().rename(columns={"size": "Languages"})
		fig = px.pie(status_counts, names="Status", values="Languages", hole=.55, color_discrete_sequence=["#246657", "#e2a25b", "#c66c43"])
		fig.update_layout(paper_bgcolor="#fbf8f1", margin=dict(l=10,r=10,t=20,b=10))
		st.plotly_chart(fig, use_container_width=True)
	st.markdown("#### All language records")
	st.dataframe(df.set_index("Language"), use_container_width=True)
else:
	st.markdown('<div class="eyebrow">DISCOVER A LANGUAGE</div>', unsafe_allow_html=True)
	st.title("Language search")
	st.write("Search the collection or narrow it down by region and language status.")
	query = st.text_input("Search", placeholder="Try a language, region, family, or keyword…", label_visibility="collapsed")
	c1, c2 = st.columns(2)
	regions = ["All regions"] + sorted(df["Region"].unique().tolist())
	statuses = ["All statuses"] + sorted(df["Status"].unique().tolist())
	region = c1.selectbox("Filter by region", regions)
	status = c2.selectbox("Filter by language status", statuses)
	results = df.copy()
	if region != "All regions":
		results = results[results["Region"] == region]
	if status != "All statuses":
		results = results[results["Status"] == status]
	if query.strip():
		results = results[results.astype(str).apply(lambda col: col.str.contains(query.strip(), case=False, na=False)).any(axis=1)]
	st.caption(f"{len(results)} language{'s' if len(results) != 1 else ''} found")
	if results.empty:
		st.info("No matches found. Try changing your search or filters.")
	for _, record in results.iterrows():
		with st.container(border=True):
			col, action = st.columns([4, 1])
			col.markdown(f"#### {record['Language']}")
			col.caption(f"{record['Region']} · {record['Status']} · {record['Language family']}")
			if action.button("View profile", key=f"profile_{record['Language']}"):
				st.session_state["selected_language"] = record["Language"]
				st.rerun()
	selected = st.session_state.get("selected_language")
	if selected and selected in results["Language"].values:
		record = df[df["Language"] == selected].iloc[0]
		st.markdown("---")
		st.markdown('<div class="eyebrow">LANGUAGE PROFILE</div>', unsafe_allow_html=True)
		st.title(record["Language"])
		x, y, z = st.columns(3)
		x.metric("Region", record["Region"])
		y.metric("Status", record["Status"])
		z.metric("Speakers", record["Speakers"])
		st.markdown(f"**Language family**  \n{record['Language family']}")
		st.markdown(f"**Traditional Country**  \n{record['Traditional Country']}")
		st.markdown(f"**About**  \n{record['Notes']}")

if __name__ == "__main__":
	LanguageExplorerApp().mainloop()