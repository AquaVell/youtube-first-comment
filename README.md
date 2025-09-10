# YouTube First Comment Script

This project is a Python script that automatically tries to post the first comment on a new YouTube video from a specific channel.  
It was inspired by a real event when MrBeast reached 100 million subscribers and announced a prize for the first comment on his next video, which would come out at a set date and time.  

## Why I built this
I built this script for fun and as a programming challenge.
I didn’t go the extra mile with faster hosting or servers closer to YouTube HQ and also I didn’t win — but it was a great learning experience.

## How it works
- The script continuously checks the number of videos on the target channel (every 0.1 seconds to avoid hitting free API limits).  
- When a new video appears, it compares the latest video ID to the ones you manually set (`lastVideoId` and `lastShortId`).  
- If it’s a new video, the script publishes a predefined comment using your account credentials.  

## Setup
1. Get a YouTube API key and a `client_secret.json` from [Google Cloud Console](https://console.cloud.google.com/).  
2. Fill in the following variables in the script:  
   - `apiKey` → Your YouTube API key  
   - `id_channel` → The target channel ID  
   - `lastVideoId` and `lastShortId` → The last known video IDs to avoid commenting on old videos  

3. Install dependencies `pip install -r requirements.txt`

4. Run the script

## Disclaimer
- This project is **for educational purposes only**.  
- Do **not** use it to spam, harass, or manipulate contests unfairly.  
- Misuse may violate YouTube’s Terms of Service and could result in account suspension.
