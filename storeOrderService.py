import storeOrderRepository

def orderItem(storeId, storeOrderId, customerId, confirmationDate, status, item):
    print(item)
    item_updated = str(item)
    print(storeId, storeOrderId, customerId, confirmationDate, status, item_updated)
    response = storeOrderRepository.orderItem(storeId, storeOrderId, customerId, confirmationDate, status, item_updated)
    return response[0]
