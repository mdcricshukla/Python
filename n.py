def remove_nth_character(input_string, n):
  
    if n<=0 or n>= len(input_string):
        return "Invalid index"

   
    result = input_string[:n] + input_string[n+1:]

    return result


input_string = input('enter the string:')
n = int(input('enter the nth index:'))


output_string = remove_nth_character(input_string, n)
print(output_string)
