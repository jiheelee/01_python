import csv, requests, json
import os
os.getenv("NAVER_ID")
#r - 읽기 모드, 파일이 없으면 Error를 발생시킴
#r+ - 읽기 쓰기가 둘다 가능, 파일이 없으면 Error를 발생시킴 
#w - 쓰기 모드, 파일이 없으면 새로 만듦
#w+ - 읽기, 쓰기 다 됨. 파일 없으면 새로 만듦
#a- 파일추가 모드, 파일이 없으면 새로 만듦
#a+ 읽기, 쓰기 둘다 되고 파일 없으면 새로 만듬
url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key=a8a3185428d35af96438a137ba46bd60&targetDt="
# &targetDt=20190113&weekGb=0
date_list = ['20190113','20190106','20181230','20181223','20181216','20181209','20181202','20181125','20181118','20181109']
boxoffice_dict = []
moviecode= []
for i in range(10):
    res = requests.get(url+f'{date_list[i]}'+"&weekGb=0").text
    movie1 = json.loads(res)
    for j in range(10):
        movie_Code = movie1["boxOfficeResult"]["weeklyBoxOfficeList"][j]["movieCd"]
        movie_title = movie1["boxOfficeResult"]["weeklyBoxOfficeList"][j]["movieNm"]
        movie_audience = movie1["boxOfficeResult"]["weeklyBoxOfficeList"][j]["audiCnt"]
        movie_date = date_list[i]
        
        
        if movie_title not in boxoffice_dict:
            boxoffice_dict.append(movie_title)
            moviecode.append(movie_Code)
            f = open("boxoffice.csv", "a+", encoding='utf-8', newline="")
            csv_w = csv.writer(f)
            csv_w.writerow([movie_Code, movie_title, movie_audience, movie_date])
            f.close()
# 영화 대표코드 , 영화명(국문) , 영화명(영문) , 영화명(원문) , 개봉연도 , 상영시간 , 장르 , 감독명 , 관람등급 , 배우1 , 배우2 , 배우3
# 배우의 경우 최대 3명입니다. 영화에 따라 1~2명일 수도 있습니다.            

url_2 = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key=a8a3185428d35af96438a137ba46bd60&movieCd="
for m2 in moviecode:
    res = requests.get(url_2 + f'{m2}').text
    movie2 = json.loads(res)
    code = movie2["movieInfoResult"]["movieInfo"]["movieCd"]
    movieNm = movie2["movieInfoResult"]["movieInfo"]["movieNm"]
    movieNmEn = movie2["movieInfoResult"]["movieInfo"]["movieNmEn"]
    movieNmOg = movie2["movieInfoResult"]["movieInfo"]["movieNmOg"]
    prdtYear = movie2["movieInfoResult"]["movieInfo"]["prdtYear"]
    showTm = movie2["movieInfoResult"]["movieInfo"]["showTm"]
    genre = []
    for i in range(len(movie2["movieInfoResult"]["movieInfo"].get("genres"))):
        genre.append(movie2["movieInfoResult"]["movieInfo"].get("genres")[i].get("genreNm"))
    genreNm = "/".join(genre)
    director = movie2["movieInfoResult"]["movieInfo"]["directors"][0]["peopleNm"]
    watchGradeNm = movie2["movieInfoResult"]["movieInfo"]["audits"][0]["watchGradeNm"]
    actors = []
    a = 0
    for i in range(len(movie2["movieInfoResult"]["movieInfo"]["actors"])-1):
        if a == 4:
            break;
        actors.append(movie2["movieInfoResult"]["movieInfo"]["actors"][i]["peopleNm"])
        a += 1
    if len(actors)>=1:
        actor1 = actors[0]
    else:
        actor1 = ""
    if len(actors)>=2:
        actor2 = actors[1]
    else:
        actor2 = ""
    if len(actors)>=3:
        actor3 = actors[2]
    else:
        actor3 = ""
        

    f = open("movie.csv", "a+", encoding='utf-8', newline="")
    csv_w = csv.writer(f)
    csv_w.writerow([code,movieNm,movieNmEn,movieNmOg,prdtYear,showTm,genreNm,director,watchGradeNm,actor1,actor2,actor3])
    f.close()


    
    
    
    
    
        
            

# f2 = open("test.csv", "r", encoding="utf-8")
# csv_r = csv.reader(f2)
# for line in csv_r:
#     print(line[0])
# f2.close()



# echo 'export KOBIS_KEY="key"' >> ~/.bashrc
# echo 'export NAVER_ID="아이디"' >> ~/.bashrc
# echo 'export NAVER_SECRET="비밀번호"' >> ~/.bashrc
