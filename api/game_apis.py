print(1)

import http.client


def getMyGames():
    conn = http.client.HTTPSConnection("www.notexponential.com")
    payload = ''
    headers = {
        'x-api-key': '03e8aca7ba031db05137',
        'userid': '890',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    conn.request("GET", "/aip2pgaming/api/index.php?type=myTeams", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

def createGame():
    conn = http.client.HTTPSConnection("www.notexponential.com")
    dataList = []
    boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
    dataList.append('--' + boundary)
    dataList.append('Content-Disposition: form-data; name=type;')

    dataList.append('Content-Type: {}'.format('multipart/form-data'))
    dataList.append('')

    dataList.append("game")
    dataList.append('--' + boundary)
    dataList.append('Content-Disposition: form-data; name=teamId1;')

    dataList.append('Content-Type: {}'.format('multipart/form-data'))
    dataList.append('')

    dataList.append("1194")
    dataList.append('--' + boundary)
    dataList.append('Content-Disposition: form-data; name=teamId2;')

    dataList.append('Content-Type: {}'.format('multipart/form-data'))
    dataList.append('')

    dataList.append("1192")
    dataList.append('--' + boundary)
    dataList.append('Content-Disposition: form-data; name=gameType;')

    dataList.append('Content-Type: {}'.format('multipart/form-data'))
    dataList.append('')

    dataList.append("TTT")
    dataList.append('--' + boundary + '--')
    dataList.append('')
    body = '\r\n'.join(dataList)
    payload = body
    headers = {
        'x-api-key': '03e8aca7ba031db05137',
        'userid': '890',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
    }
    conn.request("POST", "/aip2pgaming/api/index.php", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

def makeMove():
    conn = http.client.HTTPSConnection("www.notexponential.com")
    dataList = []
    boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
    dataList.append('--' + boundary)
    dataList.append('Content-Disposition: form-data; name=type;')

    dataList.append('Content-Type: {}'.format('multipart/form-data'))
    dataList.append('')

    dataList.append("move")
    dataList.append('--' + boundary)
    dataList.append('Content-Disposition: form-data; name=teamId;')

    dataList.append('Content-Type: {}'.format('multipart/form-data'))
    dataList.append('')

    dataList.append("1194")
    dataList.append('--' + boundary)
    dataList.append('Content-Disposition: form-data; name=gameId;')

    dataList.append('Content-Type: {}'.format('multipart/form-data'))
    dataList.append('')

    dataList.append("17")
    dataList.append('--' + boundary)
    dataList.append('Content-Disposition: form-data; name=move;')

    dataList.append('Content-Type: {}'.format('multipart/form-data'))
    dataList.append('')

    dataList.append("5,10")
    dataList.append('--' + boundary + '--')
    dataList.append('')
    body = '\r\n'.join(dataList)
    payload = body
    headers = {
        'x-api-key': '03e8aca7ba031db05137',
        'userid': '890',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
    }
    conn.request("POST", "/aip2pgaming/api/index.php?type=move&teamId=1194&gameId=17&move=5,10", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

def getMoves():
    conn = http.client.HTTPSConnection("www.notexponential.com")
    boundary = ''
    payload = ''
    headers = {
        'x-api-key': '03e8aca7ba031db05137',
        'userid': '890',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
    }
    conn.request("GET", "/aip2pgaming/api/index.php?type=moves&gameId=17&count=100", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

def getBoardMap():
    conn = http.client.HTTPSConnection("www.notexponential.com")
    boundary = ''
    payload = ''
    headers = {
        'x-api-key': '03e8aca7ba031db05137',
        'userid': '890',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
    }
    conn.request("GET", "/aip2pgaming/api/index.php?type=boardMap&gameId=16", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

def getBoardString():
    conn = http.client.HTTPSConnection("www.notexponential.com")
    payload = ''
    headers = {
        'x-api-key': '03e8aca7ba031db05137',
        'userid': '890',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    conn.request("GET", "/aip2pgaming/api/index.php?type=boardString&gameId=16", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
if __name__ == '__main__':
    getMyGames()
    makeMove()
    getMoves()
    getBoardMap()
    getBoardString()
