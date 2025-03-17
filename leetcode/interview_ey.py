def add_1(num):
    if num[-1] != 9:
        num[-1] += 1
        return num

    # [9, 9]
    # [8, 9]
    carry = 1
    new_list = []
    # [1,2,9]
    for i in range(len(num)-1, -1, -1):
        if num[i] == 9:
            carry, val = 1, 0
        else:
            carry, val = 0, num[i] + carry
        new_list.append(val)
    if carry:
        new_list.append(1)
    return new_list[::-1]
