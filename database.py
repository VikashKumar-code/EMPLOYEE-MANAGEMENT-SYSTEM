import pymysql
from tkinter import messagebox
def connect_database():
    global conn,cursor
    try:
        conn=pymysql.connect(host='localhost',user='root',password='987654321')
        cursor=conn.cursor()
    except: 
        messagebox.showerror('Error','Something went wrong, Please open mysql app before running again')
        return
    
    cursor.execute('CREATE DATABASE IF NOT EXISTS EMPLOYEE_DATA')
    cursor.execute('USE EMPLOYEE_DATA')
    cursor.execute('CREATE TABLE IF NOT EXISTS E_DATA(ID VARCHAR(20),NAME VARCHAR(50),PHONE VARCHAR(20),ROLE VARCHAR(50),GENDER VARCHAR(20),SALARY DECIMAL(10,2))')

connect_database()

def insert(id,name,phone,role,gender,salary):
    cursor.execute('INSERT INTO E_DATA VALUES(%s,%s,%s,%s,%s,%s)',(id,name,phone,role,gender,salary))
    conn.commit()

def id_exists(id):
    cursor.execute('SELECT COUNT(*) FROM E_DATA WHERE ID=%s',id)
    result=cursor.fetchone()
    return result[0]>0

def fetchemployees():
    cursor.execute('SELECT * FROM E_DATA ORDER BY ID ASC')
    result=cursor.fetchall()
    return result

def update(id,new_name,new_phone,new_role,new_gender,new_salary):
    cursor.execute('UPDATE E_DATA SET NAME=%s,PHONE=%s,ROLE=%s,GENDER=%s,SALARY=%s WHERE ID=%s',(new_name,new_phone,new_role,new_gender,new_salary,id))
    conn.commit()

def delete(id):
    cursor.execute('DELETE FROM E_DATA WHERE ID=%s',id)
    conn.commit()

def search(option,value):
    #cursor.execute(f'SELECT * FROM E_DATA WHERE {option} LIKE %s',(f'%{value}%',))
    cursor.execute(f'SELECT * FROM E_DATA WHERE {option} LIKE %s',value)
    result=cursor.fetchall()
    return result
 
def deleteall():
    cursor.execute('TRUNCATE TABLE E_DATA')
    conn.commit()

