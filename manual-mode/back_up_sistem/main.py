import pygame

import serial

USB_PORT = "/dev/ttyUSB0"

try:
   usb = serial.Serial(USB_PORT, 9600, timeout=2)
except:
   print("ERROR - Could not open USB serial port.  Please check your port name and permissions.")
   print("Exiting program.")
   exit()

class comand():
    def __init__(self) :
        pygame.init()
        window = pygame.display.set_mode((500, 500))
        clock = pygame.time.Clock()

        rect = pygame.Rect(0, 0, 20, 20)
        rect.center = window.get_rect().center
        vel = 5

        run = True
        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    print(pygame.key.name(event.key))
                    
            

            keys = pygame.key.get_pressed()
            
            if keys[pygame.K_UP]:
                usb.write(b'1')
                print("Arduino motor turned on.")
            elif keys[pygame.K_DOWN]:  
                usb.write(b'2')  # send command to Arduino
                print("Arduino motor back.")

            elif keys[pygame.K_RIGHT]:
                usb.write(b'4')  # send command to Arduino
                print("Arduino motor right.")

            elif keys[pygame.K_LEFT]:
                usb.write(b'3')  # send command to Arduino
                print("Arduino motor left.")

            elif keys[pygame.K_KP0 ]:
                usb.write(b'5')  # send command to Arduino
                print("Arduino motor centru.")


            else:
                usb.write(b'0')
                print("motor stopped")
            

            
            
            rect.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * vel
            rect.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * vel
                
            rect.centerx = rect.centerx % window.get_width()
            rect.centery = rect.centery % window.get_height()

            window.fill(0)
            pygame.draw.rect(window, (255, 0, 0), rect)
            pygame.display.flip()

        pygame.quit()
        exit()

comand()

'''USB_PORT = "/dev/ttyUSB0"  # Arduino Uno WiFi Rev2
# Imports
import serial
# Functions
def print_commands():
   """Prints available commands."""
   print("Available commands:")
   print("  a - start motor")
   print("  l - off motor")
   print("  k - Turn off Arduino LED")
   print("  x - Exit program")
# Main
# Connect to USB serial port at 9600 baud
try:
   usb = serial.Serial(USB_PORT, 9600, timeout=2)
except:
   print("ERROR - Could not open USB serial port.  Please check your port name and permissions.")
   print("Exiting program.")
   exit()
# Send commands to Arduino
print("Enter a command from the keyboard to send to the Arduino.")
print_commands()
while True:
   command = input("Enter command: ")
   
   if command == "a":  # turn on Arduino LED
      usb.write(b'on')  # send command to Arduino
      print("Arduino motor turned on.")
   elif command == "l":  # turn off Arduino LED
      usb.write(b'of')  # send command to Arduino
      print("Arduino motor turned off.")
   elif command == "x":  # exit program
      print("Exiting program.")
      exit()
   else:  # unknown command
      print("Unknown command '" + command + "'.")
      print_commands()'''