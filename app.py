from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)


def db():
    return sqlite3.connect("database.db")


def create_database():

    con=db()
    cur=con.cursor()


    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
    )
    """)


    cur.execute("""
    CREATE TABLE IF NOT EXISTS questions(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT,
    option1 TEXT,
    option2 TEXT,
    option3 TEXT,
    option4 TEXT,
    answer TEXT
    )
    """)


    con.commit()
    con.close()



@app.route("/")
def home():
    return render_template("login.html")



@app.route("/register",methods=["POST"])
def register():

    username=request.form["username"]
    password=request.form["password"]


    con=db()
    cur=con.cursor()


    cur.execute(
    "INSERT INTO users(username,password) VALUES(?,?)",
    (username,password)
    )


    con.commit()
    con.close()


    return redirect("/")



@app.route("/login",methods=["POST"])
def login():

    username=request.form["username"]
    password=request.form["password"]


    con=db()
    cur=con.cursor()


    cur.execute(
    "SELECT * FROM users WHERE username=? AND password=?",
    (username,password)
    )


    user=cur.fetchone()

    con.close()


    if user:
        return redirect("/exam")

    return "Login Failed"



@app.route("/exam")
def exam():

    con=db()
    cur=con.cursor()

    cur.execute("SELECT * FROM questions")

    questions=cur.fetchall()

    con.close()


    return render_template(
    "exam.html",
    questions=questions
    )



@app.route("/submit",methods=["POST"])
def submit():

    score=0


    con=db()
    cur=con.cursor()


    cur.execute("SELECT * FROM questions")

    questions=cur.fetchall()


    for q in questions:

        ans=request.form.get(str(q[0]))

        if ans==q[6]:
            score+=1


    con.close()


    return render_template(
    "result.html",
    score=score
    )



if __name__=="__main__":

    create_database()

    app.run(debug=True)
