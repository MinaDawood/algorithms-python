items = ['apple', 'pear', 'orange', 'banana', 'apple',
         'orange', 'apple', 'pear', 'banana', 'orange']

# filter = dict()
# for key in items:
#     filter[key] = 0
# result = set(filter.keys())
# print(result)

# count
counter = dict()
for item in items:
    if (item in counter.keys()):
        counter[item] += 1
    else:
        counter[item] = 1

print(counter)