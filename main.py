import yt_dlp
from googleapiclient.discovery import build
import time

def download_stream(url, outpath):
    ydl_opts = {
        'outtmpl': str(outpath) + '/%(channel)s_%(upload_date>%Y-%m-%d)s.%(ext)s',
        'live_from_start': True,
        'format': 'bestvideo+bestaudio',
        'concurrent-fragments': 10,    # Increase parallel fragment downloads
        'retries': 3,                  # Limit retries to 3
        'buffersize': 16777216,        # Set buffer size to 16 MB (in bytes)
        'limit-rate': 50331648        # Limit the rate to 48 MB/s in bytes
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except KeyboardInterrupt:
        print("\nDownload interrupted! Attempting to merge partial files...")

if __name__ == "__main__":
    API_KEY = "YOUR_API_KEY"
    while True:
        CHANNEL_USERNAME = input("Input channel name to track: ")
        youtube = build("youtube", "v3", developerKey=API_KEY)
        request = youtube.search().list(
            part="snippet",
            q=str(CHANNEL_USERNAME),
            type="channel",
            order="relevance",
            maxResults=10
        )
        response = request.execute()
        if len(response["items"]) != 0:
            print("Results found: " + str(len(response["items"])))
        index = 0
        channel_id = None
        while index < len(response["items"]):
            channel_id = response["items"][index]["id"]["channelId"]
            check_channel_req = youtube.channels().list(part="snippet,statistics", id=channel_id)
            channel_info = check_channel_req.execute()
            print("")
            print("Channel name: " + channel_info["items"][0]["snippet"]["title"])
            print("Description: " + channel_info["items"][0]["snippet"]["description"])
            print("Subscriber Count: " + str(channel_info["items"][0]["statistics"]["subscriberCount"]))
            print("Video Count: " + str(channel_info["items"][0]["statistics"]["videoCount"]))
            decision = input("Is this the correct channel? [Y/n]: ")
            print("")
            if decision == "Y" or decision == "y" or decision == "":
                break
            elif decision == "N" or decision == "n":
                index = index + 1
                if index == len(response["items"]):
                    index = 0
        if len(response["items"]) != 0:
            break
        else:
            print("No results found for specified channel try again. . .")

    OUT_PATH = input("Input path to output folder: ")

    while True:
        request_live = youtube.search().list(
            part="snippet",
            channelId=channel_id,
            type="video",
            eventType="live",
            order="date",
            maxResults=1
        )
        response_live = request_live.execute()

        if len(response_live["items"]) != 0:
            print("Livestream found on this channel starting the download. . .")
            video_id = response_live["items"][0]["id"]["videoId"]
            stream_url = "https://www.youtube.com/watch?v="+video_id
            try:
                download_stream(stream_url, OUT_PATH)
            except KeyboardInterrupt:
                print("\nLivestream download interrupted. Exiting...")
                break
        else:
            print("No livestream found on this channel at the moment. . .")
        time.sleep(90)
