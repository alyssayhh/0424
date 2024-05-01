with open("C:/Users/a0979/OneDrive/文件/xi_wang_raw.txt", 'r', encoding="UTF-8") as f:
    rawdata = f.read()
    
    cleaned_data = rawdata.replace('\n', '').replace(' ', '').replace('\t', '')
    
    
    processed_data = cleaned_data.replace("more", "")
    
import re

def find_and_split(processed_data, keyword):
    # 使用正则表达式找到包含关键词的部分
    matches = re.findall(r"[\w\s’']*[。,，；;！？\n]", processed_data)

    result = []
    for match in matches:
        if keyword in match:
            # 使用逗号、句号和顿号作为分隔符切割文本
            parts = re.split(r"[。,，；;！？\n]", match)
            for part in parts:
                if keyword in part:
                    result.append(part.strip())
    return result

result_list = find_and_split(processed_data, "希望")

# 输出结果
for item in result_list:
    print(item)

    # 要写入的内容
content = item
    
    # 打开文件并写入内容
with open("xi_wang_proccesed.txt", "w") as file:
    file.write(content)    
