"""user/views.py"""

from flask_restful import Resource
from flask import make_response, jsonify, request
from src import api, db
from .models import User
from .schemas import UserSchema
from .models import Employee
from .schemas import EmployeeSchema

class UserResource(Resource):

    model = User
    schema = UserSchema

    def get(self, slug):
        user = self.model.query.get(slug)
        if not user:
            return make_response(jsonify({'error': 'Resource not found'}), 404)
        return make_response(jsonify(self.schema().dump(user).data), 200)

    def patch(self, slug):
        user = self.model.query.get(slug)
        if not user:
            return make_response(jsonify({'error': 'Resource not found'}), 404)
        user, errors = self.schema().load(request.json, instance=user)
        if errors:
            return make_response(jsonify(errors), 400)
        db.session.commit()
        return make_response(jsonify(self.schema().dump(user).data), 200)

    def delete(self, slug):
        user = self.model.query.get(slug)
        if not user:
            return make_response(jsonify({'error': 'Resource not found'}), 404)
        db.session.delete(user)
        db.session.commit()
        return make_response(jsonify({}), 204)


class UserListResource(Resource):

    model = User
    schema = UserSchema

    def get(self):
        users = self.model.query.limit(20).all()
        if not users:
            return make_response(jsonify({'error': 'Resource not found'}), 404)
        return make_response(jsonify(self.schema().dump(users, many=True).data), 200)

    def post(self):
        users, errors = self.schema().load(request.json, many=True)
        if errors:
            return make_response(jsonify(errors), 400)
        else:
            db.session.add_all(users)
            db.session.commit()
            return make_response(jsonify(self.schema().dump(users, many=True).data), 201)

api.add_resource(UserResource, '/user/<slug>', endpoint='user')
api.add_resource(UserListResource, '/user', endpoint='users')





class EmployeeResource(Resource):
    model = Employee
    schema = EmployeeSchema

    def get(self, id):
        employee = self.model.query.get(id)
        if not employee:
            return make_response(jsonify({'error': 'Resource not found'}), 404)
        return make_response(jsonify(self.schema().dump(employee)), 200)

    def patch(self, id):
        employee = self.model.query.get(id)
        if not employee:
            return make_response(jsonify({'error': 'Resource not found'}), 404)
        employee, errors = self.schema().load(request.json, instance=employee)
        if errors:
            return make_response(jsonify(errors), 400)
        db.session.commit()
        return make_response(jsonify(self.schema().dump(employee)), 200)

    def delete(self, id):
        employee = self.model.query.get(id)
        if not employee:
            return make_response(jsonify({'error': 'Resource not found'}), 404)
        db.session.delete(employee)
        db.session.commit()
        return make_response(jsonify({}), 204)

class EmployeeListResource(Resource):
    model = Employee
    schema = EmployeeSchema

    def get(self):
        employees = self.model.query.limit(20).all()
        if not employees:
            return make_response(jsonify({'error': 'Resource not found'}), 404)
        return make_response(jsonify(self.schema().dump(employees, many=True)), 200)

    def post(self):
        employees, errors = self.schema().load(request.json, many=True)
        if errors:
            return make_response(jsonify(errors), 400)
        db.session.add_all(employees)
        db.session.commit()
        return make_response(jsonify(self.schema().dump(employees, many=True)), 201)

api.add_resource(EmployeeResource, '/employee/<int:id>', endpoint='employee')
api.add_resource(EmployeeListResource, '/employees', endpoint='employees')
