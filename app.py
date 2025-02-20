from flask import *
from flask_cors import CORS
import pymysql
connection=pymysql.connect(database='flaskcrud',user='root',password='')
app=Flask(__name__)
# CORS(app)
@app.route('/api/register',methods=['POST'])
def register():
    if request.method=='POST':
        username=request.form.get('username')
        useremail=request.form.get('useremail')
        password=request.form.get('password')
        confirmPassword=request.form.get('confirmPassword')
        connection=pymysql.connect(user='root',host='localhost',password='',database='flaskcrud')
        sql="insert into register(username,useremail,password)values(%s,%s,%s)"
        cursor=connection.cursor()
        cursor.execute(sql,(username,useremail,password))
        connection.commit()
        return jsonify({'success':f"Thank you for signing up {username}"})
    return 'No post request detected'

if __name__=='__main__':
    app.run(debug=True) 
