
import PySimpleGUI as sg
import cv2

layout = [
    [sg.Image(key = '-IMAGE-')],
    [sg.Text('ppl in pciture: 0', key = '-TEXT-', expand_x = True, justification = 'c')]
]
window = sg.Window('face detector',layout)

video = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:

    event, values = window.read(timeout = 0)
    if event == sg.WIN_CLOSED:
        break

    _,frame = video.read()
    gray =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiscale(
        gray,
        scaleFactor = 1.3,
        minNeighbors = 7,
        minSize = (50,50)
    )
    
    #draw rectangles
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    #update image
    imgbytes = cv2.imencode('.png',frame)[1].tobytes()
    window['-IMAGE-'].update(data = imgbytes)

    #update how many faces
    window['-TEXT-'].update(f'ppl in pciture: {len(faces)}')


window.close()