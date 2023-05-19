import psycopg2
from connections.conx import connection
from imageWork.image import getImageBytes

cursor = connection()

def getRequest(requestId, requestTypeId, requestData):
    # --------------------------------
    # Get data from table Request
    # --------------------------
    request = {}

    try:
        cursor.execute('SELECT * FROM "Request" where "id" = ' + str(requestId) + ' and "requestTypeId" = ' + str(requestTypeId) + ';')

        for data in cursor.fetchall():
            request['id'] = data[0]
            request['storeId'] = data[1]
            request['store'] = getStore(data[1])
            request['screen'] = getScreen(data[1])
            request['requestType'] = getRequestType(data[2]);
            request['applicantName'] = data[5]
            request['about'] = data[8]
            request['requestDate'] = str(data[11])
            request['requestData'] = requestData
            request['storeSignatureFlow'] = getStoreSignatureFlow(data[1], data[0], requestTypeId)
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return request


def getScreen(storeId):
    # Get data from table Screen
    print(storeId)
    screen = ''

    try:
        cursor.execute('SELECT * FROM "StoreScreen" where "storeId" = ' + str(storeId) + ';')
        screen = cursor.fetchone()[3];

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return screen


def getRequestType(requestTypeId):
    # --------------------------------
    # Get data from table RequestType
    # ------------------------
    requestType = {}
    
    try:
        cursor.execute('SELECT * FROM "RequestType" where "id" = ' + str(requestTypeId) + ';')

        for data in cursor.fetchall():
            requestType['id'] = data[0]
            requestType['code'] = data[1]
            requestType['description'] = data[2]
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    return requestType['description']

def getRequestTypeId(requestId):
    # --------------------------------
    # Get data from table RequestType
    # -----------------------
    try:
        cursor.execute('SELECT * FROM "Request" where "id" = ' + str(requestId) + ';')
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    return cursor.fetchone()[2]


def getRequestSigner(requestId, signerId):
    # -----------------------------------
    # Get data from table RequestSigner
    # ----------------------------
    requestSigner = {}

    try:
        cursor.execute('SELECT * FROM "RequestSigner" where "requestId" = ' + str(requestId) + ' and "signerId" = ' + str(signerId) + ';')

        for data in cursor.fetchall():
            requestSigner['signed'] = data[5]
            requestSigner['date'] = data[6]
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return requestSigner


def getActivationType(activationTypeId):
    # -----------------------------------
    # Get data from table ActivationType
    # ------------------------
    activationType = {}

    try:
        cursor.execute('SELECT * FROM "ActivationType" where "id" = ' + str(activationTypeId) + ';')

        for data in cursor.fetchall():
            activationType['id'] = data[0]
            activationType['description'] = data[1]
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return activationType['description']

def getTax(taxId):
    # ----------------------------
    # Get data from table Tax
    # ---------------------
    tax = ''
    try:
        cursor.execute('SELECT * FROM "Tax" where "id" = ' + str(taxId) + ';')
        tax = cursor.fetchone()[1]

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return tax


def getStoreCategory(storeCategoryId):
    # ----------------------------------
    # Get data from table StoreCategory
    # -------------------------
    storeCategory = ''

    try:
        cursor.execute('SELECT * FROM "StoreCategory" where "id" = ' + str(storeCategoryId) + ';')

        storeCategory = cursor.fetchone()[2]

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return storeCategory

def getStoreCategoryPmix(storeCategoryPmixId):
    # ----------------------------------
    # Get data from table StoreCategory
    # -------------------------
    storeCategoryPmix = ''

    try:
        cursor.execute('SELECT * FROM "StoreCategoryPmix" where "id" = ' + str(storeCategoryPmixId) + ';')

        storeCategoryPmix = cursor.fetchone()[2]

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return storeCategoryPmix


def getStorePOS(storePOSId):
    # -----------------------------
    # Get data from table StorePOS
    # ------------------------
    storePOS = ''

    try:
        cursor.execute('SELECT * FROM "StorePOS" where "id" = ' + str(storePOSId) + ';')

        storePOS = cursor.fetchone()[2]

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return storePOS

def getStoreScreen(storeScreenId):
    # -------------------------------
    # Get data from table StoreScreen
    # --------------------------
    storeScreen = ''

    try:
        cursor.execute('SELECT * FROM "StoreScreen" where "id" = ' + str(storeScreenId) + ';')

        storeScreen = cursor.fetchone()[3]

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return storeScreen

def getUserName(userId):
    # -------------------------
    # Get data from table User
    # -----------------
    user = {}

    try:
        cursor.execute('SELECT * FROM "User" where "id" = ' + str(userId) + ';')

        for data in cursor.fetchall():
            user['id'] = data[0]
            user['name'] = data[5]
            user['lastName'] = data[6]
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return user['name'] + ' ' + user['lastName']



def getUserSignature(userId):
    # -------------------------
    # Get data from table User
    # -------------------
    pathSignature = ''
    cur = connection()
    try:
        cur.execute('SELECT image FROM "UserSignature" where "userId" = ' + str(userId) + ';')

        image_bytes = cur.fetchone()[0]
        pathSignature = getImageBytes(image_bytes, getUserName(userId), userId)
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    cur.close()
    return pathSignature


def getStore(storeId):
    # --------------------------
    # Get data from table Store
    # ---------------------

    store = {}

    try:
        cursor.execute('SELECT * FROM "Store" where "id" = ' + str(storeId) + ';')

        for data in cursor.fetchall():
            store['id'] = data[0]
            store['code'] = data[1]
            store['name'] = data[2]
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    return store['name']

def getStoreSignatureFlow(storeId, requestId, requestTypeId):
    # -------------------------------------------
    # Get data from table StoreSignatureFlow
    # --------------------------------
    storeSignatureFlow = []

    try:
        cursor.execute('SELECT * FROM "StoreSignatureFlow" where "storeId" = ' + str(storeId) + ' and "requestTypeId" = ' + str(requestTypeId) + ';')

        for data in cursor.fetchall():
            storeSignatureFlow.append({
                'id': data[0],
                'storeId': getStore(data[1]),
                'requestType': getRequestType(data[2]),
                'userId': data[3],
                'user': getUserName(data[3]),
                'position': data[4],
                'signed': getRequestSigner(requestId, data[3]),
                'signature': getUserSignature(data[3]),
            })
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return storeSignatureFlow


def getRequestLog(requestId, requestTypeId):
    # --------------------------------
    # Get data from table RequestLog
    # -----------------------
    requestLog = []

    try:
        cursor.execute('SELECT * FROM "RequestLog" where "requestId" = ' + str(requestId) + ' and "requestTypeId" = ' + str(requestTypeId) + ';')

        for data in cursor.fetchall():
            requestLog.append({
                'id': data[0],
                'requestId': data[1],
                'requestType': getRequestType(data[2]),
                'date': str(data[3]),
                'user': getUserName(data[4]),
                'description': data[5],
            })
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    return requestLog