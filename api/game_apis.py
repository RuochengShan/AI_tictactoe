print(1)

#Create game:

import requests

url = "https://www.notexponential.com/aip2pgaming/api/index.php"

payload = {'type': 'game',
'teamId1': '1194',
'teamId2': '1192',
'gameType': 'TTT'}
files = [

]
headers = {
  'x-api-key': '03e8aca7ba031db05137',
  'userid': '890',
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data = payload, files = files)

print(response.text.encode('utf8'))

#Get my teams:

import requests

url = "http://www.notexponential.com/aip2pgaming/api/index.php?type=myTeams"

payload = {}
headers = {
  'x-api-key': '03e8aca7ba031db05137',
  'userid': '890',
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))

#Get my games

import requests

url = "https://www.notexponential.com/aip2pgaming/api/index.php?type=myGames"

payload = {}
headers = {
  'x-api-key': '03e8aca7ba031db05137',
  'userid': '890',
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))

#Make a move
import requests

url = "http://www.notexponential.com/aip2pgaming/api/index.php"

payload = {'type': 'move',
'teamId': '1194',
'gameId': '16',
'move': '5,9'}
files = [

]
headers = {
  'x-api-key': '03e8aca7ba031db05137',
  'userid': '890',
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data = payload, files = files)

print(response.text.encode('utf8'))

#Get board map
import requests

url = "http://www.notexponential.com/aip2pgaming/api/index.php?type=boardMap&gameId=16"

payload = {}
files = {}
headers = {
  'x-api-key': '03e8aca7ba031db05137',
  'userid': '890',
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("GET", url, headers=headers, data = payload, files = files)

print(response.text.encode('utf8'))

#Get moves
import requests

url = "http://www.notexponential.com/aip2pgaming/api/index.php?type=moves&gameId=16&count=10"

payload = {}
files = {}
headers = {
  'x-api-key': '03e8aca7ba031db05137',
  'userid': '890',
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("GET", url, headers=headers, data = payload, files = files)

print(response.text.encode('utf8'))

