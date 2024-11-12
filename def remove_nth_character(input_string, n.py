def remove_nth_character(input_string, n):
   
    if n < 0 or n >= len(input_string):
        return "Invalid index"

    
    result = input_string[:n] + input_string[n+1:]

    return result


input_string = "Hello, World!"
n = 5  # Index of the character to remove


output_string = remove_nth_character(input_string, n)
print(output_string)
