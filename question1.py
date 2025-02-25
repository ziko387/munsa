class car:
     def __init__(self,brand,model,year):
         self.brand = brand
         self.model = model
         self.year = year
     def display_info(self,brand,model,year):
         print("Brand:",brand,"Model:",model,"Year:",year)
vehicle1=car("ford","f5",int(1903))
vehicle1.display_info("ford","f5",int(1903))
vehicle2=car("toyota","m3",int(1904))
vehicle2.display_info("toyota","m3",int(1904))

