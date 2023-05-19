import psycopg2
from connections.conx import connection
from connections.queryBase import getRequest, getRequestTypeId

cursor = connection()

def getRequestDeactivation(requestId):
    # Get data from table Request
    request = {}

    try:
        requestTypeId = getRequestTypeId(requestId)
        requestDeactivation = getListDeactivation(requestId)
        request = getRequest(requestId, requestTypeId, requestDeactivation)
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return request

def getListDeactivation(requestId):
    # Get data from table RequestDeactivation
    requestDeactivation = []

    try:
        cursor.execute('SELECT * FROM "RequestDeactivation" where "requestId" = ' + str(requestId) + ';')

        for data in cursor.fetchall():
            requestDeactivation.append({
                'id': data[0],
                'pluCode': data[2],
                'description': data[3],
                'comment': data[6],
                'deactivationDate': data[4],
            })
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return requestDeactivation
