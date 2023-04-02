from flask_app import app 
from flask import flash, render_template, request, redirect, session
from flask_app.models.story_model import Story

# Move to recipes controller 
@app.route('/stories')
def display_stories():
    # if 'email' not in session:
    #     return redirect ('/')
    list_stories = Story.get_all_with_user()
    print(list_stories)
    return render_template('home.html', list_stories = list_stories)
