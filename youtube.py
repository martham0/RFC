
import os
from pytube import YouTube
import requests

# functions: validte path, validate youtube link
class Validation ():
  def __init__(self):
    self.link = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    self.path = os.getcwd()
    self.dir = 'youtube_downloads'
  
  def validate_link(self,url:str):
    try:
        response = requests.head(url, timeout=5)
        validate = response.status_code == requests.codes.ok
    except requests.exceptions.RequestException:
        validate = False
        print('Video can not be found. Enjoy being Ricked')
    if validate == True:
      self.link = url
      
  def validate_path(self,path:str):
    pass



url = input('what youtube video would you like to download?\n')
path = input('Where would you like to save the video?(full path)\n')


user_input = Validation()
user_input.validate_link(url)
user_input.validate_path(path)

# Create directory and validate existance
os.makedirs(user_input.path)

if os.path.exists(user_input.path):
    print(f"Folder '{user_input.path}' created successfully!")
else:
    print(f"Failed to create folder '{user_input.path}'")
    
yt = YouTube(user_input.link)