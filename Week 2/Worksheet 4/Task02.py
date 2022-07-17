class Car:
    def __init__(self, max_speed, max_occupants):
        self.__occupants = 0
        self.__speed = 0
        self.__max_speed = max_speed
        self.__max_occupants = max_occupants

    def accelerate(self):
        if self.__speed + 10 <= self.__max_speed:
            self.__speed += 10
            print("Car accelerated to:", self.__speed)
        else:
            print("Max speed:", self.__max_speed, "already achieved.")

    def decelerate(self):
        if self.__speed - 10 >= 0:
            self.__speed -= 10
            print("Car decelerated to:", self.__speed)
        else:
            print("Vehicle already stopped.")

    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        if speed > self.__max_speed:
            speed = self.__max_speed
            print("Maximum speed reached")
        if speed < self.__speed:
            print("Car decelerated to:", speed)
        elif speed > self.__speed:
            print("Car accelerated to:", speed)
        else:
            print("Car has still the same speed as before")
        self.__speed = speed

    def get_max_speed(self):
        return self.__max_speed

    def set_max_speed(self, max_speed):
        if max_speed < self.__max_speed:
            print("Engine downgraded successfully to", max_speed, "max speed.")
        elif max_speed > self.__max_speed:
            print("Engine upgraded successfully to", max_speed, "max speed.")
        else:
            print("Nothing changed.")
        self.__max_speed = max_speed

    def get_occupants(self):
        print("Now, there is:", self.__occupants, "occupants in the car")
        return self.__occupants

    def set_occupants(self, occupants):
        if occupants > self.__max_occupants:
            occupants = self.__max_occupants
        if occupants < self.__occupants:
            print(self.__occupants - occupants, "occupants has left the car")
        elif occupants > self.__occupants:
            print(occupants - self.__occupants, "occupants has entered the car")
        else:
            print("Occupants just switched places inside the car")
        self.__occupants = occupants

    def get_max_occupants(self):
        return self.__max_occupants

    def set_max_occupants(self, max_occupants):
        if max_occupants < self.__max_occupants:
            print("Successfully unmount", self.__max_occupants - max_occupants, "seats from the car")
            if self.__occupants > max_occupants:
                print("We had to throw out", self.__occupants - max_occupants, "occupants")
        elif max_occupants > self.__max_occupants:
            print("Successfully installed", max_occupants - self.__max_occupants, "new seats")
        else:
            print("Successfully nothing changed")
        self.__max_occupants = max_occupants


mycar = Car(50, 5)
mycar.set_occupants(10)
mycar.accelerate()
mycar.set_speed(50)
mycar.set_occupants(3)
mycar.set_speed(0)
mycar.set_speed(15)
mycar.set_speed(150)
mycar.decelerate()
