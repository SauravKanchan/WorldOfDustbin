from firebase import firebase
import json

firebase = firebase.FirebaseApplication('https://dj-hack.firebaseio.com', None)
result = firebase.get('/dustbins/', None)
#print(result)
data = {'cash': 70, 'currentUser': '', 'parent': '', 'percentFull': 100, 'queryText': 'Daddy 2 wants to buy a dustbin from Daddy 1', 'queryType': 0, 'streak': 0}
data2 = {'cash': 30, 'currentUser': '', 'parent': '', 'percentFull': 20, 'queryText': 'Daddy 1 agrees to sell a dustbin to Daddy 2', 'queryType': 1, 'streak': 0}
#data = json.dumps(data)
firebase.put('/dustbins', "1518880087182", data)

firebase.put('/dustbins',"1518880134851",data2)

