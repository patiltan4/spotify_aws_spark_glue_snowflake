import json
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import boto3
from datetime import datetime

def lambda_handler(event, context):
   client_id = os.environ.get("client_id")
   client_secret = os.environ.get("client_secret")
   
   client_credentials_manager = SpotifyClientCredentials(client_id =client_id, client_secret=client_secret)
   sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
   
   #top 100 songs currently on spotify
   playlist_link = "https://open.spotify.com/playlist/4hOKQuZbraPDIfaGbM3lKI"
    
   playlist_URI = playlist_link.split("/")[-1]
   data = sp.playlist_tracks(playlist_URI)
   #print(data)
   
   client = boto3.client('s3')
   
   #dynamic filename based on timestamp
   filename = "spotify_raw_" + str(datetime.now()) + ".json"

 
   
   client.put_object(
      Bucket = "my_bucket",
      Key = "raw_data/to_process/" + filename,
      Body = json.dumps(data)
      )
   
   
   
