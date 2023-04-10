from flask_app import app 
from flask import flash, render_template, request, redirect, session
from flask_app.models.story_model import Story

# Move to recipes controller 


@app.route('/home')                           
def home():
    return render_template('home.html')  

@app.route('/newstory')                           
def newstory():
    return render_template('newstory.html')  


@app.route('/editstory/<int:story_id>')                           
def editstory(story_id):
    return render_template('editstory.html')  



@app.route('/stories')
def display_stories():
    # if 'email' not in session:
    #     return redirect ('/')
    list_stories = Story.get_all_with_user()
    print(list_stories)
    return render_template('home.html', list_stories = list_stories)
