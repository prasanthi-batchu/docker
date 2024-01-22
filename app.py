from flask import Flask, jsonify, request
 

app = Flask(__name__)

 

@app.route('/')
def hello_world():
   return 'Hello World..  '


@app.route('/new_route')
def new_route():
   return 'This is the New Route..  '



if __name__ == '__main__':
   app.run(host='0.0.0.0')


# the container itself is a new machine.. 











# from flask import Flask, jsonify, request
# from flask_mysqldb import MySQL

# app = Flask(__name__)

# # MySQL configurations
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_PORT'] = 3307  # Port should be an integer, not a string
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'welcome1234'
# app.config['MYSQL_DB'] = 'college'  # Replace with your actual database name
# app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# mysql = MySQL(app)

# @app.route('/')
# def hello_world():
#    return 'Hello World.. from Chethan'


# @app.route('/sample_table', methods=['GET'])
# def get_all_entries():
#     cursor = mysql.connection.cursor()
#     cursor.execute("SELECT * FROM sample_table")
#     results = cursor.fetchall()
#     cursor.close()
#     return jsonify(results)


# @app.route('/insert_record', methods=['POST'])
# def insert_entry():
#     name = request.form['name']   
#     print(name)
#     cursor = mysql.connection.cursor()
#     cursor.execute("INSERT INTO sample_table (name) VALUES (%s)", [name])
#     mysql.connection.commit()
#     cursor.close()
#     return jsonify({"message": "Entry added", "name": name}) 

# if __name__ == '__main__':
#    app.run(host='0.0.0.0')






