from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

# Ensure all other imports are correct and available
from .models import BaseMixin, ReprMixin
from .api import api
from .factory import create_app
from .schemas import BaseSchema