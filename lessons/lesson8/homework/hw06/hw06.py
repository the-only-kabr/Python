# import random
# # Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


def deletWord(_list, _word):
    length = len(_list)
    count = 0
    while length > 0:
        if _word in _list[count]:
            _list.pop(count)
            length -= 1
        length -= 1
        count += 1
    return _list


#n = [str(s) for s in input('Введите слово : ').split()] замена 
n = list(map(str,input('Введите слово : ').split())
m = input('Введите проверочную последовательность : ')
print(deletWord(n, m))

# # Создайте программу для игры с конфетами человек против человека.
# # Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# # За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# # Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# # a) Добавьте игру против бота
# # b) Подумайте как наделить бота ""интеллектом""


# def give(_player, _candy, _number):
#     print(
#         f'Вы можете забрать не больше 28 конфет, всего конфет осталось {_number} ')
#     n = int(input(f'Игрок {_player} введите сколько конфект берем :'))
#     _candy += n
#     return _candy


# def findPlayer():
#     player1 = input('Введите имя игрока ')
#     player2 = input('введите имя игрока ')
#     n = random.randint(1, 2)
#     print(n)
#     if n == 1:
#         t = player1
#         player1 = player2
#         player2 = t
#     return player1, player2


# print('Кидаем жребий ')
# first, second = findPlayer()
# print(f'Первым ходит {first}')
# candy1, candy2 = 0, 0
# allNum = 201
# while allNum > 0:
#     candy1 = give(first, candy1, allNum)
#     allNum -= candy1
#     print(f' У {first} всего {candy1} конфет ')
#     if allNum <= 0:
#         print(f"Win {first}")
#     candy2 = give(first, candy2, allNum)
#     allNum -= candy2
#     print(f' У {second} всего {candy2} конфет ')
#     if allNum <= 0:
#         print(f"Win {second}")


# # Создайте программу для игры в ""Крестики-нолики"".

# print("*" * 10, " Игра Крестики-нолики для двух игроков ", "*" * 10)
# board = list(range(1, 10))


# def draw_board(board):
#     print("-" * 13)
#     for i in range(3):
#         print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
#         print("-" * 13)


# def take_input(player_token):
#     valid = False
#     while not valid:
#         player_answer = input("Куда поставим " + player_token+"? ")
#         try:
#             player_answer = int(player_answer)
#         except:
#             print("Некорректный ввод. Вы уверены, что ввели число?")
#             continue
#         if player_answer >= 1 and player_answer <= 9:
#             if (str(board[player_answer-1]) not in "XO"):
#                 board[player_answer-1] = player_token
#                 valid = True
#             else:
#                 print("Эта клетка уже занята!")
#         else:
#             print("Некорректный ввод. Введите число от 1 до 9.")


# def check_win(board):
#     win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
#                  (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
#     for each in win_coord:
#         if board[each[0]] == board[each[1]] == board[each[2]]:
#             return board[each[0]]
#     return False


# def main(board):
#     counter = 0
#     win = False
#     while not win:
#         draw_board(board)
#         if counter % 2 == 0:
#             take_input("X")
#         else:
#             take_input("O")
#         counter += 1
#         if counter > 4:
#             tmp = check_win(board)
#             if tmp:
#                 print(tmp, "выиграл!")
#                 win = True
#                 break
#         if counter == 9:
#             print("Ничья!")
#             break
#     draw_board(board)


# main(board)

# input("Нажмите Enter для выхода!")

# # Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# # Входные и выходные данные хранятся в отдельных текстовых файлах.
# # a3b1a1b2c1


# def decompression(_str):
#     _s = ""
#     for i in range(1, len(_str)+1, 2):
#         for z in range(int(_str[i])):
#             _s += _str[i-1]
#     return _s


# def compression(_str):
#     _s = ""
#     _count = 1
#     _char = _str[0]
#     for i in range(1, len(_str)):
#         if _str[i] == _char and i != len(_str)-1:
#             _count += 1
#         else:
#             _s += _char + f'{_count}'
#             _count = 1
#             _char = _str[i]
#     return _s


# enterData = open('data.txt', 'r')
# exitData = open('exitData.txt', 'w')
# enter = enterData.read()
# print(enter)
# str = compression(enter)
# exitData.write(str)

# exit = open('exitData.txt', 'r')
# newData = open('newData.txt', 'w')
# ex = exit.read()
# print(ex)
# t = decompression(ex)
# newData.write(t)
