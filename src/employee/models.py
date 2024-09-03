from sqlalchemy import UniqueConstraint
from sqlalchemy.ext.hybrid import hybrid_property
from src import db, BaseMixin, ReprMixin


class Employee(db.Model, BaseMixin, ReprMixin):
    __tablename__ = 'employee'
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100))
    department = db.Column(db.String(100))