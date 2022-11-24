from flask import request
from flask_restful import Resource, reqparse, fields, marshal_with, abort
from model.model import PersonModel


from flask_jwt import jwt_required

Person_args = reqparse.RequestParser()
Person_args.add_argument("Person_id", type=int, help='Person_id is required', required=True)
Person_args.add_argument("Person_name", type=str, help='Person_name is required', required=True)
Person_args.add_argument("Age", type=int, help='Person_age is required', required=True)
Person_args.add_argument("Gender", type=str, help='Gender is required', required=True)
Person_args.add_argument("email", type=str, help='email is required', required=True)
Person_args.add_argument("Address", type=str, help='Address is required', required=True)


Person_put_args = reqparse.RequestParser()
Person_put_args.add_argument("Person_id", type=int, help="Person id is required")
Person_put_args.add_argument("Person_name", type=str, help="Person name is required")
Person_put_args.add_argument("Age", type=str, help="Age is required")
Person_put_args.add_argument("Gender", type=str, help="Gender id is required")
Person_put_args.add_argument("email", type=str, help="email is required")
Person_put_args.add_argument("Address", type=str, help="Address is required")

resource_fields = {
                        "Person_id": fields.Integer,
                        "Person_name" : fields.String,
                        "Age" : fields.Integer,
                        "Gender": fields.String,
                        "email": fields.String,
                        "Address": fields.String
}


class Person(Resource):                    # we are working with resource that's why we created class
    @marshal_with(resource_fields)
    @jwt_required()
    def get(self, Person_id):
        result = PersonModel.query.filter_by(Person_id=Person_id).first()
        if not result:
            abort(404, message="Person id is not available")
        return result, 200


    @marshal_with(resource_fields)
    def put(self, Person_id):
        args=Person_put_args.parse_args()
        result=PersonModel.query.filter_by(Person_id=Person_id).first()

        if not result:
            abort(404, message="Person id is not available")

        if args["Person_name"]:
            result.Person_name = args["Person_name"]

        if args["Age"]:
            result.Age = args["Age"]

        if args["Gender"]:
            result.Gender = args["Gender"]

        if args["Address"]:
            result.Address = args["Address"]

        result.change_in_db()

        return result


    def delete(self, Person_id):
        result = PersonModel.query.filter_by(Person_id=Person_id).first()
        if not result:
            abort(404, message="Person id is not available")

        result.delete_from_db()


        return {Person_id: 'Person id is deleted'}, 204


class PersonPost(Resource):
    @marshal_with(resource_fields)
    def post(self):
        args = request.get_json()

        person_details = PersonModel(Person_name=args["Person_name"],Age=args["Age"],
                                     Gender=args["Gender"],email=args["email"], Address=args["Address"])
        person_details.save_to_db()
        return person_details

class Multiple_Post(Resource):
    @marshal_with(resource_fields)
    def post(self):
        content = request.get_json()
        list1 = []
        for x in content:
            person_details = PersonModel(Person_name=x["Person_name"], Age=x["Age"], Gender=x["Gender"],
                                         email=x["email"],Address=x["Address"])
            person_details.save_to_db()
            list1.append(person_details)
        return list1, 201

