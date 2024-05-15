from models import icecreamModel
from flask import jsonify

# IcecreamInventroy item create service
def create(requestData):
    try:
        responseData = icecreamModel.create(requestData)
        response = {
            "message": "Item Created Successfully",
            "data": responseData
        }
        return jsonify(response), 201
    except Exception:
        response = {
            "message": "Icecream Already Exists",
        }
        return jsonify(response),406


# IcecreamInventroy item update service
def update(requestData):
    responseData = icecreamModel.update(requestData)
    if responseData==None:
        response = {
            "message": "item NOT updated successfully",
        }
        return response
    response = {
        "message": "item updated successfully",
        "data": responseData
    }
    return jsonify(response), 201


# IcecreamInventroy item delete service
def delete(requestData):
    icecreamModel.delete(requestData)
    response = {
        "message": "item deleted successfully",
    }
    return jsonify(response), 201


# IcecreamInventroy item availability check service
def availability(requestData):
    responseData = icecreamModel.availability(requestData)
    availabe = responseData['Quantity']>0

    response = {
        "availability":availabe,
        "data": responseData
    }
    return jsonify(response), 201
