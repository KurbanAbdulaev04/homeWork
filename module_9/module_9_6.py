def all_variants(text):
    for j in range(len(text)):
        for i in range(j+1, len(text)+1):
            yield text[j:i]


a = all_variants("abc")
for i in a:
    print(i)