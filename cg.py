def max_char_count(input_string):
  
    char_count = {}
    

    for char in input_string:
                char_count[char] = char_count.get(char, 0) + 1
    
    
    max_char = max(char_count, key=char_count.get)
    
   
    return max_char, char_count[max_char]


input_string = "AAABBBBccrr"
max_char, count = max_char_count(input_string)
print(f"The character '{max_char}' appears {count} times in the input string.")
