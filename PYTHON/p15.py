class Person:
  def _init_(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print("Hi!")

class Student(Person):
  def _init_(self, name, age, major):
    super()._init_(name, age)
    self.major = major

student = Student("Sam", 23, "chemistry")
print(student.major)
student.greet()

