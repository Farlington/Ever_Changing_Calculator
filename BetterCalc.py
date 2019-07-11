# V intro V
print('ᕦ( ͡° ͜ʖ ͡°)ᕤ  Hello User, (ง ͠° ͟ل͜ ͡°)ง')
print('     V  Enter data to begin;  V')

# V Where all the numbers are saved. V
list_stuff = []

# V This part is for entering the numbers that become the average that the user needs. V
def input_num():
   n = int(input('Input data here: '))
   list_stuff.append(n)
input_num()

# V This part gives you the option to put in more numbers. V 
def option():
   global opt
   opt = input('Do you wish to input another number? (y/n) ').upper()
option()

# V This part checks and executes option. V
def opt_lop():
   while opt == 'Y':
     input_num()
     option()
   if opt.upper() == 'N':
     add = sum(list_stuff)
     div = len(list_stuff)
     print('Your average is:')
     print(add / div)
   else:
     print('( ✧≖ ͜ʖ≖) Error: Invalid input (╯ ͠° ͟ʖ ͡°)╯┻━┻')
     option()
     opt_lop()
opt_lop()

# V This part gives you the option to restart. V
def restart():
   list_stuff.clear()
   global res
   res = input('Would you like to average again? (y/n) ').upper()
restart()

# V This is the part that checks and executes restart. V
def ending():
   while res == 'Y':
     print('    V  Enter data to begin again;  V')
     input_num()
     option()
     opt_lop()
     restart()
   if res.upper() == 'N':
     print('( ͡° ͜ʖ ͡°)  See you around then. ( ͡~ ͜ʖ ͡°)')
   else:
     print('( ✧≖ ͜ʖ≖) Error: Invalid input (╯ ͠° ͟ʖ ͡°)╯┻━┻')
     restart()
     ending()
ending()