movie/

test.py(문제 1,2번)
1. import os로 영화진흥위원회 Key값을 불러와 url에 요청을 보내고 json으로 데이터를 받는다. 
2. 영화진흥위원회 오픈 API에서 날짜 데이터를 입력해 10주간 상위 10위 영화 정보를 가져온다.
3. 영화코드, 제목, 관객 수 등을 가져오고 중복된 영화들은 가장 관객 수가 많은 정보로 하나만 수집한다.
4. boxoffice.csv로 넘겨서 자료를 받는다.
5. 문제 1번에서 총 43개의 영화코드를 리스트로 함께 받아 2번에서 영화정보를 검색할 때 활용한다.
6. 영화진흥위원회로 url요청을 보내고 데이터를 받아 영화이름, 개봉년도, 상영시간 등의 정보를 받는다.
7. 정보를 movie.csv에 저장한다.

test2.py(문제 3번)
1. import os로 네이버 id, secret 값을 불러와 url에 요청을 보내고 json으로 데이터를 받는다.
2. 영화의 코드, 썸네일 url, link 등의 정보를 받고 movie_naver.csv에 저장한다.

test3.py
1. movie_naver.csv에 저장된 url으로 네이버 영화 검색 API를 통해 얻은 이미지 URL에 요청을 보내 실제 이미지 파일로 저장한다.
2. images폴더 내에 해당 주소로 받은 이미지파일을 대표 코드 이름으로 저장한다.

boxoffice.csv
movie.csv
movie_naver.csv
images/
영화코드.jpg
