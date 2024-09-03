
from .models import Employee
from .schemas import EmployeeSchema

from flask_restful import Resource
from flask import make_response, jsonify, request
from src import api, db

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
