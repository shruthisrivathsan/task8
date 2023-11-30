#create class TV with constructors parametersbrand, price, size and status

class TV:
    def __init__(self,brand, price, size, status):
        self.brand = brand
        self.price = price
        self.size = size
        self.status()
        self.reset()

    #define the reset function that has the default values of channel and volume
    def reset(self, channel, volume):
        self.channel = 1
        self.volume = 50
        
    
    #define a function that increases the volume by 1 if volume < 100
    def increase_volume(self):
        if self.volume !=100:
            self.volume += 1
    #define a function that decreases the volume by 1 if volume > 100
    def decrease_volume(self):
        if self.volume != 0:
            self.volume -=1

    #define a function that takes in the channel number and displays the 
    #current channel
    def set_channel(self, channelnumber):
        self.channelnumber = channelnumber
        current_channel = self.channel
        if channelnumber > self.channel:
            channelnumber.display(self)

    #define a function to retun the status of the tv
    def status(self, brand, channel, volume):
        self.brand = brand
        self.channel = channel
        self.volume = volume
        return (f"{self.brand} at channel {self.channel}, volume{self.volume}")
     
    # display function to display the brand, size, channel, volume and status
    def display(self):
        print(f" Brand: {self.brand} /n Size: {self.size} /n Channel: {self.channel} /n Status : {self.status} /n Volume : {self.volume}")


# create subclass LedTV with attributes screen_thickness, 
# energy_usage, lifespan, refresh_rate
class LedTV(TV):
    def __init__(self, screen_thickness, energy_usage, lifespan, refresh_rate):
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate

    # display the screen thickness,energy consumption, lifespan and refresh rate of the TV 
    def display2(self):
        print(f" Screen thickness: {self.screen_thickness} /n Energy_usage: {self.energy_usage} /n Lifespan = {self.lifespan} /n Refresh_rate:{self.refresh_rate}")


# create subclass LedTV with attributes viewing angle,backlight
# displays all the features and functions of the tv
class PlasmaTV(TV):
    def __init__(self, viewing_angle, backlight, display_details):
        self.viewing_angle = viewing_angle
        self.backlight = backlight
        self.displaydetails()
        
    def displaydetails(self):
        self.display()
        self.display2()
        print(f" Viewing angle: {self.viewing_angle} /n Blacklight: {self.backlight}")

#objects created to call the classes and display the details
tv_details = TV()
led_details = LedTV()
plasma_details = PlasmaTV()
plasma_details.displaydetails()