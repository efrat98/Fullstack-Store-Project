from marshmallow import Schema,fields,validate
class userRegisterSchema(Schema):
    name= fields.Str(required=True,validate=validate.Length(min=2,max=20))
    password=fields.Str(required=True,validate=validate.Length(min=7,max=20))
    email=fields.Email(required=True)
    phone=fields.Str(required=True,validate=validate.Length(10))

class userLoginSchema(Schema):
    password = fields.Str(required=True, validate=validate.Length(min=7, max=20))
    email = fields.Email(required=True)