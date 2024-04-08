def is_anonims(str1, str2):
    if len(str1) != len(str2):
        return False

    str_list = list(str1)
    for char in str2:
        if char in str_list:
            str_list.remove(char)
        else:
            return False

    return len(str_list) == 0


def tests():
    assert is_anonims('asd', 'asc') == False
    assert is_anonims('asd', 'dsa') == True
    assert is_anonims('aaa', 'aaa') == True


def test2():
    assert is_anonims('wwwaaa', 'aaawww') == False
