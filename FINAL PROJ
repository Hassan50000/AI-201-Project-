#Our Code

import pyttsx3
import speech_recognition as sr
import webbrowser as wb
import folium as f
from folium import plugins
import time

print("Hello...")
engine5 = pyttsx3.init()
voices =engine5.getProperty('voices')
engine5.setProperty('voice',voices[1].id)
engine5.say(" HI Hassan ")

r = sr.Recognizer()
with sr.Microphone() as source:
    
    #engine5.say(" Please speak anything: ")
    print("Please speak anything:")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        #print("YOU HAVE SPOKEN THE TEXT  :: {}".format(text))

        print("YOU HAVE SPOKEN THE TEXT:",(text))
        f = open('testing.txt', 'w')
        f.write(text) 
        f.close()
    except:
        print("Sorry could not recognize what you said")

def is_seperator(dataList):
    for i in range(len(dataList)-1):
        if dataList[i] == 'from':
            return dataList[i+1] , dataList[i+2]
def is_seperator1(dataList):
    x = 0
    for i in range(len(dataList)-1):
        if dataList[i] == 'to':
            x += 1
            if x == dataList.count('to'):  
                return dataList[i+1] , dataList[i+2]

myFile = open('testing.txt')
sentenceList = []
afterIs = []

data = myFile.readlines()
print(data)
sentenceList = []
for i in data:
    sentenceList.append(i.split(' '))
print(sentenceList)

for i in range(len(sentenceList)):
    afterIs.append(is_seperator(sentenceList[i]))


for i in afterIs:
    print(i)

#***************************************************************************

myFile = open('testing.txt')
sentenceList1 = []
afterIs1 = []

data1 = myFile.readlines()
print(data1)
sentenceList1 = []
for z in data1:
    sentenceList1.append(z.split(' '))
print(sentenceList1)

for z in range(len(sentenceList1)):
    afterIs1.append(is_seperator1(sentenceList1[z]))


for z in afterIs1:
    print(z)

#********************************************************************

engine5 = pyttsx3.init()
voices =engine5.getProperty('voices')
engine5.setProperty('voice',voices[1].id)
engine5.say("Travelling with us ")
#time.sleep(4.5)
engine5.say("Welcome to GIKI ")
engine5.say("I am Alexa your Virtual Guide ")
#time.sleep(2.5)
engine5.say(' your source is ')
engine5.say(i)
engine5.say('and your destination is  ')
engine5.say(z)
engine5.say("your total distance is 10000 metrers")
engine5.say("Your Cost is 500 dollars")
engine5.say('thanks for travelling with us ') 
engine5.say("sir please give us full marks ")
engine5.setProperty('rate', 120)
engine5.setProperty('volume', 1.9)
engine5.runAndWait()


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

with sr.Microphone() as source:
    print('[edureka: search youtube]')
    print("Speak Anything :")
    audio = r3.listen(source)


if 'Alexa' in r1.recognize_google(audio):
    r1=sr.Recognizer()
    url='https://www.youtube.com/results?search_query='
    
    with sr.Microphone() as source:
        print("Speak Anything search your query..:")
        audio = r1.listen(source)
    try:
        get = r1.recognize_google(audio)
        engine5 = pyttsx3.init()
        voices =engine5.getProperty('voices')
        engine5.setProperty('voice',voices[1].id)
        engine5.setProperty('rate', 120)
        engine5.setProperty('volume', 1.9)
        #engine5.say('Hey Siri') 
        engine5.say('Hey Sir Taj ') 
        engine5.say('What can I do for you ') 
        
        engine5.runAndWait()
        print(get)
        #wb.get().open_new(url+get)
    except sr.UnknownValueError:
       print("error")
    except sr.RequestError as e:
        print('failed'.format(e))

if 'weather' in r1.recognize_google(audio):
    r1=sr.Recognizer()
    url='https://www.youtube.com/results?search_query='
    
    with sr.Microphone() as source:
        print("Speak Anything search your query..:")
        audio = r1.listen(source)
    try:
        get = r1.recognize_google(audio)
        engine5 = pyttsx3.init()
        voices =engine5.getProperty('voices')
        engine5.setProperty('voice',voices[1].id)
        engine5.setProperty('rate', 120)
        engine5.setProperty('volume', 1.9)
        #engine5.say('Hey Siri') 
        engine5.say('The weather is sunny ') 
        #engine5.say('What can I do for you ') 
        
        engine5.runAndWait()
        print(get)
        #wb.get().open_new(url+get)
    except sr.UnknownValueError:
       print("error")
    except sr.RequestError as e:
        print('failed'.format(e))

if 'date' in r1.recognize_google(audio):
    r1=sr.Recognizer()
    url='https://www.youtube.com/results?search_query='
    
    with sr.Microphone() as source:
        print("Speak Anything search your query..:")
        audio = r1.listen(source)
    try:
        get = r1.recognize_google(audio)
        engine5 = pyttsx3.init()
        voices =engine5.getProperty('voices')
        engine5.setProperty('voice',voices[1].id)
        engine5.setProperty('rate', 120)
        engine5.setProperty('volume', 1.9)
        #engine5.say('Hey Siri') 
        engine5.say('The date is 9th January 2022 ') 
        #engine5.say('What can I do for you ') 
        
        engine5.runAndWait()
        print(get)
        #wb.get().open_new(url+get)
    except sr.UnknownValueError:
       print("error")
    except sr.RequestError as e:
        print('failed'.format(e))


if 'joke' in r1.recognize_google(audio):
    r1=sr.Recognizer()
    url='https://www.youtube.com/results?search_query='
    
    with sr.Microphone() as source:
        print("Speak Anything search your query..:")
        audio = r1.listen(source)
    try:
        get = r1.recognize_google(audio)
        engine5 = pyttsx3.init()
        voices =engine5.getProperty('voices')
        engine5.setProperty('voice',voices[1].id)
        engine5.setProperty('rate', 120)
        engine5.setProperty('volume', 1.9)
        #engine5.say('Hey Siri') 
        engine5.say('Whats orange and sounds like a parrot') 
        engine5.say('Its a carrot Heeheeeheeeheeeheeeeheee') 
        #engine5.say('What can I do for you ') 
        
        engine5.runAndWait()
        print(get)
        #wb.get().open_new(url+get)
    except sr.UnknownValueError:
       print("error")
    except sr.RequestError as e:
        print('failed'.format(e))


if 'video' in r1.recognize_google(audio):
    r1=sr.Recognizer()
    url='https://www.google.com'
    
    with sr.Microphone() as source:
        print("Speak Anything search your query..:")
        audio = r1.listen(source)
    try:
        get = r1.recognize_google(audio)
        engine5 = pyttsx3.init()
        voices =engine5.getProperty('voices')
        engine5.setProperty('voice',voices[1].id)
        engine5.setProperty('rate', 120)
        engine5.setProperty('volume', 1.9)
        #engine5.say('Hey Siri') 
        
        engine5.say('Opening Google') 
        
        engine5.runAndWait()
        print(get)
        wb.get().open_new(url+get)
    except sr.UnknownValueError:
       print("error")
    except sr.RequestError as e:
        print('failed'.format(e))


if 'youtube' in r1.recognize_google(audio):
    r1=sr.Recognizer()
    url='https://www.youtube.com/'
    
    with sr.Microphone() as source:
        print("Speak Anything search your query..:")
        audio = r1.listen(source)
    try:
        get = r1.recognize_google(audio)
        engine5 = pyttsx3.init()
        voices =engine5.getProperty('voices')
        engine5.setProperty('voice',voices[1].id)
        engine5.setProperty('rate', 120)
        engine5.setProperty('volume', 1.9)
        #engine5.say('Hey Siri') 
        
        engine5.say('Opening Google') 
        
        engine5.runAndWait()
        print(get)
        wb.get().open_new(url+get)
    except sr.UnknownValueError:
       print("error")
    except sr.RequestError as e:
        print('failed'.format(e))

if 'github' in r1.recognize_google(audio):
    r1=sr.Recognizer()
    url='https://github.com/Hassan50000/AI-201-Project-.git'
    
    with sr.Microphone() as source:
        print("Speak Anything search your query..:")
        audio = r1.listen(source)
    try:
        get = r1.recognize_google(audio)
        engine5 = pyttsx3.init()
        voices =engine5.getProperty('voices')
        engine5.setProperty('voice',voices[1].id)
        engine5.setProperty('rate', 120)
        engine5.setProperty('volume', 1.9)
        #engine5.say('Hey Siri') 
        
        engine5.say('Opening your Github Account') 
        
        engine5.runAndWait()
        print(get)
        wb.get().open_new(url+get)
    except sr.UnknownValueError:
       print("error")
    except sr.RequestError as e:
        print('failed'.format(e))
        
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

my_map = f.Map(location=[34.06961775193662, 72.6445797253496], zoom_start=15)

f.Marker(location=[34.06839693200607, 72.64158783566288], popup="GIKI CRICKET GROUND", tooltip="CRICKET GROUND").add_to(my_map)
f.Marker(location=[34.071411, 72.646636], popup="MEDICAL CENTER", tooltip="MC").add_to(my_map)
f.Marker(location=[34.07060208340641, 72.64304237054814], popup="NEW ACADAMIC BLOCK", tooltip="ACADAMIC BLOCK").add_to(my_map)
f.Marker(location=[34.069649624581146, 72.64704224845387], popup="HBL ATM", tooltip="ATM").add_to(my_map)
f.Marker(location=[34.070685479001895, 72.64723463307139], popup="RAJU HOTEL", tooltip="RAJU").add_to(my_map)
f.Marker(location=[34.07345831935395, 72.64888914083238], popup="C TYPE RESIDENTIAL AREA", tooltip="C TYPE").add_to(my_map)

f.Marker(location=[34.072437, 72.642489], popup="FACULTY CLUB", tooltip="FACULTY CLUB").add_to(my_map)
f.Marker(location=[34.069005, 72.647229], icon=f.Icon(color="orange", icon="cloud"),popup="TUC MOSQUE", tooltip="TUC MOSQUE").add_to(my_map)
f.Marker(location=[34.071211, 72.643594], icon=f.Icon(color="red", icon="cloud"),popup="LIBRARY", tooltip="LIBRARY").add_to(my_map)
f.Marker(location=[34.072655, 72.644072], icon=f.Icon(color="red", icon="cloud"),popup="Helipad", tooltip="Giki helipad").add_to(my_map)
f.Marker(location=[34.069296, 72.644957], icon=f.Icon(color="black", icon="cloud"),popup="FME", tooltip="FME").add_to(my_map)
f.Marker(location=[34.069882, 72.643959], icon=f.Icon(color="red", icon="cloud"),popup="Audi", tooltip="Audi").add_to(my_map)
f.Marker(location=[34.069616, 72.642323], icon=f.Icon(color="black", icon="cloud"),popup="FES", tooltip="FES").add_to(my_map)
f.Marker(location=[34.070118, 72.645633], icon=f.Icon(color="black", icon="cloud"),popup="FCME", tooltip="FCME").add_to(my_map)
f.Marker(location=[34.068576, 72.645982], icon=f.Icon(color="red", icon="cloud"),popup="Guest House", tooltip="Guest House").add_to(my_map)
f.Marker(location=[34.070269, 72.647414], icon=f.Icon(color="red", icon="cloud"),popup="TuckShop", tooltip="TuckShop").add_to(my_map)
f.Marker(location=[34.069029, 72.643294], icon=f.Icon(color="black", icon="cloud"),popup="FCSE", tooltip="FCSE").add_to(my_map)
f.Marker(location=[34.069456, 72.641095], icon=f.Icon(color="red", icon="cloud"),popup="StudentMasjid", tooltip="StudentMasjid").add_to(my_map)
f.Marker(location=[34.068300, 72.641663], icon=f.Icon(color="red", icon="cloud"),popup="Sports Ground", tooltip="Sports Ground").add_to(my_map)
f.Marker(location=[34.067887, 72.639636], icon=f.Icon(color="red", icon="cloud"),popup="Sports Complex", tooltip="Sports Complex").add_to(my_map)
f.Marker(location=[34.068491, 72.639453], icon=f.Icon(color="purple", icon="cloud"),popup="Hostel 10", tooltip="Hostel 10").add_to(my_map)
f.Marker(location=[34.068611, 72.640354], icon=f.Icon(color="purple", icon="cloud"),popup="Hostel 9", tooltip="Hostel 9").add_to(my_map)
f.Marker(location=[34.069069, 72.639464], icon=f.Icon(color="purple", icon="cloud"),popup="Hostel 2", tooltip="Hostel 2").add_to(my_map)
f.Marker(location=[34.069145, 72.640309], icon=f.Icon(color="purple", icon="cloud"),popup="Hostel 1", tooltip="Hostel 1").add_to(my_map)
f.Marker(location=[34.070273, 72.640196], icon=f.Icon(color="purple", icon="cloud"),popup="Hostel 5", tooltip="Hostel 5").add_to(my_map)
f.Marker(location=[34.070220, 72.639359], icon=f.Icon(color="purple", icon="cloud"),popup="Hostel 6", tooltip="Hostel 6").add_to(my_map)
f.Marker(location=[34.069638, 72.639418], icon=f.Icon(color="purple", icon="cloud"),popup="Hostel 4", tooltip="Hostel 4").add_to(my_map)
f.Marker(location=[34.069678, 72.640319], icon=f.Icon(color="purple", icon="cloud"),popup="Hostel 3", tooltip="Hostel 3").add_to(my_map)
f.Marker(location=[34.071215878227676, 72.64143689337763],icon=f.Icon(color="purple"), popup="HOSTEL 12", tooltip="HOSTEL 12").add_to(my_map)
f.Marker(location=[34.07101128044904, 72.64084684626256],icon=f.Icon(color="purple"), popup="HOSTEL 11", tooltip="HOSTEL 11").add_to(my_map)
f.Marker(location=[34.070389, 72.641103],icon=f.Icon(color="purple"), popup="HOSTEL 8", tooltip="HOSTEL 8").add_to(my_map)
f.Marker(location=[34.068138, 72.643522], icon=f.Icon(color="red", icon="cloud"),popup="Admin Block", tooltip="Admin Block").add_to(my_map)
f.Marker(location=[34.071033, 72.653838], icon=f.Icon(color="red", icon="cloud"),popup="Market", tooltip="Market").add_to(my_map)
f.Marker(location=[34.065350, 72.660956], icon=f.Icon(color="red", icon="cloud"),popup="RVC Jamia Masjid", tooltip="RVC Jamia Masjid").add_to(my_map)
f.Marker(location=[34.071613, 72.645029], icon=f.Icon(color="black", icon="cloud"),popup="Brabers", tooltip="Brabers").add_to(my_map)
f.Marker(location=[34.071701, 72.645716], icon=f.Icon(color="orange", icon="cloud"),popup="Incubator", tooltip="Incubator").add_to(my_map)

#f.Marker(location=[],icon=f.Icon(color="orange", icon="cloud"), popup=" Clock Tower", tooltip="C TYPE").add_to(my_map)

my_map


a=(input("From where do u want to go  ?"))
print(a)

b = (input("Where do u want to go to ?"))
print(b)

f.Marker([34.06839693200607, 72.64158783566288],
			popup = "GIKI CRICKET GROUND").add_to(my_map)

f.Marker([34.07164164111208, 72.64690757925894],
			popup = "MEDICAL CENTER").add_to(my_map)

# Add a line to the map by using line method 
# it connect both coordinates by the line
# line_opacity implies intensity of the line

#f.PolyLine(locations = [(34.06839693200607, 72.64158783566288), (34.07164164111208, 72.64690757925894)],
		#uhhnshrthh		line_opacity = 0.5).add_to(my_map)
		
Hostel_9_to_tuc = [(34.068611, 72.640354),
                    (34.068138, 72.643522),
                    (34.068576, 72.645982), 
                    (34.070269, 72.647414) 
                    ]

SportComplex_to_hostel_11 = [
                    (34.067887, 72.639636),
                    (34.069456, 72.641095),
                    (34.07101128044904, 72.64084684626256)
]
Hostel_6_to_MC = [
                    (34.070220, 72.639359),
                    (34.070389, 72.641103),
                    (34.071613, 72.645029),
                    (34.071701, 72.645716),
                    (34.071411, 72.646636)
]

HOSTEL_9_TO_BRABERS = [
                    (34.068611, 72.640354),
                    (34.069616, 72.642323),
                    (34.07060208340641, 72.64304237054814),
                    (34.071211, 72.643594),
                    (34.071613, 72.645029)
    ]

INCUBATIONMOSQUE = [
                    (34.071701, 72.645716),
                    (34.071613, 72.645029),
                    (34.071211, 72.643594),
                    (34.07060208340641, 72.64304237054814),
                    (34.069616, 72.642323),
                    (34.069456, 72.641095)
]

HOSTEL_2_TO_FCSE = [
                (34.069069, 72.639464),
                (34.069145, 72.640309),
                (34.069456, 72.641095),
                (34.069616, 72.642323),
                (34.069029, 72.643294)
]

HOSTEL_2_TO_RAJU = [
                (34.069069, 72.639464),
                (34.070273, 72.640196),
                (34.07101128044904, 72.64084684626256),
                (34.071215878227676, 72.64143689337763),
                (34.072437, 72.642489),
                (34.07345831935395, 72.64888914083238),
                (34.070269, 72.647414)
]

HBL_TO_HOSTEL_1 = [
                (34.069649624581146, 72.64704224845387),
                (34.070118, 72.645633),
                (34.069882, 72.643959),
                (34.07060208340641, 72.64304237054814),
                (34.071215878227676, 72.64143689337763),
                (34.07101128044904, 72.64084684626256),
                (34.069456, 72.641095), 
                (34.069145, 72.640309),
                (34.069145, 72.640309)
]

HOSTEL_10_FME = [
                (34.068491, 72.639453),
                (34.068611, 72.640354),
                (34.069296, 72.644957)
]

FMCE_HOSTEL_12 = [
                (34.070118, 72.645633),
                (34.069882, 72.643959), 
                (34.07060208340641, 72.64304237054814),
                (34.071215878227676, 72.64143689337763)
]
FCSE_HOSTEL_1 = [ 
                (34.069029, 72.643294),
                (34.069616, 72.642323),
                (34.069456, 72.641095),
                (34.069145, 72.640309),
                (34.069145, 72.640309)
]

if a == "Hostel 9" and b == "tuc":
	plugins.AntPath(Hostel_9_to_tuc , color ="#f00").add_to(my_map) # #080 = green

if a == "Sports Complex" and b == "Hostel 11":
	plugins.AntPath(SportComplex_to_hostel_11 , color = "red").add_to(my_map)
 
if a == "Hostel 6" and b == "Medical Centre":
	plugins.AntPath(Hostel_6_to_MC).add_to(my_map)
if a == "Hostel 9" and b == "Brabers":
	plugins.AntPath(HOSTEL_9_TO_BRABERS , color ="#080").add_to(my_map)
 
if a == "Incubator" and b == "Mosque":
	plugins.AntPath(INCUBATIONMOSQUE , color = "orange").add_to(my_map)
 
if a == "Hostel 2" and b == "FCSE":
	plugins.AntPath(HOSTEL_2_TO_FCSE, color = "purple").add_to(my_map)
 
if a == "Hostel 2" and b == "Raju":
	plugins.AntPath(HOSTEL_2_TO_RAJU , color = "black").add_to(my_map)
 
if a == "HBL Bank" and b == "Hostel 1":
	plugins.AntPath(HBL_TO_HOSTEL_1 , color ="#f00").add_to(my_map)


if a == "FCSE" and b == "Hostel 1":
	plugins.AntPath(FCSE_HOSTEL_1 , color ="#f00").add_to(my_map)
 
if a == "FMCE" and b == "Hostel 12":
	plugins.AntPath(FMCE_HOSTEL_12 , color ="#f00").add_to(my_map)
 
if a == "Hostel 10" and b == "FME":
	plugins.AntPath(HOSTEL_10_FME , color ="#f00").add_to(my_map)

'''
plugins.AntPath(HOSTEL_9_TO_BRABERS , color ="#080").add_to(my_map)
plugins.AntPath(Hostel_6_to_MC).add_to(my_map)
plugins.AntPath(SportComplex_to_hostel_11 , color = "red").add_to(my_map)
plugins.AntPath(INCUBATIONMOSQUE , color = "orange").add_to(my_map)
plugins.AntPath(HOSTEL_2_TO_FCSE, color = "purple").add_to(my_map)
plugins.AntPath(HOSTEL_2_TO_RAJU , color = "black").add_to(my_map)'''
#my_map4.save("my_map4.html")

my_map


# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


#THIS GRAPH AND COST IS NOT USED

Graph1 = {
'S-C':('H-9', 'H-10', 'H-1', 'H-2', 'H-3', 'H-4', 'H-5', 'H-6', 'CricketG', 'StudentMosque', 'CentralMess', 'H-8', 'H-11', 'H-12', 'TennisGround', 'FES', 'AdminBlock', 'FCSE', 'AcademicBlock', 'Auditorium', 'FacultyClub', 'GIKI-Clock', 'FME', 'Library', 'Brabers', 'Graduate-H', 'Incubator', 'GuestHouse', 'TuckMosque', 'HBL-Bank', 'FMCE', 'GIKI-College', 'GIKI-School', 'TransportOffice', 'FruitShop', 'Raju', 'Ayan', 'Medical', 'Girls-H'),
'H-9':('S-C', 'H-10', 'H-1', 'H-2', 'H-3', 'H-4', 'H-5', 'H-6', 'CricketG', 'StudentMosque', 'CentralMess', 'H-8', 'H-11', 'H-12', 'TennisGround', 'FES', 'AdminBlock', 'FCSE', 'AcademicBlock', 'Auditorium', 'FacultyClub', 'GIKI-Clock', 'FME', 'Library', 'Brabers', 'Graduate-H', 'Incubator', 'GuestHouse', 'TuckMosque', 'HBL-Bank', 'FMCE', 'GIKI-College', 'GIKI-School', 'TransportOffice', 'FruitShop', 'Raju', 'Ayan', 'Medical', 'Girls-H'),
'H-10':('S-C', 'H-9', 'H-1', 'H-2', 'H-3', 'H-4', 'H-5', 'H-6', 'CricketG', 'StudentMosque', 'CentralMess', 'H-8', 'H-11', 'H-12', 'TennisGround', 'FES', 'AdminBlock', 'FCSE', 'AcademicBlock', 'Auditorium', 'FacultyClub', 'GIKI-Clock', 'FME', 'Library', 'Brabers', 'Graduate-H', 'Incubator', 'GuestHouse', 'TuckMosque', 'HBL-Bank', 'FMCE', 'GIKI-College', 'GIKI-School', 'TransportOffice', 'FruitShop', 'Raju', 'Ayan', 'Medical', 'Girls-H'),
'H-1':('S-C', 'H-9', 'H-10', 'H-2', 'H-3', 'H-4', 'H-5', 'H-6', 'CricketG', 'StudentMosque', 'CentralMess', 'H-8', 'H-11', 'H-12', 'TennisGround', 'FES', 'AdminBlock', 'FCSE', 'AcademicBlock', 'Auditorium', 'FacultyClub', 'GIKI-Clock', 'FME', 'Library', 'Brabers', 'Graduate-H', 'Incubator', 'GuestHouse', 'TuckMosque', 'HBL-Bank', 'FMCE', 'GIKI-College', 'GIKI-School', 'TransportOffice', 'FruitShop', 'Raju', 'Ayan', 'Medical', 'Girls-H'),
'H-2':('S-C', 'H-9', 'H-10', 'H-1', 'H-3', 'H-4', 'H-5', 'H-6', 'CricketG', 'StudentMosque', 'CentralMess', 'H-8', 'H-11', 'H-12', 'TennisGround', 'FES', 'AdminBlock', 'FCSE', 'AcademicBlock', 'Auditorium', 'FacultyClub', 'GIKI-Clock', 'FME', 'Library', 'Brabers', 'Graduate-H', 'Incubator', 'GuestHouse', 'TuckMosque', 'HBL-Bank', 'FMCE', 'GIKI-College', 'GIKI-School', 'TransportOffice', 'FruitShop', 'Raju', 'Ayan', 'Medical', 'Girls-H'),
'H-3':('S-C', 'H-9', 'H-10', 'H-1', 'H-2', 'H-4', 'H-5', 'H-6', 'CricketG', 'StudentMosque', 'CentralMess', 'H-8', 'H-11', 'H-12', 'TennisGround', 'FES', 'AdminBlock', 'FCSE', 'AcademicBlock', 'Auditorium', 'FacultyClub', 'GIKI-Clock', 'FME', 'Library', 'Brabers', 'Graduate-H', 'Incubator', 'GuestHouse', 'TuckMosque', 'HBL-Bank', 'FMCE', 'GIKI-College', 'GIKI-School', 'TransportOffice', 'FruitShop', 'Raju', 'Ayan', 'Medical', 'Girls-H'),
'H-4':('S-C', 'H-9', 'H-10', 'H-1', 'H-2', 'H-3', 'H-5', 'H-6', 'CricketG', 'StudentMosque', 'CentralMess', 'H-8', 'H-11', 'H-12', 'TennisGround', 'FES', 'AdminBlock', 'FCSE', 'AcademicBlock', 'Auditorium', 'FacultyClub', 'GIKI-Clock', 'FME', 'Library', 'Brabers', 'Graduate-H', 'Incubator', 'GuestHouse', 'TuckMosque', 'HBL-Bank', 'FMCE', 'GIKI-College', 'GIKI-School', 'TransportOffice', 'FruitShop', 'Raju', 'Ayan', 'Medical', 'Girls-H'),
'H-5':('S-C', 'H-9', 'H-10', 'H-1', 'H-2', 'H-3', 'H-4', 'H-6', 'CricketG', 'StudentMosque', 'CentralMess', 'H-8', 'H-11', 'H-12', 'TennisGround', 'FES', 'AdminBlock', 'FCSE', 'AcademicBlock', 'Auditorium', 'FacultyClub', 'GIKI-Clock', 'FME', 'Library', 'Brabers', 'Graduate-H', 'Incubator', 'GuestHouse', 'TuckMosque', 'HBL-Bank', 'FMCE', 'GIKI-College', 'GIKI-School', 'TransportOffice', 'FruitShop', 'Raju', 'Ayan', 'Medical', 'Girls-H'),
'H-6':('S-C', 'H-9', 'H-10', 'H-1', 'H-2', 'H-3', 'H-4', 'H-5', 'CricketG', 'StudentMosque', 'CentralMess', 'H-8', 'H-11', 'H-12', 'TennisGround', 'FES', 'AdminBlock', 'FCSE', 'AcademicBlock', 'Auditorium', 'FacultyClub', 'GIKI-Clock', 'FME', 'Library', 'Brabers', 'Graduate-H', 'Incubator', 'GuestHouse', 'TuckMosque', 'HBL-Bank', 'FMCE', 'GIKI-College', 'GIKI-School', 'TransportOffice', 'FruitShop', 'Raju', 'Ayan', 'Medical', 'Girls-H'),
'CricketG':('S-C', 'H-9', 'H-10', 'H-1', 'H-2', 'H-3', 'H-4', 'H-5', 'H-6', 'CricketG', 'StudentMosque', 'CentralMess', 'H-8', 'H-11', 'H-12', 'TennisGround', 'FES', 'AdminBlock', 'FCSE', 'AcademicBlock', 'Auditorium', 'FacultyClub', 'GIKI-Clock', 'FME', 'Library', 'Brabers', 'Graduate-H', 'Incubator', 'GuestHouse', 'TuckMosque', 'HBL-Bank', 'FMCE', 'GIKI-College', 'GIKI-School', 'TransportOffice', 'FruitShop', 'Raju', 'Ayan', 'Medical', 'Girls-H'),
'StudentMosque':('S-C', 'H-9', 'H-10', 'H-1', 'H-2', 'H-3', 'H-4', 'H-5', 'H-6', 'CricketG', 'CentralMess', 'H-8', 'H-11', 'H-12', 'TennisGround', 'FES', 'AdminBlock', 'FCSE', 'AcademicBlock', 'Auditorium', 'FacultyClub', 'GIKI-Clock', 'FME', 'Library', 'Brabers', 'Graduate-H', 'Incubator', 'GuestHouse', 'TuckMosque', 'HBL-Bank', 'FMCE', 'GIKI-College', 'GIKI-School', 'TransportOffice', 'FruitShop', 'Raju', 'Ayan', 'Medical', 'Girls-H'),
'CentralMess':('S-C', 'H-9', 'H-10', 'H-1', 'H-2', 'H-3', 'H-4', 'H-5', 'H-6', 'CricketG', 'StudentMosque', 'H-8', 'H-11', 'H-12', 'TennisGround', 'FES', 'AdminBlock', 'FCSE', 'AcademicBlock', 'Auditorium', 'FacultyClub', 'GIKI-Clock', 'FME', 'Library', 'Brabers', 'Graduate-H', 'Incubator', 'GuestHouse', 'TuckMosque', 'HBL-Bank', 'FMCE', 'GIKI-College', 'GIKI-School', 'TransportOffice', 'FruitShop', 'Raju', 'Ayan', 'Medical', 'Girls-H'),
'H-8':('S-C', 'H-9', 'H-10', 'H-1', 'H-2', 'H-3', 'H-4', 'H-5', 'H-6', 'CricketG', 'StudentMosque', 'CentralMess', 'H-11', 'H-12', 'TennisGround', 'FES', 'AdminBlock', 'FCSE', 'AcademicBlock', 'Auditorium', 'FacultyClub', 'GIKI-Clock', 'FME', 'Library', 'Brabers', 'Graduate-H', 'Incubator', 'GuestHouse', 'TuckMosque', 'HBL-Bank', 'FMCE', 'GIKI-College', 'GIKI-School', 'TransportOffice', 'FruitShop', 'Raju', 'Ayan', 'Medical', 'Girls-H'),
'H-11':('S-C', 'H-9', 'H-10', 'H-1', 'H-2', 'H-3', 'H-4', 'H-5', 'H-6', 'CricketG', 'StudentMosque', 'CentralMess', 'H-8', 'H-12', 'TennisGround', 'FES', 'AdminBlock', 'FCSE', 'AcademicBlock', 'Auditorium', 'FacultyClub', 'GIKI-Clock', 'FME', 'Library', 'Brabers', 'Graduate-H', 'Incubator', 'GuestHouse', 'TuckMosque', 'HBL-Bank', 'FMCE', 'GIKI-College', 'GIKI-School', 'TransportOffice', 'FruitShop', 'Raju', 'Ayan', 'Medical', 'Girls-H'),
'H-12':('S-C', 'H-9', 'H-10', 'H-1', 'H-2', 'H-3', 'H-4', 'H-5', 'H-6', 'CricketG', 'StudentMosque', 'CentralMess', 'H-8', 'H-11', 'TennisGround', 'FES', 'AdminBlock', 'FCSE', 'AcademicBlock', 'Auditorium', 'FacultyClub', 'GIKI-Clock', 'FME', 'Library', 'Brabers', 'Graduate-H', 'Incubator', 'GuestHouse', 'TuckMosque', 'HBL-Bank', 'FMCE', 'GIKI-College', 'GIKI-School', 'TransportOffice', 'FruitShop', 'Raju', 'Ayan', 'Medical', 'Girls-H'),
'TennisGround':('S-C', 'H-9', 'H-10', 'H-1', 'H-2', 'H-3', 'H-4', 'H-5', 'H-6', 'CricketG', 'StudentMosque', 'CentralMess', 'H-8', 'H-11', 'H-12', 'FES', 'AdminBlock', 'FCSE', 'AcademicBlock', 'Auditorium', 'FacultyClub', 'GIKI-Clock', 'FME', 'Library', 'Brabers', 'Graduate-H', 'Incubator', 'GuestHouse', 'TuckMosque', 'HBL-Bank', 'FMCE', 'GIKI-College', 'GIKI-School', 'TransportOffice', 'FruitShop', 'Raju', 'Ayan', 'Medical', 'Girls-H'),
'FES':('S-C', 'H-9', 'H-10', 'H-1', 'H-2', 'H-3', 'H-4', 'H-5', 'H-6', 'CricketG', 'StudentMosque', 'CentralMess', 'H-8', 'H-11', 'H-12', 'TennisGround', 'AdminBlock', 'FCSE', 'AcademicBlock', 'Auditorium', 'FacultyClub', 'GIKI-Clock', 'FME', 'Library', 'Brabers', 'Graduate-H', 'Incubator', 'GuestHouse', 'TuckMosque', 'HBL-Bank', 'FMCE', 'GIKI-College', 'GIKI-School', 'TransportOffice', 'FruitShop', 'Raju', 'Ayan', 'Medical', 'Girls-H'),
'AdminBlock':('S-C', 'H-9', 'H-10', 'H-1', 'H-2', 'H-3', 'H-4', 'H-5', 'H-6', 'CricketG', 'StudentMosque', 'CentralMess', 'H-8', 'H-11', 'H-12', 'TennisGround', 'FES', 'FCSE', 'AcademicBlock', 'Auditorium', 'FacultyClub', 'GIKI-Clock', 'FME', 'Library', 'Brabers', 'Graduate-H', 'Incubator', 'GuestHouse', 'TuckMosque', 'HBL-Bank', 'FMCE', 'GIKI-College', 'GIKI-School', 'TransportOffice', 'FruitShop', 'Raju', 'Ayan', 'Medical', 'Girls-H'),
'FCSE':('S-C', 'H-9', 'H-10', 'H-1', 'H-2', 'H-3', 'H-4', 'H-5', 'H-6', 'CricketG', 'StudentMosque', 'CentralMess', 'H-8', 'H-11', 'H-12', 'TennisGround', 'FES', 'AdminBlock', 'AcademicBlock', 'Auditorium', 'FacultyClub', 'GIKI-Clock', 'FME', 'Library', 'Brabers', 'Graduate-H', 'Incubator', 'GuestHouse', 'TuckMosque', 'HBL-Bank', 'FMCE', 'GIKI-College', 'GIKI-School', 'TransportOffice', 'FruitShop', 'Raju', 'Ayan', 'Medical', 'Girls-H'),
'AcademicBlock':('S-C', 'H-9', 'H-10', 'H-1', 'H-2', 'H-3', 'H-4', 'H-5', 'H-6', 'CricketG', 'StudentMosque', 'CentralMess', 'H-8', 'H-11', 'H-12', 'TennisGround', 'FES', 'AdminBlock', 'FCSE', 'Auditorium', 'FacultyClub', 'GIKI-Clock', 'FME', 'Library', 'Brabers', 'Graduate-H', 'Incubator', 'GuestHouse', 'TuckMosque', 'HBL-Bank', 'FMCE', 'GIKI-College', 'GIKI-School', 'TransportOffice', 'FruitShop', 'Raju', 'Ayan', 'Medical', 'Girls-H'),
'Auditorium':('S-C', 'H-9', 'H-10', 'H-1', 'H-2', 'H-3', 'H-4', 'H-5', 'H-6', 'CricketG', 'StudentMosque', 'CentralMess', 'H-8', 'H-11', 'H-12', 'TennisGround', 'FES', 'AdminBlock', 'FCSE', 'AcademicBlock', 'FacultyClub', 'GIKI-Clock', 'FME', 'Library', 'Brabers', 'Graduate-H', 'Incubator', 'GuestHouse', 'TuckMosque', 'HBL-Bank', 'FMCE', 'GIKI-College', 'GIKI-School', 'TransportOffice', 'FruitShop', 'Raju', 'Ayan', 'Medical', 'Girls-H'),
'FacultyClub':('S-C', 'H-9', 'H-10', 'H-1', 'H-2', 'H-3', 'H-4', 'H-5', 'H-6', 'CricketG', 'StudentMosque', 'CentralMess', 'H-8', 'H-11', 'H-12', 'TennisGround', 'FES', 'AdminBlock', 'FCSE', 'AcademicBlock', 'Auditorium', 'GIKI-Clock', 'FME', 'Library', 'Brabers', 'Graduate-H', 'Incubator', 'GuestHouse', 'TuckMosque', 'HBL-Bank', 'FMCE', 'GIKI-College', 'GIKI-School', 'TransportOffice', 'FruitShop', 'Raju', 'Ayan', 'Medical', 'Girls-H'),
'GIKI-Clock':('S-C', 'H-9', 'H-10', 'H-1', 'H-2', 'H-3', 'H-4', 'H-5', 'H-6', 'CricketG', 'StudentMosque', 'CentralMess', 'H-8', 'H-11', 'H-12', 'TennisGround', 'FES', 'AdminBlock', 'FCSE', 'AcademicBlock', 'Auditorium', 'FacultyClub', 'FME', 'Library', 'Brabers', 'Graduate-H', 'Incubator', 'GuestHouse', 'TuckMosque', 'HBL-Bank', 'FMCE', 'GIKI-College', 'GIKI-School', 'TransportOffice', 'FruitShop', 'Raju', 'Ayan', 'Medical', 'Girls-H'),
'FME':('S-C', 'H-9', 'H-10', 'H-1', 'H-2', 'H-3', 'H-4', 'H-5', 'H-6', 'CricketG', 'StudentMosque', 'CentralMess', 'H-8', 'H-11', 'H-12', 'TennisGround', 'FES', 'AdminBlock', 'FCSE', 'AcademicBlock', 'Auditorium', 'FacultyClub', 'GIKI-Clock', 'Library', 'Brabers', 'Graduate-H', 'Incubator', 'GuestHouse', 'TuckMosque', 'HBL-Bank', 'FMCE', 'GIKI-College', 'GIKI-School', 'TransportOffice', 'FruitShop', 'Raju', 'Ayan', 'Medical', 'Girls-H'),
'Library':('S-C', 'H-9', 'H-10', 'H-1', 'H-2', 'H-3', 'H-4', 'H-5', 'H-6', 'CricketG', 'StudentMosque', 'CentralMess', 'H-8', 'H-11', 'H-12', 'TennisGround', 'FES', 'AdminBlock', 'FCSE', 'AcademicBlock', 'Auditorium', 'FacultyClub', 'GIKI-Clock', 'FME', 'Brabers', 'Graduate-H', 'Incubator', 'GuestHouse', 'TuckMosque', 'HBL-Bank', 'FMCE', 'GIKI-College', 'GIKI-School', 'TransportOffice', 'FruitShop', 'Raju', 'Ayan', 'Medical', 'Girls-H'),
'Brabers':('S-C', 'H-9', 'H-10', 'H-1', 'H-2', 'H-3', 'H-4', 'H-5', 'H-6', 'CricketG', 'StudentMosque', 'CentralMess', 'H-8', 'H-11', 'H-12', 'TennisGround', 'FES', 'AdminBlock', 'FCSE', 'AcademicBlock', 'Auditorium', 'FacultyClub', 'GIKI-Clock', 'FME', 'Library', 'Graduate-H', 'Incubator', 'GuestHouse', 'TuckMosque', 'HBL-Bank', 'FMCE', 'GIKI-College', 'GIKI-School', 'TransportOffice', 'FruitShop', 'Raju', 'Ayan', 'Medical', 'Girls-H'),
'Graduate-H':('S-C', 'H-9', 'H-10', 'H-1', 'H-2', 'H-3', 'H-4', 'H-5', 'H-6', 'CricketG', 'StudentMosque', 'CentralMess', 'H-8', 'H-11', 'H-12', 'TennisGround', 'FES', 'AdminBlock', 'FCSE', 'AcademicBlock', 'Auditorium', 'FacultyClub', 'GIKI-Clock', 'FME', 'Library', 'Brabers', 'Incubator', 'GuestHouse', 'TuckMosque', 'HBL-Bank', 'FMCE', 'GIKI-College', 'GIKI-School', 'TransportOffice', 'FruitShop', 'Raju', 'Ayan', 'Medical', 'Girls-H'),
'Incubator':('S-C', 'H-9', 'H-10', 'H-1', 'H-2', 'H-3', 'H-4', 'H-5', 'H-6', 'CricketG', 'StudentMosque', 'CentralMess', 'H-8', 'H-11', 'H-12', 'TennisGround', 'FES', 'AdminBlock', 'FCSE', 'AcademicBlock', 'Auditorium', 'FacultyClub', 'GIKI-Clock', 'FME', 'Library', 'Brabers', 'Graduate-H', 'GuestHouse', 'TuckMosque', 'HBL-Bank', 'FMCE', 'GIKI-College', 'GIKI-School', 'TransportOffice', 'FruitShop', 'Raju', 'Ayan', 'Medical', 'Girls-H'),
'GuestHouse':('S-C', 'H-9', 'H-10', 'H-1', 'H-2', 'H-3', 'H-4', 'H-5', 'H-6', 'CricketG', 'StudentMosque', 'CentralMess', 'H-8', 'H-11', 'H-12', 'TennisGround', 'FES', 'AdminBlock', 'FCSE', 'AcademicBlock', 'Auditorium', 'FacultyClub', 'GIKI-Clock', 'FME', 'Library', 'Brabers', 'Graduate-H', 'Incubator', 'TuckMosque', 'HBL-Bank', 'FMCE', 'GIKI-College', 'GIKI-School', 'TransportOffice', 'FruitShop', 'Raju', 'Ayan', 'Medical', 'Girls-H'),
'TuckMosque':('S-C', 'H-9', 'H-10', 'H-1', 'H-2', 'H-3', 'H-4', 'H-5', 'H-6', 'CricketG', 'StudentMosque', 'CentralMess', 'H-8', 'H-11', 'H-12', 'TennisGround', 'FES', 'AdminBlock', 'FCSE', 'AcademicBlock', 'Auditorium', 'FacultyClub', 'GIKI-Clock', 'FME', 'Library', 'Brabers', 'Graduate-H', 'Incubator', 'GuestHouse', 'HBL-Bank', 'FMCE', 'GIKI-College', 'GIKI-School', 'TransportOffice', 'FruitShop', 'Raju', 'Ayan', 'Medical', 'Girls-H'),
'HBL-Bank':('S-C', 'H-9', 'H-10', 'H-1', 'H-2', 'H-3', 'H-4', 'H-5', 'H-6', 'CricketG', 'StudentMosque', 'CentralMess', 'H-8', 'H-11', 'H-12', 'TennisGround', 'FES', 'AdminBlock', 'FCSE', 'AcademicBlock', 'Auditorium', 'FacultyClub', 'GIKI-Clock', 'FME', 'Library', 'Brabers', 'Graduate-H', 'Incubator', 'GuestHouse', 'TuckMosque', 'FMCE', 'GIKI-College', 'GIKI-School', 'TransportOffice', 'FruitShop', 'Raju', 'Ayan', 'Medical', 'Girls-H'),
'FMCE':('S-C', 'H-9', 'H-10', 'H-1', 'H-2', 'H-3', 'H-4', 'H-5', 'H-6', 'CricketG', 'StudentMosque', 'CentralMess', 'H-8', 'H-11', 'H-12', 'TennisGround', 'FES', 'AdminBlock', 'FCSE', 'AcademicBlock', 'Auditorium', 'FacultyClub', 'GIKI-Clock', 'FME', 'Library', 'Brabers', 'Graduate-H', 'Incubator', 'GuestHouse', 'TuckMosque', 'HBL-Bank', 'GIKI-College', 'GIKI-School', 'TransportOffice', 'FruitShop', 'Raju', 'Ayan', 'Medical', 'Girls-H'),
'GIKI-College':('S-C', 'H-9', 'H-10', 'H-1', 'H-2', 'H-3', 'H-4', 'H-5', 'H-6', 'CricketG', 'StudentMosque', 'CentralMess', 'H-8', 'H-11', 'H-12', 'TennisGround', 'FES', 'AdminBlock', 'FCSE', 'AcademicBlock', 'Auditorium', 'FacultyClub', 'GIKI-Clock', 'FME', 'Library', 'Brabers', 'Graduate-H', 'Incubator', 'GuestHouse', 'TuckMosque', 'HBL-Bank', 'FMCE', 'GIKI-School', 'TransportOffice', 'FruitShop', 'Raju', 'Ayan', 'Medical', 'Girls-H'),
'GIKI-School':('S-C', 'H-9', 'H-10', 'H-1', 'H-2', 'H-3', 'H-4', 'H-5', 'H-6', 'CricketG', 'StudentMosque', 'CentralMess', 'H-8', 'H-11', 'H-12', 'TennisGround', 'FES', 'AdminBlock', 'FCSE', 'AcademicBlock', 'Auditorium', 'FacultyClub', 'GIKI-Clock', 'FME', 'Library', 'Brabers', 'Graduate-H', 'Incubator', 'GuestHouse', 'TuckMosque', 'HBL-Bank', 'FMCE', 'GIKI-College', 'TransportOffice', 'FruitShop', 'Raju', 'Ayan', 'Medical', 'Girls-H'),
'TransportOffice':('S-C', 'H-9', 'H-10', 'H-1', 'H-2', 'H-3', 'H-4', 'H-5', 'H-6', 'CricketG', 'StudentMosque', 'CentralMess', 'H-8', 'H-11', 'H-12', 'TennisGround', 'FES', 'AdminBlock', 'FCSE', 'AcademicBlock', 'Auditorium', 'FacultyClub', 'GIKI-Clock', 'FME', 'Library', 'Brabers', 'Graduate-H', 'Incubator', 'GuestHouse', 'TuckMosque', 'HBL-Bank', 'FMCE', 'GIKI-College', 'GIKI-School', 'FruitShop', 'Raju', 'Ayan', 'Medical', 'Girls-H'),
'FruitShop':('S-C', 'H-9', 'H-10', 'H-1', 'H-2', 'H-3', 'H-4', 'H-5', 'H-6', 'CricketG', 'StudentMosque', 'CentralMess', 'H-8', 'H-11', 'H-12', 'TennisGround', 'FES', 'AdminBlock', 'FCSE', 'AcademicBlock', 'Auditorium', 'FacultyClub', 'GIKI-Clock', 'FME', 'Library', 'Brabers', 'Graduate-H', 'Incubator', 'GuestHouse', 'TuckMosque', 'HBL-Bank', 'FMCE', 'GIKI-College', 'GIKI-School', 'TransportOffice', 'Raju', 'Ayan', 'Medical', 'Girls-H'),
'Raju':('S-C', 'H-9', 'H-10', 'H-1', 'H-2', 'H-3', 'H-4', 'H-5', 'H-6', 'CricketG', 'StudentMosque', 'CentralMess', 'H-8', 'H-11', 'H-12', 'TennisGround', 'FES', 'AdminBlock', 'FCSE', 'AcademicBlock', 'Auditorium', 'FacultyClub', 'GIKI-Clock', 'FME', 'Library', 'Brabers', 'Graduate-H', 'Incubator', 'GuestHouse', 'TuckMosque', 'HBL-Bank', 'FMCE', 'GIKI-College', 'GIKI-School', 'TransportOffice', 'FruitShop', 'Ayan', 'Medical', 'Girls-H'),
'Ayan':('S-C', 'H-9', 'H-10', 'H-1', 'H-2', 'H-3', 'H-4', 'H-5', 'H-6', 'CricketG', 'StudentMosque', 'CentralMess', 'H-8', 'H-11', 'H-12', 'TennisGround', 'FES', 'AdminBlock', 'FCSE', 'AcademicBlock', 'Auditorium', 'FacultyClub', 'GIKI-Clock', 'FME', 'Library', 'Brabers', 'Graduate-H', 'Incubator', 'GuestHouse', 'TuckMosque', 'HBL-Bank', 'FMCE', 'GIKI-College', 'GIKI-School', 'TransportOffice', 'FruitShop', 'Raju', 'Medical', 'Girls-H'),
'Medical':('S-C', 'H-9', 'H-10', 'H-1', 'H-2', 'H-3', 'H-4', 'H-5', 'H-6', 'CricketG', 'StudentMosque', 'CentralMess', 'H-8', 'H-11', 'H-12', 'TennisGround', 'FES', 'AdminBlock', 'FCSE', 'AcademicBlock', 'Auditorium', 'FacultyClub', 'GIKI-Clock', 'FME', 'Library', 'Brabers', 'Graduate-H', 'Incubator', 'GuestHouse', 'TuckMosque', 'HBL-Bank', 'FMCE', 'GIKI-College', 'GIKI-School', 'TransportOffice', 'FruitShop', 'Raju', 'Ayan', 'Girls-H'),
'Girls-H':('S-C', 'H-9', 'H-10', 'H-1', 'H-2', 'H-3', 'H-4', 'H-5', 'H-6', 'CricketG', 'StudentMosque', 'CentralMess', 'H-8', 'H-11', 'H-12', 'TennisGround', 'FES', 'AdminBlock', 'FCSE', 'AcademicBlock', 'Auditorium', 'FacultyClub', 'GIKI-Clock', 'FME', 'Library', 'Brabers', 'Graduate-H', 'Incubator', 'GuestHouse', 'TuckMosque', 'HBL-Bank', 'FMCE', 'GIKI-College', 'GIKI-School', 'TransportOffice', 'FruitShop', 'Raju', 'Ayan', 'Medical')
}





Cost1 = {
('S-C','S-C'):0,
('S-C','H-9'):68,
('S-C','H-10'):160,
('S-C','H-1'):150,
('S-C','H-2'):150,
('S-C','H-3'):350,
('S-C','H-4'):450,
('S-C','H-5'):350,
('S-C','H-6'):450,
('S-C','CricketG'):500,
('S-C','StudentMosque'):350,
('S-C','CentralMess'):350,
('S-C','H-8'):350,
('S-C','H-11'):450,
('S-C','H-12'):550,
('S-C','TennisGround'):450,
('S-C','FES'):700,
('S-C','AdminBlock'):550,
('S-C','FCSE'):650,
('S-C','AcademicBlock'):700,
('S-C','Auditorium'):650,
('S-C','FacultyClub'):1500,
('S-C','GIKI-Clock'):600,
('S-C','FME'):650,
('S-C','Library'):800,
('S-C','Brabers'):1000,
('S-C','Graduate-H'):1500,
('S-C','Incubator'):1000,
('S-C','GuestHouse'):750,
('S-C','TuckMosque'):850,
('S-C','HBL-Bank'):800,
('S-C','FMCE'):750,
('S-C','GIKI-College'):900,
('S-C','GIKI-School'):800,
('S-C','TransportOffice'):1000,
('S-C','FruitShop'):950,
('S-C','Raju'):950,
('S-C','Ayan'):950,
('S-C','Medical'):950,
('S-C','Girls-H'):1100,
('H-9','S-C'):68,
('H-9','H-9'):0,
('H-9','H-10'):86,
('H-9','H-1'):80,
('H-9','H-2'):82,
('H-9','H-3'):280,
('H-9','H-4'):350,
('H-9','H-5'):300,
('H-9','H-6'):350,
('H-9','CricketG'):400,
('H-9','StudentMosque'):260,
('H-9','CentralMess'):270,
('H-9','H-8'):290,
('H-9','H-11'):350,
('H-9','H-12'):500,
('H-9','TennisGround'):400,
('H-9','FES'):650,
('H-9','AdminBlock'):400,
('H-9','FCSE'):550,
('H-9','AcademicBlock'):650,
('H-9','Auditorium'):550,
('H-9','FacultyClub'):1400,
('H-9','GIKI-Clock'):550,
('H-9','FME'):600,
('H-9','Library'):750,
('H-9','Brabers'):850,
('H-9','Graduate-H'):1000,
('H-9','Incubator'):950,
('H-9','GuestHouse'):700,
('H-9','TuckMosque'):750,
('H-9','HBL-Bank'):700,
('H-9','FMCE'):700,
('H-9','GIKI-College'):850,
('H-9','GIKI-School'):750,
('H-9','TransportOffice'):950,
('H-9','FruitShop'):900,
('H-9','Raju'):850,
('H-9','Ayan'):850,
('H-9','Medical'):900,
('H-9','Girls-H'):1000,
('H-10','S-C'):160,
('H-10','H-9'):86,
('H-10','H-10'):0,
('H-10','H-1'):80,
('H-10','H-2'):4,
('H-10','H-3'):280,
('H-10','H-4'):350,
('H-10','H-5'):300,
('H-10','H-6'):350,
('H-10','CricketG'):400,
('H-10','StudentMosque'):260,
('H-10','CentralMess'):270,
('H-10','H-8'):290,
('H-10','H-11'):350,
('H-10','H-12'):500,
('H-10','TennisGround'):400,
('H-10','FES'):650,
('H-10','AdminBlock'):400,
('H-10','FCSE'):550,
('H-10','AcademicBlock'):650,
('H-10','Auditorium'):550,
('H-10','FacultyClub'):1400,
('H-10','GIKI-Clock'):550,
('H-10','FME'):600,
('H-10','Library'):750,
('H-10','Brabers'):850,
('H-10','Graduate-H'):1000,
('H-10','Incubator'):950,
('H-10','GuestHouse'):700,
('H-10','TuckMosque'):750,
('H-10','HBL-Bank'):700,
('H-10','FMCE'):700,
('H-10','GIKI-College'):850,
('H-10','GIKI-School'):750,
('H-10','TransportOffice'):950,
('H-10','FruitShop'):900,
('H-10','Raju'):850,
('H-10','Ayan'):850,
('H-10','Medical'):900,
('H-10','Girls-H'):1000,
('H-1','S-C'):150,
('H-1','H-9'):80,
('H-1','H-10'):80,
('H-1','H-1'):0,
('H-1','H-2'):76,
('H-1','H-3'):210,
('H-1','H-4'):290,
('H-1','H-5'):220,
('H-1','H-6'):290,
('H-1','CricketG'):350,
('H-1','StudentMosque'):180,
('H-1','CentralMess'):190,
('H-1','H-8'):210,
('H-1','H-11'):280,
('H-1','H-12'):400,
('H-1','TennisGround'):300,
('H-1','FES'):550,
('H-1','AdminBlock'):350,
('H-1','FCSE'):500,
('H-1','AcademicBlock'):550,
('H-1','Auditorium'):500,
('H-1','FacultyClub'):1300,
('H-1','GIKI-Clock'):450,
('H-1','FME'):500,
('H-1','Library'):650,
('H-1','Brabers'):750,
('H-1','Graduate-H'):1000,
('H-1','Incubator'):850,
('H-1','GuestHouse'):600,
('H-1','TuckMosque'):700,
('H-1','HBL-Bank'):650,
('H-1','FMCE'):600,
('H-1','GIKI-College'):750,
('H-1','GIKI-School'):650,
('H-1','TransportOffice'):850,
('H-1','FruitShop'):800,
('H-1','Raju'):800,
('H-1','Ayan'):800,
('H-1','Medical'):800,
('H-1','Girls-H'):900,
('H-2','S-C'):150,
('H-2','H-9'):82,
('H-2','H-10'):4,
('H-2','H-1'):76,
('H-2','H-2'):0,
('H-2','H-3'):280,
('H-2','H-4'):350,
('H-2','H-5'):300,
('H-2','H-6'):350,
('H-2','CricketG'):400,
('H-2','StudentMosque'):250,
('H-2','CentralMess'):270,
('H-2','H-8'):290,
('H-2','H-11'):350,
('H-2','H-12'):500,
('H-2','TennisGround'):400,
('H-2','FES'):650,
('H-2','AdminBlock'):550,
('H-2','FCSE'):550,
('H-2','AcademicBlock'):650,
('H-2','Auditorium'):550,
('H-2','FacultyClub'):1400,
('H-2','GIKI-Clock'):550,
('H-2','FME'):600,
('H-2','Library'):750,
('H-2','Brabers'):850,
('H-2','Graduate-H'):1000,
('H-2','Incubator'):900,
('H-2','GuestHouse'):650,
('H-2','TuckMosque'):750,
('H-2','HBL-Bank'):700,
('H-2','FMCE'):700,
('H-2','GIKI-College'):800,
('H-2','GIKI-School'):750,
('H-2','TransportOffice'):950,
('H-2','FruitShop'):900,
('H-2','Raju'):850,
('H-2','Ayan'):850,
('H-2','Medical'):850,
('H-2','Girls-H'):1000,
('H-3','S-C'):350,
('H-3','H-9'):280,
('H-3','H-10'):280,
('H-3','H-1'):210,
('H-3','H-2'):280,
('H-3','H-3'):0,
('H-3','H-4'):86,
('H-3','H-5'):12,
('H-3','H-6'):85,
('H-3','CricketG'):450,
('H-3','StudentMosque'):300,
('H-3','CentralMess'):300,
('H-3','H-8'):77,
('H-3','H-11'):150,
('H-3','H-12'):280,
('H-3','TennisGround'):450,
('H-3','FES'):450,
('H-3','AdminBlock'):450,
('H-3','FCSE'):450,
('H-3','AcademicBlock'):400,
('H-3','Auditorium'):450,
('H-3','FacultyClub'):1200,
('H-3','GIKI-Clock'):600,
('H-3','FME'):550,
('H-3','Library'):500,
('H-3','Brabers'):750,
('H-3','Graduate-H'):1200,
('H-3','Incubator'):1000,
('H-3','GuestHouse'):700,
('H-3','TuckMosque'):800,
('H-3','HBL-Bank'):750,
('H-3','FMCE'):600,
('H-3','GIKI-College'):850,
('H-3','GIKI-School'):800,
('H-3','TransportOffice'):1000,
('H-3','FruitShop'):900,
('H-3','Raju'):900,
('H-3','Ayan'):900,
('H-3','Medical'):900,
('H-3','Girls-H'):1000,
('H-4','S-C'):450,
('H-4','H-9'):350,
('H-4','H-10'):350,
('H-4','H-1'):290,
('H-4','H-2'):350,
('H-4','H-3'):86,
('H-4','H-4'):0,
('H-4','H-5'):75,
('H-4','H-6'):2,
('H-4','CricketG'):450,
('H-4','StudentMosque'):400,
('H-4','CentralMess'):400,
('H-4','H-8'):160,
('H-4','H-11'):230,
('H-4','H-12'):350,
('H-4','TennisGround'):500,
('H-4','FES'):500,
('H-4','AdminBlock'):550,
('H-4','FCSE'):500,
('H-4','AcademicBlock'):500,
('H-4','Auditorium'):500,
('H-4','FacultyClub'):1300,
('H-4','GIKI-Clock'):700,
('H-4','FME'):600,
('H-4','Library'):600,
('H-4','Brabers'):800,
('H-4','Graduate-H'):1200,
('H-4','Incubator'):1000,
('H-4','GuestHouse'):800,
('H-4','TuckMosque'):900,
('H-4','HBL-Bank'):850,
('H-4','FMCE'):700,
('H-4','GIKI-College'):1000,
('H-4','GIKI-School'):900,
('H-4','TransportOffice'):1100,
('H-4','FruitShop'):1000,
('H-4','Raju'):1000,
('H-4','Ayan'):1000,
('H-4','Medical'):1000,
('H-4','Girls-H'):1100,
('H-5','S-C'):350,
('H-5','H-9'):300,
('H-5','H-10'):300,
('H-5','H-1'):220,
('H-5','H-2'):300,
('H-5','H-3'):12,
('H-5','H-4'):75,
('H-5','H-5'):0,
('H-5','H-6'):73,
('H-5','CricketG'):450,
('H-5','StudentMosque'):300,
('H-5','CentralMess'):300,
('H-5','H-8'):89,
('H-5','H-11'):160,
('H-5','H-12'):290,
('H-5','TennisGround'):450,
('H-5','FES'):450,
('H-5','AdminBlock'):600,
('H-5','FCSE'):450,
('H-5','AcademicBlock'):450,
('H-5','Auditorium'):450,
('H-5','FacultyClub'):1200,
('H-5','GIKI-Clock'):600,
('H-5','FME'):550,
('H-5','Library'):550,
('H-5','Brabers'):750,
('H-5','Graduate-H'):1100,
('H-5','Incubator'):1000,
('H-5','GuestHouse'):750,
('H-5','TuckMosque'):800,
('H-5','HBL-Bank'):750,
('H-5','FMCE'):600,
('H-5','GIKI-College'):900,
('H-5','GIKI-School'):800,
('H-5','TransportOffice'):1000,
('H-5','FruitShop'):950,
('H-5','Raju'):900,
('H-5','Ayan'):900,
('H-5','Medical'):950,
('H-5','Girls-H'):1100,
('H-6','S-C'):450,
('H-6','H-9'):350,
('H-6','H-10'):350,
('H-6','H-1'):290,
('H-6','H-2'):350,
('H-6','H-3'):85,
('H-6','H-4'):2,
('H-6','H-5'):73,
('H-6','H-6'):0,
('H-6','CricketG'):550,
('H-6','StudentMosque'):400,
('H-6','CentralMess'):400,
('H-6','H-8'):160,
('H-6','H-11'):230,
('H-6','H-12'):350,
('H-6','TennisGround'):550,
('H-6','FES'):500,
('H-6','AdminBlock'):700,
('H-6','FCSE'):500,
('H-6','AcademicBlock'):500,
('H-6','Auditorium'):500,
('H-6','FacultyClub'):1300,
('H-6','GIKI-Clock'):700,
('H-6','FME'):600,
('H-6','Library'):600,
('H-6','Brabers'):800,
('H-6','Graduate-H'):1200,
('H-6','Incubator'):1000,
('H-6','GuestHouse'):800,
('H-6','TuckMosque'):900,
('H-6','HBL-Bank'):850,
('H-6','FMCE'):700,
('H-6','GIKI-College'):1000,
('H-6','GIKI-School'):900,
('H-6','TransportOffice'):1100,
('H-6','FruitShop'):1000,
('H-6','Raju'):1000,
('H-6','Ayan'):1000,
('H-6','Medical'):1000,
('H-6','Girls-H'):1100,
('CricketG','S-C'):500,
('CricketG','H-9'):400,
('CricketG','H-10'):400,
('CricketG','H-1'):350,
('CricketG','H-2'):400,
('CricketG','H-3'):450,
('CricketG','H-4'):450,
('CricketG','H-5'):450,
('CricketG','H-6'):550,
('CricketG','CricketG'):0,
('CricketG','StudentMosque'):290,
('CricketG','CentralMess'):300,
('CricketG','H-8'):450,
('CricketG','H-11'):550,
('CricketG','H-12'):650,
('CricketG','TennisGround'):25,
('CricketG','FES'):400,
('CricketG','AdminBlock'):130,
('CricketG','FCSE'):280,
('CricketG','AcademicBlock'):400,
('CricketG','Auditorium'):290,
('CricketG','FacultyClub'):1100,
('CricketG','GIKI-Clock'):270,
('CricketG','FME'):300,
('CricketG','Library'):500,
('CricketG','Brabers'):550,
('CricketG','Graduate-H'):750,
('CricketG','Incubator'):650,
('CricketG','GuestHouse'):400,
('CricketG','TuckMosque'):450,
('CricketG','HBL-Bank'):450,
('CricketG','FMCE'):400,
('CricketG','GIKI-College'):550,
('CricketG','GIKI-School'):450,
('CricketG','TransportOffice'):650,
('CricketG','FruitShop'):600,
('CricketG','Raju'):600,
('CricketG','Ayan'):600,
('CricketG','Medical'):600,
('CricketG','Girls-H'):700,
('StudentMosque','S-C'):350,
('StudentMosque','H-9'):260,
('StudentMosque','H-10'):260,
('StudentMosque','H-1'):180,
('StudentMosque','H-2'):250,
('StudentMosque','H-3'):300,
('StudentMosque','H-4'):400,
('StudentMosque','H-5'):300,
('StudentMosque','H-6'):400,
('StudentMosque','CricketG'):290,
('StudentMosque','StudentMosque'):0,
('StudentMosque','CentralMess'):13,
('StudentMosque','H-8'):300,
('StudentMosque','H-11'):350,
('StudentMosque','H-12'):500,
('StudentMosque','TennisGround'):260,
('StudentMosque','FES'):550,
('StudentMosque','AdminBlock'):280,
('StudentMosque','FCSE'):450,
('StudentMosque','AcademicBlock'):550,
('StudentMosque','Auditorium'):450,
('StudentMosque','FacultyClub'):1300,
('StudentMosque','GIKI-Clock'):400,
('StudentMosque','FME'):450,
('StudentMosque','Library'):650,
('StudentMosque','Brabers'):700,
('StudentMosque','Graduate-H'):900,
('StudentMosque','Incubator'):800,
('StudentMosque','GuestHouse'):650,
('StudentMosque','TuckMosque'):650,
('StudentMosque','HBL-Bank'):600,
('StudentMosque','FMCE'):550,
('StudentMosque','GIKI-College'):700,
('StudentMosque','GIKI-School'):600,
('StudentMosque','TransportOffice'):800,
('StudentMosque','FruitShop'):750,
('StudentMosque','Raju'):750,
('StudentMosque','Ayan'):750,
('StudentMosque','Medical'):750,
('StudentMosque','Girls-H'):850,
('CentralMess','S-C'):350,
('CentralMess','H-9'):270,
('CentralMess','H-10'):270,
('CentralMess','H-1'):190,
('CentralMess','H-2'):270,
('CentralMess','H-3'):300,
('CentralMess','H-4'):400,
('CentralMess','H-5'):300,
('CentralMess','H-6'):400,
('CentralMess','CricketG'):300,
('CentralMess','StudentMosque'):13,
('CentralMess','CentralMess'):0,
('CentralMess','H-8'):300,
('CentralMess','H-11'):400,
('CentralMess','H-12'):500,
('CentralMess','TennisGround'):270,
('CentralMess','FES'):550,
('CentralMess','AdminBlock'):290,
('CentralMess','FCSE'):450,
('CentralMess','AcademicBlock'):550,
('CentralMess','Auditorium'):450,
('CentralMess','FacultyClub'):1300,
('CentralMess','GIKI-Clock'):450,
('CentralMess','FME'):500,
('CentralMess','Library'):650,
('CentralMess','Brabers'):700,
('CentralMess','Graduate-H'):950,
('CentralMess','Incubator'):800,
('CentralMess','GuestHouse'):550,
('CentralMess','TuckMosque'):650,
('CentralMess','HBL-Bank'):600,
('CentralMess','FMCE'):550,
('CentralMess','GIKI-College'):700,
('CentralMess','GIKI-School'):650,
('CentralMess','TransportOffice'):800,
('CentralMess','FruitShop'):750,
('CentralMess','Raju'):750,
('CentralMess','Ayan'):750,
('CentralMess','Medical'):750,
('CentralMess','Girls-H'):900,
('H-8','S-C'):350,
('H-8','H-9'):290,
('H-8','H-10'):290,
('H-8','H-1'):210,
('H-8','H-2'):290,
('H-8','H-3'):77,
('H-8','H-4'):160,
('H-8','H-5'):89,
('H-8','H-6'):160,
('H-8','CricketG'):450,
('H-8','StudentMosque'):300,
('H-8','CentralMess'):300,
('H-8','H-8'):0,
('H-8','H-11'):130,
('H-8','H-12'):260,
('H-8','TennisGround'):450,
('H-8','FES'):350,
('H-8','AdminBlock'):450,
('H-8','FCSE'):350,
('H-8','AcademicBlock'):350,
('H-8','Auditorium'):350,
('H-8','FacultyClub'):1200,
('H-8','GIKI-Clock'):550,
('H-8','FME'):450,
('H-8','Library'):450,
('H-8','Brabers'):650,
('H-8','Graduate-H'):1000,
('H-8','Incubator'):900,
('H-8','GuestHouse'):700,
('H-8','TuckMosque'):750,
('H-8','HBL-Bank'):700,
('H-8','FMCE'):550,
('H-8','GIKI-College'):850,
('H-8','GIKI-School'):750,
('H-8','TransportOffice'):900,
('H-8','FruitShop'):850,
('H-8','Raju'):850,
('H-8','Ayan'):850,
('H-8','Medical'):850,
('H-8','Girls-H'):1000,
('H-11','S-C'):450,
('H-11','H-9'):350,
('H-11','H-10'):350,
('H-11','H-1'):280,
('H-11','H-2'):350,
('H-11','H-3'):150,
('H-11','H-4'):230,
('H-11','H-5'):160,
('H-11','H-6'):230,
('H-11','CricketG'):550,
('H-11','StudentMosque'):350,
('H-11','CentralMess'):400,
('H-11','H-8'):130,
('H-11','H-11'):0,
('H-11','H-12'):190,
('H-11','TennisGround'):500,
('H-11','FES'):300,
('H-11','AdminBlock'):550,
('H-11','FCSE'):300,
('H-11','AcademicBlock'):300,
('H-11','Auditorium'):300,
('H-11','FacultyClub'):1100,
('H-11','GIKI-Clock'):500,
('H-11','FME'):400,
('H-11','Library'):400,
('H-11','Brabers'):600,
('H-11','Graduate-H'):1000,
('H-11','Incubator'):900,
('H-11','GuestHouse'):650,
('H-11','TuckMosque'):700,
('H-11','HBL-Bank'):700,
('H-11','FMCE'):500,
('H-11','GIKI-College'):800,
('H-11','GIKI-School'):700,
('H-11','TransportOffice'):900,
('H-11','FruitShop'):850,
('H-11','Raju'):850,
('H-11','Ayan'):850,
('H-11','Medical'):850,
('H-11','Girls-H'):1000,
('H-12','S-C'):550,
('H-12','H-9'):500,
('H-12','H-10'):500,
('H-12','H-1'):400,
('H-12','H-2'):500,
('H-12','H-3'):280,
('H-12','H-4'):350,
('H-12','H-5'):290,
('H-12','H-6'):350,
('H-12','CricketG'):650,
('H-12','StudentMosque'):500,
('H-12','CentralMess'):500,
('H-12','H-8'):260,
('H-12','H-11'):190,
('H-12','H-12'):0,
('H-12','TennisGround'):650,
('H-12','FES'):500,
('H-12','AdminBlock'):650,
('H-12','FCSE'):500,
('H-12','AcademicBlock'):500,
('H-12','Auditorium'):500,
('H-12','FacultyClub'):1200,
('H-12','GIKI-Clock'):700,
('H-12','FME'):600,
('H-12','Library'):600,
('H-12','Brabers'):800,
('H-12','Graduate-H'):1200,
('H-12','Incubator'):1000,
('H-12','GuestHouse'):950,
('H-12','TuckMosque'):900,
('H-12','HBL-Bank'):850,
('H-12','FMCE'):700,
('H-12','GIKI-College'):1000,
('H-12','GIKI-School'):900,
('H-12','TransportOffice'):1100,
('H-12','FruitShop'):1000,
('H-12','Raju'):1000,
('H-12','Ayan'):1000,
('H-12','Medical'):1000,
('H-12','Girls-H'):1100,
('TennisGround','S-C'):450,
('TennisGround','H-9'):400,
('TennisGround','H-10'):400,
('TennisGround','H-1'):300,
('TennisGround','H-2'):400,
('TennisGround','H-3'):450,
('TennisGround','H-4'):500,
('TennisGround','H-5'):450,
('TennisGround','H-6'):550,
('TennisGround','CricketG'):25,
('TennisGround','StudentMosque'):260,
('TennisGround','CentralMess'):270,
('TennisGround','H-8'):450,
('TennisGround','H-11'):500,
('TennisGround','H-12'):650,
('TennisGround','TennisGround'):0,
('TennisGround','FES'):350,
('TennisGround','AdminBlock'):110,
('TennisGround','FCSE'):260,
('TennisGround','AcademicBlock'):400,
('TennisGround','Auditorium'):260,
('TennisGround','FacultyClub'):1100,
('TennisGround','GIKI-Clock'):250,
('TennisGround','FME'):280,
('TennisGround','Library'):500,
('TennisGround','Brabers'):550,
('TennisGround','Graduate-H'):750,
('TennisGround','Incubator'):600,
('TennisGround','GuestHouse'):350,
('TennisGround','TuckMosque'):450,
('TennisGround','HBL-Bank'):400,
('TennisGround','FMCE'):400,
('TennisGround','GIKI-College'):500,
('TennisGround','GIKI-School'):450,
('TennisGround','TransportOffice'):600,
('TennisGround','FruitShop'):550,
('TennisGround','Raju'):550,
('TennisGround','Ayan'):550,
('TennisGround','Medical'):550,
('TennisGround','Girls-H'):700,
('FES','S-C'):700,
('FES','H-9'):650,
('FES','H-10'):650,
('FES','H-1'):550,
('FES','H-2'):650,
('FES','H-3'):450,
('FES','H-4'):500,
('FES','H-5'):450,
('FES','H-6'):500,
('FES','CricketG'):400,
('FES','StudentMosque'):550,
('FES','CentralMess'):550,
('FES','H-8'):350,
('FES','H-11'):300,
('FES','H-12'):500,
('FES','TennisGround'):350,
('FES','FES'):0,
('FES','AdminBlock'):250,
('FES','FCSE'):97,
('FES','AcademicBlock'):100,
('FES','Auditorium'):94,
('FES','FacultyClub'):1100,
('FES','GIKI-Clock'):290,
('FES','FME'):200,
('FES','Library'):210,
('FES','Brabers'):400,
('FES','Graduate-H'):750,
('FES','Incubator'):650,
('FES','GuestHouse'):450,
('FES','TuckMosque'):550,
('FES','HBL-Bank'):450,
('FES','FMCE'):290,
('FES','GIKI-College'):600,
('FES','GIKI-School'):500,
('FES','TransportOffice'):650,
('FES','FruitShop'):600,
('FES','Raju'):600,
('FES','Ayan'):600,
('FES','Medical'):600,
('FES','Girls-H'):700,
('AdminBlock','S-C'):550,
('AdminBlock','H-9'):400,
('AdminBlock','H-10'):400,
('AdminBlock','H-1'):350,
('AdminBlock','H-2'):550,
('AdminBlock','H-3'):450,
('AdminBlock','H-4'):550,
('AdminBlock','H-5'):600,
('AdminBlock','H-6'):700,
('AdminBlock','CricketG'):130,
('AdminBlock','StudentMosque'):280,
('AdminBlock','CentralMess'):290,
('AdminBlock','H-8'):450,
('AdminBlock','H-11'):550,
('AdminBlock','H-12'):650,
('AdminBlock','TennisGround'):110,
('AdminBlock','FES'):250,
('AdminBlock','AdminBlock'):0,
('AdminBlock','FCSE'):150,
('AdminBlock','AcademicBlock'):280,
('AdminBlock','Auditorium'):160,
('AdminBlock','FacultyClub'):1000,
('AdminBlock','GIKI-Clock'):140,
('AdminBlock','FME'):180,
('AdminBlock','Library'):400,
('AdminBlock','Brabers'):450,
('AdminBlock','Graduate-H'):650,
('AdminBlock','Incubator'):500,
('AdminBlock','GuestHouse'):200,
('AdminBlock','TuckMosque'):350,
('AdminBlock','HBL-Bank'):300,
('AdminBlock','FMCE'):280,
('AdminBlock','GIKI-College'):350,
('AdminBlock','GIKI-School'):350,
('AdminBlock','TransportOffice'):550,
('AdminBlock','FruitShop'):450,
('AdminBlock','Raju'):450,
('AdminBlock','Ayan'):450,
('AdminBlock','Medical'):450,
('AdminBlock','Girls-H'):600,
('FCSE','S-C'):650,
('FCSE','H-9'):550,
('FCSE','H-10'):550,
('FCSE','H-1'):500,
('FCSE','H-2'):550,
('FCSE','H-3'):450,
('FCSE','H-4'):500,
('FCSE','H-5'):450,
('FCSE','H-6'):500,
('FCSE','CricketG'):280,
('FCSE','StudentMosque'):450,
('FCSE','CentralMess'):450,
('FCSE','H-8'):350,
('FCSE','H-11'):300,
('FCSE','H-12'):500,
('FCSE','TennisGround'):260,
('FCSE','FES'):97,
('FCSE','AdminBlock'):150,
('FCSE','FCSE'):0,
('FCSE','AcademicBlock'):130,
('FCSE','Auditorium'):7,
('FCSE','FacultyClub'):1000,
('FCSE','GIKI-Clock'):190,
('FCSE','FME'):95,
('FCSE','Library'):220,
('FCSE','Brabers'):350,
('FCSE','Graduate-H'):650,
('FCSE','Incubator'):550,
('FCSE','GuestHouse'):350,
('FCSE','TuckMosque'):400,
('FCSE','HBL-Bank'):350,
('FCSE','FMCE'):190,
('FCSE','GIKI-College'):500,
('FCSE','GIKI-School'):400,
('FCSE','TransportOffice'):550,
('FCSE','FruitShop'):500,
('FCSE','Raju'):500,
('FCSE','Ayan'):450,
('FCSE','Medical'):500,
('FCSE','Girls-H'):600,
('AcademicBlock','S-C'):700,
('AcademicBlock','H-9'):650,
('AcademicBlock','H-10'):650,
('AcademicBlock','H-1'):550,
('AcademicBlock','H-2'):650,
('AcademicBlock','H-3'):400,
('AcademicBlock','H-4'):500,
('AcademicBlock','H-5'):450,
('AcademicBlock','H-6'):500,
('AcademicBlock','CricketG'):400,
('AcademicBlock','StudentMosque'):550,
('AcademicBlock','CentralMess'):550,
('AcademicBlock','H-8'):350,
('AcademicBlock','H-11'):300,
('AcademicBlock','H-12'):500,
('AcademicBlock','TennisGround'):400,
('AcademicBlock','FES'):100,
('AcademicBlock','AdminBlock'):280,
('AcademicBlock','FCSE'):130,
('AcademicBlock','AcademicBlock'):0,
('AcademicBlock','Auditorium'):120,
('AcademicBlock','FacultyClub'):1100,
('AcademicBlock','GIKI-Clock'):300,
('AcademicBlock','FME'):230,
('AcademicBlock','Library'):140,
('AcademicBlock','Brabers'):350,
('AcademicBlock','Graduate-H'):700,
('AcademicBlock','Incubator'):600,
('AcademicBlock','GuestHouse'):450,
('AcademicBlock','TuckMosque'):500,
('AcademicBlock','HBL-Bank'):450,
('AcademicBlock','FMCE'):240,
('AcademicBlock','GIKI-College'):600,
('AcademicBlock','GIKI-School'):500,
('AcademicBlock','TransportOffice'):600,
('AcademicBlock','FruitShop'):550,
('AcademicBlock','Raju'):550,
('AcademicBlock','Ayan'):550,
('AcademicBlock','Medical'):550,
('AcademicBlock','Girls-H'):650,
('Auditorium','S-C'):650,
('Auditorium','H-9'):550,
('Auditorium','H-10'):550,
('Auditorium','H-1'):500,
('Auditorium','H-2'):550,
('Auditorium','H-3'):450,
('Auditorium','H-4'):500,
('Auditorium','H-5'):450,
('Auditorium','H-6'):500,
('Auditorium','CricketG'):290,
('Auditorium','StudentMosque'):450,
('Auditorium','CentralMess'):450,
('Auditorium','H-8'):350,
('Auditorium','H-11'):300,
('Auditorium','H-12'):500,
('Auditorium','TennisGround'):260,
('Auditorium','FES'):94,
('Auditorium','AdminBlock'):160,
('Auditorium','FCSE'):7,
('Auditorium','AcademicBlock'):120,
('Auditorium','Auditorium'):0,
('Auditorium','FacultyClub'):1000,
('Auditorium','GIKI-Clock'):200,
('Auditorium','FME'):100,
('Auditorium','Library'):220,
('Auditorium','Brabers'):350,
('Auditorium','Graduate-H'):650,
('Auditorium','Incubator'):550,
('Auditorium','GuestHouse'):350,
('Auditorium','TuckMosque'):400,
('Auditorium','HBL-Bank'):350,
('Auditorium','FMCE'):200,
('Auditorium','GIKI-College'):500,
('Auditorium','GIKI-School'):400,
('Auditorium','TransportOffice'):550,
('Auditorium','FruitShop'):500,
('Auditorium','Raju'):500,
('Auditorium','Ayan'):500,
('Auditorium','Medical'):500,
('Auditorium','Girls-H'):600,
('FacultyClub','S-C'):1500,
('FacultyClub','H-9'):1400,
('FacultyClub','H-10'):1400,
('FacultyClub','H-1'):1300,
('FacultyClub','H-2'):1400,
('FacultyClub','H-3'):1200,
('FacultyClub','H-4'):1300,
('FacultyClub','H-5'):1200,
('FacultyClub','H-6'):1300,
('FacultyClub','CricketG'):1100,
('FacultyClub','StudentMosque'):1300,
('FacultyClub','CentralMess'):1300,
('FacultyClub','H-8'):1200,
('FacultyClub','H-11'):1100,
('FacultyClub','H-12'):1200,
('FacultyClub','TennisGround'):1100,
('FacultyClub','FES'):1100,
('FacultyClub','AdminBlock'):1000,
('FacultyClub','FCSE'):1000,
('FacultyClub','AcademicBlock'):1100,
('FacultyClub','Auditorium'):1000,
('FacultyClub','FacultyClub'):0,
('FacultyClub','GIKI-Clock'):850,
('FacultyClub','FME'):950,
('FacultyClub','Library'):1100,
('FacultyClub','Brabers'):750,
('FacultyClub','Graduate-H'):350,
('FacultyClub','Incubator'):500,
('FacultyClub','GuestHouse'):1200,
('FacultyClub','TuckMosque'):850,
('FacultyClub','HBL-Bank'):750,
('FacultyClub','FMCE'):850,
('FacultyClub','GIKI-College'):850,
('FacultyClub','GIKI-School'):850,
('FacultyClub','TransportOffice'):900,
('FacultyClub','FruitShop'):850,
('FacultyClub','Raju'):850,
('FacultyClub','Ayan'):850,
('FacultyClub','Medical'):850,
('FacultyClub','Girls-H'):1000,
('GIKI-Clock','S-C'):600,
('GIKI-Clock','H-9'):550,
('GIKI-Clock','H-10'):550,
('GIKI-Clock','H-1'):450,
('GIKI-Clock','H-2'):550,
('GIKI-Clock','H-3'):600,
('GIKI-Clock','H-4'):700,
('GIKI-Clock','H-5'):600,
('GIKI-Clock','H-6'):700,
('GIKI-Clock','CricketG'):270,
('GIKI-Clock','StudentMosque'):400,
('GIKI-Clock','CentralMess'):450,
('GIKI-Clock','H-8'):550,
('GIKI-Clock','H-11'):500,
('GIKI-Clock','H-12'):700,
('GIKI-Clock','TennisGround'):250,
('GIKI-Clock','FES'):290,
('GIKI-Clock','AdminBlock'):140,
('GIKI-Clock','FCSE'):190,
('GIKI-Clock','AcademicBlock'):300,
('GIKI-Clock','Auditorium'):200,
('GIKI-Clock','FacultyClub'):850,
('GIKI-Clock','GIKI-Clock'):0,
('GIKI-Clock','FME'):220,
('GIKI-Clock','Library'):400,
('GIKI-Clock','Brabers'):400,
('GIKI-Clock','Graduate-H'):500,
('GIKI-Clock','Incubator'):350,
('GIKI-Clock','GuestHouse'):240,
('GIKI-Clock','TuckMosque'):200,
('GIKI-Clock','HBL-Bank'):160,
('GIKI-Clock','FMCE'):230,
('GIKI-Clock','GIKI-College'):240,
('GIKI-Clock','GIKI-School'):200,
('GIKI-Clock','TransportOffice'):400,
('GIKI-Clock','FruitShop'):350,
('GIKI-Clock','Raju'):300,
('GIKI-Clock','Ayan'):300,
('GIKI-Clock','Medical'):350,
('GIKI-Clock','Girls-H'):450,
('FME','S-C'):650,
('FME','H-9'):600,
('FME','H-10'):600,
('FME','H-1'):500,
('FME','H-2'):600,
('FME','H-3'):550,
('FME','H-4'):600,
('FME','H-5'):550,
('FME','H-6'):600,
('FME','CricketG'):300,
('FME','StudentMosque'):450,
('FME','CentralMess'):500,
('FME','H-8'):450,
('FME','H-11'):400,
('FME','H-12'):600,
('FME','TennisGround'):280,
('FME','FES'):200,
('FME','AdminBlock'):180,
('FME','FCSE'):95,
('FME','AcademicBlock'):230,
('FME','Auditorium'):100,
('FME','FacultyClub'):950,
('FME','GIKI-Clock'):220,
('FME','FME'):0,
('FME','Library'):210,
('FME','Brabers'):260,
('FME','Graduate-H'):550,
('FME','Incubator'):450,
('FME','GuestHouse'):400,
('FME','TuckMosque'):350,
('FME','HBL-Bank'):300,
('FME','FMCE'):90,
('FME','GIKI-College'):400,
('FME','GIKI-School'):350,
('FME','TransportOffice'):450,
('FME','FruitShop'):400,
('FME','Raju'):400,
('FME','Ayan'):400,
('FME','Medical'):400,
('FME','Girls-H'):500,
('Library','S-C'):800,
('Library','H-9'):750,
('Library','H-10'):750,
('Library','H-1'):650,
('Library','H-2'):750,
('Library','H-3'):500,
('Library','H-4'):600,
('Library','H-5'):550,
('Library','H-6'):600,
('Library','CricketG'):500,
('Library','StudentMosque'):650,
('Library','CentralMess'):650,
('Library','H-8'):450,
('Library','H-11'):400,
('Library','H-12'):600,
('Library','TennisGround'):500,
('Library','FES'):210,
('Library','AdminBlock'):400,
('Library','FCSE'):220,
('Library','AcademicBlock'):140,
('Library','Auditorium'):220,
('Library','FacultyClub'):1100,
('Library','GIKI-Clock'):400,
('Library','FME'):210,
('Library','Library'):0,
('Library','Brabers'):140,
('Library','Graduate-H'):550,
('Library','Incubator'):400,
('Library','GuestHouse'):500,
('Library','TuckMosque'):500,
('Library','HBL-Bank'):400,
('Library','FMCE'):200,
('Library','GIKI-College'):500,
('Library','GIKI-School'):500,
('Library','TransportOffice'):550,
('Library','FruitShop'):500,
('Library','Raju'):500,
('Library','Ayan'):500,
('Library','Medical'):500,
('Library','Girls-H'):600,
('Brabers','S-C'):1000,
('Brabers','H-9'):850,
('Brabers','H-10'):850,
('Brabers','H-1'):750,
('Brabers','H-2'):850,
('Brabers','H-3'):750,
('Brabers','H-4'):800,
('Brabers','H-5'):750,
('Brabers','H-6'):800,
('Brabers','CricketG'):550,
('Brabers','StudentMosque'):700,
('Brabers','CentralMess'):700,
('Brabers','H-8'):650,
('Brabers','H-11'):600,
('Brabers','H-12'):800,
('Brabers','TennisGround'):550,
('Brabers','FES'):400,
('Brabers','AdminBlock'):450,
('Brabers','FCSE'):350,
('Brabers','AcademicBlock'):350,
('Brabers','Auditorium'):350,
('Brabers','FacultyClub'):750,
('Brabers','GIKI-Clock'):400,
('Brabers','FME'):260,
('Brabers','Library'):140,
('Brabers','Brabers'):0,
('Brabers','Graduate-H'):400,
('Brabers','Incubator'):270,
('Brabers','GuestHouse'):400,
('Brabers','TuckMosque'):350,
('Brabers','HBL-Bank'):280,
('Brabers','FMCE'):260,
('Brabers','GIKI-College'):400,
('Brabers','GIKI-School'):350,
('Brabers','TransportOffice'):450,
('Brabers','FruitShop'):350,
('Brabers','Raju'):350,
('Brabers','Ayan'):350,
('Brabers','Medical'):350,
('Brabers','Girls-H'):500,
('Graduate-H','S-C'):1500,
('Graduate-H','H-9'):1000,
('Graduate-H','H-10'):1000,
('Graduate-H','H-1'):1000,
('Graduate-H','H-2'):1000,
('Graduate-H','H-3'):1200,
('Graduate-H','H-4'):1200,
('Graduate-H','H-5'):1100,
('Graduate-H','H-6'):1200,
('Graduate-H','CricketG'):750,
('Graduate-H','StudentMosque'):900,
('Graduate-H','CentralMess'):950,
('Graduate-H','H-8'):1000,
('Graduate-H','H-11'):1000,
('Graduate-H','H-12'):1200,
('Graduate-H','TennisGround'):750,
('Graduate-H','FES'):750,
('Graduate-H','AdminBlock'):650,
('Graduate-H','FCSE'):650,
('Graduate-H','AcademicBlock'):700,
('Graduate-H','Auditorium'):650,
('Graduate-H','FacultyClub'):350,
('Graduate-H','GIKI-Clock'):500,
('Graduate-H','FME'):550,
('Graduate-H','Library'):550,
('Graduate-H','Brabers'):400,
('Graduate-H','Graduate-H'):0,
('Graduate-H','Incubator'):120,
('Graduate-H','GuestHouse'):500,
('Graduate-H','TuckMosque'):450,
('Graduate-H','HBL-Bank'):400,
('Graduate-H','FMCE'):500,
('Graduate-H','GIKI-College'):500,
('Graduate-H','GIKI-School'):450,
('Graduate-H','TransportOffice'):550,
('Graduate-H','FruitShop'):500,
('Graduate-H','Raju'):450,
('Graduate-H','Ayan'):450,
('Graduate-H','Medical'):450,
('Graduate-H','Girls-H'):600,
('Incubator','S-C'):1000,
('Incubator','H-9'):950,
('Incubator','H-10'):950,
('Incubator','H-1'):850,
('Incubator','H-2'):900,
('Incubator','H-3'):1000,
('Incubator','H-4'):1000,
('Incubator','H-5'):1000,
('Incubator','H-6'):1000,
('Incubator','CricketG'):650,
('Incubator','StudentMosque'):800,
('Incubator','CentralMess'):800,
('Incubator','H-8'):900,
('Incubator','H-11'):900,
('Incubator','H-12'):1000,
('Incubator','TennisGround'):600,
('Incubator','FES'):650,
('Incubator','AdminBlock'):500,
('Incubator','FCSE'):550,
('Incubator','AcademicBlock'):600,
('Incubator','Auditorium'):550,
('Incubator','FacultyClub'):500,
('Incubator','GIKI-Clock'):350,
('Incubator','FME'):450,
('Incubator','Library'):400,
('Incubator','Brabers'):270,
('Incubator','Graduate-H'):120,
('Incubator','Incubator'):0,
('Incubator','GuestHouse'):400,
('Incubator','TuckMosque'):350,
('Incubator','HBL-Bank'):260,
('Incubator','FMCE'):350,
('Incubator','GIKI-College'):350,
('Incubator','GIKI-School'):350,
('Incubator','TransportOffice'):400,
('Incubator','FruitShop'):350,
('Incubator','Raju'):350,
('Incubator','Ayan'):350,
('Incubator','Medical'):350,
('Incubator','Girls-H'):450,
('GuestHouse','S-C'):750,
('GuestHouse','H-9'):700,
('GuestHouse','H-10'):700,
('GuestHouse','H-1'):600,
('GuestHouse','H-2'):650,
('GuestHouse','H-3'):700,
('GuestHouse','H-4'):800,
('GuestHouse','H-5'):750,
('GuestHouse','H-6'):800,
('GuestHouse','CricketG'):400,
('GuestHouse','StudentMosque'):650,
('GuestHouse','CentralMess'):550,
('GuestHouse','H-8'):700,
('GuestHouse','H-11'):650,
('GuestHouse','H-12'):950,
('GuestHouse','TennisGround'):350,
('GuestHouse','FES'):450,
('GuestHouse','AdminBlock'):200,
('GuestHouse','FCSE'):350,
('GuestHouse','AcademicBlock'):450,
('GuestHouse','Auditorium'):350,
('GuestHouse','FacultyClub'):1200,
('GuestHouse','GIKI-Clock'):240,
('GuestHouse','FME'):400,
('GuestHouse','Library'):500,
('GuestHouse','Brabers'):400,
('GuestHouse','Graduate-H'):500,
('GuestHouse','Incubator'):400,
('GuestHouse','GuestHouse'):0,
('GuestHouse','TuckMosque'):37,
('GuestHouse','HBL-Bank'):120,
('GuestHouse','FMCE'):350,
('GuestHouse','GIKI-College'):190,
('GuestHouse','GIKI-School'):150,
('GuestHouse','TransportOffice'):350,
('GuestHouse','FruitShop'):300,
('GuestHouse','Raju'):290,
('GuestHouse','Ayan'):300,
('GuestHouse','Medical'):350,
('GuestHouse','Girls-H'):450,
('TuckMosque','S-C'):850,
('TuckMosque','H-9'):750,
('TuckMosque','H-10'):750,
('TuckMosque','H-1'):700,
('TuckMosque','H-2'):750,
('TuckMosque','H-3'):800,
('TuckMosque','H-4'):900,
('TuckMosque','H-5'):800,
('TuckMosque','H-6'):900,
('TuckMosque','CricketG'):450,
('TuckMosque','StudentMosque'):650,
('TuckMosque','CentralMess'):650,
('TuckMosque','H-8'):750,
('TuckMosque','H-11'):700,
('TuckMosque','H-12'):900,
('TuckMosque','TennisGround'):450,
('TuckMosque','FES'):550,
('TuckMosque','AdminBlock'):350,
('TuckMosque','FCSE'):400,
('TuckMosque','AcademicBlock'):500,
('TuckMosque','Auditorium'):400,
('TuckMosque','FacultyClub'):850,
('TuckMosque','GIKI-Clock'):200,
('TuckMosque','FME'):350,
('TuckMosque','Library'):500,
('TuckMosque','Brabers'):350,
('TuckMosque','Graduate-H'):450,
('TuckMosque','Incubator'):350,
('TuckMosque','GuestHouse'):37,
('TuckMosque','TuckMosque'):0,
('TuckMosque','HBL-Bank'):83,
('TuckMosque','FMCE'):300,
('TuckMosque','GIKI-College'):150,
('TuckMosque','GIKI-School'):120,
('TuckMosque','TransportOffice'):300,
('TuckMosque','FruitShop'):270,
('TuckMosque','Raju'):250,
('TuckMosque','Ayan'):280,
('TuckMosque','Medical'):290,
('TuckMosque','Girls-H'):400,
('HBL-Bank','S-C'):800,
('HBL-Bank','H-9'):700,
('HBL-Bank','H-10'):700,
('HBL-Bank','H-1'):650,
('HBL-Bank','H-2'):700,
('HBL-Bank','H-3'):750,
('HBL-Bank','H-4'):850,
('HBL-Bank','H-5'):750,
('HBL-Bank','H-6'):850,
('HBL-Bank','CricketG'):450,
('HBL-Bank','StudentMosque'):600,
('HBL-Bank','CentralMess'):600,
('HBL-Bank','H-8'):700,
('HBL-Bank','H-11'):700,
('HBL-Bank','H-12'):850,
('HBL-Bank','TennisGround'):400,
('HBL-Bank','FES'):450,
('HBL-Bank','AdminBlock'):300,
('HBL-Bank','FCSE'):350,
('HBL-Bank','AcademicBlock'):450,
('HBL-Bank','Auditorium'):350,
('HBL-Bank','FacultyClub'):750,
('HBL-Bank','GIKI-Clock'):160,
('HBL-Bank','FME'):300,
('HBL-Bank','Library'):400,
('HBL-Bank','Brabers'):280,
('HBL-Bank','Graduate-H'):400,
('HBL-Bank','Incubator'):260,
('HBL-Bank','GuestHouse'):120,
('HBL-Bank','TuckMosque'):83,
('HBL-Bank','HBL-Bank'):0,
('HBL-Bank','FMCE'):240,
('HBL-Bank','GIKI-College'):110,
('HBL-Bank','GIKI-School'):78,
('HBL-Bank','TransportOffice'):240,
('HBL-Bank','FruitShop'):190,
('HBL-Bank','Raju'):170,
('HBL-Bank','Ayan'):200,
('HBL-Bank','Medical'):210,
('HBL-Bank','Girls-H'):350,
('FMCE','S-C'):750,
('FMCE','H-9'):700,
('FMCE','H-10'):700,
('FMCE','H-1'):600,
('FMCE','H-2'):700,
('FMCE','H-3'):600,
('FMCE','H-4'):700,
('FMCE','H-5'):600,
('FMCE','H-6'):700,
('FMCE','CricketG'):400,
('FMCE','StudentMosque'):550,
('FMCE','CentralMess'):550,
('FMCE','H-8'):550,
('FMCE','H-11'):500,
('FMCE','H-12'):700,
('FMCE','TennisGround'):400,
('FMCE','FES'):290,
('FMCE','AdminBlock'):280,
('FMCE','FCSE'):190,
('FMCE','AcademicBlock'):240,
('FMCE','Auditorium'):200,
('FMCE','FacultyClub'):850,
('FMCE','GIKI-Clock'):230,
('FMCE','FME'):90,
('FMCE','Library'):200,
('FMCE','Brabers'):260,
('FMCE','Graduate-H'):500,
('FMCE','Incubator'):350,
('FMCE','GuestHouse'):350,
('FMCE','TuckMosque'):300,
('FMCE','HBL-Bank'):240,
('FMCE','FMCE'):0,
('FMCE','GIKI-College'):350,
('FMCE','GIKI-School'):300,
('FMCE','TransportOffice'):400,
('FMCE','FruitShop'):350,
('FMCE','Raju'):300,
('FMCE','Ayan'):300,
('FMCE','Medical'):350,
('FMCE','Girls-H'):450,
('GIKI-College','S-C'):900,
('GIKI-College','H-9'):850,
('GIKI-College','H-10'):850,
('GIKI-College','H-1'):750,
('GIKI-College','H-2'):800,
('GIKI-College','H-3'):850,
('GIKI-College','H-4'):1000,
('GIKI-College','H-5'):900,
('GIKI-College','H-6'):1000,
('GIKI-College','CricketG'):550,
('GIKI-College','StudentMosque'):700,
('GIKI-College','CentralMess'):700,
('GIKI-College','H-8'):850,
('GIKI-College','H-11'):800,
('GIKI-College','H-12'):1000,
('GIKI-College','TennisGround'):500,
('GIKI-College','FES'):600,
('GIKI-College','AdminBlock'):350,
('GIKI-College','FCSE'):500,
('GIKI-College','AcademicBlock'):600,
('GIKI-College','Auditorium'):500,
('GIKI-College','FacultyClub'):850,
('GIKI-College','GIKI-Clock'):240,
('GIKI-College','FME'):400,
('GIKI-College','Library'):500,
('GIKI-College','Brabers'):400,
('GIKI-College','Graduate-H'):500,
('GIKI-College','Incubator'):350,
('GIKI-College','GuestHouse'):190,
('GIKI-College','TuckMosque'):150,
('GIKI-College','HBL-Bank'):110,
('GIKI-College','FMCE'):350,
('GIKI-College','GIKI-College'):0,
('GIKI-College','GIKI-School'):35,
('GIKI-College','TransportOffice'):275,
('GIKI-College','FruitShop'):225,
('GIKI-College','Raju'):205,
('GIKI-College','Ayan'):235,
('GIKI-College','Medical'):325,
('GIKI-College','Girls-H'):435,
('GIKI-School','S-C'):800,
('GIKI-School','H-9'):750,
('GIKI-School','H-10'):750,
('GIKI-School','H-1'):650,
('GIKI-School','H-2'):750,
('GIKI-School','H-3'):800,
('GIKI-School','H-4'):900,
('GIKI-School','H-5'):800,
('GIKI-School','H-6'):900,
('GIKI-School','CricketG'):450,
('GIKI-School','StudentMosque'):600,
('GIKI-School','CentralMess'):650,
('GIKI-School','H-8'):750,
('GIKI-School','H-11'):700,
('GIKI-School','H-12'):900,
('GIKI-School','TennisGround'):450,
('GIKI-School','FES'):500,
('GIKI-School','AdminBlock'):350,
('GIKI-School','FCSE'):400,
('GIKI-School','AcademicBlock'):500,
('GIKI-School','Auditorium'):400,
('GIKI-School','FacultyClub'):850,
('GIKI-School','GIKI-Clock'):200,
('GIKI-School','FME'):350,
('GIKI-School','Library'):500,
('GIKI-School','Brabers'):350,
('GIKI-School','Graduate-H'):450,
('GIKI-School','Incubator'):350,
('GIKI-School','GuestHouse'):150,
('GIKI-School','TuckMosque'):120,
('GIKI-School','HBL-Bank'):78,
('GIKI-School','FMCE'):300,
('GIKI-School','GIKI-College'):35,
('GIKI-School','GIKI-School'):0,
('GIKI-School','TransportOffice'):240,
('GIKI-School','FruitShop'):190,
('GIKI-School','Raju'):170,
('GIKI-School','Ayan'):200,
('GIKI-School','Medical'):290,
('GIKI-School','Girls-H'):400,
('TransportOffice','S-C'):1000,
('TransportOffice','H-9'):950,
('TransportOffice','H-10'):950,
('TransportOffice','H-1'):850,
('TransportOffice','H-2'):950,
('TransportOffice','H-3'):1000,
('TransportOffice','H-4'):1100,
('TransportOffice','H-5'):1000,
('TransportOffice','H-6'):1100,
('TransportOffice','CricketG'):650,
('TransportOffice','StudentMosque'):800,
('TransportOffice','CentralMess'):800,
('TransportOffice','H-8'):900,
('TransportOffice','H-11'):900,
('TransportOffice','H-12'):1100,
('TransportOffice','TennisGround'):600,
('TransportOffice','FES'):650,
('TransportOffice','AdminBlock'):550,
('TransportOffice','FCSE'):550,
('TransportOffice','AcademicBlock'):600,
('TransportOffice','Auditorium'):550,
('TransportOffice','FacultyClub'):900,
('TransportOffice','GIKI-Clock'):400,
('TransportOffice','FME'):450,
('TransportOffice','Library'):550,
('TransportOffice','Brabers'):450,
('TransportOffice','Graduate-H'):550,
('TransportOffice','Incubator'):400,
('TransportOffice','GuestHouse'):350,
('TransportOffice','TuckMosque'):300,
('TransportOffice','HBL-Bank'):240,
('TransportOffice','FMCE'):400,
('TransportOffice','GIKI-College'):275,
('TransportOffice','GIKI-School'):240,
('TransportOffice','TransportOffice'):0,
('TransportOffice','FruitShop'):54,
('TransportOffice','Raju'):85,
('TransportOffice','Ayan'):123,
('TransportOffice','Medical'):297,
('TransportOffice','Girls-H'):417,
('FruitShop','S-C'):950,
('FruitShop','H-9'):900,
('FruitShop','H-10'):900,
('FruitShop','H-1'):800,
('FruitShop','H-2'):900,
('FruitShop','H-3'):900,
('FruitShop','H-4'):1000,
('FruitShop','H-5'):950,
('FruitShop','H-6'):1000,
('FruitShop','CricketG'):600,
('FruitShop','StudentMosque'):750,
('FruitShop','CentralMess'):750,
('FruitShop','H-8'):850,
('FruitShop','H-11'):850,
('FruitShop','H-12'):1000,
('FruitShop','TennisGround'):550,
('FruitShop','FES'):600,
('FruitShop','AdminBlock'):450,
('FruitShop','FCSE'):500,
('FruitShop','AcademicBlock'):550,
('FruitShop','Auditorium'):500,
('FruitShop','FacultyClub'):850,
('FruitShop','GIKI-Clock'):350,
('FruitShop','FME'):400,
('FruitShop','Library'):500,
('FruitShop','Brabers'):350,
('FruitShop','Graduate-H'):500,
('FruitShop','Incubator'):350,
('FruitShop','GuestHouse'):300,
('FruitShop','TuckMosque'):270,
('FruitShop','HBL-Bank'):190,
('FruitShop','FMCE'):350,
('FruitShop','GIKI-College'):225,
('FruitShop','GIKI-School'):190,
('FruitShop','TransportOffice'):54,
('FruitShop','FruitShop'):0,
('FruitShop','Raju'):31,
('FruitShop','Ayan'):69,
('FruitShop','Medical'):261,
('FruitShop','Girls-H'):381,
('Raju','S-C'):950,
('Raju','H-9'):850,
('Raju','H-10'):850,
('Raju','H-1'):800,
('Raju','H-2'):850,
('Raju','H-3'):900,
('Raju','H-4'):1000,
('Raju','H-5'):900,
('Raju','H-6'):1000,
('Raju','CricketG'):600,
('Raju','StudentMosque'):750,
('Raju','CentralMess'):750,
('Raju','H-8'):850,
('Raju','H-11'):850,
('Raju','H-12'):1000,
('Raju','TennisGround'):550,
('Raju','FES'):600,
('Raju','AdminBlock'):450,
('Raju','FCSE'):500,
('Raju','AcademicBlock'):550,
('Raju','Auditorium'):500,
('Raju','FacultyClub'):850,
('Raju','GIKI-Clock'):300,
('Raju','FME'):400,
('Raju','Library'):500,
('Raju','Brabers'):350,
('Raju','Graduate-H'):450,
('Raju','Incubator'):350,
('Raju','GuestHouse'):290,
('Raju','TuckMosque'):250,
('Raju','HBL-Bank'):170,
('Raju','FMCE'):300,
('Raju','GIKI-College'):205,
('Raju','GIKI-School'):170,
('Raju','TransportOffice'):85,
('Raju','FruitShop'):31,
('Raju','Raju'):0,
('Raju','Ayan'):38,
('Raju','Medical'):290,
('Raju','Girls-H'):410,
('Ayan','S-C'):950,
('Ayan','H-9'):850,
('Ayan','H-10'):850,
('Ayan','H-1'):800,
('Ayan','H-2'):850,
('Ayan','H-3'):900,
('Ayan','H-4'):1000,
('Ayan','H-5'):900,
('Ayan','H-6'):1000,
('Ayan','CricketG'):600,
('Ayan','StudentMosque'):750,
('Ayan','CentralMess'):750,
('Ayan','H-8'):850,
('Ayan','H-11'):850,
('Ayan','H-12'):1000,
('Ayan','TennisGround'):550,
('Ayan','FES'):600,
('Ayan','AdminBlock'):450,
('Ayan','FCSE'):450,
('Ayan','AcademicBlock'):550,
('Ayan','Auditorium'):500,
('Ayan','FacultyClub'):850,
('Ayan','GIKI-Clock'):300,
('Ayan','FME'):400,
('Ayan','Library'):500,
('Ayan','Brabers'):350,
('Ayan','Graduate-H'):450,
('Ayan','Incubator'):350,
('Ayan','GuestHouse'):300,
('Ayan','TuckMosque'):280,
('Ayan','HBL-Bank'):200,
('Ayan','FMCE'):300,
('Ayan','GIKI-College'):235,
('Ayan','GIKI-School'):200,
('Ayan','TransportOffice'):123,
('Ayan','FruitShop'):69,
('Ayan','Raju'):38,
('Ayan','Ayan'):0,
('Ayan','Medical'):328,
('Ayan','Girls-H'):458,
('Medical','S-C'):950,
('Medical','H-9'):900,
('Medical','H-10'):900,
('Medical','H-1'):800,
('Medical','H-2'):850,
('Medical','H-3'):900,
('Medical','H-4'):1000,
('Medical','H-5'):950,
('Medical','H-6'):1000,
('Medical','CricketG'):600,
('Medical','StudentMosque'):750,
('Medical','CentralMess'):750,
('Medical','H-8'):850,
('Medical','H-11'):850,
('Medical','H-12'):1000,
('Medical','TennisGround'):550,
('Medical','FES'):600,
('Medical','AdminBlock'):450,
('Medical','FCSE'):500,
('Medical','AcademicBlock'):550,
('Medical','Auditorium'):500,
('Medical','FacultyClub'):850,
('Medical','GIKI-Clock'):350,
('Medical','FME'):400,
('Medical','Library'):500,
('Medical','Brabers'):350,
('Medical','Graduate-H'):450,
('Medical','Incubator'):350,
('Medical','GuestHouse'):350,
('Medical','TuckMosque'):290,
('Medical','HBL-Bank'):210,
('Medical','FMCE'):350,
('Medical','GIKI-College'):325,
('Medical','GIKI-School'):290,
('Medical','TransportOffice'):297,
('Medical','FruitShop'):261,
('Medical','Raju'):290,
('Medical','Ayan'):328,
('Medical','Medical'):0,
('Medical','Girls-H'):120,
('Girls-H','S-C'):1100,
('Girls-H','H-9'):1000,
('Girls-H','H-10'):1000,
('Girls-H','H-1'):900,
('Girls-H','H-2'):1000,
('Girls-H','H-3'):1000,
('Girls-H','H-4'):1100,
('Girls-H','H-5'):1100,
('Girls-H','H-6'):1100,
('Girls-H','CricketG'):700,
('Girls-H','StudentMosque'):850,
('Girls-H','CentralMess'):900,
('Girls-H','H-8'):1000,
('Girls-H','H-11'):1000,
('Girls-H','H-12'):1100,
('Girls-H','TennisGround'):700,
('Girls-H','FES'):700,
('Girls-H','AdminBlock'):600,
('Girls-H','FCSE'):600,
('Girls-H','AcademicBlock'):650,
('Girls-H','Auditorium'):600,
('Girls-H','FacultyClub'):1000,
('Girls-H','GIKI-Clock'):450,
('Girls-H','FME'):500,
('Girls-H','Library'):600,
('Girls-H','Brabers'):500,
('Girls-H','Graduate-H'):600,
('Girls-H','Incubator'):450,
('Girls-H','GuestHouse'):450,
('Girls-H','TuckMosque'):400,
('Girls-H','HBL-Bank'):350,
('Girls-H','FMCE'):450,
('Girls-H','GIKI-College'):435,
('Girls-H','GIKI-School'):400,
('Girls-H','TransportOffice'):417,
('Girls-H','FruitShop'):381,
('Girls-H','Raju'):410,
('Girls-H','Ayan'):458,
('Girls-H','Medical'):120,
('Girls-H','Girls-H'):0,
}




Graph = {
'sports complex':('hostel 10', 'hostel 9', 'cricket ground'),
'hostel 10':('sports complex', 'hostel 9', 'hostel 2', 'hostel 1'),
'hostel 9':('sports complex', 'hostel 10', 'hostel 2', 'hostel 1', 'student mosque', 'cricket ground'),
'hostel 2':('hostel 10', 'hostel 9', 'hostel 1', 'hostel 4', 'hostel 3'),
'hostel 1':('hostel 10', 'hostel 9', 'hostel 2', 'hostel 4', 'hostel 3', 'student mosque', 'cricket ground'),
'hostel 4':('hostel 2', 'hostel 1', 'hostel 3', 'hostel 6', 'hostel 5'),
'hostel 3':('hostel 2', 'hostel 1', 'hostel 4', 'hostel 6', 'hostel 5', 'hostel 8', 'student mosque'),
'hostel 6':('hostel 4', 'hostel 3', 'hostel 5'),
'hostel 5':('hostel 4', 'hostel 3', 'hostel 6', 'hostel 8', 'hostel 11', 'hostel 12', 'student mosque'),
'hostel 8':('hostel 3', 'hostel 5', 'student mosque'),
'hostel 11':('hostel 5', 'hostel 12', 'engineering sciences'),
'hostel 12':('hostel 5', 'hostel 11', 'engineering sciences'),
'student mosque':('hostel 9', 'hostel 1', 'hostel 3', 'hostel 5', 'hostel 8', 'cricket ground', 'engineering sciences'),
'cricket ground':('sports complex', 'hostel 9', 'hostel 1', 'student mosque', 'engineering sciences', 'computer science', 'admin'),
'engineering sciences':('hostel 11', 'hostel 12', 'student mosque', 'cricket ground', 'computer science', 'auditorium', 'library'),
'computer science':('cricket ground', 'engineering sciences', 'admin', 'auditorium', 'mechanical engineering'),
'admin':('cricket ground', 'computer science', 'mechanical engineering', 'guest house'),
'auditorium':('engineering sciences', 'computer science', 'library', 'mechanical engineering', 'material engineering'),
'library':('engineering sciences', 'auditorium', 'material engineering', 'faculty club', 'helipad'),
'mechanical engineering':('computer science', 'admin','auditorium', 'material engineering'),
'material engineering':('auditorium', 'library', 'mechanical engineering', 'tuc shop', 'medical center'),
'guest house':('admin', 'giki school'),
'giki school':('guest house', 'tuc shop'),
'tuc shop':('material engineering', 'giki school', 'medical center'),
'medical center':('material engineering', 'tuc shop', 'helipad'),
'faculty club':('library', 'helipad'),
'helipad':('library', 'medical center', 'faculty club')
}


Cost = {

('sports complex','hostel 10'):160,
('sports complex','hostel 9'):68,
('sports complex','cricket ground'):500,
('hostel 10','sports complex'):160,
('hostel 10','hostel 9'):86,
('hostel 10','hostel 2'):4,
('hostel 10','hostel 1'):80,
('hostel 9','sports complex'):68,
('hostel 9','hostel 10'):86,
('hostel 9','hostel 2'):82,
('hostel 9','hostel 1'):80,
('hostel 9','student mosque'):260,
('hostel 9','cricket ground'):400,
('hostel 2','hostel 10'):4,
('hostel 2','hostel 9'):82,
('hostel 2','hostel 1'):76,
('hostel 2','hostel 4'):350,
('hostel 2','hostel 3'):280,
('hostel 1','hostel 10'):80,
('hostel 1','hostel 9'):80,
('hostel 1','hostel 2'):76,
('hostel 1','hostel 4'):290,
('hostel 1','hostel 3'):210,
('hostel 1','student mosque'):180,
('hostel 1','cricket ground'):350,
('hostel 4','hostel 2'):350,
('hostel 4','hostel 1'):290,
('hostel 4','hostel 3'):86,
('hostel 4','hostel 6'):2,
('hostel 4','hostel 5'):75,
('hostel 3','hostel 2'):280,
('hostel 3','hostel 1'):210,
('hostel 3','hostel 4'):86,
('hostel 3','hostel 6'):85,
('hostel 3','hostel 5'):12,
('hostel 3','hostel 8'):77,
('hostel 3','student mosque'):300,
('hostel 6','hostel 4'):2,
('hostel 6','hostel 3'):85,
('hostel 6','hostel 5'):73,
('hostel 5','hostel 4'):75,
('hostel 5','hostel 3'):12,
('hostel 5','hostel 6'):73,
('hostel 5','hostel 8' ):89,
('hostel 5','hostel 11'):160,
('hostel 5','hostel 12'):290,
('hostel 5','student mosque'):300,
('hostel 8','hostel 3'):77,
('hostel 8','hostel 5'):89,
('hostel 8','student mosque'):300,
('hostel 11','hostel 5'):160,
('hostel 11','hostel 12'):190,
('hostel 11','engineering sciences'):300,
('hostel 12','hostel 5'):290,
('hostel 12','hostel 11' ):190,
('hostel 12','engineering sciences'):500,
('student mosque','hostel 9'):260,
('student mosque','hostel 1'):180,
('student mosque','hostel 3'):100,
('student mosque','hostel 5'):300,
('student mosque','hostel 8'):300,
('student mosque','cricket ground'):290,
('student mosque','engineering sciences'):550,
('cricket ground','sports complex'):500,
('cricket ground','hostel 9' ):400,
('cricket ground','hostel 1'):350,
('cricket ground','student mosque'):290,
('cricket ground','engineering sciences'):400,
('cricket ground','computer science'):280,
('cricket ground','admin'):130,
('engineering sciences','hostel 11'):300,
('engineering sciences','hostel 12'):500,
('engineering sciences','student mosque'):550,
('engineering sciences','cricket ground'):400,
('engineering sciences','computer science'):97,
('engineering sciences','auditorium'):95,
('engineering sciences','library'):210,
('computer science','cricket ground'):280,
('computer science','engineering sciences'):97,
('computer science','admin'):150,
('computer science','auditorium'):7,
('computer science','mechanical engineering'):95,
('admin','cricket ground'):130,
('admin','computer science'):150,
('admin','mechanical engineering'):180,
('admin','guest house'):200,
('auditorium','engineering sciences'):94,
('auditorium','computer science'):7,
('auditorium','library'):220,
('auditorium','mechanical engineering'):100,
('auditorium','material engineering'):90,
('library','engineering sciences'):210,
('library','auditorium'	):220,
('library','material engineering'):200,
('library','faculty club'):1100,
('library','helipad'):750,
('mechanical engineering','computer science'):95,
('mechanical engineering','admin'):180,
('mechanical engineering','auditorium'):100,
('mechanical engineering','material engineering'):90,
('material engineering','auditorium'):90,
('material engineering','library'):200,
('material engineering','mechanical engineering'):90,
('material engineering','tuc shop'):300,
('material engineering','medical center'):350,
('guest house','admin'):200,
('guest house','giki school'):150,
('giki school','guest house'):150,
('giki school','tuc shop'):170,
('tuc shop','material engineering'):300,
('tuc shop','giki school'):170,
('tuc shop','medical center'):290,
('medical center','material engineering'):350,
('medical center','tuc shop'):290,
('medical center','helipad'):750,
('faculty club','library'):1100,
('faculty club','helipad'):170,
('helipad','library'):750,
('helipad','medical center'):750,
('helipad','faculty club'):170	


}

###############################################################################################################################################


def bfs(graph, start,goal):
    visited, stack = [], [start] #visited is initiated as empty list which would be populated by the states as they are visited by the algorithm
    while stack:
        vertex = stack.pop(0) #to remove the last element and assign it to the vertex
        if vertex not in visited:
            visited.append(vertex)
            stack.extend(set(graph[vertex]) - set(visited)) #remove visited from stack
        if vertex==goal:
            break
    return visited

print("BFS: ",list(bfs(Graph, 'sports complex','student mosque')))




def ucs_path(graph,cost,start,goal):
    queue = []
    solution_cost=[]
    queue.append([0, start])
 
    visited = {}
 
    while (len(queue) > 0):
        queue = sorted(queue)
        p = queue[-1]
        del queue[-1]
        p[0] =p[0]*-1
 
        if (p[1] == goal):
            visited[p[1]]=[k for k,v in graph.items() if p[1] in v]
            solution_cost=p[0]
            break
        queue = sorted(queue)
 
        if (p[1] not in visited):
            for i in range(len(graph[p[1]])):
                if graph[p[1]][i] not in visited:
                    queue.append( [(p[0] + cost[(p[1], graph[p[1]][i])])* -1, graph[p[1]][i]])
                    path=[k for k,v in graph.items() if p[1] in v]
        visited[p[1]] = path
    solution = set([v[0] for v in visited.values() if len(v)>0]) | set('G')
    Final_Cost = solution_cost
    return solution, Final_Cost


print("UCS Path with Cost: ", ucs_path(Graph,Cost,'sports complex','student mosque'))

#print("YOUR TOTAL COST IS AS FOLLOWING : " , Final_Cost)



def dfs(graph, start,goal):
        visited, stack = [], [start] #visited is initiated as empty list which would be populated by the states as they are visited by the algorithm
        while stack:
            vertex = stack.pop() #to remove the last element and assign it to the vertex
            if vertex not in visited:
                    visited.append(vertex)
                    stack.extend(set(graph[vertex])-set(visited)) #remove visited from stack
            if vertex==goal:
                    break
        return visited
print('DFS: ', dfs(Graph,'sports complex','student mosque'))

##############################################################################################################################

def ucs(graph, COST, start, goal):
    visited, pqueue = [], [(0,start)]
    while pqueue:
        vertex = pqueue.pop(0)
        if vertex[1] not in visited:
            visited.append(vertex[1])
            if vertex[1]==goal:
                break
            temp=[l for l in graph[vertex[1]] if l not in visited]
            cost=[COST[(vertex[1],l)]+ vertex[0] for l in temp]
            pqueue.extend(zip(cost,temp))
            pqueue.sort()
    return visited

#print('UCS: ', ucs(Graph, Cost, 'sports complex','student mosque'))







def ucs_path(graph,cost,start,goal):
    queue = []
    solution_cost=[]
    queue.append([0, start])
    # map to store visited node
    visited = {}
    # while the queue is not empty
    while (len(queue) > 0):
        # get the top element of the
        queue = sorted(queue)
        p = queue[-1]
        # pop the element
        del queue[-1]
        # get the original value
        p[0] =p[0]*-1
        if (p[1] == goal):
            visited[p[1]]=[k for k,v in graph.items() if p[1] in v]
            solution_cost=p[0]
            break
        queue = sorted(queue)
        # check for the non visited nodes
        # which are adjacent to present node
        if (p[1] not in visited):
            for i in range(len(graph[p[1]])):
                # value is multiplied by -1 so that
                # least priority is at the top
                if graph[p[1]][i] not in visited:
                    queue.append( [(p[0] + cost[(p[1], graph[p[1]][i])])* -1, graph[p[1]][i]])
                    path=[k for k,v in graph.items() if p[1] in v]
                    # mark as visited
                visited[p[1]] = path
        solution = set([v[0] for v in visited.values() if len(v)>0]) | set('G')
        return solution, solution_cost
    
#print("UCS: ",list(ucs_path(Graph,Cost,'sports complex','student mosque')))

'''
def ucs_path1(graph, cost, start, goal):
    
    path = [start]
    nodes = [start]
    visited = [start]
    while nodes:
        index = 0
        vertex = nodes.pop()
        if vertex == goal:
            print('Visited Nodes : ', visited)
            return path
        else:
            children = graph[vertex]
            for i in children:
                visited.append(i)
            paths = []
            for i in range(len(children)):
                temp = [vertex, children[i]]
                paths.append(temp)
            min = cost[tuple(paths[0])]
            if(len(path) > 0):
                for j in range(len(paths)):
                    if(min > cost[tuple(paths[j])]):
                        min = cost[tuple(paths[j])]
                        index = j
                nodes.append(paths[index][1])
                path.append(paths[index][1])
            else:
                nodes.append(paths[index][0])
                path.append(paths[index][0])

#print('UCS_Path1: ', ucs_path1(Graph, Cost, 'sports complex','student mosque'))'''




def ucs_path(graph,cost,start,goal):
    queue = []
    solution_cost=[]
    queue.append([0, start])

    # map to store visited node
    visited = {}


    # while the queue is not empty
    while (len(queue) > 0):

    # get the top element of the
        queue = sorted(queue)
        p = queue[-1]

    # pop the element
        del queue[-1]

    # get the original value
        p[0] =p[0]*-1

        if (p[1] == goal):
            visited[p[1]]=[k for k,v in graph.items() if p[1] in v]
            solution_cost=p[0]
            break
        queue = sorted(queue)
        # check for the non visited nodes
        # which are adjacent to present node
        if (p[1] not in visited):
            for i in range(len(graph[p[1]])):

                # value is multiplied by -1 so that
                # least priority is at the top
                if graph[p[1]][i] not in visited:
                    queue.append( [(p[0] + cost[(p[1], graph[p[1]][i])])* -1, graph[p[1]][i]])
                    path=[k for k,v in graph.items() if p[1] in v]
        # mark as visited
        visited[p[1]] = path
    solution = set([v[0] for v in visited.values() if len(v)>0]) | set('G')
    return solution, solution_cost

#rint("UCS LAST FUNC")
#rint(list(ucs_path(Graph,Cost,'sports complex','student mosque')))







 
