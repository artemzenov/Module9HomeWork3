first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (
    len(first_elem) - len(second_elem)
    for first_elem, second_elem in zip(first, second)
    if len(first_elem) != len(second_elem)
    )

second_result = (
    len(first[i_index]) == len(second[i_index])
    for i_index in range(min(len(first), len(second)))
    )

print(list(first_result))
print(list(second_result))
