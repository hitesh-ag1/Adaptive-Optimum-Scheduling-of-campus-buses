# Adaptive-Optimum-Scheduling-of-campus-buses
The project will be addressing Goal 11 of the UN sustainable development goals which is to make cities and human settlements inclusive, safe, resilient and sustainable. 
This theme will be applied to the NTU community and the project will focus on solving the problem with the scheduling of campus buses with utmost practicality and scalability so that the solution could be implemented in the real world. 
To be more specific, the project’s aim will be to minimize waiting time, fuel wastage and overcrowding of buses in peak hours.

# Project Description - 
The project will focus on solving the problem by developing a:
(1) Backend computer vision system inside the buses which detects the number of people entering and leaving the buses.
(2) Frontend application for users showing the crowd in the incoming buses so that if they are full, users can find an alternative.
(3) Backend database which can be used in the future for predicting demand of buses using machine learning techniques.

# Outline of the details - 

(1) Data provided by NTU in HTTP request call: eg, [{'angle': 225, 'lon': 103.696123, 'id': 31416, 'type': 'Brown', 'speed': 31, 'lat': 1.341283, 'strange': '0'}, {'angle': 251, 'lon': 103.682832, 'id': 31534, 'type': 'Brown', 'speed': 17, 'lat': 1.34573, 'strange': '0'}]. Used Python Requests library to obtain this data every 2 seconds. 
(2) When the speed of buses go less than 8 km/hr, only then are the cameras activated.
(3) For detecting the number of people entering and leaving the buses, pyimage’s object tracking algorithm, pre-trained mobilenet ssd caffe model was used directly from the internet in Python. The solution was implemented in Python and works for only one camera at once (not parallely) i.e. data is sent to database only one camera at a time as the Multithreading library wasn’t working locally on my laptop. But it can be implemented parallely over the cloud. As there was no dataset for NTU’s actual conditions, example video is taken from the internet.
(4) The data is collected and written to Firebase Realtime Database which was chosen due to its scalability. It can be viewed at: https://campus-bus-269f9.firebaseio.com/ . It goes from BusID -> Time -> All the attributes i.e. Loop colour, Latitude, Longitude, Number of people, Speed.
(5) Finally, the front end application is made using Pygame and tkinter. Here, the data is read from the database explained previously.

# Navigating through the code:
(1) The “Platform” folder is purely the front end i.e. Point 5 of the previous section. Inside it, the “fire.py” file is reading data from the database and the “main.py” file is the main frontend file. The rest of the files are supporting files for main.py.

(2) The “Codebase” has the backend files i.e. Points 1-4 of the previous section. The “people-counter.py” is the file which detects how many people are entering and leaving the bus. The pre-trained MobileNet SSD caffe model is used from the “mobilenet_ssd” folder and the algorithm for object tracking in the “pyimagesearch” folder. “Videos” folder has example input videos for the model. “Output” folder has the recording of the model running on the video. The “fire.py” file is the same as the one in the frontend folder. “getBusData” is the http request file for obtaining NTU’s realtime current bus data. “Crowd.txt” is used as a support file for “getBusData.py.” The “busDataProcess.py” is for managing firebase and computer vision together i.e. switching on the camera’s only when speed of bus is less than 8 km/h, counting number of people who went inside and came outside the doors and writing it to the realtime database.

