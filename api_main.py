import pymysql
from app import app
from config import mysql
from flask import Flask, jsonify, request
from werkzeug.security import *
from flask_restful import Resource, Api


api = Api(app)

# index page


@app.route("/")
def helloWorld():
    return "hello AVS APPLICATION USER \n"

# **************************** USER MANIPULATION*******************************************************************************
# CRUD Operation - Register  new user

@app.route('/adduser', methods=['POST'])
def add_user():
    try:
        json = request.json
        phone = json['phone']
        matricule = json['matricule']
        password = json['password']
        mail = json['mail']
        if matricule and password and phone and mail and request.method == 'POST':
            SQL_Query = "INSERT INTO user (matricule, password ,mail , phone) VALUES(%s, %s, %s ,%s)"
            data = (mtricule, password,mail,phone)
            connection = MySql.connect()
            Pointer = connection.cursor()
            Pointer.execute(SQL_Query, data)
            connection.commit()
            response = jsonify(' user added!')
            response.status_code = 200
            return response
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        Pointer.close()
        connection.close()


app.route('/auth', methods=['POST'])
def get_user():
    try:
        json = request.json
   
        matricule = json['matricule']
        password = json['password']
    
        if matricule and password and request.method == 'POST':
            select_query = "SELECT * FROM user where matricule = " + "'" + matricule + "' and password = " + "'" + password + "')"
            record = Pointer.fetchone()
            response = jsonify(record)
            response.status_code = 200
            return response
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        Pointer.close()
        connection.close()






class Auth(Resource):
    
   def post(self):
    
        json = request.json
   
        matricule = json['matricule']
        password = json['password']
    
        if matricule and password and request.method == 'POST':
            select_query = "SELECT * FROM user where matricule = " + "'" + matricule + "' and password = " + "'" + password + "')"
            record = Pointer.fetchone()
            response = jsonify(record)
            response.status_code = 200
            return response






class Registration(Resource):
    
   def post(self):
    
        json = request.json
        phone = json['phone']
        matricule = json['matricule']
        password = json['password']
        mail = json['mail']
        if matricule and password and phone and mail and request.method == 'POST':
            SQL_Query = "INSERT INTO user (matricule, password ,mail , phone) VALUES(%s, %s, %s ,%s)"
            data = (mtricule, password,mail, phone)
            connection = MySql.connect()
            Pointer = connection.cursor()
            Pointer.execute(SQL_Query, data)
            connection.commit()
            response = jsonify(' user added!')
            response.status_code = 200
            return response
        
# CRUD Operation - READ all user


@app.route('/users/')
def all_emp():
    try:
        connection = mysql.connect()
        Pointer = connection.cursor(pymysql.cursors.DictCursor)
        Pointer.execute(" select * FROM user ")
        record = Pointer.fetchall()
        response = jsonify(record)
        response.status_code = 200
        return response
        

    except Exception as e:
           print(e)
    finally:
        Pointer.close()
        connection.close()


# CRUD Operation - READ  user b y matricule
@app.route('/user/<id>')
def emp(id):
    try:
        connection = mysql.connect()
        Pointer = connection.cursor(pymysql.cursors.DictCursor)
        Pointer.execute("SELECT matricule , password FROM user WHERE matricule=%s", id)
        record = Pointer.fetchone()
        response = jsonify(record)
        response.status_code = 200
        return response

    except Exception as e:
        print(e)
    finally:
        Pointer.close()
        connection.close()

# CRUD Operation - DELETE


@app.route('/delete/<id>')
def delete_user(id):
    try:
        connection = MySql.connect()
        Pointer = connection.cursor()
        Pointer.execute("DELETE FROM user WHERE matricule=%s", (id,))
        connection.commit()
        response = jsonify('user deleted!')
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        Pointer.close()
        connection.close()









# CRUD Operation - UPDATE user


@app.route('/update', methods=['POST'])
def update_user():
    try:
        json = request.json
        
        name = json['name']
        name = json['name']
        Publisher= json['Publisher_']
        if Book_name and Author_name and Publisher_name and id and request.method == 'POST':
            SQL_Query = "UPDATE user SET name=%s, Author=%s, Publisher=%s WHERE matricule=%s"
            data = (Book_name, Author_name, Publisher_name, id,)
            connection = MySql.connect()
            Pointer = connection.cursor()
            Pointer.execute(sql, data)
            connection.commit()
            response = jsonify('user updated!')
            response.status_code = 200
            return response
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        Pointer.close()
        connection.close()





# ****************************BOX MANIPULATION*******************************************************************************
# CRUD Operation - Register  new BOX

@app.route('/addbox', methods=['POST'])
def add_box():
    try:
        json = request.json
        matbox = json['matbox']
        disponible = json['disponible']
        if matbox and disponible and request.method == 'POST':
            SQL_Query = "INSERT INTO box  VALUES(%s, %s)"
            data = (Book_name, Author_name, Publisher_name,)
            connection = MySql.connect()
            Pointer = connection.cursor()
            Pointer.execute(SQL_Query, data)
            connection.commit()
            response = jsonify(' box added!')
            response.status_code = 200
            return response
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        Pointer.close()
        connection.close()

# CRUD Operation - READ all box


@app.route('/boxs/')
def all_box():
    try:
        connection = mysql.connect()
        Pointer = connection.cursor(pymysql.cursors.DictCursor)
        Pointer.execute("SELECT * FROM box where disponible='oui' ")
        record = Pointer.fetchall()
        response = jsonify(record)
        response.status_code = 200
        return response
        

    except Exception as e:
        print(e)
    finally:
        Pointer.close()
        connection.close()


# CRUD Operation - READ  user b y matricule
@app.route('/box/<id>')
def box(id):
    try:
        connection = mysql.connect()
        Pointer = connection.cursor(pymysql.cursors.DictCursor)
        Pointer.execute("SELECT * from box WHERE matbox=%s", id)
        record = Pointer.fetchone()
        response = jsonify(record)
        response.status_code = 200
        return response

    except Exception as e:
        print(e)
    finally:
        Pointer.close()
        connection.close()

# CRUD Operation - DELETE


@app.route('/delete/<id>')
def delete_box(id):
    try:
        connection = MySql.connect()
        Pointer = connection.cursor()
        Pointer.execute("DELETE FROM box WHERE matbox=%s", (id,))
        connection.commit()
        response = jsonify('box deleted!')
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        Pointer.close()
        connection.close()









# CRUD Operation - UPDATE user


@app.route('/update', methods=['POST'])
def update_box():
    try:
        json = request.json
        
        name = json['name']
        name = json['name']
        Publisher= json['Publisher_']
        if Book_name and Author_name and Publisher_name and id and request.method == 'POST':
            SQL_Query = "UPDATE user SET name=%s, Author=%s, Publisher=%s WHERE matricule=%s"
            data = (Book_name, Author_name, Publisher_name, id,)
            connection = MySql.connect()
            Pointer = connection.cursor()
            Pointer.execute(sql, data)
            connection.commit()
            response = jsonify('user updated!')
            response.status_code = 200
            return response
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        Pointer.close()
        connection.close()

api.add_resource(Registration, '/register')
api.add_resource(Auth, '/auth')

if __name__ == "__main__":
    app.debug = True
   
    app.run(host="10.206.206.78")
