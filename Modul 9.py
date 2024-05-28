from termcolor import colored, cprint

print("Program Logo MIT dengan Termcolor")
print("=================================")

# Baris ke-1
def A():
  for i in range (4):
    cprint(" "*2,"red" ,"on_red",end="")
    print(" ",end="")
  cprint(" "*5,"red" ,"on_red",end="")
  print()

#Baris ke-2
def B():
    for i in range(3):
      cprint(" "*2,"red" ,"on_red",end="")
      print(" ", end="")
    print()

#Baris ke-3
def C():
  for i in range(3):
    cprint(" "*2,"red" ,"on_red",end="")
    print(" ", end="")
  cprint(" "*2,"red" ,"on_light_grey",end="")
  print(" ", end="")
  cprint(" "*2,"red" ,"on_red",end="")
  print()

#Baris ke-4 dan 5
def D():
  for i in range (2):
    cprint(" "*2,"red" ,"on_red",end="")
    print(" "*4, end="")
    cprint(" "*2,"red" ,"on_red",end="")
    print(" ",end="")
    cprint(" "*2,"red" ,"on_light_grey",end="")
    print(" ", end="")
    cprint(" "*2,"red" ,"on_red",end="")
    print()  

#Tampilkan fungsi
A()
B()
C()
D()



