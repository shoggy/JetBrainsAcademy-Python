def list_sum(some_list):
    if some_list == []:
        return 0
    if len(some_list) == 1:  # base case
        return some_list[0]
    return some_list[0] + list_sum(some_list[1:])
