first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(word) for word in first_strings if len(word) > 5]
second_result = [(str1, str2) for str1 in first_strings for str2 in second_strings if len(str1) == len(str2)]
third_result = {word: len(word) for word in first_strings+second_strings if len(word) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)