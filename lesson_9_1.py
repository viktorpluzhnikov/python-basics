from time import sleep
class TrafficLight:

    __color = "color"

    def running(self):
        while True:
            print("red")
            sleep(7)
            print("yellow")
            sleep(2)
            print("green")
            sleep(5)
            return

trafficlight = TrafficLight()
trafficlight.running()

