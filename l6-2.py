class road:
   
    def __init__(self,lenght,width) :
        self._length = lenght
        self._width = width
    

    def mass(self,weight,thickness):
        massa = self._length * self._width * weight * thickness
        print("Масса асфальта составляет {}".format(massa))
a = road(1000,30)
a.mass(26,5)