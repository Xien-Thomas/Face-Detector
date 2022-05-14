
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

    #update image
    imgbytes = cv2.imencode('.png',frame)[1].tobytes()
    window['-IMAGE-'].update(data = imgbytes)
window.close()