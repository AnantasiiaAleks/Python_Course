'''
В файле first_tour.txt записано число K и данные об участниках турнира по
настольной игре «Орлеан»: фамилии, имена и количество баллов, набранных в
первом туре. Во второй тур проходят участники, которые набрали более K
баллов в первом туре.
Напишите программу, которая выводит в файл second_tour.txt данные всех
участников, прошедших во второй тур, с нумерацией.
В первой строке нужно вывести в файл second_tour.txt количество участников
второго тура. Затем программа должна вывести фамилии, инициалы и
количество баллов всех участников, прошедших во второй тур, с нумерацией.
Имя нужно сократить до одной буквы. Список должен быть отсортирован по
убыванию набранных баллов.
'''

with open('first_tour.txt', 'r', encoding='utf-8') as f:
    first_tour_list = f.readlines()
    print(first_tour_list)

max_score = int(first_tour_list[0].strip())
print(max_score)

players = {}
filter_players = {}
count = 1

for line in first_tour_list[1:]:
    player_data = line.strip().split()
    name = f'"{player_data[1][0]}. {player_data[0]}'
    score = int(player_data[-1])
    players[name] = score

for player, score in players.items():
    if score > max_score:
        filter_players[player] = score

sorted_filter_players = dict(sorted(filter_players.items(), key=lambda x: x[1], reverse=True))

with open("second_tour.txt", "w") as f:
    f.write(f"{len(sorted_filter_players)}\n")
    for player, score in sorted_filter_players.items():
        f.write(f"{count}) {player} {score}\n")
        count += 1
