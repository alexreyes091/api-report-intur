import psycopg2
from connections.conx import connection
from imageWork.image import getImageBytes
from connections.queryBase import getRequest, getRequestTypeId, getStoreCategory
from connections.queryCreation import getSaleChannel

cursor = connection()

def getRequestActivation(requestId):
    # Get data from table Request
    request = {}

    try:
        requestTypeId = getRequestTypeId(requestId)
        requestActivation = getListActivation(requestId)
        request = getRequest(requestId, requestTypeId, requestActivation)
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return request


def getListActivation(requestId):
    # Get data from table RequestChangePrice
    requestActivation = []

    try:
        cursor.execute('SELECT * FROM "RequestActivation" where "requestId" = ' + str(requestId) + ';')

        for data in cursor.fetchall():
            requestActivation.append({
                'id': data[0],
                'requestId': data[1],
                'pluCode': data[2],
                'pluName': data[3],
                'price': float(data[4]),
                'totalCost': float(data[5]),
                'activationDate': str(data[6]),
                'deactivationDate': str(data[7]),
                'schedule': str(data[8]),
                'saleChannel': getSaleChannel(str(data[10])),
                'storeCategory': getStoreCategory(str(data[11])),
            })
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return requestActivation