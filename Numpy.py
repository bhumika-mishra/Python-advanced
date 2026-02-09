import numpy as np 
data_type = [('Name','S15'),('Class',int),('Height', float)]
student_details = [('James',5,48.5),('Nail',6,52.5),('Paul',5,42.10),('Pit',5,40.11)]
students = np.array(student_details, dtype = data_type)
print("Original Array : ")
print(students)
print("Sort by Height :")
print(np.sort(students, order = 'Height'))