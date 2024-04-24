with open("C:/Users/a0979/Downloads/xi_wang_raw.txt",'r', encoding="UTF-8") as f:
    rawLIST = f.readlines()

    # 去除每个元素的换行符
    cleaned_list = [element.strip() for element in rawLIST]

    join_string = ' '.join(cleaned_list)
    
    result_string_without_spaces = join_string.replace(" ", "")
    print(result_string_without_spaces)    
    
    elements = join_string.split("more")
for element in elements:
    # 去除首尾空格，并打印在不同的行上
    print(element.strip())

    
