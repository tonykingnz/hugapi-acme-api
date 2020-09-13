import storeService
import hug

@hug.get('/stores', examples='nameTerm=Apple%20Store&addressTerm=Infinity%20Loop&pageSize=162&pageIndex=12&orderBy=name%20desc')
def listStore(nameTerm, addressTerm, pageSize=20, pageIndex=1, orderBy='name asc'):
    try:
        pageSize = int(pageSize)
        pageIndex = int(pageIndex)

        response = storeService.list(nameTerm, addressTerm, pageSize, pageIndex, orderBy)
        return (response, 200)
    except Exception:
        raise
        #return ("bad request", 400)

@hug.post('/stores', examples='name=Testing%20like%20crazy824y3ru2i3b328937894&address=fictiona%20street%202000')
def createStore(body):
    try:
        response = storeService.create(body['name'], body['address'])
        return (response, 201)
    except Exception:
        return ('bad request', 400)

#@hug.put()'
#serviceStore.update(nameStore, addressStore)
