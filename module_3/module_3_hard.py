data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(data):
    total = 0

    if isinstance(data, str):
        total += len(data)
    elif isinstance(data, int):
        total += data
    elif isinstance(data, (list, set, tuple)):
        for item in data:
            summ = calculate_structure_sum(item)
            total += summ
    elif isinstance(data, dict):
        for key, value in data.items():
            sum_key = calculate_structure_sum(key)
            sum_value = calculate_structure_sum(value)
            total += sum_key + sum_value

    return total


result = calculate_structure_sum(data_structure)
print(result)