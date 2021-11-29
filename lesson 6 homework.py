text = input("Введіть текст: ")
text_str = text.split(' ')
maxLen = 0
letter = ""
count = 0
for i in text_str:
    if len(text_str[count]) > maxLen:
         maxLen = len(text_str[count])
         letter = i
    count += 1
print(f"Слово {letter} має найбільшу довжину {maxLen} символів")
