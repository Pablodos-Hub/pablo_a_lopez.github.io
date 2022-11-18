from flask import Flask,request, render_template
from flask import Flask, url_for, redirect
 
app = Flask(__name__)
 
@app.get("/")
def raiz():
   return render_template("mi_cv.html")

