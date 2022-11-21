# С клавиатуры вводятся слова через запятую с пробелом. 
# Выведите на экран три наиболее часто встречаемых слова, 
# вместе с количеством этих слов. 
# Количество должно быть отделено от слова двоеточием и пробелом. 
# Каждая пара слово-количество должна быть выведена на отдельной строчке. 
# Для простоты гарантируется, что в строке нет слов с одинаковой встречаемостью.

# Формат ввода
# три, три, и, ещё, три, будет, дырка, и, будет, и, дырка, и, дырка, и, дырка

# Формат вывода
# и: 5 дырка: 4 три: 3

# Примечания
# Рекомендация: чтобы быстрее решить задачу, нужно составить словарь, 
# в котором ключами будут встреченные слова, а значениями - их количество в строке. 
# Далее работайте с этим словарем по своему усмотрению. 
# Далее один из вариантов - отсортировать кортежи, 
# в которых на первом месте стоит количество слов, а на втором - сами слова.
# Учтите, что различных слов в строке может быть меньше трех. В этом случае нужно вывести все.

from collections import defaultdict

txt = input().replace(",", "").split()
txt_output = ""

mydict = defaultdict(int)

for key in txt:
    mydict[key] += 1

# используем лямду функцию, para[1] - сортировка по значению
sort_dict = sorted(mydict.items(), key = lambda para: para[1], reverse = True)

counter = len(sort_dict) - (len(sort_dict) - 3)

for para in sort_dict:
    if counter == 0:
        break
    else:
        txt_output += str(para[0]) + ": " + str(para[1]) + "\n"
        counter -= 1

print(txt_output)