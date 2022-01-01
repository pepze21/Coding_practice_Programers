# 22:23

combination_of_menu = []

def get_combination(start_range, combination, num_iter, ordered_menu):
    for i in range(start_range, len(ordered_menu)):
        # print('i =', i)
        if num_iter >= 2:
            get_combination(i + 1, combination + ordered_menu[i], num_iter - 1, ordered_menu)
        elif num_iter == 1:
            # print(start_range, combination, num_iter, ordered_menu)
            for j in range(i, len(ordered_menu)):
                # print('ordered_menu =', ordered_menu[j])
                combination_of_menu.append(combination + ordered_menu[j])
            break

def solution(orders, course):
    ALPHABETS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ordered_menu = ''
    for order in orders:
        for menu in order:
            if menu not in ordered_menu:
                ordered_menu += menu  
    # print(ordered_menu)
    get_combination(0, '', 2, ordered_menu)
    print(combination_of_menu)
    # for case in combination_of_menu:
        
    # for i in range(len(ordered_menu)):
    #     for j in range(i + 1, len(ordered_menu)):
    #         ordered_menu[i] + ordered_menu[j]
            # print(i, j)
        # for j in range(i,)