# 字符串常用内置函数

# 1. len() 计算字符串长度
string = "hello world"
print(len(string))  # 11

# 2. lower() 转换为小写
string = "HELLO WORLD"
print(string.lower())  # hello world

# 3. upper() 转换为大写
string = "hello world"
print(string.upper())  # HELLO WORLD

# 4. replace() 替换字符串
string = "hello world"
print(string.replace("l", "L"))  # heLLo WorLd

# 5. split() 分割字符串
string = "hello world"
print(string.split())  # ['hello', 'world']
# 也可以指定分隔符
string = "hello,world"
print(string.split(","))  # ['hello', 'world']

# 6. join() 连接字符串
string = "-".join(["hello", "world"])
print(string)  # hello-world
# 也可以指定分隔符
string = ",".join(["hello", "world"])
print(string)  # hello,world

# 7. strip() 去除字符串两端的空白字符
string = "  hello world  "
print(string.strip())  # hello world
# 也可以指定去除的字符
string = "##hello##world##"
print(string.strip("##"))  # hello##world##

# 8. lstrip() 去除字符串左侧的空白字符
string = "  hello world  "
print(string.lstrip())  # hello world 

# 9. rstrip() 去除字符串右侧的空白字符
string = "  hello world  "
print(string.rstrip())  #  hello world

# 10. find() 查找子字符串的位置
string = "hello world"
print(string.find("l"))  # 2
# 也可以指定起始位置
print(string.find("l", 3))  # 3

# 11. rfind() 从右侧查找子字符串的位置
string = "hello world"
print(string.rfind("l"))  # 9
# 也可以指定起始位置
print(string.rfind("l", 3))  # 9

# 12. index() 查找子字符串的位置，如果没有找到，会抛出异常
string = "hello world"
print(string.index("l"))  # 2
# 也可以指定起始位置
print(string.index("l", 3))  # 3

# 13. rindex() 从右侧查找子字符串的位置，如果没有找到，会抛出异常
string = "hello world"
print(string.rindex("l"))  # 9
# 也可以指定起始位置
print(string.rindex("l", 3))  # 9

# 14. count() 计算子字符串出现的次数
string = "hello world"
print(string.count("l"))  # 3
# 也可以指定起始位置和结束位置
print(string.count("l", 3, 7))  # 1

# 15. startswith() 判断字符串是否以指定字符串开头
string = "hello world"
print(string.startswith("he"))  # True
# 也可以指定起始位置
print(string.startswith("he", 1))  # False

# 16. endswith() 判断字符串是否以指定字符串结尾
string = "hello world"
print(string.endswith("ld"))  # True
# 也可以指定起始位置
print(string.endswith("ld", 8))  # False

# 17. isalnum() 判断字符串是否由字母和数字组成
string = "hello123"
print(string.isalnum())  # True
string = "hello world"
print(string.isalnum())  # False

# 18. isalpha() 判断字符串是否只由字母组成
string = "hello"
print(string.isalpha())  # True
string = "hello123"
print(string.isalpha())  # False

# 19. isdigit() 判断字符串是否只由数字组成
string = "123456"
print(string.isdigit())  # True
string = "hello world"
print(string.isdigit())  # False

# 20. islower() 判断字符串是否只由小写字母组成
string = "hello world"
print(string.islower())  # False
string = "hello world".lower()
print(string.islower())  # True

# 21. isupper() 判断字符串是否只由大写字母组成
string = "HELLO WORLD"
print(string.isupper())  # False
string = "HELLO WORLD".upper()
print(string.isupper())  # True

# 22. isspace() 判断字符串是否只由空白字符组成
string = "   "
print(string.isspace())  # True
string = "hello world"
print(string.isspace())  # False

# 23.capitalize() 首字母大写
string = "hello world"
print(string.capitalize())  # Hello world

# 24. title() 每个单词的首字母大写
string = "hello world"
print(string.title())  # Hello World

#26.center() 字符串居中
string = "hello world"
print(string.center(20, "*"))  # ********hello world*********

#27. bytes.decode() 解码字节为字符串
bytes_str = b"hello world"
print(bytes_str.decode())  # hello world
print(bytes_str.decode("utf-8"))  # hello world

#28. encode() 编码字符串为字节  
string = "hello world"
print(string.encode())  # b'hello world'

#29. format() 格式化字符串
string = "hello {}"
print(string.format("world"))  # hello world

#30. isnumeric() 判断字符串是否只由数字组成
string = "123456"
print(string.isnumeric())  # True
string = "hello world"
print(string.isnumeric())  # False

#31. swapcase() 大小写互换
string = "HeLLo WoRLD"
print(string.swapcase())  # hEllO wOrld

#32. zfill() 字符串左侧填充0
string = "123"
print(string.zfill(5))  # 000123