with open("/Users/yanghsinhsuanalyssa/Downloads/xi_wang_raw.txt", 'r', encoding="UTF-8") as f:
    rawLIST = f.readlines()
    print(rawLIST)


    # 去除每个元素的换行符
    cleaned_list = [element.strip() for element in rawLIST]

    join_string = ' '.join(cleaned_list)
    
    result_string_without_spaces = join_string.replace(" ", "")
    print(result_string_without_spaces)    
    
    # Input string with spaces
input_string = "result_string_without_spaces"

# Replace spaces with newlines
output_string = input_string.replace("\t", "\n")

# Print the result
print(output_string)
