import sys
import nxt
import usb
import time

class Conveyer:

    def __init__(self, device):

        self.port  = nxt.motor.PORT_A
        self.thrust, self.tacho = 100, 90

        self.motor = nxt.motor.Motor(
            device, self.port
        )

    def _motor_on(self):

        motor_state = self.motor._read_state()
        motor_state = state[0].mode

        return (motor_state == nxt.motor.MODE_MOTOR_ON)

    def _motor_wait(self):

        # Wait for motor mode to change
        while self._motor_on():
            continue

    def left(self):

        self.motor.weak_turn(-self.thrust, self.tacho)
        self._motor_wait()

    def right(self):

        self.motor.weak_turn(self.thrust, self.tacho)
        self._motor_wait()

def main():

    try:
        device = nxt.locator.find_one_brick()
    except nxt.locator.BrickNotFoundError:
        print 'Brick not found'
        sys.exit(1)

    conveyer = Conveyer(device)

    conveyer.left()
    conveyer.right()

if __name__ == '__main__':
    main()
