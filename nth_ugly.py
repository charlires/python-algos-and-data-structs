def nth_ugly_number(n):
    ugly_numbers = [1]  # The first ugly number is 1
    i2 = i3 = i5 = 0  # Pointers for the multiples of 2, 3, and 5

    while len(ugly_numbers) < n:
        next_ugly = min(ugly_numbers[i2] * 2, ugly_numbers[i3] * 3, ugly_numbers[i5] * 5)
        ugly_numbers.append(next_ugly)

        # Update the pointers based on the selected multiple
        if next_ugly == ugly_numbers[i2] * 2:
            i2 += 1
        if next_ugly == ugly_numbers[i3] * 3:
            i3 += 1
        if next_ugly == ugly_numbers[i5] * 5:
            i5 += 1
    print(ugly_numbers)
    return ugly_numbers[-1]

# Example usage:
n = 10
result = nth_ugly_number(n)
print(f"The {n}th ugly number is: {result}")