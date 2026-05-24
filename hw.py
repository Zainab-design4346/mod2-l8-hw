def get_rightmost_set_bit(n):
    if n == 0:
        return 0
    return n & -n

num = 12
result = get_rightmost_set_bit(num)
print(f"The rightmost set bit value of {num} is: {result}")