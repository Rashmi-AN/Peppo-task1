from flask import Flask
from flask_restful import Api
from Resources.resource import Person,PersonPost, Multiple_Post
from db import db
from flask_jwt import JWT
from security import auth, identity

app = Flask(__name__)                    # here we are  building our application
app.secret_key = "#0#"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://rashmi1:rashmi123@localhost/Flask"
db.init_app(app)
app.app_context().push()
api = Api(app)                                # here we are buiding Api for our application.
jwt = JWT(app, auth, identity)

api.add_resource(Person, "/person/<string:Person_id>")
api.add_resource(PersonPost, "/person")
api.add_resource(Multiple_Post, "/multiple")


if __name__ == '__main__':
    app.run(debug=True)




