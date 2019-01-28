import requests
import csv

f = open("movie_naver.csv","r+",encoding="utf-8")
csv_r = csv.reader(f)

for img in csv_r:
    file = img[0]+".jpg"
    url = img[1]
    res = requests.get(url, timeout=0.5)
    
    if res.status_code == 200:
        with open("./images/"+file, 'wb') as f:#폴더를 만들어주고 시작해야함
            f.write(res.content)
            
f.close()
