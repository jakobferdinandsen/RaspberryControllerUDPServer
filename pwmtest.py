import RPi.GPIO as IO

import time

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


def backward(val):
    in1.ChangeDutyCycle(0)
    in2.ChangeDutyCycle(val)


def forward(val):
    in2.ChangeDutyCycle(0)
    in1.ChangeDutyCycle(val)


while True:
    for x in range(0, 51):
        backward(x)
        time.sleep(0.1)

    for x in range(0, 51):
        backward(50 - x)
        time.sleep(0.1)

    for x in range(0, 51):
        forward(x)
        time.sleep(0.1)

    for x in range(0, 51):
        forward(50 - x)
        time.sleep(0.1)

