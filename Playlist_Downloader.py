from bs4 import BeautifulSoup
import requests
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
playlist=input("Enter playlist link: ")
current_dir=os.getcwd()
playlist_name=input("Enter the name of the playlist: ")
while True:
    where_to_save=input("Enter the place you want your playlist folder to be saved in: ")
    try:
        os.chdir(where_to_save)
        break
    except:
        print("invalid path")
os.makedirs(playlist_name)
path_to_save=(str(os.getcwd())+"\\"+playlist_name)
os.chdir(current_dir)
tag1=[]
while len(tag1)<1:
    website=requests.get(playlist)
    website=website.text
    soup=BeautifulSoup(website,"html.parser")
    tags=soup.find_all("a")
    tag1=["https://www.youtube.com"+str(tag.get("href")) for tag in tags if str(tag.get("href")).startswith("/watch?")]
    tag1=list(set(tag1))
lk = os.path.join(os.getcwd(), "chromedriver", )
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2,"download.default_directory" : path_to_save}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(lk, options=chrome_options)
i=0
counter=0
while i<len(tag1):
    link=tag1[i]
    driver.get("https://ytmp3.cc/en13/")
    sleep(5)
    input_link=driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/form/input[1]")
    input_link.send_keys(link,Keys.ENTER)
    sleep(3)
    try:
        down=driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[3]/a[1]")
        down.click()
        sleep(6)
        i+=1
        counter+=1
        print(i,"/",len(tag1)," songs downloaded")
    except:
        i += 1
        continue
print("process done "+counter+" songs downloaded to "+path_to_save)