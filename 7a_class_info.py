

class  student :
    def __init__(self,name,age ,sex,course):
      self.name=name
      self.age = age
      self.sex = sex
      self.course = course
      


    def rio(self):
     
      print("name is " + self.name)
      print("age is  is "+ self.age)
      print("sex is "+ self.sex)
      print("course is "+ self.course)


s1= student("rio","20","male","bscit")
s1.rio()
