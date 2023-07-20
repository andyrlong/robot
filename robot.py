import RPi.GPIO as GPIO
from gpiozero import Robot
from time import sleep

class Robot:
    def __init__(self):
        self.x = 0
        self.y = 0

        # Set up GPIO pins for motor control
        self.left_motor_pin1 = 4
        self.left_motor_pin2 = 14
        self.right_motor_pin1 = 17
        self.right_motor_pin2 = 18

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.left_motor_pin1, GPIO.OUT)
        GPIO.setup(self.left_motor_pin2, GPIO.OUT)
        GPIO.setup(self.right_motor_pin1, GPIO.OUT)
        GPIO.setup(self.right_motor_pin2, GPIO.OUT)

    def move_forward(self, distance):
        robot.forward()
        print("Moving forward for {} feet".format(distance))
        sleep(1) 
        self.y += distance

    def move_backward(self, distance):
        robot.backward()
        print("Moving backward for {} feet".format(distance))
        sleep(1) 
        self.y -= distance

    def rotate_left(self):
        robot.left()
        print("Rotating left")
        sleep(1)


    def rotate_right(self):
        robot.right()
        print("Rotating right")
        sleep(1)  

    def avoid_object(self):
        self.rotate_left()
        self.move_forward(1)
        self.rotate_right()

    def run_program(self):
        self.move_forward(2)
        self.avoid_object()
        self.move_forward(1)
        self.rotate_right()
        self.move_forward(1)
        self.rotate_left()
        self.move_forward(3)
        self.rotate_left()
        self.move_forward(3)

        print("Robot's final position: (x={}, y={})".format(self.x, self.y))

        # Clean up GPIO pins
        GPIO.cleanup()


# Create an instance of the Robot class
robot = Robot()
# Run the program
robot.run_program()