"""
Tata Forage Data Visualisation - Audio & MP4 Video Generator
Synthesizes speech narration for all 7 slides using Windows SAPI and renders presentation_video.mp4 via MoviePy.
"""

import os
import sys
import wave
import contextlib
import win32com.client
from moviepy import ImageClip, AudioFileClip, concatenate_videoclips

SLIDE_DIR = "slides"
AUDIO_DIR = "audio"
OUTPUT_VIDEO = "presentation_video.mp4"

os.makedirs(AUDIO_DIR, exist_ok=True)

# Narration Scripts for all 7 slides
SCRIPTS = {
    1: (
        "Good morning, Chief Executive Officer and Chief Marketing Officer. Today, I am pleased to present "
        "the strategic data visualization and revenue performance analysis for our online retail business. "
        "As our retail platform expands globally, executive leadership requires clear, data driven insights "
        "to evaluate revenue drivers, spot seasonal trends, identify key geographic growth markets, and protect "
        "our top customer relationships. In this presentation, I will walk you through our data preparation workflow, "
        "analyze monthly revenue performance across 2011, examine top international markets, evaluate customer revenue "
        "concentration, and provide actionable strategic recommendations for the CEO and CMO to capture future growth opportunities."
    ),
    2: (
        "Before conducting any business analysis, ensuring absolute data hygiene was our top priority. We audited "
        "our primary dataset containing 531,283 retail transaction records. To guarantee accurate executive insights, "
        "we enforced two strict data cleaning rules aligned with Tata guidelines. First, we filtered out all records "
        "with a Quantity below 1. Negative or zero quantities represent product returns, cancellations, or inventory adjustments. "
        "Including them would distort sales volume and obscure true purchasing behavior. Second, we removed records with a Unit "
        "Price below zero to eliminate bad debt and administrative price write offs. Following these rules, all valid transaction "
        "records were preserved, ensuring our final dataset of 531,283 rows provides a reliable foundation for executive decision making."
    ),
    3: (
        "Turning to our first key business question: How did monthly revenue perform throughout 2011? Looking at the line chart, "
        "we observe steady baseline sales from January through August, averaging approximately £700,000 per month. January opened at "
        "£691,365, followed by a slight dip in February to £523,632, before stabilizing across spring and summer. The most critical insight "
        "occurs in Q4. Starting in September, revenue surged to £1.06 million, rising further to £1.15 million in October, and reaching a "
        "massive annual peak of £1.51 million in November. November revenue grew by more than 115 percent compared to the year baseline. "
        "This dramatic upward curve reflects strong holiday seasonality, early Christmas shopping, and major promotional activity."
    ),
    4: (
        "Our second analysis examines international expansion by evaluating the top 10 countries by revenue, excluding our domestic UK market. "
        "The Netherlands leads all international markets with total revenue of £285,446, closely followed by EIRE at £283,454. Germany ranks "
        "third at £228,867, France fourth at £209,715, and Australia fifth at £138,521. Spain, Switzerland, Belgium, Sweden, and Japan complete "
        "our top ten. Notice the compelling relationship between revenue and volume: while Netherlands and EIRE generate nearly identical revenue, "
        "Netherlands achieved this across 200,937 units compared to EIRE's 147,447 units. This indicates higher bulk order sizes in the Netherlands."
    ),
    5: (
        "Next, we examine customer revenue concentration. The column chart highlights our top 10 individual customer accounts, ranked from "
        "highest to lowest. Our top account, Customer ID 14646 based in the Netherlands, is our single largest contributor, generating an "
        "impressive £280,206 across 74 orders. Customer ID 18102 ranks second with £259,657, and Customer ID 17450 ranks third at £194,551. "
        "Combined, these top 10 VIP accounts generate over £1.53 million in total revenue. Notably, Customer ID 16446 generated £168,473 across "
        "just two massive orders, while Customer ID 14911 placed 201 individual orders. This reveals two distinct high-value customer profiles: "
        "high-frequency repeat buyers and large wholesale buyers."
    ),
    6: (
        "Moving to Question 4, this geographic map visualizes total product demand volume across international markets. Western Europe forms "
        "the core of our international demand footprint. Netherlands leads global product demand with 200,937 units sold, followed by EIRE with "
        "147,447 units, Germany with 119,263 units, and France with 112,104 units. Outside Europe, Australia represents our strongest global "
        "market with 84,209 units, while Japan shows solid demand with 26,016 units. This distribution proves that while European proximity "
        "drives our current sales volume, Asia Pacific represents a high-potential growth frontier for global expansion."
    ),
    7: (
        "To conclude, I present three actionable strategic recommendations for our executive leadership. First, for the CEO: Supply Chain and "
        "Inventory Optimization. Given our Q4 revenue surge to £1.51 million in November, we must ramp up inventory procurement by August to "
        "prevent stockouts during peak holiday demand. Second, for the CMO: Key Account Loyalty Program. Our top 10 customers account for over "
        "£1.53 million in sales. We recommend establishing a VIP Client Management team with bespoke volume discounts to protect these critical "
        "relationships. Third, Targeted Geographic Expansion: Focus marketing capital on high-yield European hubs—Netherlands, EIRE, Germany, "
        "and France—while scaling logistics support for high-growth Asia Pacific markets like Australia. Thank you for your time and leadership."
    )
}

def generate_audio_files():
    print("Generating audio narration files using Windows SAPI...")
    speaker = win32com.client.Dispatch('SAPI.SpVoice')
    speaker.Rate = 2  # Executive presentation pace (~155 wpm) for ~5 min duration
    stream = win32com.client.Dispatch('SAPI.SpFileStream')

    audio_paths = {}
    for i in range(1, 8):
        wav_path = os.path.abspath(os.path.join(AUDIO_DIR, f"audio_{i}.wav"))
        print(f"  - Synthesizing audio_{i}.wav...")
        stream.Open(wav_path, 3, False)  # SSFMCreateForWrite
        speaker.AudioOutputStream = stream
        speaker.Speak(SCRIPTS[i])
        stream.Close()
        audio_paths[i] = wav_path
        
    return audio_paths

def get_audio_duration(wav_path):
    with contextlib.closing(wave.open(wav_path, 'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        return duration

def build_presentation_video(audio_paths):
    print("\nAssembling presentation_video.mp4 with MoviePy...")
    video_clips = []
    total_duration = 0.0

    for i in range(1, 8):
        slide_img = os.path.join(SLIDE_DIR, f"slide_{i}.png")
        audio_file = audio_paths[i]
        
        audio_dur = get_audio_duration(audio_file)
        duration = audio_dur + 1.0  # audio length + 1s pause
        total_duration += duration
        
        print(f"  - Slide {i}: Image '{slide_img}' | Audio '{audio_file}' | Audio Length: {audio_dur:.2f}s | Slide Duration: {duration:.2f}s")
        
        audio_clip = AudioFileClip(audio_file)
        img_clip = ImageClip(slide_img).with_duration(duration).with_audio(audio_clip)
        video_clips.append(img_clip)

    print(f"\nTotal presentation video duration: {total_duration / 60:.2f} minutes ({total_duration:.1f} seconds)")
    
    final_video = concatenate_videoclips(video_clips, method="compose")
    
    print(f"Rendering final MP4 to '{OUTPUT_VIDEO}'...")
    final_video.write_videofile(
        OUTPUT_VIDEO,
        fps=2,
        codec='libx264',
        audio_codec='aac',
        preset='ultrafast'
    )
    
    file_size_mb = os.path.getsize(OUTPUT_VIDEO) / (1024 * 1024)
    print(f"\nSUCCESS: Presentation video rendered successfully!")
    print(f"File Path: {os.path.abspath(OUTPUT_VIDEO)}")
    print(f"File Size: {file_size_mb:.2f} MB")

if __name__ == "__main__":
    paths = generate_audio_files()
    build_presentation_video(paths)
