from random import randrange

def task_enter():
    print(f'Task #{__name__[4:]}.')
    while True:
        int_num = input("Enter positive integer number or '/break' to change task: ")
        if int_num == '/break':
            return
        elif input_valid_condition(int_num):
            task_basic_func(int_num)
        else:
            print("Invalid integer. Try again.")
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def input_valid_condition(input_data):
    return int(input_data) > 0
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def task_basic_func(in_data):
    k = int(in_data)
    min_coef = 0
    max_coef = 100
    coef = randrange(1, max_coef + 1)
    with open('t4.txt', 'w') as fl:
        if coef == 1:
            fl.write(f"x^{k} ")
        else:
            fl.write(f"{coef}*x^{k} ")
    with open('t4.txt', 'a') as fl:
        for i in range(1, k):
            coef = randrange(min_coef, max_coef + 1)
            if coef == 1:
                fl.write(f"+ x^{k - i} ")
            elif coef != 0:
                fl.write(f"+ {coef}*x^{k - i} ")
            


        coef = randrange(min_coef, max_coef + 1)
        if coef != 0:
            fl.write(f"+ {coef} ")
        fl.write('= 0')
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------

