import storeItemRepository

def createItem(storeId, name, unit, image, category, lastPrice):
    response = storeItemRepository.create(storeId, name, unit, image, category, lastPrice)
    return response[0]

def list(storeId, categoryTerm, unitTerm, nameTerm, pageSize, pageIndex):
    storeId = str(storeId)
    pageIndex = int(pageIndex)
    pageSize = int(pageSize)

    '''
    
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

    '''     
    return storeItemRepository.list(storeId, categoryTerm, unitTerm, nameTerm, pageSize, pageIndex)

def update(nameStore, addressStore, storeId):
    response = storeItemRepository.update(nameStore, addressStore, storeId)
    return response
