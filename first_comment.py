import os
import sys
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
import googleapiclient.errors
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import requests
import time

apiKey = "" # Your API Key
id_channel = "" # Target Channel ID

#Insert last videoID ans ShortID (both just to make sure)
lastVideoId = ""
lastShortId = ""
comment = "Congrats on 100 Mill!"

youtube = build("youtube", "v3", developerKey=apiKey)

def get_channel_stats(youtube, id_channel):
    oldCount = -1
    request = youtube.channels().list(part = ["statistics", "contentDetails","snippet", "status"], id = id_channel)
    while(oldCount != -2):
        time.sleep(0.1)
        response = request.execute()
        videos = response["items"][0]["statistics"]["videoCount"]
        if(oldCount == (int(videos) - 1)):
            oldCount = -2
        else:
            oldCount = int(videos)
        print(videos)
    stats = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    return stats
    
def getVideoId(youtube, stats):
    request = youtube.playlistItems().list(
        part=['snippet'],
        playlistId = stats
    )
    i = 0
    while(i == 0):
        response = request.execute()
        latestVideoId = response["items"][0]["snippet"]["resourceId"]["videoId"]
        print(latestVideoId)
        if(str(latestVideoId) != lastVideoId and str(latestVideoId) != lastShortId):   
            break
    return latestVideoId



scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def commentVideo():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    scriptPath = os.path.dirname(__file__)
    client_secret_Path = os.path.join(scriptPath, "client_secret.json")
    client_secrets_file = client_secret_Path

    # Get credentials and create an API client
    flow = InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    flow.run_local_server(port=8080, prompt="consent", authorization_prompt_message="")
    credentials = flow.credentials
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    #Loop waiting for new video
    stats = get_channel_stats(youtube, id_channel)
    #Gets latest video ID
    latestVideoId = getVideoId(youtube, stats)
    #Comment
    request_body = {
        "snippet": {
            "videoId": latestVideoId,
            "topLevelComment": {
                "snippet": {
                    "textOriginal": comment
                }
            }
        }
    }

    request = youtube.commentThreads().insert(
        part="snippet",
        body=request_body
    )
    response = request.execute()
    print(response)

commentVideo()