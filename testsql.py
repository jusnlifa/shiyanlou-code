# coding=utf-8
import psycopg2

conn = psycopg2.connect(database='tmitter',user="postgres",password='123456',host='127.0.0.1',port='5432')

print("open database successfully")

# cur= conn.cursor()
# cur.execute("select * from employees")
# rows = cur.fetchall()
# for r in rows:
# 	print("id=",r[0])

conn.close()