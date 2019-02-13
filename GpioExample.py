# A easy Gpio library example for the Udoo Neo created by David Smerkous
# The current things this library can do

# digitalWriting/Reading - Soon to come PWM

from neo import Gpio  # import Gpio library
from time import sleep  # import sleep to wait for blinks

neo = Gpio()  # create new Neo object

pinTwo = 24    # pin to use S0
pinThree = -3  #I don't know
pinFour = 25    # pin to use S1
pinFive = 26    # pin to use S2
pinSix = 27  # pin to useS3


neo.pinMode(pinTwo, neo.OUTPUT)  # Use innerbank pin 2 and set it as output either 0 (neo.INPUT) or 1 (neo.OUTPUT)
neo.pinMode(pinFour, neo.INPUT)  # Use pin three(innerbank) and read set state to read

# Blink example
for a in range(0, 10):  # Do for five times
    neo.digitalWrite(pinFour ,neo.HIGH)  # write high value to pin
    neo.digitalWrite(pinSix, neo.HIGH)
    sleep(0.1)  # wait one second

    neo.digitalWrite(pinFour,neo.LOW)  # write low value to pin
    neo.digitalWrite(pinSix, neo.Low)
    sleep(0.1)  # wait one second

    neo.digitalWrite(pinTwo, neo.HIGH)  # write high value to pin
    neo.digitalWrite(pinSix, neo.HIGH)
    sleep(0.1)  # wait one second

    neo.digitalWrite(pinTwo, neo.LOW)  # write low value to pin
    neo.digitalWrite(pinTwo, neo.LOW)
    sleep(0.1)  # wait one secondneo.digitalWrite(pinTwo, pinSix, neo.HIGH)  # write high value to pin

    neo.digitalWrite(pinTwo, neo.HIGH)
    neo.digitalWrite(pinFour, neo.HIGH)
    neo.digitalWrite(pinFive, neo.HIGH)
    neo.digitalWrite(pinSix, neo.HIGH)

    sleep(0.1)  # wait one second



# Read pin
print("Current pin(" + str(pinThree) + ") state is: " + str(neo.digitalRead(
    pinThree)))  # read current value of pinThree(To succesfully read a pin it must be either pulled to ground or 3.3v, a non connected wire will not work)

