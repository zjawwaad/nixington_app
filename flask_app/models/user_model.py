from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import EMAIL_REGEX, DATABASE

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.baby_name = data['baby_name']
        self.baby_bday = data['baby_bday']
        self.email = data['email']
        self.password = data['password']
        self.created_at= data['created_at']
        self.updated_at=['updated_at']

    @classmethod
    def create( cls, data ):
        query = "Insert INTO users(first_name, last_name, baby_name, baby_bday, email, password)"
        query += "VALUES (%(first_name)s, %(last_name)s, %(baby_name)s, %(baby_bday)s, %(email)s, %(password)s)"
        result = connectToMySQL('nixington_schema').query_db(query, data)
        return result

    @classmethod
    def get_one_email(cls , data ):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL('nixington_schema').query_db(query, data)

        if len( result ) > 0:
            current_user = cls( result[0] )
            return current_user
        else:
            return None


    @staticmethod
    def validate( data ):
        is_valid = True
        if len( data['first_name'] ) < 2:
            flash ("First name must be at least two characters" "error_registration_first_name")
            is_valid = False
        if len( data['last_name'] ) < 2:
            flash ("Last name must be at least two characters" "error_registration_last_name")
            is_valid = False
        if not EMAIL_REGEX.match( data['email'] ):
            flash( "Invalid email", "error_registration_email" )
            is_valid = False
        if data['password'] != data['confirm']:
            flash( "Passwords do not match", "error_registration_confirm" )
            is_valid = False
        return is_valid

