from tabulate import tabulate
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="Ri1Ya2@",database="db")

def insert(name,age,city):
    res=con.cursor()
    sql="insert into users(name,age,city)values(%s,%s,%s)"
    users=(name,age,city)
    res.execute(sql,users)
    con.commit()
    print("Data insert success")

def update(name,age,city,id):
    res = con.cursor()
    sql = "update users set name=%s,age=%s,city=%s where id=%s"
    users = (name, age, city,id)
    res.execute(sql, users)
    con.commit()
    print("Data update success")


def select():
    res=con.cursor()
    sql="SELECT ID,NAME,AGE,CITY FROM USERS"
    res.execute(sql)
    result=res.fetchall()
    print(tabulate(result,headers=["ID","NAME","AGE","CITY"]))

def delete(id):
    res = con.cursor()
    sql = "delete from users where id=%s"
    users=(id,)
    con.commit()
    print("Data delete success")


while True:
    print("1.Insert data")
    print("2.update data")
    print("3.select data")
    print("4.delete data")
    print("5.exit")
    choice=int (input("enter your choice"))
    if choice==1:
        name=input("enter name:")
        age=input("enter age:")
        city=input("enter city:")
        insert(name,age,city)
    elif choice == 2:
        id=input("enter the ID:")
        name = input("enter name:")
        age = input("enter age:")
        city = input("enter city:")
        update(name, age, city,id)
    elif choice == 3:
        select()
    elif choice == 4:
        id= input("enter the ID to delete:")
        delete(id)
    elif choice==5:
        quit()
    else:
        print("invalid selection")






