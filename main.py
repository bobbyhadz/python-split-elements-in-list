# Split the elements of a list in Python

my_list = ['a-1', 'b-2', 'c-3', 'd-4']

result = [item.split('-', 1)[0] for item in my_list]
print(result)  # 👉️ ['a', 'b', 'c', 'd']