# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

# Создайте программу для игры в ""Крестики-нолики"".

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

# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

enterData =


def compression(_list):
    _s = ""
    _str = _list[0]
    _c = 1
    for i in range(1, len(_list)):
        if _str == _list[i]:
            _c += 1
        else:
            _s += _str + f'{_c}'
            _str = _list[i]
            _c = 1
    return _s


str = "aaababbcbbb"
s = compression(str)
print(s)
#(a, 3) (b, 1) (a, 1) (b, 2) (c, 1) (b, 3)
