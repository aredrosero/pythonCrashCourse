class Student:
  
  def __init__(self,name,year):
     self.name = name
     self.year = year
     self.grades = []
     self.attendance = {}
     
  def add_grade(self, grade):
    if type(grade) is Grade:
      self.grades.append(grade)
  def get_average(self):
    if not self.grades:  # Verifica que la lista de calificaciones no esté vacía
      return 0
    total_score = sum(grade.score for grade in self.grades)  # Suma los puntajes de las calificaciones
    average = total_score / len(self.grades)  # Calcula el promedio
    return average
''' def get_average(self):
        self.get_average = (sum(self.grades)/len(self.grades))
        return self.get_average'''

  
class Grade:
  minimum_passing = 65

  def __init__(self, score):
    self.score = score
  def is_passing(self):
        return self.score >= self.minimum_passing
  '''def is_passing(self):
    if self.score >= minimum_passing:
      return True
    elif self.score< minimum_passing:
      return False'''

    


roger = Student("Roger van der Weyden",  10)

sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)


pieter.add_grade(Grade(100))
pieter.add_grade(Grade(75))
pieter.add_grade(Grade(90))

# Obtener el promedio de calificaciones de Pieter
print("Promedio de calificaciones de Pieter:", pieter.get_average())

# Verificar si una calificación es suficiente para aprobar
grade_1 = Grade(75)
print("Es la calificación 75 suficiente para aprobar?", grade_1.is_passing())  # Devuelve True

grade_2 = Grade(50)
print("Es la calificación 50 suficiente para aprobar?", grade_2.is_passing())  # Devuelve False