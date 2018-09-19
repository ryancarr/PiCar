import pygame
import RPi.GPIO as gpio

#Associate pin numbers with direction
rightForward  = 11
rightBackward = 13
leftForward   = 15
leftBackward  = 16

# Set minimum joystick threshold for movement
threshold = 0.6

def init():
    #setup GPIO using board numbering
    gpio.setmode(gpio.BOARD)

    gpio.setup(rightForward, gpio.OUT)
    gpio.setup(rightBackward, gpio.OUT)
    gpio.setup(leftForward, gpio.OUT)
    gpio.setup(leftBackward, gpio.OUT)

def backward():
    gpio.output(leftBackward, gpio.HIGH)
    gpio.output(leftForward, gpio.LOW)
    gpio.output(rightBackward, gpio.HIGH)
    gpio.output(rightForward, gpio.LOW)

def forward():
    gpio.output(leftBackward, gpio.LOW)
    gpio.output(leftForward, gpio.HIGH)
    gpio.output(rightBackward, gpio.LOW)
    gpio.output(rightForward, gpio.HIGH)

def left():
    gpio.output(leftBackward, gpio.HIGH)
    gpio.output(leftForward, gpio.LOW)
    gpio.output(rightBackward, gpio.LOW)
    gpio.output(rightForward, gpio.HIGH)

def right():
    gpio.output(leftForward, gpio.HIGH)
    gpio.output(leftBackward, gpio.LOW)
    gpio.output(rightForward, gpio.LOW)
    gpio.output(rightBackward, gpio.HIGH)    

def stop():
    gpio.output(leftForward, gpio.LOW)
    gpio.output(leftBackward, gpio.LOW)
    gpio.output(rightForward, gpio.LOW)
    gpio.output(rightBackward, gpio.LOW)

# Initialize the GPIO pins on the board
init()
# Initialize the pygame library
pygame.init()

# Connect the first JoyStick
joy = pygame.joystick.Joystick(0)
joy.init()

keepLooping = True
while keepLooping:
    events = pygame.event.get()
    for event in events:
        # Check if a button has been pressed
        if event.type == pygame.JOYBUTTONDOWN:
            # If start button is pressed exit
            if joy.get_button(3):
                keepLooping = False
            # If DPAD Up
            if joy.get_button(4):
                forward()
            if joy.get_button(5):
                right()
            if joy.get_button(6):
                backward()
            if joy.get_button(7):
                left()

        if event.type == pygame.JOYBUTTONUP:
            stop()


# Stop and cleanup GPIO
print "Stopping motors."
stop()
print "Cleaning up GPIO"
gpio.cleanup()
joy.quit()