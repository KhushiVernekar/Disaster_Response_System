from flask import Flask, render_template, request, flash, redirect
import sqlite3
import pickle
import numpy as np
import os

import google.generativeai as genai

import telepot
bot=telepot.Bot("7883809940:AAHxSEcFE2JEMJZDjkJeZNbOFH3ETN6bSog")
ch_id="5412131478"


app = Flask(__name__)
chat_history = []


import pickle
modell=pickle.load(open('model/dtt.pkl','rb'))

from RouteMap import GetMap

# Load Gemini AI model
genai.configure(api_key='AIzaSyB2zvehKi1RBJ4dyWvg1i1-YiG_RAopFtg')
gemini_model = genai.GenerativeModel('gemini-pro')
chat = gemini_model.start_chat(history=[])
    

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@app.route('/crowd', methods=['GET', 'POST'])
def crowd():
    if request.method == 'POST':
        os.system("python crowd.py")
        return render_template('crowd.html')
    return render_template('crowd.html')


@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/userlog', methods=['GET', 'POST'])
def userlog():
    if request.method == 'POST':

        connection = sqlite3.connect('user_data.db')
        cursor = connection.cursor()

        name = request.form['name']
        password = request.form['password']

        query = "SELECT name, password FROM user WHERE name = '"+name+"' AND password= '"+password+"'"
        cursor.execute(query)

        result = cursor.fetchall()

        if result:
            return render_template('fetal.html')
        else:
            return render_template('index.html', msg='Sorry, Incorrect Credentials Provided,  Try Again')

    return render_template('index.html')


@app.route('/userreg', methods=['GET', 'POST'])
def userreg():
    if request.method == 'POST':

        connection = sqlite3.connect('user_data.db')
        cursor = connection.cursor()

        name = request.form['name']
        password = request.form['password']
        mobile = request.form['phone']
        email = request.form['email']
        
        print(name, mobile, email, password)

        command = """CREATE TABLE IF NOT EXISTS user(name TEXT, password TEXT, mobile TEXT, email TEXT)"""
        cursor.execute(command)

        cursor.execute("INSERT INTO user VALUES ('"+name+"', '"+password+"', '"+mobile+"', '"+email+"')")
        connection.commit()

        return render_template('index.html', msg='Successfully Registered')
    
    return render_template('index.html')

@app.route('/logout')
def logout():
    return render_template('index.html')


@app.route("/fetalPage", methods=['GET', 'POST'])
def fetalPage():
    return render_template('fetal.html')


@app.route("/predict", methods = ['POST', 'GET'])
def predictPage():
    if request.method == 'POST':

        
        To = request.form['to']
        To = To.split(',')
        

        var3 = request.form['dep']

        var4 = request.form['depe']
        var5 = request.form['deps']
        var6 = request.form['mag']

        var7 = request.form['magt']
        var8 = request.form['mage']
        var9 = request.form['mags']

        var10 = request.form['gap']
        var11 = request.form['hord']
        var12 = request.form['hore']
        var13 = request.form['root']

        data = np.array([[ var3, var4, var5, var6, var7,var8,var9,var10,var11,var12,var13]])
        result = modell.predict(data)[0]
        
        
        print(result)

        
        if result == 1 :
            res='Earth Quake Detected'
            bot.sendMessage(ch_id,f"Alert! {res} near  \n Latitude :{To[0]} \n Longitude : {To[1]}")
            fromm=['12.8823','77.4449']
            mapres = GetMap(fromm, To)
            print(res)
            return render_template('predict.html', pred = result,status=res,mapres=mapres)
        elif result == 0: 
            res='NO Earth Quake'
            fromm=['12.8823','77.4449']
            mapres = GetMap(fromm, To)
            print(res)
            return render_template('predict.html', pred = result,status=res,mapres=False)


        

    return render_template('predict.html',mapres=False)



@app.route('/analyse', methods=['GET', 'POST'])
def analyse():
    if request.method == 'POST':
        user_input = request.form['query']
        # Get response from Gemini AI model
        gemini_response = chat.send_message(user_input)

        data = gemini_response.text
        print(data)
        result = []
        for row in data.split('*'):
            if row.strip() != '':
                result.append(row)
        print(result)

        import csv
        f = open('data.csv', 'r')
        data = csv.reader(f)
        header = next(data)
        # Update chat history with both responses
        chat_history.append([user_input, result])
        try:
            for row in data:
                if row[1] in user_input:
                    name = row[0]
                    Link = row[2]
                    break
            return render_template('chatbot.html', status="Sever", chat_history=chat_history, name=name, Link=Link)
        except:
            return render_template('chatbot.html', chat_history=chat_history)
    return render_template('chatbot.html')
    
if __name__ == '__main__':
	app.run(debug = True)
