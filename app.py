from flask import Flask, render_template, request, json
from flaskext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash

app = Flask(__name__)
mysql = MySQL()

#MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Dontstands0'
app.config['MYSQL_DATABASE_DB'] = 'BucketList'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route("/")
def main():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/signUp', methods=['POST'])
def signUp():
    try:
        #read teh posted values from the UI
        name = request.form['inputName']
        email = request.form['inputEmail']
        password = request.form['inputPassword']

        # validate the received values
        if name and email and password:

            conn = mysql.connect()
            cursor = conn.cursor()
            hashed_password = generate_password_hash(password)
            cursor.callproc('sp_createUser',(name,email,hashed_password))
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return json.dumps({'message':'User created successfully !'})
            else:
                return json.dumps({'error':str(data[0])})

            return json.dumps({'html':'<span>All fields good !!</span>'})
        else:
            return json.dumps({'html':'<span>Enter the required fields</span>'})

        cursor.close()
        conn.close()
    except Exception as e:
        return json.dumps({'error':str(e)})

if __name__ == "__main__":
    app.run()
