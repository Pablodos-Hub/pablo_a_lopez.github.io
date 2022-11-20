from flask import Flask,request, render_template
 
app = Flask(__name__)
 
@app.get("/")
def main():
   return render_template("mi_cv.html")

