class employee:
 def __init__(self, id, name, location, salary ):
   self.id = id
   self.name = name
   self.location = location
   self.salary = salary
 def GetEmployee(self):
   print("Employee_ID: " + str(self.id) + " Employee_Name: " + self.name + " Employee_Location: " + self.location + " Employee_Salary: " + str(self.salary))