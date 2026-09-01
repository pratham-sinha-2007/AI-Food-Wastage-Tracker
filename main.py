from tf_keras.models import load_model  # TensorFlow is required for Keras to work
import cv2  # Install opencv-python
import numpy as np
import pygame
import random
import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()
portsList = []

for one in ports:
    portsList.append(str(one))
    print(str(one))

com = input("Select Com Port for Arduino #: ")

for i in range(len(portsList)):
    if portsList[i].startswith("COM" + str(com)):
        use = "COM" + str(com)
        print(use)

serialInst.baudrate = 9600
serialInst.port = use
serialInst.open()

pygame.init()
screen = pygame.display.set_mode((1050, 600))
pygame.display.set_caption("Food Waste Tracker")
default_background = pygame.image.load('spiderman_default.png')
GradeA_background = pygame.image.load('spiderman_GradeA.png')
GradeB_background = pygame.image.load('spiderman_GradeB.png')
GradeC_background = pygame.image.load('spiderman_GradeC.png')


Close_program = False

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model("keras_Model.h5", compile=False)

# Load the labels
class_names = open("labels.txt", "r").readlines()

# CAMERA can be 0 or 1 based on default camera of your computer
camera = cv2.VideoCapture(1)
camera2 = cv2.VideoCapture(0)

back = 0

while True:
    # Grab the webcamera's image.
    ret, image = camera.read()
    ret2, image2 = camera2.read()

    image2 = cv2.resize(image2, (224, 224), interpolation=cv2.INTER_AREA)
    # Resize the raw image into (224-height,224-width) pixels
    image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)

    # Show the image in a window
    cv2.imshow("Webcam Image", image)
    if back == 0:
        screen.blit(default_background, (0, 0))
    elif back == 1:
        screen.blit(GradeA_background, (0, 0))
    elif back == 2:
        screen.blit(GradeB_background, (0, 0))
    elif back == 3:
        screen.blit(GradeC_background, (0, 0))

    # Make the image a numpy array and reshape it to the models input shape.
    image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

    # Normalize the image array
    image = (image / 127.5) - 1

    # Predicts the model
    prediction = model.predict(image)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Print prediction and confidence score
    #print("Class:", class_name[2:], end="")
    #print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")
    print(class_name[2:])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            Close_program = True
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if class_name[2:] == 'Grade A\n' and np.round(confidence_score * 100) > 55:
                    back = 1
                    command = "TOKEN"
                    serialInst.write(command.encode('utf-8'))
                    print("Grade A")
                if class_name[2:] == 'Grade B and C\n' and np.round(confidence_score * 100) > 75:
                    back = 2
                if class_name[2:] == 'Grade D\n' and np.round(confidence_score * 100) > 75:
                    back = 3
                    a = random.randint(10, 99)
                    cv2.imwrite(r"D:\\Pratham\\Hackverse Hackathon\\converted_keras\\Grade D photos\\"+str(a)+".jpg",image2)
            if event.key == pygame.K_ESCAPE:
                    back = 0
            
    if Close_program == True:
        break
    pygame.display.update()
    

camera.release()
cv2.destroyAllWindows()
