import csv, requests, json
import os
NAVER_ID = os.getenv("NAVER_ID")
NAVER_SECRET = os.getenv("NAVER_SECRET")
# text = "말모이"
# 영화별로 다음과 같은 내용을 저장합니다. 영진위 영화 대표코드 , 영화 썸네일 이미지의 URL , 하
# 이퍼텍스트 link , 유저 평점
f = open("boxoffice.csv","r",encoding = "utf-8")
movies = csv.reader(f)

for movie in movies:
    data = requests.get("https://openapi.naver.com/v1/search/movie.json?query="+ movie[1],
                headers = {
                    "X-Naver-Client-Id":f'{NAVER_ID}',
                    "X-Naver-Client-Secret":f'{NAVER_SECRET}'
                }
    )
    moviecode = movie[0]
    data = data.json()
    url = data["items"][0]["image"]
    link = data["items"][0]["link"]
    rating = data["items"][0]["userRating"]
    
    f = open("movie_naver.csv", "a+", encoding = "utf-8")
    csv_w = csv.writer(f)
    csv_w.writerow([moviecode,url,link,rating])
    f.close()

