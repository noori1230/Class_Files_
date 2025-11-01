class Car:
    def __init__ (self,model,year,color,for_sales):
        self.model = model
        self.year = year
        self.color = color
        self.for_sales = for_sales
    
    def drive (self):
        print ("you drive the car")

    def stop (self):
        print ("you stop the car")