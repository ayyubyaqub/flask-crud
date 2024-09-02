
""" utils/schemas.py"""

# from flask_marshmallow import Marshmallow
# from marshmallow_sqlalchemy import ModelSchema, ModelSchemaOpts
# from .models import db


# class FlaskMarshmallowFactory(Marshmallow):

#     def __init__(self,  *args, **kwargs):
#         super(FlaskMarshmallowFactory, self).__init__(*args, **kwargs)


# class BaseOpts(ModelSchemaOpts):
#     def __init__(self, meta):
#         if not hasattr(meta, 'sql_session'):
#             meta.sqla_session = db.session
#         super(BaseOpts, self).__init__(meta)


# class BaseSchema(ModelSchema):
#     OPTIONS_CLASS = BaseOpts

# ma = FlaskMarshmallowFactory()



# new code

# from flask_marshmallow import Marshmallow
# from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, SQLAlchemySchemaOpts
# from .models import db

# class FlaskMarshmallowFactory(Marshmallow):

#     def __init__(self, *args, **kwargs):
#         super(FlaskMarshmallowFactory, self).__init__(*args, **kwargs)


# class BaseOpts(SQLAlchemySchemaOpts):
#     def __init__(self, meta):
#         if not hasattr(meta, 'sql_session'):
#             meta.sqla_session = db.session
#         super(BaseOpts, self).__init__(meta)


# class BaseSchema(SQLAlchemyAutoSchema):
#     OPTIONS_CLASS = BaseOpts

# ma = FlaskMarshmallowFactory()


from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from .models import db

class FlaskMarshmallowFactory(Marshmallow):

    def __init__(self, *args, **kwargs):
        super(FlaskMarshmallowFactory, self).__init__(*args, **kwargs)


class BaseSchema(SQLAlchemyAutoSchema):
    class Meta:
        sqla_session = db.session

ma = FlaskMarshmallowFactory()
