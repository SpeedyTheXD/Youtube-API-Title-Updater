# Title auto-updater

This program auto-updates your Youtube's video title

## How to use:

1. To use this program u need two files: client_secret.json and token.json
2. After obtaining these two files (which will be explained below), move them to the same folder as "youtube_title_updater.py" 
3. Put your Youtube video's link into the "input_video.txt" file
4. Open an IDE and run the "youtube_title_updater.py" file
5. Check if it works or not!
6. You can modify the change_video_tile() function to whatever suits your use. Have fun!


   *P/s: You can schedule your code to be run daily by using task scheduler in Windows or host it on a cloud website (I used PythonAnywhere)*


## How to obtain client_secret.json and token.json

- To get the client_secret.json file you can follow the steps in this video: [https://www.youtube.com/watch?v=kr_OYm3ZmUI](https://www.youtube.com/watch?v=-rYPc30VB-A&pp=ygUeY2xpZW50X3NlY3JldC5qc29uIGZvciB5b3V0dWJl)

    ***You need to make sure to rename the whatever client.json file you got to client_secret.json for the .py file to work*** 

- To get the token.json file:

    1. Install the Google API client library
    
       - Run this code in your terminal to install library for Python to work with Youtube Data API
       
          `pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib`

    2. Run the "youtube_title_updater.py" file, it will generates the token.json file for u if client_secret.json is valid

       **If your token.json file doesn't work, you might have to manually add this line to your token.json file:**

           "type": "authorized_user",

## My demo video:

[![Watch the video](https://img.youtube.com/vi/cQadDqgcadA/maxresdefault.jpg)](https://youtu.be/cQadDqgcadA)

### [Watch this video](https://youtu.be/cQadDqgcadA)

















