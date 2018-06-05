
def sum_of_list(list):
    result = 0

    for element in list:
        result += element
    return result


def product_of_list(list):
    result = 1

    for element in list:
        result *= element
    return result


if __name__ == "__main__":
    l = [1, 2, 3, 4, 5]

    print(l)
    print("Sum of list is:", sum_of_list(l))
    print("Product of list is:", product_of_list(l))
