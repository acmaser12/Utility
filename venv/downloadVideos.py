# downloadVideos.py
# downloads videos from Vimeo from a specified folder
# updated: 1.14.19
# written by: Adam Maser

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import vimeo

userName = "vtraining@paradigmeducation.com"
password = "Paradigm875!"
project_id = "1164689"  # this is the folder ID, change this depending on the desired folder

# login sequence using Selenium (ensures that the program is operating logged in)
driver = webdriver.Chrome('/chromedriver')  # path to Chromedriver
driver.get("https://vimeo.com/log_in")
element = driver.find_element_by_id("signup_email")
element.send_keys(userName)
element = driver.find_element_by_id("login_password")
element.send_keys(password)
element.send_keys(Keys.RETURN)

# define client API
client = vimeo.VimeoClient(
  token='ccab009a3669b3d9c8b7fb9a56d0ec83',
  key='0a872ceb37ed22b4ddf42db995149cf5469da3dd',
  secret='J1RaEfqL7jYsHepWHTXNLz419XvDRhpBXbg9J0NTKsPSgdYD8lSUSMW+7ZMN65eQB6cpv5Nn'
         '+d3zdl7mnnltj0rFuXCdZ4i0yQ1ESAGeUwSZdgP/+OMuNIpGSge91gLr'
)

# loop through all the videos on page and gather links
# note: the query parameters of the link - needs to be adjusted for projects > 100 videos
# also, timeout must be set high b/c of all the API calls
response = client.get("https://api.vimeo.com/me/projects/1164689/videos?per_page=100", timeout=9999)
videoList = response.json()

# iterate through the json data and adds video ids to array
video_ids = []
for item in videoList["data"]:
    toTrim = item["uri"]
    video_ids.append(toTrim[8:])  # trims first 8 characters off of uri, hard-coded
    # DEBUG print(item["uri"][8:])

# loop through the video_ids array and call api for download at each out.
for item in video_ids:
    response = client.get("https://api.vimeo.com/videos/" + item)
    videoInfo = response.json()
    downloadLink = videoInfo["download"][0]["link"]  # references json data
    # DEBUG print(downloadLink)
    # send selenium to download link:
    # only enable next line if you are ready for A LOT of downloading

    # driver.get(downloadLink)

# NEXT STEPS
# 1) navigate to converter site
# 2) upload files (Selenium?)
# 3) download converted file (probably already done automatically)
# 4) save to folder and exit
