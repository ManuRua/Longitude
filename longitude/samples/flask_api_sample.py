from pprint import pprint
from longitude.core.rest_api.flask import LongitudeFlaskAPI
from longitude.core.rest_api.base import LongitudeRESTAPI

from marshmallow import Schema, fields

if __name__ == "__main__":
    class UserSchema(Schema):
        is_admin = fields.Boolean(default=False)
        username = fields.String(allow_none=False)
        first_name = fields.String(allow_none=False)
        last_name = fields.String(allow_none=False)


    class UserDetailSchema(Schema):
        details = fields.String()


    schemas = [UserSchema]
    api = LongitudeFlaskAPI(schemas=schemas)
    api.setup()
    api.add_path('/')
    api.add_path('/users', ['get', 'post'])  # This will use the UserSchema automagically
    api.add_path('/users/details', {'get': UserDetailSchema, 'post': UserDetailSchema})

    pprint(api._spec.to_dict())
