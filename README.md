`mr.gpt.ipynb` has the main pipeline

# Scraper
```bash
yt-dlp "ytsearchall:icici lombard" \
    --force-write-archive \
    --download-archive "processed_videos.txt" \
    --write-info-json --write-subs --write-auto-subs --get-comments --skip-download \
    --extractor-args "youtube:player-client=android,web" \
    --sleep-requests 0 --sleep-interval 0 \
    -o "ICICI_Lombard_Today/%(upload_date)s_%(title)s.%(ext)s"
```
- use with --proxy to avoid ip bans (use residential rotating proxies)
- run from project root folder, data will be stored in ICICI_Lombard_Today subfolder and list of already processed videos in processed_videos.txt, so that scraping is resumable
- change the 'ytsearchall' search term before running for other targets
- can redirect new data from other targets to seperate subfolder for faster processing

# Data Processing
run to install libraries
```bash
pip install google-genai pandas openpyxl deep-translator
```
run cells in `mr.gpt.ipynb` *sequentially* to get the filtered data, following is a overview of each cell
- first cell saves `structured_customer_truth.csv` with filtered data and tags
- second cell saves `D2_Insight_Summary.md`
- third cell saves `D3_Full_Taxonomy_Audit.md`
- fourth cell adds translated text column, and saves to `structured_customer_truth_translated.xlsx`

read comments at top of each cell for more info
