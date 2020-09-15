import storeService
import hug

@hug.get('/stores', examples='nameTerm=Apple%20Store&addressTerm=Infinity%20Loop&pageSize=162&pageIndex=12&orderBy=name%20desc')
def listStore(storeId=None, nameTerm=None, addressTerm=None, pageSize=20, pageIndex=0, orderBy='name asc'):
    try:
        pageSize = int(pageSize)
        pageIndex = int(pageIndex)

        response = storeService.list(nameTerm, addressTerm, pageSize, pageIndex, orderBy)
        return (response, 200)
    except Exception:
        return ("bad request", 400)

@hug.post('/stores')
def createStore(body):
    try:
        response = storeService.create(body['name'], body['address'])
        return (response, 201)
    except Exception:
        return ('bad request', 400)

@hug.put('/stores/{storeId}')
def updateStore(storeId, body):
    try:
        response = storeService.update(body['nameStore'], body['addressStore'], storeId)
        return (response, 204)
    except Exception:
        raise
        #return ('bad request', 400)

