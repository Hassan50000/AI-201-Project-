# OUR AI 201 PROJECT

import pyttsx3
import gtts
from gtts import gTTS


import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Please speak anything:")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("YOU HAVE SPOKEN THE TEXT  :: {}".format(text))
    except:
        print("Sorry we could not recognize what you just said speak again")
        
    sound = "recorded.wav"
    r = sr.Recognizer()
   
   
    with sr.AudioFile(sound) as source:
          r.adjust_for_ambient_noise(source)
          print("Converting Audio To Text : ")
          audio = r.listen(source)
   
    try:
          print("Your Converted Audio Is : \n" + r.recognize_google(audio))
   
   
    except Exception as e:
          print("Error {} : ".format(e) )
          
   
    engine = pyttsx3.init()

    engine.say("welcome to MAP of GIKI... ")
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.5)
    engine.runAndWait()
    
   
    tts = gTTS(text="  TRAVELLING WITH US... ", lang='en')
    tts.save("audiofile.mp3")
    print("Your text has been converted  .. congratulations ")
    
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        print(" Where do you want to travel..")
        audio = r.listen(source)
        print(" Pleease waitt...")

        try:
            print("You have said \n" + r.recognize_google(audio))
            print("Audio Recorded Successfully \n ")


        except Exception as e:
            print("Error :  " + str(e))

    with open("fileaudio.wav", "wb") as f:
            f.write(audio.get_wav_data())  
            
          
# Implementing basic bffs andd dfs through random map as an example andd testing

Graph = {
    'S':('A','D'),
    'A':('B','C'),
    'D':('B','E'),
    'B':('C','E'),
    'E':('G'),
    'C':('G')
}

print(Graph)

Cost = {
    ('S','A'):3,
    ('S','D'):2,
    ('A','B'):5,
    ('A','C'):10,
    ('B','C'):2,
    ('B','E'):1,
    ('D','E'):4,
    ('D','B'):1,
    ('C','G'):4,
    ('E','G'):3
}

print(Cost)

def dfs_paths(Graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(Graph[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))
                
print(list(dfs_paths(Graph, 'S','G')))



print("The individual / possible paths of Depth first Search from start node to goal are : \n ")

paths_dfs = list(dfs_paths(Graph, 'S', 'G'))
for i in paths_dfs:
    temp=0
    
    print(i)
    print(end="  Cost is : ")

    for j in range(len(i)-1):
        temp=temp + Cost[(i[j],i[j+1])]

    print(temp)
    print("\n")
    
    
    
def bfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop(0)
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))
                
                
                
print(list(bfs_paths(Graph, 'S','G')))

print("The individual / possible paths of Breadth first Search from start node to goal are : \n ")

paths_bfs = list(bfs_paths(Graph, 'S', 'G'))


for i in paths_bfs:
    temp=0
    
    print(i)
    print(end="  Cost is : ")

    for j in range(len(i)-1):
        temp=temp + Cost[(i[j],i[j+1])]

    print(temp)
    print("\n")
    
    
    
    
 ''' FURTHER CODE ..... '''
    
    
    
    
 
