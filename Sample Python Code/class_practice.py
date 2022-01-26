class Lightbulb:
    def __init__(self, wattage: int, is_led: bool, brand_name: str, is_on: bool = False, brightness: int = 0):
        self.wattage = wattage
        self.is_led = is_led
        self.brand_name = brand_name
        self.is_on = is_on
        self.brightness = brightness

    def turn_on(self):
        if self.is_on == True:
            print("Lightbulb is already on")
            print(self.is_on)
        else:
            self.is_on = True
            print("lightbulb is now on")
            print(self.is_on)

    def turn_off(self):
        if self.is_on == False:
            print("Lightbulb is already off")
            print(self.is_on)
        else:
            self.is_on = False
            print("lightbulb is now off")
            print(self.is_on)

    def to_string(self):
        print(self.brand_name, self.is_led)

    def set_brightness(self, brightness_level):
        assert 0 <= brightness_level <= 10, 'Level outside bounds'
        self.brightness = brightness_level
        print("brightness has been set to ", brightness_level)


# creating a new object and passing values for the attributes
a_object = Lightbulb(10, True, "A34 Lightbulb")

# calling the afoo() method from a_obj
a_object.turn_on()
a_object.turn_off()
a_object.to_string()
a_object.set_brightness(8)
