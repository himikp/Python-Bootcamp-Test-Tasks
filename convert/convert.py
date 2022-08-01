from moviepy.editor import *
import os
import requests
import wget

video_url= input("Enter url for video to convert: ")

def download_video(url=''):
    
    try:    
        response = requests.get(url=url, stream=True)
               
        with open('req_video.mp4', 'wb') as file:
            for chunk in response.iter_content():
                if chunk:
                    file.write(chunk)
            
        return 'Video successfully downloaded!'
    
    except Exception as _ex:
        return 'Check the URL please!'

def video_to_gif():
    clip = (VideoFileClip("req_video.mp4"))
    clip.write_gif("output.gif", fps = 2)
    print (os.getcwd() + "\output.gif")


def main():
    download_video(video_url)
    video_to_gif()
    
    
if __name__ == "__main__":
    main()
