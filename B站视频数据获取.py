import requests
from bs4 import BeautifulSoup
import datetime
import time


#定义URL
url="https://www.bilibili.com/video/BV11p421R7Sw/"
#定义时间间隔（秒）
interval=10

# 定义 API 的 headers
headers ={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"
}
def get_info():   
    response = requests.get(url,headers=headers)
    html=response.text
    soup=BeautifulSoup(html,"html.parser")

    #播放量 views
    item=soup.find("span",attrs={"class":"view item"})
    if item:
        views = item.get_text(strip=True)

    #点赞数 likes
    item=soup.find("span",attrs={"class":"video-like-info video-toolbar-item-text"})
    if item:
        likes = item.get_text(strip=True)

    #收藏量 marks
    item=soup.find("span",attrs={"class":"video-fav-info video-toolbar-item-text"})
    if item:
        marks = item.get_text(strip=True)
    #投币数 coins
    item=soup.find('span', attrs={ "class":'video-coin-info video-toolbar-item-text'})
    if item:
        coins = item.get_text(strip=True)
    #弹幕数 bullets 
    item=soup.find('span', attrs={ "class":'dm item'})
    if item:
        bullets = item.get_text(strip=True)

    #获取时间
    f_time=datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")

    # 将获取的信息保存
    with open("data.txt",mode="a") as f:
        f.write(f_time+"    ")
        f.write(" 播放"+views)
        f.write(" 点赞"+likes)
        f.write(" 收藏"+marks)
        f.write(" 硬币"+coins)
        f.write(" 弹幕"+bullets)
        f.write("\n")
 #运行次数
n=0  
while True:
    get_info()
    n+=1
    print(n)
    time.sleep(interval)    
    
