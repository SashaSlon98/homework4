# coding : utf-8

# комментарий 

print("Great Python Programm!!!")
print("Привет, программист!")
name = input("Ваше имя: ")
print(name, ", добро пожаловать в мир Python!")
answer = input("Давайте поработаем? (Да/Нет): ")
if answer == 'Да' or answer == 'да':
        print("Отлично")
        word = str(input("Введите слово: "))
        length = len(word)
        for letter in range(length, 0, -1):
                if word[letter - 1]!= 'з' and word[letter - 1]!= 'я':
                         print( word[letter - 1])

elif answer == 'Нет' or answer == 'нет':
        print("В таком случае, до свидания!")
else:
        print("Неизвестный выбор")
        
input("Конец программы.")

