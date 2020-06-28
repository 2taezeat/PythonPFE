def all_add_function(para):
    result = 0
    for n in para:
        result = result + int(n)

    return result



input_numbers = input('더할 수를 여러개 입력 하시오 > ').split()
total = all_add_function(input_numbers)
print(total)
