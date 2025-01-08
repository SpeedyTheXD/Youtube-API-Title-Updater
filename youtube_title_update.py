import os
import re
import google.auth
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request


SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
CREDENTIALS_FILE = 'token.json'
CLIENT_SECRET_FILE = 'client_secret.json'


def authenticate_youtube():

    """Authenticate and return the YouTube API client."""
    credentials = None

    if os.path.exists(CREDENTIALS_FILE):
        try:
            # Load the credentials from the token file
            credentials, _ = google.auth.load_credentials_from_file(CREDENTIALS_FILE)
            
            if credentials and credentials.expired and credentials.refresh_token:
                credentials.refresh(Request())  
            elif not credentials.valid:
                print("Token is invalid, re-authenticating...")
                credentials = None  
        
        except Exception as e:
            print(f"Error loading credentials: {e}")
            credentials = None  

    if not credentials or not credentials.valid:
        
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())  
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            credentials = flow.run_console()

        with open(CREDENTIALS_FILE, 'w') as token:
            token.write(credentials.to_json())

    youtube = build('youtube', 'v3', credentials=credentials)
    return youtube


def change_video_title(youtube, video_id, new_title):

    """Change the title of a specific YouTube video."""
    request = youtube.videos().list(part="snippet", id=video_id)
    response = request.execute()

    if response['items']:
        video = response['items'][0]
        video['snippet']['title'] = new_title

        update_request = youtube.videos().update(
            part="snippet",
            body={
                "id": video_id,
                "snippet": video['snippet']
            }
        )
        update_response = update_request.execute()
        return update_response
    else:
        print("Video not found.")
        return None


def get_video_title(youtube, video_id):

    """Get the current title of a specific YouTube video."""
    request = youtube.videos().list(part="snippet", id=video_id)
    response = request.execute()

    if response['items']:
        video = response['items'][0]
        return video['snippet']['title']
    else:
        return None
    

def make_new_title(current_title):  # Just change the code to whatever you want the title to be

    return current_title + " updated"

def get_video_id():

    with open('input_video.txt', 'r') as file:
        url = file.read()
        video_id = url.split('v=')[1]

        return video_id

if __name__ == '__main__':

    youtube = authenticate_youtube()
    video_id = get_video_id()
    current_title = get_video_title(youtube, video_id)
    new_title = make_new_title(current_title)

    result = change_video_title(youtube, video_id, new_title)
    if result:
        print(f"Title changed successfully: {result}")
    else:
        print("Failed to change title.")
