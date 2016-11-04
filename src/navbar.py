import flask
from flask import Flask, g, redirect, url_for, render_template, request, jsonify, json, url_for







app = Flask(__name__)



@app.route("/")
def root():
  return render_template('navbar_root.html') 

@app.route("/page1/")
def page1():
  return render_template('navbar_page1.html')

@app.route("/page2/")
def page2():
  return render_template('navbar_page2.html')

@app.route("/page3/")
def page3():
  return render_template('navbar_page3.html')
  
@app.route("/page4/")
def page4():
  return render_template('navbar_page4.html')

  
# All movies route	
@app.route('/movies/')
def page5():
    json_data=open('static/movies.json').read()
    movies= json.loads(json_data)
    return render_template("movies.html", results=movies)
	
# Single movies route	
@app.route('/movies/<movie_title>/')
def page6(movie_title):
    json_data=open('static/movies.json').read()
    movies= json.loads(json_data)
    json_data=open('static/cast.json').read()
    cast= json.loads(json_data)
    return render_template("movie.html", movies=movies, cast=cast, movie_title=movie_title)
	

  
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
