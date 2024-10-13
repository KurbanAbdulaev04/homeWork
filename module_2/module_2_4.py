numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primers = []
not_primers = []

for i in numbers:
    is_prime = True
    if i > 1:
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
    else:
        is_prime = False

    if i == 1:
        pass
    elif is_prime:
        primers.append(i)
    else:
        not_primers.append(i)

print(primers)
print(not_primers)