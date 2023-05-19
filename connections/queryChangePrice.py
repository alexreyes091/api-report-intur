import psycopg2
from connections.conx import connection
from imageWork.image import getImageBytes
from connections.queryBase import getRequest, getRequestTypeId

cursor = connection()

def getRequestChangePrice(requestId):
    # Get data from table Request
    request = {}

    try:
        requestTypeId = getRequestTypeId(requestId)
        requestChangePrice = getListChangePrice(requestId)
        request = getRequest(requestId, requestTypeId, requestChangePrice)
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return request


def getListChangePrice(requestId):
    # Get data from table RequestChangePrice
    requestChangePrice = []

    try:
        cursor.execute('SELECT * FROM "RequestChangePrice" where "requestId" = ' + str(requestId) + ';')

        for data in cursor.fetchall():
            requestChangePrice.append({
                'id': data[0],
                'requestId': data[1],
                'pluCode': data[2],
                'description': data[3],
                'currentPrice': float(data[4]),
                'newPrice': float(data[5]),
                'applicationData': str(data[6]),
            })
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return requestChangePrice