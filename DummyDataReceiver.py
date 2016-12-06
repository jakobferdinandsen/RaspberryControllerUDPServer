import RPi.GPIO as IO
import socket
import dataformatter

# RECEIVER SETUP
UDP_IP = "192.168.43.234"
UDP_PORT = 5555

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
formatter = dataformatter.JoystickDataPacketTranslator()

# ENGINE CONTROL SETUP
IO.setwarnings(False)

IO.setmode(IO.BCM)

IO.setup(9, IO.OUT)  # IN_1
IO.setup(8, IO.OUT)  # IN_2
IO.setup(7, IO.OUT)  # INH_1
IO.setup(11, IO.OUT)  # INH_2

in1 = IO.PWM(9, 500)
in2 = IO.PWM(8, 500)
inh1 = IO.PWM(7, 500)
inh2 = IO.PWM(11, 500)
in1.start(0)
in2.start(0)
inh1.start(100)
inh2.start(100)

# WHEEL POS CONTROL
servoPIN12 = 18
move1 = 0
IO.setup(servoPIN12, IO.OUT)
wheelPWM = IO.PWM(servoPIN12, 50)
wheelPWM.start(5)

# FUNCTIONS

def backward(val):
    in1.ChangeDutyCycle(0)
    in2.ChangeDutyCycle(val)


def forward(val):
    in2.ChangeDutyCycle(0)
    in1.ChangeDutyCycle(val)


def wheelpos(val):
    turnValue = val
    if turnValue > 0 and turnValue <= 32:
        # drej 1 tak til hoejre
        x = 6
        wheelPWM.ChangeDutyCycle(x)

    if turnValue > 32 and turnValue <= 64:
        # drej 2 tak til hoejre
        x = 7
        wheelPWM.ChangeDutyCycle(x)

    if turnValue > 64 and turnValue <= 96:
        # drej 3 tak til hoejre
        x = 8
        wheelPWM.ChangeDutyCycle(x)

    if turnValue > 96:
        # drej 4 tak til hoejre
        x = 9
        wheelPWM.ChangeDutyCycle(x)

    if turnValue > -32 and turnValue < 32:
        # 5 = lige ud
        x = 5
        wheelPWM.ChangeDutyCycle(x)

        # Til venstre
    if turnValue < 0 and turnValue >= -32:
        # drej 1 tak til venstre
        x = 4
        wheelPWM.ChangeDutyCycle(x)

    if turnValue < -32 and turnValue >= -64:
        # drej 2 tak til venstre
        x = 3
        wheelPWM.ChangeDutyCycle(x)

    if turnValue < -64 and turnValue >= -96:
        # drej 3 tak til venstre
        x = 2
        wheelPWM.ChangeDutyCycle(x)

    if turnValue < -96:
        # drej 4 tak til venstre
        x = 1
        wheelPWM.ChangeDutyCycle(x)




while True:
    data, addr = sock.recvfrom(1024)
    formatter.interpretDataString(data)

    if formatter.l2 == -1:
        forward((formatter.r2+1)*10)

    if formatter.r2 == -1:
        backward((formatter.l2+1)*10)

    wheelpos(formatter.l3x)

