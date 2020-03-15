class Temperature():
    def __init__(self,fahrenite = 32):
        self.fahrenite=fahrenite
        self.celsius=self.convert_to_celsius(fahrenite)

    def convert_to_celsius(self, f):
        return "Converted to celsius:  "+str((f-32) * (5 / 9))

    def convert_to_fahrenite(self, c):
        return "Converted to fahrenite:  "+str((c * (5 / 9)) + 32)

    def set_fahrenite(self, value):
        self._fahrenite = value
        self._celsius = self.convert_to_celsius(value)
        print(self._celsius)

    def set_celsius(self, value):
        self._fahrenite = self.convert_to_fahrenite(value)
        self._celsius = value                                 
        print(self._fahrenite )

    def grt_fahrenite (self):
       return int(self._fahrenite )

    def get_celsius(self):
        return int(self._celsius)

    fahrenite = property(get_fahrenite , set_fahrenite )
    celsius = property(get_celsius, set_celsius)


t=Temperature
t.set_fahrenite(37)
t.set_celsius(23)
print("Given   fahrenite : ",t.get_fahrenite())                                                
print("Given celsius : ",t.get_celsius())                                               
                                               

                                             
        
    

     
