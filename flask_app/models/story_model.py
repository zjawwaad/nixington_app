from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE
from flask_app.models.user_model import User

class Story:
    def __init__( self , data ):
        self.id = data['id']
        self.my_story = data['my_story']
        self.created_at= data['created_at']
        self.updated_at=['updated_at']

    @classmethod
    def get_all_with_user( cls ):
        query = 'SELECT * FROM stories JOIN users ON stories.user_id = users.id;'
        
        results = connectToMySQL (DATABASE).query_db ( query )
        list_stories = []
        print( results )
        for row in results: 
            current_story = cls( row )
            user_data= {
                **row,
                'created_at' : row['users.created_at'],
                'updated_at' : row['users.updated_at'],
                'id' : row ['users.id']
            }
            current_user = User( user_data )
            current_story.user = current_user
            list_stories.append( current_story )
        return list_stories

    @classmethod
    def get_one_with_user( cls, data ):
        query = 'SELECT * FROM stories JOIN users ON stories.user_id = users.id WHERE stories.id = %(id)s;'

        results = connectToMySQL (DATABASE).query_db ( query, data )
        if len( results ) > 0:
            current_story = cls( results[0] )
            user_data = {
                **results[0],
                'created_at' : results[0]['users.created_at'],
                'updated_at' :  results[0]['users.updated_at'],
                'id' :  results[0] ['users.id']
            }
            current_story.user = User( user_data)
            return current_story
        else:
            return None