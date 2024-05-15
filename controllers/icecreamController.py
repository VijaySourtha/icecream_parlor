from flask import request
from services import icecreamService

# IcecreamInventroy item create controller
def create():
    body = request.json
    return icecreamService.create(body)


# IcecreamInventroy item update controller
def update(id):
    body = request.json
    body['id']=id
    return icecreamService.update(body)


# IcecreamInventroy item delete controller
def delete(id):
     return icecreamService.delete(id)


# IcecreamInventroy item availability check controller
def availability():
    body = request.json
    return icecreamService.availability(body)
    