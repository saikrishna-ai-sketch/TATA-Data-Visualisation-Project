# Tata Forage Data Visualisation - Executive Presentation & Video Capstone

## Overview
This repository contains the complete executive presentation package for the **Tata Data Visualisation: Empowering Business with Effective Insights** virtual experience program. 

The presentation is specifically addressed to the **Chief Executive Officer (CEO)** and **Chief Marketing Officer (CMO)**. It translates cleaned retail transaction data into strategic, actionable business insights.

---

## Deliverables Summary

1. **[presentation_script.md](file:///c:/Users/jangi/OneDrive/Desktop/TATA-Forage-Data-Visualisation/presentation_script.md)**: Full ~5-minute slide-by-slide executive narration script with exact verified numbers, visual cues, slide timestamps, and executive summaries.
2. **Slide Visual Assets (`slides/`)**: 7 high-resolution (1920x1080) slide graphics rendered in dark-navy corporate executive style (`slide_1.png` through `slide_7.png`).
3. **`presentation_video.mp4`**: Compiled 5-minute MP4 presentation video featuring synchronized TTS voice narration, slide transitions, and animated timing.
4. **[data_cleaning.py](file:///c:/Users/jangi/OneDrive/Desktop/TATA-Forage-Data-Visualisation/data_cleaning.py)** & **`cleaned_online_retail.csv`**: Tata Forage verified dataset containing 531,283 clean records.

---

## Executive Presentation Structure (~5 Minutes)

| Slide | Title | Key Metric / Insight | Duration |
| :--- | :--- | :--- | :--- |
| **Slide 1** | Title & Executive Introduction | Scope & Agenda for CEO & CMO | ~45 sec |
| **Slide 2** | Data Cleaning Workflow | Audit of 531,283 rows (`Quantity >= 1`, `UnitPrice >= 0`) | ~40 sec |
| **Slide 3** | Question 1: 2011 Monthly Revenue | Line Chart: Q4 Peak at **£1,509,496.33** (+115% vs baseline) | ~50 sec |
| **Slide 4** | Question 2: Top 10 Countries (Excl. UK) | Bar Chart: **Netherlands (£285.4k)** & **EIRE (£283.5k)** lead | ~50 sec |
| **Slide 5** | Question 3: Top 10 Customers | Column Chart: Top account **ID 14646 (£280.2k)** across 74 orders | ~45 sec |
| **Slide 6** | Question 4: Global Product Demand | Geographic Map: **Netherlands (200.9k units)** & **EIRE (147.4k units)** | ~45 sec |
| **Slide 7** | Strategic Growth Recommendations | Q4 Inventory Prep, VIP Loyalty Program, EU/APAC Scaling | ~45 sec |

---

## Key Data Verification Metrics

All data points in the presentation and video are strictly verified against `cleaned_online_retail.csv`:

### Question 1: 2011 Monthly Revenue Trend
- **Jan**: £691,364.56
- **Feb**: £523,631.89
- **Mar**: £717,639.36
- **Apr**: £537,808.62
- **May**: £770,536.02
- **Jun**: £761,739.90
- **Jul**: £719,221.19
- **Aug**: £759,138.38
- **Sep**: £1,058,590.17
- **Oct**: £1,154,979.30
- **Nov**: **£1,509,496.33** (*Annual Peak*)
- **Dec**: £638,792.68 (*Partial month through Dec 9*)

### Question 2: Top 10 Countries by Revenue (Excl. UK)
1. **Netherlands**: £285,446.34 (200,937 units)
2. **EIRE**: £283,453.96 (147,447 units)
3. **Germany**: £228,867.14 (119,263 units)
4. **France**: £209,715.11 (112,104 units)
5. **Australia**: £138,521.31 (84,209 units)
6. **Spain**: £61,577.11 (27,951 units)
7. **Switzerland**: £57,089.90 (30,630 units)
8. **Belgium**: £41,196.34 (23,237 units)
9. **Sweden**: £38,378.33 (36,083 units)
10. **Japan**: £37,416.37 (26,016 units)

### Question 3: Top 10 Customers by Revenue Concentration
1. **ID 14646**: £280,206.02 (74 orders)
2. **ID 18102**: £259,657.30 (60 orders)
3. **ID 17450**: £194,550.79 (46 orders)
4. **ID 16446**: £168,472.50 (2 orders)
5. **ID 14911**: £143,825.06 (201 orders)
6. **ID 12415**: £124,914.53 (21 orders)
7. **ID 14156**: £117,379.63 (55 orders)
8. **ID 17511**: £91,062.38 (31 orders)
9. **ID 16029**: £81,024.84 (63 orders)
10. **ID 12346**: £77,183.60 (1 order)

---

## Actionable Recommendations for Executive Leadership

### For the CEO
1. **Q4 Inventory & Supply Chain Expansion**: Build up buffer inventory by August to prevent stockouts during the Q4 peak (£1.51M in Nov).
2. **APAC Logistics Footprint**: Establish regional distribution partnerships in Australia and Japan to reduce shipping lead times.

### For the CMO
1. **VIP Key Account Management**: Top 10 customer accounts contribute over £1.53M in sales. Assign dedicated Account Managers and custom volume pricing tiers.
2. **Targeted European Expansion**: Concentrate marketing expenditure in high-conversion EU markets (Netherlands, EIRE, Germany, France).

---

## How to Re-Run Video & Chart Generation

```bash
# 1. Regenerate slide charts
python generate_charts.py

# 2. Synthesize narration and render video
python generate_audio_and_video.py
```
