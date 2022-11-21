from db import db

class PersonModel(db.Model):
    __tablename__ = "person_model"
    Person_id = db.Column(db.Integer, primary_key=True)
    Person_name = db.Column(db.String(20))
    Age = db.Column(db.Integer)
    Gender = db.Column(db.String(10))
    email = db.Column(db.String(20), unique=True)
    Address = db.Column(db.String(50))

    def __init__(self, Person_name, Age, Gender, email, Address):
        # self.Person_id = Person_id
         self.Person_name = Person_name
         self.Age = Age
         self.Gender = Gender
         self.email = email
         self.Address = Address

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def change_in_db(self):
        db.session.commit()


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()