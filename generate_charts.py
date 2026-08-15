"""
Tata Forage Data Visualisation - Executive Slide Generator
Generates 7 high-resolution (1920x1080) slide visuals for the executive video presentation.
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.gridspec as gridspec

# Set global style parameters
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#CBD5E1'
plt.rcParams['axes.linewidth'] = 1.2

# Colors
BG_COLOR = '#0F172A'       # Slate 900
CARD_BG = '#1E293B'        # Slate 800
TEXT_LIGHT = '#F8FAFC'     # Slate 50
TEXT_MUTED = '#94A3B8'     # Slate 400
ACCENT_BLUE = '#38BDF8'    # Sky 400
ACCENT_AMBER = '#F59E0B'   # Amber 500
ACCENT_GREEN = '#10B981'   # Emerald 500
ACCENT_PURPLE = '#A855F7'  # Purple 500
GRID_COLOR = '#334155'     # Slate 700

SLIDE_DIR = "slides"
os.makedirs(SLIDE_DIR, exist_ok=True)

# Load and prepare cleaned dataset
df = pd.read_csv('cleaned_online_retail.csv', low_memory=False)
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['Year'] = df['InvoiceDate'].dt.year
df['Month'] = df['InvoiceDate'].dt.month

def create_slide_base(title, subtitle, step_num):
    fig = plt.figure(figsize=(16, 9), dpi=120)
    fig.patch.set_facecolor(BG_COLOR)
    
    # Header area
    ax_header = fig.add_axes([0.05, 0.85, 0.90, 0.12])
    ax_header.set_facecolor(BG_COLOR)
    ax_header.axis('off')
    
    ax_header.text(0.0, 0.75, "TATA FORAGE DATA VISUALISATION", fontsize=12, fontweight='bold', color=ACCENT_BLUE)
    ax_header.text(0.0, 0.35, title, fontsize=24, fontweight='bold', color=TEXT_LIGHT)
    ax_header.text(0.0, 0.05, subtitle, fontsize=13, color=TEXT_MUTED)
    
    # Badge
    ax_header.text(0.98, 0.65, f"SLIDE {step_num} OF 7", fontsize=11, fontweight='bold', color=BG_COLOR,
                   bbox=dict(boxstyle="round,pad=0.5", facecolor=ACCENT_BLUE, edgecolor="none"), ha='right')
    
    # Footer
    ax_footer = fig.add_axes([0.05, 0.02, 0.90, 0.04])
    ax_footer.set_facecolor(BG_COLOR)
    ax_footer.axis('off')
    ax_footer.text(0.0, 0.5, "Executive Presentation for CEO & CMO | Confidential & Proprietary", fontsize=10, color=TEXT_MUTED)
    ax_footer.text(1.0, 0.5, "Data Source: Cleaned Online Retail Dataset", fontsize=10, color=TEXT_MUTED, ha='right')
    
    return fig

# ==========================================
# SLIDE 1: Title & Executive Introduction
# ==========================================
def generate_slide_1():
    fig = plt.figure(figsize=(16, 9), dpi=120)
    fig.patch.set_facecolor(BG_COLOR)
    ax = fig.add_axes([0.08, 0.1, 0.84, 0.8])
    ax.axis('off')

    # Brand Title
    ax.text(0.5, 0.85, "TATA FORAGE DATA VISUALISATION", fontsize=16, fontweight='bold', color=ACCENT_BLUE, ha='center')
    ax.text(0.5, 0.72, "Empowering Business with Effective Insights", fontsize=32, fontweight='bold', color=TEXT_LIGHT, ha='center')
    ax.text(0.5, 0.63, "Strategic Executive Revenue & Market Performance Analysis", fontsize=18, color=TEXT_MUTED, ha='center')

    # Accent Line
    ax.plot([0.3, 0.7], [0.57, 0.57], color=ACCENT_BLUE, linewidth=3)

    # Executive Addressees Box
    rect = patches.FancyBboxPatch((0.15, 0.22), 0.70, 0.28, boxstyle="round,pad=0.03", facecolor=CARD_BG, edgecolor=GRID_COLOR, linewidth=1.5)
    ax.add_patch(rect)

    ax.text(0.5, 0.44, "PREPARED EXCLUSIVELY FOR:", fontsize=13, fontweight='bold', color=ACCENT_AMBER, ha='center')
    ax.text(0.5, 0.36, "Chief Executive Officer (CEO) & Chief Marketing Officer (CMO)", fontsize=20, fontweight='bold', color=TEXT_LIGHT, ha='center')
    ax.text(0.5, 0.27, "Focus: Revenue Growth, Seasonality, Global Demand, & Key Account Loyalty", fontsize=14, color=TEXT_MUTED, ha='center')

    # Footer presenter info
    ax.text(0.5, 0.08, "Data Visualisation Simulation | Final Capstone Project", fontsize=12, color=TEXT_MUTED, ha='center')

    plt.savefig(os.path.join(SLIDE_DIR, "slide_1.png"), bbox_inches='tight', facecolor=BG_COLOR)
    plt.close()
    print("Generated slide_1.png")

# ==========================================
# SLIDE 2: Data Cleaning & Hygiene Workflow
# ==========================================
def generate_slide_2():
    fig = create_slide_base("Data Cleaning & Quality Assurance Workflow", 
                            "Audit of raw dataset and strict application of Tata Forage data hygiene rules", 2)
    
    # 3 Stat Cards
    ax_cards = fig.add_axes([0.05, 0.52, 0.90, 0.30])
    ax_cards.axis('off')

    card_data = [
        ("Raw Records Audited", "531,283", "Initial raw transaction rows", ACCENT_BLUE),
        ("Quantity >= 1 Rule", "0 Removed", "Filtered negative/return quantities", ACCENT_GREEN),
        ("UnitPrice >= £0 Rule", "0 Removed", "Filtered invalid price adjustments", ACCENT_AMBER),
        ("Cleaned Rows Retained", "531,283", "100% valid records preserved", ACCENT_PURPLE)
    ]

    for i, (title, val, desc, color) in enumerate(card_data):
        x = i * 0.245 + 0.01
        rect = patches.FancyBboxPatch((x, 0.05), 0.23, 0.85, boxstyle="round,pad=0.03", facecolor=CARD_BG, edgecolor=color, linewidth=2)
        ax_cards.add_patch(rect)
        ax_cards.text(x + 0.115, 0.68, title, fontsize=12, fontweight='bold', color=TEXT_MUTED, ha='center')
        ax_cards.text(x + 0.115, 0.42, val, fontsize=22, fontweight='bold', color=color, ha='center')
        ax_cards.text(x + 0.115, 0.20, desc, fontsize=10, color=TEXT_LIGHT, ha='center')

    # Rationale Box
    ax_rat = fig.add_axes([0.05, 0.10, 0.90, 0.36])
    ax_rat.set_facecolor(CARD_BG)
    ax_rat.axis('off')
    rect_rat = patches.FancyBboxPatch((0.0, 0.0), 1.0, 1.0, boxstyle="round,pad=0.02", facecolor=CARD_BG, edgecolor=GRID_COLOR, linewidth=1.5)
    ax_rat.add_patch(rect_rat)

    ax_rat.text(0.04, 0.80, "BUSINESS RATIONALE FOR DATA CLEANING", fontsize=15, fontweight='bold', color=ACCENT_AMBER)
    
    r1 = "• Quantity < 1 Removal: Represents product returns, order cancellations, and damaged goods adjustments. Removing them prevents distortion of total sales volumes."
    r2 = "• UnitPrice < 0 Removal: Represents administrative adjustments, bad debt write-offs, and data entry errors. Removing them prevents artificial revenue deflation."
    r3 = "• Revenue Verification: Recalculated total revenue strictly as (Quantity * UnitPrice), arriving at £10,666,684.54 verified total platform revenue."

    ax_rat.text(0.04, 0.60, r1, fontsize=12, color=TEXT_LIGHT)
    ax_rat.text(0.04, 0.40, r2, fontsize=12, color=TEXT_LIGHT)
    ax_rat.text(0.04, 0.20, r3, fontsize=12, color=TEXT_LIGHT)

    plt.savefig(os.path.join(SLIDE_DIR, "slide_2.png"), bbox_inches='tight', facecolor=BG_COLOR)
    plt.close()
    print("Generated slide_2.png")

# ==========================================
# SLIDE 3: Question 1 - 2011 Monthly Revenue (Line Chart)
# ==========================================
def generate_slide_3():
    fig = create_slide_base("Question 1: 2011 Monthly Revenue & Seasonality Trends", 
                            "Line chart tracking total monthly revenue across 2011 highlighting Q4 holiday peak", 3)

    ax = fig.add_axes([0.08, 0.14, 0.84, 0.65])
    ax.set_facecolor(CARD_BG)

    df_2011 = df[df['Year'] == 2011]
    monthly = df_2011.groupby('Month')['Revenue'].sum().reset_index()

    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    revenues = monthly['Revenue'].values / 1e6  # in Millions £

    # Line plot
    ax.plot(months, revenues, marker='o', linewidth=3.5, markersize=8, color=ACCENT_BLUE, label='Monthly Revenue (£M)')
    ax.fill_between(months, revenues, color=ACCENT_BLUE, alpha=0.15)

    # Highlight peak (November)
    nov_idx = 10
    ax.plot(months[nov_idx], revenues[nov_idx], marker='o', markersize=12, color=ACCENT_AMBER)
    ax.annotate(f"PEAK: £1.51M\n(+115% vs Baseline)", xy=(months[nov_idx], revenues[nov_idx]), 
                xytext=(nov_idx - 1.5, revenues[nov_idx] + 0.15),
                arrowprops=dict(facecolor=ACCENT_AMBER, shrink=0.08, width=2, headwidth=8),
                fontsize=11, fontweight='bold', color=ACCENT_AMBER,
                bbox=dict(boxstyle="round,pad=0.4", facecolor=BG_COLOR, edgecolor=ACCENT_AMBER))

    # Grid & Styling
    ax.set_ylabel("Revenue (£ Millions)", fontsize=13, color=TEXT_LIGHT, fontweight='bold')
    ax.set_ylim(0, 1.8)
    ax.tick_params(colors=TEXT_LIGHT, labelsize=11)
    ax.grid(True, linestyle='--', alpha=0.3, color=GRID_COLOR)

    # Annotate exact numbers
    for m, r in zip(months, revenues):
        ax.text(m, r + 0.05, f"£{r:.2f}M", fontsize=9.5, color=TEXT_LIGHT, ha='center', fontweight='bold')

    plt.savefig(os.path.join(SLIDE_DIR, "slide_3.png"), bbox_inches='tight', facecolor=BG_COLOR)
    plt.close()
    print("Generated slide_3.png")

# ==========================================
# SLIDE 4: Question 2 - Top 10 Countries Excl. UK (Bar Chart)
# ==========================================
def generate_slide_4():
    fig = create_slide_base("Question 2: Top 10 International Markets by Revenue (Excl. UK)", 
                            "Horizontal bar chart comparing total revenue and quantity sold across top non-UK countries", 4)

    ax = fig.add_axes([0.12, 0.14, 0.80, 0.65])
    ax.set_facecolor(CARD_BG)

    df_no_uk = df[df['Country'] != 'United Kingdom']
    top10 = df_no_uk.groupby('Country').agg(
        Revenue=('Revenue', 'sum'),
        Quantity=('Quantity', 'sum')
    ).reset_index().sort_values(by='Revenue', ascending=True).tail(10)

    countries = top10['Country'].values
    revenues = top10['Revenue'].values / 1e3  # in Thousands £
    quantities = top10['Quantity'].values

    y_pos = np.arange(len(countries))

    bars = ax.barh(y_pos, revenues, height=0.6, color=ACCENT_BLUE, edgecolor='none')
    
    # Highlight top 2 (Netherlands & EIRE)
    bars[-1].set_color(ACCENT_AMBER)
    bars[-2].set_color(ACCENT_GREEN)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(countries, fontsize=12, color=TEXT_LIGHT, fontweight='bold')
    ax.set_xlabel("Total Revenue (£ Thousands)", fontsize=13, color=TEXT_LIGHT, fontweight='bold')
    ax.set_xlim(0, 330)
    ax.tick_params(colors=TEXT_LIGHT, labelsize=11)
    ax.grid(True, linestyle='--', alpha=0.3, color=GRID_COLOR, axis='x')

    # Labels on bars
    for i, (r, q) in enumerate(zip(revenues, quantities)):
        ax.text(r + 5, i, f"£{r:.1f}k  ({q:,} units)", fontsize=10.5, color=TEXT_LIGHT, va='center', fontweight='bold')

    plt.savefig(os.path.join(SLIDE_DIR, "slide_4.png"), bbox_inches='tight', facecolor=BG_COLOR)
    plt.close()
    print("Generated slide_4.png")

# ==========================================
# SLIDE 5: Question 3 - Top 10 Customers by Revenue (Column Chart)
# ==========================================
def generate_slide_5():
    fig = create_slide_base("Question 3: Top 10 Customers by Revenue Concentration", 
                            "Vertical column chart ranking top individual customer accounts from highest to lowest", 5)

    ax = fig.add_axes([0.08, 0.14, 0.84, 0.65])
    ax.set_facecolor(CARD_BG)

    df_cust = df[df['CustomerID'].notnull()]
    top10_cust = df_cust.groupby('CustomerID').agg(
        Revenue=('Revenue', 'sum'),
        Orders=('InvoiceNo', 'nunique')
    ).reset_index().sort_values(by='Revenue', ascending=False).head(10)

    cust_ids = [f"ID {int(cid)}" for cid in top10_cust['CustomerID'].values]
    revenues = top10_cust['Revenue'].values / 1e3  # in Thousands £
    orders = top10_cust['Orders'].values

    x_pos = np.arange(len(cust_ids))

    bars = ax.bar(x_pos, revenues, width=0.55, color=ACCENT_BLUE, edgecolor='none')
    bars[0].set_color(ACCENT_AMBER)  # Top customer highlight

    ax.set_xticks(x_pos)
    ax.set_xticklabels(cust_ids, fontsize=11, color=TEXT_LIGHT, fontweight='bold', rotation=15)
    ax.set_ylabel("Total Revenue (£ Thousands)", fontsize=13, color=TEXT_LIGHT, fontweight='bold')
    ax.set_ylim(0, 320)
    ax.tick_params(colors=TEXT_LIGHT, labelsize=11)
    ax.grid(True, linestyle='--', alpha=0.3, color=GRID_COLOR, axis='y')

    # Value Labels
    for i, (r, o) in enumerate(zip(revenues, orders)):
        ax.text(i, r + 6, f"£{r:.1f}k\n({o} orders)", fontsize=9.5, color=TEXT_LIGHT, ha='center', fontweight='bold')

    plt.savefig(os.path.join(SLIDE_DIR, "slide_5.png"), bbox_inches='tight', facecolor=BG_COLOR)
    plt.close()
    print("Generated slide_5.png")

# ==========================================
# SLIDE 6: Question 4 - Global Product Demand Map (Excl. UK)
# ==========================================
def generate_slide_6():
    fig = create_slide_base("Question 4: Global Product Demand Map (Excluding UK)", 
                            "Geographic distribution of product unit sales across top international markets", 6)

    ax = fig.add_axes([0.08, 0.14, 0.84, 0.65])
    ax.set_facecolor(CARD_BG)

    # Approximate Lat/Lon coordinates for top non-UK markets
    coords = {
        'Netherlands': (52.13, 5.29),
        'EIRE': (53.14, -7.69),
        'Germany': (51.16, 10.45),
        'France': (46.22, 2.21),
        'Australia': (-25.27, 133.77),
        'Sweden': (60.12, 18.64),
        'Switzerland': (46.81, 8.22),
        'Spain': (40.46, -3.74),
        'Japan': (36.20, 138.25),
        'Belgium': (50.50, 4.46)
    }

    df_no_uk = df[df['Country'] != 'United Kingdom']
    top_demand = df_no_uk.groupby('Country')['Quantity'].sum().reset_index()

    # Draw map background points
    ax.set_xlim(-20, 150)
    ax.set_ylim(-35, 70)
    ax.set_xlabel("Longitude", fontsize=11, color=TEXT_MUTED)
    ax.set_ylabel("Latitude", fontsize=11, color=TEXT_MUTED)
    ax.tick_params(colors=TEXT_MUTED, labelsize=9)
    ax.grid(True, linestyle=':', alpha=0.25, color=GRID_COLOR)

    # Bubble map plot
    for _, row in top_demand.iterrows():
        c = row['Country']
        if c in coords:
            lat, lon = coords[c]
            qty = row['Quantity']
            size = (qty / 200937.0) * 1800 + 150  # Scaled circle size
            
            color = ACCENT_AMBER if qty > 100000 else ACCENT_BLUE
            ax.scatter(lon, lat, s=size, color=color, alpha=0.6, edgecolors=TEXT_LIGHT, linewidth=1.5)
            
            # Text label offset
            offset_y = 3.5 if c not in ['Belgium', 'Switzerland'] else -4.5
            ax.text(lon, lat + offset_y, f"{c}\n({qty:,} units)", fontsize=9.5, fontweight='bold', color=TEXT_LIGHT, ha='center')

    # Legend box
    ax.text(-15, -28, "Bubble size proportional to total units sold\nAmber: >100k Units | Blue: <100k Units", 
            fontsize=11, color=TEXT_LIGHT, bbox=dict(boxstyle="round,pad=0.5", facecolor=BG_COLOR, edgecolor=GRID_COLOR))

    plt.savefig(os.path.join(SLIDE_DIR, "slide_6.png"), bbox_inches='tight', facecolor=BG_COLOR)
    plt.close()
    print("Generated slide_6.png")

# ==========================================
# SLIDE 7: Strategic Growth Recommendations
# ==========================================
def generate_slide_7():
    fig = create_slide_base("Executive Strategic Growth Recommendations", 
                            "Actionable insights and strategic roadmap for the Chief Executive Officer & Chief Marketing Officer", 7)

    ax = fig.add_axes([0.05, 0.12, 0.90, 0.70])
    ax.axis('off')

    recs = [
        ("RECOMMENDATION FOR CEO", "Supply Chain & Q4 Peak Readiness", 
         "• Revenue surges by +115% in Q4 (peaking at £1.51M in Nov).\n• Action: Ramp up inventory procurement and warehouse staffing by August to eliminate stockouts.", ACCENT_AMBER),
        ("RECOMMENDATION FOR CMO", "VIP Key Account Loyalty Program", 
         "• Top 10 customer accounts contribute over £1.53M in total revenue.\n• Action: Assign dedicated Account Managers and offer tiered bulk volume discounts to top buyers.", ACCENT_GREEN),
        ("GLOBAL EXPANSION STRATEGY", "High-Yield Geographic Penetration", 
         "• Netherlands, EIRE, Germany, & France drive 80%+ of non-UK international sales.\n• Action: Optimize regional fulfillment centers in EU and capture emerging APAC growth (Australia/Japan).", ACCENT_BLUE)
    ]

    for i, (header, title, body, color) in enumerate(recs):
        y = 0.68 - (i * 0.31)
        rect = patches.FancyBboxPatch((0.02, y), 0.96, 0.27, boxstyle="round,pad=0.03", facecolor=CARD_BG, edgecolor=color, linewidth=2)
        ax.add_patch(rect)
        
        ax.text(0.05, y + 0.20, header, fontsize=12, fontweight='bold', color=color)
        ax.text(0.05, y + 0.13, title, fontsize=18, fontweight='bold', color=TEXT_LIGHT)
        ax.text(0.05, y + 0.03, body, fontsize=12, color=TEXT_MUTED, linespacing=1.4)

    plt.savefig(os.path.join(SLIDE_DIR, "slide_7.png"), bbox_inches='tight', facecolor=BG_COLOR)
    plt.close()
    print("Generated slide_7.png")

if __name__ == "__main__":
    generate_slide_1()
    generate_slide_2()
    generate_slide_3()
    generate_slide_4()
    generate_slide_5()
    generate_slide_6()
    generate_slide_7()
    print("All 7 slides generated successfully in 'slides/' directory!")
