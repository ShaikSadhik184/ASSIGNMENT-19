def find_max(a, b, c, d):
    max_num = a
    if b > max_num:
        max_num = b
    if c > max_num:
        max_num = c
    if d > max_num:
        max_num = d
    return max_num

print(find_max(10, 20, 5, 30))  # Output: 30
