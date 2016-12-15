class Student:

    def __init__ (self, name, hometown, age, height, fav_IC):

        self.name=name
        self.hometown=hometown
        self.age=age
        self.height=height
        self.fav_IC=fav_IC

    def print_summary (self):
        print("This is " + str(self.name) + " they are from " + str(self.hometown) + " they are " + str(self.age) + " years old, they are " + str(self.height) + " cm, and they like the most " + str(self.fav_IC) + "ice cream flavor")
    


    def get_giraffe_gap(self):
        x=500-float(self.height)
        print(str(x))
