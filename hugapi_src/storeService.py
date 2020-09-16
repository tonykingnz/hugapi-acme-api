import storeRepository

def create(name, address):
    response = storeRepository.create(name, address)
    return response[0]

def list(storeId, name, address, pageSize, pageIndex, orderByTerm, orderByAscOrDesc):
    pageIndex = int(pageIndex)
    pageSize = int(pageSize)
    if orderByTerm == 'storeId':
        orderByTerm = 'store_id'
    elif orderByTerm == 'name':
        orderByTerm = 'name'
    elif orderByTerm == 'address':
        orderByTerm = 'address'
    else:
        raise Exception("Invalid paramter. Only storeId, name and address", 400)
    if orderByAscOrDesc == 'asc':
        orderByAscOrDesc = 'ASC'
    elif orderByAscOrDesc == 'desc':
        orderByAscOrDesc = 'DESC'
    else:
        raise Exception("Invalid paramter. Only asc or desc", 400)
        
    return storeRepository.list(storeId, name, address, pageSize, pageIndex, orderByTerm, orderByAscOrDesc)

def update(nameStore, addressStore, storeId):
    response = storeRepository.update(nameStore, addressStore, storeId)
    return response
