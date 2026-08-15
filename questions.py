import sqlite3

con=sqlite3.connect("database.db")

cur=con.cursor()


questions=[

(
"What is Python?",
"Programming Language",
"Operating System",
"Database",
"Browser",
"Programming Language"
),


(
"What is CPU?",
"Central Processing Unit",
"Control Processing Unit",
"Computer Unit",
"Power Unit",
"Central Processing Unit"
),


(
"What is HTML?",
"Hyper Text Markup Language",
"High Text Machine Language",
"Home Tool Language",
"Hyper Transfer Language",
"Hyper Text Markup Language"
),


(
"Which tool is used for scanning networks?",
"Nmap",
"Chrome",
"Excel",
"Word",
"Nmap"
),


(
"What is phishing?",
"Fake website/message attack",
"Programming language",
"Database",
"Hardware",
"Fake website/message attack"
)

]


for q in questions:

    cur.execute("""
    INSERT INTO questions
    (question,option1,option2,option3,option4,answer)
    VALUES(?,?,?,?,?,?)
    """,q)


con.commit()

con.close()

print("Questions Added")
