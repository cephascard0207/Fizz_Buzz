#FizzBuzz
#Created by Cephas Cardozo
#Developed using Python

#welcome_print
print("FizzBuzz")
print("Created By Cephas Cardozo")
print("Developed using Python\n")

#for_loop
for number in range(1, 101):
  #conditionals
  if number % 3 == 0 and number % 5 == 0:
    #print_statement
    print("FizzBuzz")
  elif number % 3 == 0:
    #print_statement
    print("Fizz")
  elif number % 5 == 0:
    #print_statement
    print("Buzz")
  else:
    #print_statement
    print(number)
#end_of_program