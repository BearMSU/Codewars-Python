def sequence_sum(begin_number, end_number, step):
    #your code here
    if end_number < begin_number:
        return 0
    else:
        return sum(range(begin_number, end_number + 1, step))