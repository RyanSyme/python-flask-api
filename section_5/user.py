import sqlite3
from flask_restful import Resource, reqparse

class User:
    pass


class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        type=str,
        required=True,
        help="This field cannot be blank"
    )
    parser.add_argument(
        'password',
        type=str,
        required=True,
        help="This field cannot be blank"
    )

    def post(self):
        data = UserRegister.parser.parsre_args()

        connection = sqlite3.connect('data.db')
        cursor = connect.cursor()

        query = "INSERT INTO users VALUES (Null, ?, ?)"
        cursor.execute(query, (data['username'], data['password']))

        connection.commit()
        connection.close()

        return {"message": "User created successfully"}, 201
