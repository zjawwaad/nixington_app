from flask_app import app 
from flask import flash, render_template, request, redirect, session
from flask_app.models.user_model import User
from flask_bcrypt import Bcrypt

# from curses import flash
bcrypt= Bcrypt( app )

@app.route('/')                           
def login():
    return render_template('home.html')  



@app.route ('/registration', methods = ['POST'])
def register(): 

    if User.validate( request.form ) == False:
        return redirect( '/' )

    user_exists = User.get_one_email( request.form )
    if user_exists != None:
        flash( "This email already exists", "error_registration_email")
        return redirect( '/' )
    #proceed to create user
    data = { 
        **request.form,
        "password" : bcrypt.generate_password_hash( request.form['password'])
    }
    user_id = User.create( data )
    
    session['first_name'] = data['first_name']
    session['email'] = data['email']
    session['user_id'] = user_id

    return redirect( '/stories' )



if __name__=="__main__":
    app.run(debug=True)     
