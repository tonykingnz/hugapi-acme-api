import exceptions
import storeService
import hug

@hug.get('/stores', examples='nameTerm=Apple%20Store&addressTerm=Infinity%20Loop&pageSize=162&pageIndex=12&orderBy=name%20desc')
def listStore(nameTerm, addressTerm, pageSize, pageIndex, orderBy):
   return storeService.list(nameTerm, addressTerm, pageSize, pageIndex, orderBy)

#    try:
#        response = storeService.list(nameTerm, addressTerm, pageSize, pageIndex, orderBy)
#        return (response, 200)
#    except APICustomError as e:
#        return ("bad request", 400)

@hug.post('/stores', examples='name=Testing%20like%20crazy824y3ru2i3b328937894&address=fictiona%20street%202000')
def createStore(name, address):
    return storeService.create(name, address)

#@hug.put()'
#serviceStore.update(nameStore, addressStore)
