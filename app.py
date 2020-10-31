import json
import storeService
import storeItemService
import storeOrderService
import hug

#
#Store
#

@hug.get('/stores', examples='storeId=3&nameTerm=Apple%20Store&addressTerm=Infinity%20Loop&pageSize=162&pageIndex=12&orderBy=storeI%20asc')
def listStore(storeId=None, nameTerm=None, addressTerm=None, pageSize=20, pageIndex=0, orderBy='storeId asc'):
    try:
        response = storeService.list(storeId, nameTerm, addressTerm, pageSize, pageIndex, orderBy)
        return (response, 200)
    except Exception:
        return ("bad request", 400)

@hug.post('/stores')
def createStore(body):
    try:
        response = storeService.create(body['name'], body['address'])
        response_with_statuscode = {'body': response, 'status_code': 201}
        return json.dumps(response_with_statuscode)
    
    except Exception:
        #raise
        response = {"message":"Store not created", "status_code": 400}
        return json.dumps(response)

@hug.put('/stores/{storeId}')
def updateStore(storeId, body):
    try:
        response = storeService.update(body['name'], body['address'], storeId)
        return (response, 204)
    except Exception:
        return ('Store not updated', 400)

#
#Store Items
#

@hug.post('/stores/{storeId}/items')
def createStoreItem(storeId, body):
    try:
        response = storeItemService.createItem(storeId, body['name'], body['unit'], body['image'], body['category'], body['lastPrice'])
        return (response, 201)
    except Exception:
        return ('Bad request, may the key is dublicated', 400)

@hug.get('/stores/{storeId}/items', examples='51/items?categoryTerm=service&unitTerm=kg&nameTerm=meat&pageSize=20&pageIndex=0')
def listStore(storeId, categoryTerm, unitTerm=None, nameTerm=None, pageSize=20, pageIndex=0):
    try:
        response = storeItemService.list(storeId, categoryTerm, unitTerm, nameTerm, pageSize, pageIndex)
        return (response, 200)
    except Exception:
        #raise
        return ("bad request", 400)

#
#Order item
#

@hug.post('/stores/{storeId}/orders')
def orderItem(storeId, body):
    try:
        response= storeOrderService.orderItem(storeId, body['storeOrderId'], body['customerId'], body['confirmationDate'], body['status'], body['item'])
        return (response, 201)
    except Exception:
        raise
        #return ("Bad request", 400)

