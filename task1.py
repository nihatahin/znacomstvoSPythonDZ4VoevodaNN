def task_enter():
    print(f'Task #{__name__[4:]}.')
    while True:
        d = input("Enter accurcy meaning (example: 0.001) or '/break' to change task: ")
        if d == '/break':
            return
        elif input_valid_condition(d):
            task_basic_func(d)
        else:
            print("Invalid value. Try again.")
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def input_valid_condition(input_data):
    if 0.1 >= float(input_data) > 0:
        cnt = 0
        for i in range(len(input_data)):
            if input_data[i].isdigit():
                dgt = int(input_data[i])
                if (dgt == 0):
                    continue
                elif (dgt == 1):
                    cnt += 1
                    continue
                else:
                    return False
        else:
            return not(cnt > 1)
    else:
        return False
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def task_basic_func(in_data):
    dens = float(in_data)
    cnt = 1
    cur_pi = 4 * sum_mem(0)
    first_pi = cur_pi
    while True:
        cur_pi += 4 * sum_mem(cnt)
        if int(first_pi / dens) != int(cur_pi / dens):
            cnt += 1
            first_pi = cur_pi
        else:
            break
    print(f"Your pi number is {str(first_pi)[ : (len(in_data))]}")
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def sum_mem(n):
    return ((-1)**n) / (2 * n + 1)
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------