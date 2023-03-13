class Dog:

  def __init__(self,name,age):
    self.name = name
    self.age = age

  def introduce(self):
    return "Hello, my name is " + self.name + " and I am " + str(self.age) + " years old"

  def is_older(self, dog):
    return self.age >= dog.age
    

cujo = Dog("Cujo", 10)
vincent = Dog("Vincent", 5)

print(cujo.introduce())
print(cujo.is_older(vincent))   
