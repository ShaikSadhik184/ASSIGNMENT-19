def multiply_list(my_list):
    product_num = 1
    for num in my_list:
        product_num *= num
    return product_num

my_list = [1, 2, 3, 4, 5]
print(multiply_list(my_list))  # Output: 120
