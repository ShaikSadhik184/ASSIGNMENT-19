def check_range(num, lower, upper):
    if num >= lower and num <= upper:
        return True
    else:
        return False

print(check_range(5, 1, 10))  # Output: True
print(check_range(15, 1, 10))  # Output: False
