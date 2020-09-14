import storeRepository

def create(name, address):
    response = storeRepository.create(name, address)
    return response[0]

def list(name, address, pageSize, pageIndex, orderBy):
    return storeRepository.list(name, address, pageSize, pageIndex, orderBy)

def update(nameStore, addressStore, storeId):
    response = storeRepository.update(nameStore, addressStore, storeId)
    return response
