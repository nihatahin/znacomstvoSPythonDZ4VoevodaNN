def task_enter():
    print(f'Task #{__name__[4:]}.')
    while True:
        list_num = input("Enter list of numbers split with spacebar (example: 0 1 2 3 4 5) or '/break' to change task: ")
        if list_num == '/break':
            return
        elif input_valid_condition(list_num):
            task_basic_func(list_num.split())
        else:
            print("Invalid list. Try again.")
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def input_valid_condition(input_data):
    for i in range(len(input_data)):
        if not(input_data[i].isdigit() or input_data[i] == '.' or input_data[i] == '-' or input_data[i] == ' '):
            return False
    else:
        return True
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def task_basic_func(in_data): 
    reb_dct = {}
    for i in range(len(in_data)):
        in_data[i] = int(in_data[i])
        if type(reb_dct.get(in_data[i])) == int:
            reb_dct[in_data[i]] = reb_dct.get(in_data[i]) + 1
        else:
            reb_dct[in_data[i]] = 1
 #   print(reb_dct)

    not_rep = []
    for k in reb_dct:
        if reb_dct[k] == 1:
            not_rep.append(k)

    print(f"List of unique elements is {not_rep}.")

