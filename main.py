from flask import Flask, render_template, url_for
from flask import request
user_details = {}


app= Flask (__name__)
app.config['SECRET_KEY'] = 'DontTellAnyone'

@app.route('/')
def landing():
    return render_template ('landing.html')


@app.route('/index', methods=['GET','POST'])
def index():
    return render_template ('index.html')


@app.route('/login_validation', methods=['GET','POST'])
def login_validation():
    email = request.values['email']
    password = request.values['password']
    if email in user_details.keys():
        if password == user_details[email][2]:
            return render_template('display.html')
        else:
            return render_template('index.html')
    else:
        return render_template('index.html')
   

@app.route('/registration', methods=['GET','POST'])
def registration():
    return render_template ('registration.html')


@app.route('/registration_validation', methods=['GET','POST'])
def registration_validation():
    firstname = request.values['firstname']
    lastname = request.values['lastname']
    email = request.values['email']
    password = request.values['password']

    user_details[email] = (firstname, lastname, email, password)
    return render_template('index.html')





@app.route('/display')
def display():
    return render_template ('display.html') 


@app.route('/addlist')
def addlist():
    return render_template ('addlist.html')


@app.route('/viewlist')
def viewlist():
    return render_template ('viewlist.html')     


@app.route('/update')
def update():
    return render_template ('update.html') 




if __name__=='__main__':
    app.run(debug= True)