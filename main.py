print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill=0

if height >=120:
  print("You can ride the roller coaster")
  age=int(input("Enter your age "))
  if age<12:
    bill=5
    print("Child tickets are $5")
  elif age<=18:
    bill=7
    print("Youth Tickets are $7")
  else:
    bill=12
    print("Adult Tickets are $12")
  wants_photo=input("Do you want a Picture? Y or N ")
  if wants_photo=="Y":
    bill+=3
      
  print(f"Your Final Bill is ${bill}")
      
else:
  print("You are too short to ride the roller coaster")


# number=int(input("Enter a Number? "))

# if number%2==0:
#   print("The number is an even number")
# else:
#   print("The number is an odd number")