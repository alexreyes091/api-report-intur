import psycopg2
from connections.conx import connection
from imageWork.image import getImageBytes
from connections.queryBase import ( 
    getRequest, getRequestTypeId, getActivationType, 
    getStoreCategory, getStoreCategoryPmix, getStorePOS, 
    getTax, 
)

cursor = connection()

def getRequestCreation(requestId):
    # Get data from table Request
    request = {}

    try:
        requestTypeId = getRequestTypeId(requestId)
        requestCreation = getListCreation(requestId)
        request = getRequest(requestId, requestTypeId, requestCreation)
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return request


def getListCreation(requestId):
    # Get data from table RequestCreation
    requestCreation = []

    try:
        cursor.execute('SELECT * FROM "RequestCreation" where "requestId" = ' + str(requestId) + ';')

        for data in cursor.fetchall():
            requestCreation.append({
                'id': data[0],
                'requestId': data[1],
                'activationType': getActivationType(data[2]).upper(),
                'storeCategory': getStoreCategory(data[3]).upper(),
                'storeCategoryPmix': getStoreCategoryPmix(data[4]).upper(),
                'storePOS': getStorePOS(data[5]).upper(),
                'tax': getTax(data[6]),
                'bkpn': data[7],
                'daysDuration': data[8],
                'schedule': data[9],
                'oldAge': data[10],
                'oldAgeQty': data[11],
                'oldAgeDiscount': data[12],
                'totalCost': data[13],
                'kitchenTimeChilis': data[14],
                'countingFrequency': data[15],
                'startDate': str(data[16])[:10],
                'endDate': str(data[17])[:10],
                'requestPLU': getPrice(requestId),
                'requestModifier': getRequestModifier(requestId),
                'requestRecipe': getRecipe(requestId),
                'requestPack': getPack(requestId),
            })
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return requestCreation

def getPrice(requestId):
    # Get data from table RequestCreation
    price = []

    try:
        cursor.execute('SELECT * FROM "RequestPrice" where "requestId" = ' + str(requestId) + ';')

        for data in cursor.fetchall():
            price.append({
                'saleChannel': getSaleChannel(data[2]),
                'clientTicket': data[3],
                'KitchenMonitor': data[4],
                'namePosButton': data[5],
                'price': data[6],
            })
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return price

def getPriceId(requestId):
    # Get data from table RequestCreation
    id = 0

    try:
        cursor.execute('SELECT * FROM "RequestPrice" where "requestId" = ' + str(requestId) + ';')
        id = cursor.fetchone()[0]

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return id

def getSaleChannel(saleChannelId):
    # Get data from table SaleChanel
    saleChannel = ''

    try:
        cursor.execute('SELECT * FROM "SaleChannel" where "id" = ' + str(saleChannelId) + ';')
        saleChannel = cursor.fetchone()[1]
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return saleChannel

def getRequestModifier(requestId):
    # Get data from table RequestModifier
    requestModifier = []

    try:
        cursor.execute('SELECT * FROM "RequestModifier" where "requestId" = ' + str(requestId) + ';')

        for data in cursor.fetchall():
            requestModifier.append({
                'id': data[0],
                'name': data[2],
                'minimun': data[3],
                'maximun': data[4],
                'istake': data[6],
                'ishere': data[7],
                'requestModifierOption': getRequestModifierOption(data[0]),
            })
        print(requestModifier)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return requestModifier


def getRequestModifierOption(requestModifierId):
    # Get data from table RequestModifierOption
    requestModifierOption = []

    try:
        cursor.execute('SELECT * FROM "RequestModifierDetail" where "requestModifierId" = ' + str(requestModifierId) + ';')

        for data in cursor.fetchall():
            requestModifierOption.append({
                'id': data[0],
                'recipeCode': data[2],
                'itemName': data[4],
                'itemMin': data[6],
                'itemMax': data[7],
                'price': data[9],
                'cost': data[10],
            })
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return requestModifierOption


def getRecipe(requestId):
    # Get data from table RequestRecipe
    recipe = []

    try:
        cursor.execute('SELECT * FROM "RequestRecipe" where "requestId" = ' + str(requestId) + ';')

        for data in cursor.fetchall():
            recipe.append({
                'id': data[0],
                'sapCode': data[2],
                'description': data[3],
                'measure': data[4],
                'amount': data[5],
                'unitCost': data[6],
                'totalCost': data[7],
                'pluCode': data[9],
            })
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return recipe

def getPack(requestId):
    id = getPriceId(requestId)
    pack = []

    try:
        cursor.execute('SELECT * FROM "RequestPack" where "requestPriceId" = ' + str(id) + ';')
        
        for data in cursor.fetchall():
            pack.append({
                'id': data[0],
                'sapCode': data[2],
                'description': data[3],
                'quantity': data[4],
                'mphere': data[6],
                'mptake': data[7],
                'mpcar': data[8],
            })
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    return pack