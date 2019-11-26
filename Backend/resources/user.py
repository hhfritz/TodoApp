from flask_restful import Resource

class User(Resource):
    __tablename__ = 'users'
    # __table_args__ = tuple(db.UniqueConstraint('id', 'username', name='my_2uniq'))

    id = db.Column(db.String(), primary_key=True, unique=True)
    api_key = db.Column(db.String(), primary_key=True, unique=True)
    username = db.Column(db.String(), primary_key=True)
    firstname = db.Column(db.String())
    lastname = db.Column(db.String())
    password = db.Column(db.String())
    email = db.Column(db.String())

    def __init__(self, id, api_key, firstname, lastname, email, password, username):
        self.id = id
        self.api_key = api_key
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.username = username

    def __repr__(self):
        return '<id {}'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'api_key': self.api_key,
            'username': self.username,
            'first_name': self.firstname,
            'last_name': self.lastname,
            'password': self.password,
            'email': self.email
        }

    def get(self):
        return {"message": "Hello World (get)"}
    def post(self):
        return {"message": "Hello World (post)"}