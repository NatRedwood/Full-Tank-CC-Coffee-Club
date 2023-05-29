import time
import serial
import pygame
    
pygame.mixer.init() # Initialize PyGame

teaBagsLow = pygame.mixer.Sound("teaBagLow.wav")        # Create a sound object
teaBagsOut = pygame.mixer.Sound("teaBagOut.wav")        # Create a sound object
teaFact1   = pygame.mixer.Sound("teaFact1.wav")         # Create a sound object
teaFact2   = pygame.mixer.Sound("teaFact2.wav")         # Create a sound object
teaFact3   = pygame.mixer.Sound("teaFact3.wav")         # Create a sound object
teaFact4   = pygame.mixer.Sound("teaFact4.wav")         # Create a sound object
teaFact5   = pygame.mixer.Sound("teaFact5.wav")         # Create a sound object
teaFact6   = pygame.mixer.Sound("teaFact6.wav")         # Create a sound object
teaFact7   = pygame.mixer.Sound("teaFact7.wav")         # Create a sound object
teaFact8   = pygame.mixer.Sound("teaFact8.wav")         # Create a sound object

factCounter = 0

# Create a serial object and connect to the Arduino Uno
serialPort = serial.Serial(port = "COM4", baudrate=9600,
                           bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)


# Main program loop
while(1):

    # Wait for some serial data
    if (serialPort.in_waiting > 0):
        serialString = str(serialPort.readline())

        # Check to see if the data is a measurement reading
        stringArray = serialString.split(':')
        
        if((len(stringArray) > 1) and (stringArray[0] == "b'Data")):
            numberOfBags = int(stringArray[1])
            print(str(numberOfBags) + str(" bags remaining"))

            if((numberOfBags > 0) and (numberOfBags < 20)):
                teaBagsLow.play()
            elif(numberOfBags == 0):
                teaBagsOut.play()
            else:
                factCounter += 1
                
                if(factCounter > 7):
                    factCounter = 0

                if(factCounter == 0):
                    teaFact1.play()
                if(factCounter == 1):
                    teaFact2.play()
                if(factCounter == 2):
                    teaFact3.play()
                if(factCounter == 3):
                    teaFact4.play()
                if(factCounter == 4):
                    teaFact5.play()
                if(factCounter == 5):
                    teaFact6.play()
                if(factCounter == 6):
                    teaFact7.play()
                if(factCounter == 7):
                    teaFact8.play()                   
                        
        elif(stringArray[0] == "b'Open"):
            print("Container opened")                
        else:
            print(stringArray[0])
            
        
