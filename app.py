from flask import Flask, render_template,request
import csv, requests

app = Flask(__name__)

@app.route('/movie')
def movie():
    f = open("csv/movie.csv","r",encoding="utf-8")
    movie_list = csv.reader(f)
    
    return render_template("movie.html", movie_list=movie_list)
    
    
if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0', port=8080)