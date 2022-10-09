def task_enter():
    print(f'Task #{__name__[4:]}.')
    task_basic_func()
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def task_basic_func():
    with open('t5_1.txt', 'r', encoding='utf-8') as f1:
        poly_str1 = f1.read()
    with open('t5_2.txt', 'r', encoding='utf-8') as f2:
        poly_str2 = f2.read()

    print(poly_str1)
    print(poly_str2)

    
    poly1 = polynom_convertion(poly_str1)
    
    poly2 = polynom_convertion(poly_str2)

    list_fin = []

    for i in range(len(poly1)):
        for j in range(len(list_fin)):
            if poly1[i][0] == list_fin[j][0]:
                list_fin[j][1] = round(list_fin[j][1] + poly1[i][1], 10)
                break
        else:
            list_fin.append(list(poly1[i]))
        
    for i in range(len(poly2)):
        for j in range(len(list_fin)):
            if poly2[i][0] == list_fin[j][0]:
                list_fin[j][1] = round(list_fin[j][1] + poly2[i][1], 10)
                break
        else:
            list_fin.append(list(poly2[i]))


    list_fin = sort_lists_list(list_fin)
    print(list_fin)   
    list_fin_to_str = print_fin_poly(list_fin)
    with open("t5_fin.txt", 'w', encoding='utf-8') as ff:
        ff.write(list_fin_to_str[0])
        print(list_fin_to_str[0], end='')

    with open("t5_fin.txt", 'a', encoding='utf-8') as ff:
        for i in range(1,len(list_fin_to_str)):
            ff.write(list_fin_to_str[i])
            print(list_fin_to_str[i], end='')

    print()

    
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def polynom_convertion(input_data):
    input_data = input_data.replace(' ', '')
    if input_data[-2 : ] != '=0':
        print(f'{input_data} is invalid polynom.')

    terms = term_div(input_data)


    term_list = []
    for i in range(len(terms)):
        term_list.append(term_recon(terms[i]))
    
    return term_list
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def term_div(strochka):
    parts = []
    pos = 0
    while True:
        pos += 1
        if strochka[pos] == '+':
            parts.append(strochka[ : pos])
            strochka = strochka[pos + 1 : ]
            pos = 0
        elif strochka[pos] == '-':
            parts.append(strochka[ : pos])
            strochka = strochka[pos : ]
            pos = 0
        elif strochka[pos] == '=':
            parts.append(strochka[ : pos])
            return parts
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def term_recon(t_str):
    length = len(t_str)
    for i in range(length):
        if t_str[i] == "x":
            coef = 0
            deg = -1
            if  i == 0:
                coef = 1
            elif t_str[i - 1] == '-':
                coef = -1
            else:
                coef = float(t_str[: i - 1])
            #--------
            if i == length - 1:
                deg = 1
            else:
                deg = float(t_str[i + 2 : length])
            
            return (deg, coef)
    else:
        return (0, float(t_str))
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def max_min_deg(cart_list):
    max_deg = cart_list[0][0]
    min_deg = cart_list[0][0]
    for i in range(1, len(cart_list)):
        if max_deg < cart_list[i][0]:
            max_deg = cart_list[i][0]
        elif min_deg > cart_list[i][0]:
            min_deg = cart_list[i][0]
    return (min_deg, max_deg)
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def sort_lists_list(llist):
    for i in range(len(llist)):
        for j in range(len(llist) - 1):
            if llist[j][0] < llist[j + 1][0]:
                temp = llist[j]
                llist[j] = llist[j + 1]
                llist[j + 1] = temp
    return llist
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def print_fin_poly(coef_list):
    list_to_print = []
    for i in range(len(coef_list)):
        if int(coef_list[i][1] * 1000000) != 0:
            if coef_list[i][0] == 0:
                if (coef_list[i][1] > 0) and (i > 0):
                    list_to_print.append("+")
                list_to_print.append(f"{coef_list[i][1]}")
            else:
                if (coef_list[i][1] > 0) and (i > 0):
                    list_to_print.append("+")
                if coef_list[i][1] != 1:
                    list_to_print.append(f"{coef_list[i][1]}*")
                list_to_print.append("x")
                if coef_list[i][0] != 1:
                    list_to_print.append(f"^{coef_list[i][0]}")
    else:
        list_to_print.append("=0")
        return list_to_print
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
