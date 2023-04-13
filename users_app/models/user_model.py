from users_app.config.mysqlconnection import connectToMySQL

from users_app import DATABASE

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']

    @classmethod
    def get_all(cls):
        query = """
            SELECT * FROM users;
        """

        results = connectToMySQL(DATABASE).query_db(query)

        users = []

        if results:
            for dict in results:
                new_user = cls(dict)
                users.append(new_user)

        return users

    @classmethod
    def create(cls, data):
        query = """
            INSERT INTO users(first_name, last_name, email) 
            VALUES(%(first_name)s, %(last_name)s, %(email)s)
        """

        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def get_one(cls, id):
        data = {
            'id' : id
        }

        query = """
            SELECT * FROM users WHERE id = %(id)s;
        """

        results = connectToMySQL(DATABASE).query_db(query, data)

        person = cls(results[0])

        return person

    @classmethod
    def update(cls, data):

        query = """
            UPDATE users SET first_name = %(first_name)s, 
            last_name = %(last_name)s, email = %(email)s
            WHERE id = %(id)s;
        """

        connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def delete(cls, id):
        data = {
            'id' : id
        }

        query = """
            DELETE FROM users WHERE id = %(id)s
        """

        connectToMySQL(DATABASE).query_db(query, data)