import getBusData
import os
import time
from firebase import firebase
from datetime import datetime


while True:
	#b = getBusData.Bus()
	#b.update_response()
	#a = (b.get_all())
	a=[{'angle': 225, 'lon': 103.696123, 'id': 31416, 'type': 'Brown', 'speed': 2, 'lat': 1.341283, 'strange': '0'}, {'angle': 251, 'lon': 103.682832, 'id': 31534, 'type': 'Brown', 'speed': 15, 'lat': 1.34573, 'strange': '0'}]
	start_time = time.time()

	for i in range(len(a)):
		t = datetime.now().strftime("%d %m %Y %H:%M:%S")
		FBConn = firebase.FirebaseApplication('https://campus-bus-269f9.firebaseio.com/', None)
		print(FBConn.put('/-M07Dj-iCMw29oBZgnkU/Bus_ids/'+str(a[i]["id"]),t,{'Number of People': 0,
                    'Speed': a[i]["speed"],
                    'Color':a[i]["type"],
                    'Longitude': a[i]["lon"],
                    'Latitude': a[i]["lat"]
                    }))
		if (a[i]["speed"]<=8):
			os.system('python people_counter.py --prototxt mobilenet_ssd/MobileNetSSD_deploy.prototxt --model mobilenet_ssd/MobileNetSSD_deploy.caffemodel --input videos/example_01.mp4 --output output/output_03.avi --bus-id '+str(a[i]["id"]))
			f = open('crowd.txt', 'r')
			contents = f.read()
			contents = int(contents)
			print(FBConn.put('/-M07Dj-iCMw29oBZgnkU/Bus_ids/'+str(a[i]["id"])+'/'+t,'Number of People',contents))
	
	if (time.time() - start_time < 2):
		time.sleep(2 - (time.time() - start_time))

	break