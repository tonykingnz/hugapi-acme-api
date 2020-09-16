import storeRepository

def create(name, address):
    response = storeRepository.create(name, address)
    return response[0]

def list(storeId, name, address, pageSize, pageIndex, orderBy):
    pageIndex = int(pageIndex)
    pageSize = int(pageSize)
    if orderBy == 'storeId asc':
        orderBy = 'storeId asc'
    elif orderBy == 'storeId desc':
        orderBy = 'storeId desc'
    elif orderBy == 'name asc':
        orderBy = 'name asc'
    elif orderBy == 'name desc':
        orderB  = 'name desc'
    elif orderBy == 'address asc':
        orderBy = 'address asc'
    elif orderBy == 'address desc':
        orderB  = 'address  desc'
    else:
        raise Exception("Invalid paramter. Only asc or desc", 400)
        
    return storeRepository.list(storeId, name, address, pageSize, pageIndex, orderBy)

def update(nameStore, addressStore, storeId):
    response = storeRepository.update(nameStore, addressStore, storeId)
    return response
