import random
while(True):
  temp=random.randint(10,99)
  humid=random.randint(10,99)
  print("current temperature:",temp)
  print("current humidity:",humid,"%")
  temp_ref=37
  humid_ref=35
  if temp>temp_ref andhumid<humid_ref:
     print("Sound alarm")
  else:
     print("Sound off")
  break
