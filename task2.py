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
    num = int(in_data)
    cnt_list = []
    dev = 2
    while (num > 1)  or (dev < num // 2):
        if num % dev > 0:
            dev += 1
        else:
            cnt_list.append(dev)
            num //= dev

    print(f"Factorization result is {cnt_list} for {in_data}.")
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
