import storeRepository

def create(name, address):
    response = storeRepository.create(name, address)
    return response[0]

def list(name, address, pageSize, pageIndex, orderBy):
    return storeRepository.list(name, address, pageSize, pageIndex, orderBy)
