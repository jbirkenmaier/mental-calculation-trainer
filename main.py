import function_library as fl
import random 

choice_1 = input('{:<30} {:<10}\n'
                 '{:<30} {:<10}\n'
                 '{:<30} {:<10}\n'
                 '{:<30} {:<10}\n'.format('For integer addition (+)','enter 1',
                                          'For integer subtraction (-)','enter 2',
                                          'For integer multiplication (*)','enter 3',
                                          'For integer division (/)', 'enter 4'))

if int(choice_1)<=4:
    choice_2_space = input('{:<30} {:<10}\n'
                           '{:<30} {:<10}\n'
                           '{:<30} {:<10}\n'
                           '{:<30} {:<10}\n'
                           '{:<30} {:<10}\n'.format('For numbers from 0 to 100','enter 1',
                                                    'For numbers from 0 to 1000','enter 2',
                                                    'For numbers from 0 to 10000','enter 3',
                                                    'For numbers from 0 to 100000', 'enter 4',
                                                    'For numbers from 0 to 1000000', 'enter 5'))
    
if int(choice_2_space) == 1 and int(choice_1) == 1:
    while True:
        rand_int_1 = random.randint(0,100)
        rand_int_2 = random.randint(0,100)
        user_solution = int(input('%i + %i = ' %(rand_int_1,rand_int_2)))
        solution = int(rand_int_1)+int(rand_int_2)
        print(solution == user_solution, ', the correct solution is: ', solution)

if int(choice_2_space) == 2 and int(choice_1) == 1:
    while True:
        rand_int_1 = random.randint(0,1000)
        rand_int_2 = random.randint(0,1000)
        user_solution = int(input('%i + %i = ' %(rand_int_1,rand_int_2)))
        solution = int(rand_int_1)+int(rand_int_2)
        print(solution == user_solution, ', the correct solution is: ', solution)
        
if int(choice_2_space) == 3 and int(choice_1) == 1:
    while True:
        rand_int_1 = random.randint(0,10000)
        rand_int_2 = random.randint(0,10000)
        user_solution = int(input('%i + %i = ' %(rand_int_1,rand_int_2)))
        solution = int(rand_int_1)+int(rand_int_2)
        print(solution == user_solution, ', the correct solution is: ', solution)

if int(choice_2_space) == 4 and int(choice_1) == 1:
    while True:
        rand_int_1 = random.randint(0,100000)
        rand_int_2 = random.randint(0,100000)
        user_solution = int(input('%i + %i = ' %(rand_int_1,rand_int_2)))
        solution = int(rand_int_1)+int(rand_int_2)
        print(solution == user_solution, ', the correct solution is: ', solution)

if int(choice_2_space) == 5 and int(choice_1) == 1:
    while True:
        rand_int_1 = random.randint(0,1000000)
        rand_int_2 = random.randint(0,1000000)
        user_solution = int(input('%i + %i = ' %(rand_int_1,rand_int_2)))
        solution = int(rand_int_1)+int(rand_int_2)
        print(solution == user_solution, ', the correct solution is: ', solution)

if int(choice_2_space) == 1 and int(choice_1) == 2:
    while True:
        rand_int_1 = random.randint(0,100)
        rand_int_2 = random.randint(0,100)
        user_solution = int(input('%i - %i = ' %(rand_int_1,rand_int_2)))
        solution = int(rand_int_1)-int(rand_int_2)
        print(solution == user_solution, ', the correct solution is: ', solution)

if int(choice_2_space) == 2 and int(choice_1) == 2:
    while True:
        rand_int_1 = random.randint(0,1000)
        rand_int_2 = random.randint(0,1000)
        user_solution = int(input('%i - %i = ' %(rand_int_1,rand_int_2)))
        solution = int(rand_int_1)-int(rand_int_2)
        print(solution == user_solution, ', the correct solution is: ', solution)
        
if int(choice_2_space) == 3 and int(choice_1) == 2:
    while True:
        rand_int_1 = random.randint(0,10000)
        rand_int_2 = random.randint(0,10000)
        user_solution = int(input('%i - %i = ' %(rand_int_1,rand_int_2)))
        solution = int(rand_int_1)-int(rand_int_2)
        print(solution == user_solution, ', the correct solution is: ', solution)

if int(choice_2_space) == 4 and int(choice_1) == 2:
    while True:
        rand_int_1 = random.randint(0,100000)
        rand_int_2 = random.randint(0,100000)
        user_solution = int(input('%i - %i = ' %(rand_int_1,rand_int_2)))
        solution = int(rand_int_1)-int(rand_int_2)
        print(solution == user_solution, ', the correct solution is: ', solution)

if int(choice_2_space) == 5 and int(choice_1) == 2:
    while True:
        rand_int_1 = random.randint(0,1000000)
        rand_int_2 = random.randint(0,1000000)
        user_solution = int(input('%i - %i = ' %(rand_int_1,rand_int_2)))
        solution = int(rand_int_1)-int(rand_int_2)
        print(solution == user_solution, ', the correct solution is: ', solution)

if int(choice_2_space) == 1 and int(choice_1) == 3:
    while True:
        rand_int_1 = random.randint(0,100)
        rand_int_2 = random.randint(0,100)
        user_solution = int(input('%i * %i = ' %(rand_int_1,rand_int_2)))
        solution = int(rand_int_1)*int(rand_int_2)
        print(solution == user_solution, ', the correct solution is: ', solution)

if int(choice_2_space) == 2 and int(choice_1) == 3:
    while True:
        rand_int_1 = random.randint(0,1000)
        rand_int_2 = random.randint(0,1000)
        user_solution = int(input('%i * %i = ' %(rand_int_1,rand_int_2)))
        solution = int(rand_int_1)*int(rand_int_2)
        print(solution == user_solution, ', the correct solution is: ', solution)
        
if int(choice_2_space) == 3 and int(choice_1) == 3:
    while True:
        rand_int_1 = random.randint(0,10000)
        rand_int_2 = random.randint(0,10000)
        user_solution = int(input('%i * %i = ' %(rand_int_1,rand_int_2)))
        solution = int(rand_int_1)*int(rand_int_2)
        print(solution == user_solution, ', the correct solution is: ', solution)

if int(choice_2_space) == 4 and int(choice_1) == 3:
    while True:
        rand_int_1 = random.randint(0,100000)
        rand_int_2 = random.randint(0,100000)
        user_solution = int(input('%i * %i = ' %(rand_int_1,rand_int_2)))
        solution = int(rand_int_1)*int(rand_int_2)
        print(solution == user_solution, ', the correct solution is: ', solution)

if int(choice_2_space) == 5 and int(choice_1) == 3:
    while True:
        rand_int_1 = random.randint(0,1000000)
        rand_int_2 = random.randint(0,1000000)
        user_solution = int(input('%i * %i = ' %(rand_int_1,rand_int_2)))
        solution = int(rand_int_1)*int(rand_int_2)
        print(solution == user_solution, ', the correct solution is: ', solution)


if int(choice_2_space) == 1 and int(choice_1) == 4:
    while True:
        rand_int_1 = random.randint(0,100)
        rand_int_2 = random.randint(0,100)
        user_solution = int(input('%i / %i = ' %(rand_int_1,rand_int_2)))
        solution = int(rand_int_1)/int(rand_int_2)
        print(solution == user_solution, ', the correct solution is: %.4f'%solution)

if int(choice_2_space) == 2 and int(choice_1) == 4:
    while True:
        rand_int_1 = random.randint(0,1000)
        rand_int_2 = random.randint(0,1000)
        user_solution = int(input('%i / %i = ' %(rand_int_1,rand_int_2)))
        solution = int(rand_int_1)/int(rand_int_2)
        print(solution == user_solution, ', the correct solution is: %.4f'%solution)
        
if int(choice_2_space) == 3 and int(choice_1) == 4:
    while True:
        rand_int_1 = random.randint(0,10000)
        rand_int_2 = random.randint(0,10000)
        user_solution = int(input('%i / %i = ' %(rand_int_1,rand_int_2)))
        solution = int(rand_int_1)/int(rand_int_2)
        print(solution == user_solution, ', the correct solution is: %.4f'%solution)

if int(choice_2_space) == 4 and int(choice_1) == 4:
    while True:
        rand_int_1 = random.randint(0,100000)
        rand_int_2 = random.randint(0,100000)
        user_solution = int(input('%i / %i = ' %(rand_int_1,rand_int_2)))
        solution = int(rand_int_1)/int(rand_int_2)
        print(solution == user_solution, ', the correct solution is: %.4f'%solution)

if int(choice_2_space) == 5 and int(choice_1) == 4:
    while True:
        rand_int_1 = random.randint(0,1000000)
        rand_int_2 = random.randint(0,1000000)
        user_solution = int(input('%i / %i = ' %(rand_int_1,rand_int_2)))
        solution = int(rand_int_1)/int(rand_int_2)
        print(solution == user_solution, ', the correct solution is: %.4f'%solution)

