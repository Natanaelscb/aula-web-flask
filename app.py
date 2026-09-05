from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("admim/index.html")

@app.route("/categorias")
def listarcategoria():
    conn = conexao()
    categoria = conn.execute('select * from categoria')
    
    return render_template("admim/listar_categoria.html", categoria = categoria)

def conexao():
    conn= sqlite3.connect('database.db')
    return conn

@app.route("/produtos")
def produtos():
    return "<h1> Cadastre seus produtos </h1>"

app.run(debug=True)
