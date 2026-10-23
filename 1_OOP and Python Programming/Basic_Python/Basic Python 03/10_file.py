# .csv coma separated value
# .txt text file

# 'w' / 'r' / 'a'
# with open('massage.txt', 'w') as file:
#     file.write("I love you, Python")


# with open('massage.txt', 'a') as file:
#     file.write("I love you, Python")


with open('massage.txt', 'r') as file:
    text = file.read()
    print(text)