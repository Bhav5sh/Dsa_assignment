def remove_duplicates(string):
    seen = set()     
    result = []   
    
    for char in string:
        if char not in seen:
            seen.add(char)
            result.append(char)
    
    return ''.join(result)


input_str = "aryacollegearya"
output_str = remove_duplicates(input_str)
print("Output:", output_str)
