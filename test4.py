def find_del_number(list_numb: set):
    del_numb = set()
    for index in range(1, len(list_numb) + 2):
        if index not in list_numb:
            del_numb.add(index)
    return del_numb

