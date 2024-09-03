from src import ma, BaseSchema
from .models import Employee


class EmployeeSchema(BaseSchema):
    class Meta:
        model = Employee

    id = ma.Integer(load=True, partial=True)
    name = ma.String()
    position = ma.String()
    department = ma.String()    