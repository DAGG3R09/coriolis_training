from Q1_max import  max2

def max_list(list):
    if list == []:
        return

    max = list[0]

    for l in list[1:]:
        max = max2(max, l)

    return max

if __name__ == "__main__":
    print(max_list([1,2,3,4,5,6]))
    print(max_list([6, 23, 4, 1, 5, 10]))
    print(max_list([23, 4, 1, 5, 10]))