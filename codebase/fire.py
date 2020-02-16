from firebase import firebase
def getVacancies():
    result=[]
    FBConn = firebase.FirebaseApplication('https://campus-bus-269f9.firebaseio.com/', None)
    ans2 = ((FBConn.get('-M07Dj-iCMw29oBZgnkU/Bus_ids/', None)))
    new2 = list(ans2.keys())
    for i in new2:
        ans = ((FBConn.get('-M07Dj-iCMw29oBZgnkU/Bus_ids/'+i, None)))
        new = list(ans.keys())
        new1 = new[len(new)-1]
        fin = (FBConn.get('-M07Dj-iCMw29oBZgnkU/Bus_ids/'+i+'/'+new1+'/Number of People', None))
        result.append([i, FBConn.get('-M07Dj-iCMw29oBZgnkU/Bus_ids/'+i+'/'+new1+'/Color', None), fin])
    return result