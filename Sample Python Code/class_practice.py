class Lightbulb:
    def __init__(self, wattage=0, is_led=False, brand_name="", is_on=False, brightness=0):
        print("init method is invoked")
        self.wattage = wattage
        self.is_led = is_led
        self.brand_name = brand_name
        self.is_on = is_on
        self.brightness = brightness

    def turn_on(self):
        self.is_on = True
        print("lightbulb is now on")

    def turn_off(self):
        self.is_on = False
        print("lightbulb is now off")

    def to_string(self):
        print(self.brand_name)

    def set_brightness(self, brightness):
        self.brightness = brightness
        print("brightness has been set to ", brightness)


# creating a new object and passing values for the attributes
a_object = Lightbulb(10, True, "A34 Lightbulb", True, 26)

# calling the afoo() method from a_obj
a_object.turn_on()
