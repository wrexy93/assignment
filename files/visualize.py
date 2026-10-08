"""
visualize.py
Chart-building functions for the Region Stats screen. Each function returns a
matplotlib Figure so the app screens can embed it directly, e.g. st.pyplot(fig)
if using Streamlit, regardless of which UI framework is chosen.

IMPORTANT: calling one of these functions only BUILDS a chart in memory and
returns it - it does not display or save anything by itself. To actually see
a chart you must either:
  - call fig.savefig("name.png")   to save it as an image, or
  - call plt.show()                to pop up a window (needs a display)
Run this file directly (python visualize.py) for a working example of both.
"""

import os
import matplotlib.pyplot as plt


def region_count_chart(region_counts, top_n=15):
    """Bar chart of number of languages per region (top_n regions shown)."""
    items = list(region_counts.items())[:top_n]
    labels = [i[0] for i in items]
    values = [i[1] for i in items]

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(labels, values, color="#4C72B0")
    ax.set_title("Number of Languages per Region")
    ax.set_xlabel("Region")
    ax.set_ylabel("Language Count")
    ax.tick_params(axis="x", rotation=45)
    fig.tight_layout()
    return fig


def completeness_pie_chart(completeness_stats):
    """Pie chart showing how many languages have known coordinates vs not."""
    labels = ["Has coordinates", "Missing coordinates"]
    values = [completeness_stats["with_coordinates"], completeness_stats["without_coordinates"]]

    fig, ax = plt.subplots(figsize=(5, 5))
    ax.pie(values, labels=labels, autopct="%1.1f%%", colors=["#55A868", "#C44E52"])
    ax.set_title("Location Data Completeness")
    fig.tight_layout()
    return fig


def language_map(records, region_code=None):
    """
    Scatter plot of language locations using lat/lon as a simple stand-in map.
    If region_code is given, only languages linked to that region are plotted.
    """
    points = [r for r in records if r["has_coordinates"]]
    if region_code:
        points = [r for r in points if region_code in r["regions"]]

    lats = [r["lat"] for r in points]
    lons = [r["lon"] for r in points]

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.scatter(lons, lats, s=15, alpha=0.6, color="#8172B2")
    title = f"Language Locations ({region_code})" if region_code else "Language Locations (All Regions)"
    ax.set_title(title)
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    fig.tight_layout()
    return fig


if __name__ == "__main__":
    # Working example: builds all three charts from the real data, saves
    # them to a charts/ folder next to this script (always works, no
    # display needed), and also tries to pop up windows if your machine
    # supports it. Run this file directly to check the charts look right.
    from data_loader import load_austlang
    from analysis import count_languages_per_region, coordinate_completeness

    records = load_austlang()

    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "charts")
    os.makedirs(out_dir, exist_ok=True)

    fig1 = region_count_chart(count_languages_per_region(records))
    fig1.savefig(os.path.join(out_dir, "region_counts.png"))

    fig2 = completeness_pie_chart(coordinate_completeness(records))
    fig2.savefig(os.path.join(out_dir, "completeness.png"))

    fig3 = language_map(records, "WA")
    fig3.savefig(os.path.join(out_dir, "wa_map.png"))

    print(f"Saved 3 charts to: {out_dir}")
    print("Opening them in a window now (close the windows to end the script)...")

    try:
        plt.show()
    except Exception as e:
        print(f"Could not open a display window ({e}) - but the PNG files above were saved fine.")
