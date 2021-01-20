import json
import requests

def loginFunction(userName , password):
    data_get = {
        "username": userName,
        "password": password
    }

    x = requests.request(method='post', url='http://127.0.0.1:8000/logs/login/', data=data_get)

    if x.status_code != 200:
        print("invalid or user with this name and password not exist.")
        return 0                                            #If zero then invalid username or password...

    else:
        return x.json()


def changePassword(email,newPassword):
    print("Write API here which will change the user password for the given email.")


def getAllUsersDetail():
    x = requests.request(method='get', url='http://127.0.0.1:8000/logs/profile/')
    if x.status_code != 200:
        return 0                                            #If zero then invalid username or password...

    else:
        return x.json()

def addNewSupervisor(name,email,password):
    data_get = {
        "name": name,
        "email" : email,
        "password": password,
        "role" : "spervisor"
        }

    x = requests.request(method='post', url='http://127.0.0.1:8000/logs/profile/', data=data_get)
    if x.status_code != 200:
        return 0
    else:
        return 1

def editSupervisor(id , name,email,password):
    data_get = {
        "name": name,
        "email": email,
        "password": password,
        "role": "spervisor"
    }

    x = requests.request(method='put', url='http://127.0.0.1:8000/logs/profile/'+str(id)+"/", data=data_get)
    if x.status_code != 200:
        return 0
    else:
        return 1
    print(x)

def addNewInspector(name,email,password):
    data_get = {
        "name": name,
        "email" : email,
        "password": password,
        "role" : "inspector"
        }

    x = requests.request(method='post', url='http://127.0.0.1:8000/logs/profile/', data=data_get)
    if x.status_code != 200:
        return 0
    else:
        return 1

def editInspector(id , name,email,password):
    data_get = {
        "name": name,
        "email": email,
        "password": password,
        "role": "inspector"
    }

    x = requests.request(method='put', url='http://127.0.0.1:8000/logs/profile/'+str(id)+"/", data=data_get)
    if x.status_code != 200:
        return 0
    else:
        return 1
    print(x)

def getAllBatchData():
    x = requests.request(method='get', url='http://127.0.0.1:8000/logs/batch/')
    if x.status_code != 200:
        return 0  # If zero then invalid username or password...

    else:
        return x.json()

def deleteSuperVisor(userID):
    print(userID)
    x = requests.request(method='delete', url='http://127.0.0.1:8000/logs/profile/'+str(userID))
    return x

def stat(user_id=1):

    batches = requests.request(method='get', url='http://127.0.0.1:8000/logs/batch/')
    batches = batches.json()
    # logged in user id

    results = requests.request(method='get', url='http://127.0.0.1:8000/logs/results/')
    results = results.json()

    temp = []
    for batch in batches:
        if batch['user_id'] == user_id:
            temp.append(batch)
    batches = temp
    temp = []
    for batch in batches:
        for r in results:
            if r['test_id'] == batch['test_id']:
                temp.append(r)

    results = temp

    NofBatches = len(batches)
    total_packets = len(results)
    valid = 0
    invalid = 0
    for i in results:
        if i['result_status'] == 'valid':
            valid += 1
        else:
            invalid += 1

    return NofBatches , total_packets ,valid , invalid

def saveInspectionResult(result):
    data_get = {"result_status": result,
                "test_id": 1}
    x = requests.request(method='post', url='http://127.0.0.1:8000/logs/results/', data=data_get)
    print(x)