class Car(object):
    def __init__(self,cartype,model):
        self.type = cartype
        self.model = model

    def isCruiseControlSupported(self):
        import pdb
        pdb.set_trace()
        return True

class Nissan(Car):
    def __init__(self,cartype,model,year):
        Car.__init__(self,cartype,model)
        self.year = year

if __name__ == "__main__":
    cObj = Nissan("Nissan", "Versa", "1997")
    cObj.isCruiseControlSupported()
    print cObj.__dict__
