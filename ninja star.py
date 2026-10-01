numbers = [14, 7, 92, 3, 58, 21, 76]

largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num

print("Array:", numbers)
print("Largest number:", largest)