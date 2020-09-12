import storeRepository

def create(name, address):
    return storeRepository.create(name, address)

def list(name, address, pageSize=20, pageIndex=1, orderBy='name asc'):
    return storeRepository.list(name, address, pageSize, pageIndex, orderBy)
#    try:
#        return storeRepository.list(name, address, pageSize, pageIndex, orderBy)
#    except:
#        raise ApiCustomError("Store name must not be duplicated")
