from flask import Flask, render_template, url_for

app= Flask (__name__)

@app.route('/')
def landing():
    return render_template ('landing.html')


@app.route('/index')
def index():
    return render_template ('index.html')


@app.route('/registration')
def registration():
    return render_template ('registration.html')


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