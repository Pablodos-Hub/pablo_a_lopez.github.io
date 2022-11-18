from flask import Flask,request, render_template
 
app = Flask(__name__)
 
@app.get("/")
def raiz():
   return render_template("main.html")

@app.get("/saludo.html")
def pagina2():
   return render_template("saludo.html",nombre =nombre)

def nombre():
   return request.args.get("nombre","algo")