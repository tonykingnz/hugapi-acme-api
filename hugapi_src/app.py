import storeService
import hug

@hug.get('/stores', examples='storeId=3&nameTerm=Apple%20Store&addressTerm=Infinity%20Loop&pageSize=162&pageIndex=12&orderBy=storeI%20asc')
def listStore(storeId=None, nameTerm=None, addressTerm=None, pageSize=20, pageIndex=0, orderBy='storeId asc'):
    try:
        response = storeService.list(storeId, nameTerm, addressTerm, pageSize, pageIndex, orderBy)
        return (response, 200)
    except Exception:
        raise
        #return ("bad request", 400)

@hug.post('/stores')
def createStore(body):
    try:
        response = storeService.create(body['name'], body['address'])
        return (response, 201)
    except Exception:
        return ('Store not created', 400)

@hug.put('/stores/{storeId}')
def updateStore(storeId, body):
    try:
        response = storeService.update(body['nameStore'], body['addressStore'], storeId)
        return (response, 204)
    except Exception:
        return ('Store not updated', 400)

