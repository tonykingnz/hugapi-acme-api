import storeRepository

def create(name, address):
    response = storeRepository.create(name, address)
    return response[0]

def list(storeId, name, address, pageSize, pageIndex, orderByTerm, orderByAscOrDesc):
    pageIndex = int(pageIndex)
    pageSize = int(pageSize)
    if orderByTerm == 'storeId':
        return orderByTerm = 'store_id'
    elif orderByTerm == 'name':
        return orderByTerm = 'name'
    elif orderByTerm == 'address':
        return orderByTerm = 'address'
    else:
        raise Exception:
            return ("Invalid paramter. Only storeId, name and address", 400)
    if orderByAscOrDesc == 'asc':
        return orderByTerm = 'asc'
    elif orderByAscOrDesc == 'asc':
        return orderByTerm = 'asc'
    else:
        raise Exception:
            return ("Invalid paramter. Only asc or desc", 400)
        
    return storeRepository.list(storeId, name, address, pageSize, pageIndex, orderByTerm, orderByAscOrDesc)

def update(nameStore, addressStore, storeId):
    response = storeRepository.update(nameStore, addressStore, storeId)
    return response
