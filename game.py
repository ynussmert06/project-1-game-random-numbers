import random
import sqlite3
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# '8434994248:AAEMhFC3K9PkomWRGzEuJbiWzXrtvEGc9h0'

# создадим базу данный для сохранения рекордов
table = sqlite3.connect("record_table")
cursorr = table.cursor()
human_table = ("""CREATE TABLE IF NOT EXISTS chel_record(
                name_player text,
                lvl text,
                score_player integer
                )""")
pk_table =("""CREATE TABLE IF NOT EXISTS pk_record(
                name_player text,
                score_pk integer
                )""")
cursorr.execute(human_table)
cursorr.execute(pk_table)
table.commit()

name = input("введите имя игрока: ")
game = input("выберите режи игры:  человек угадывает: chel, компьютер угадывает: pk ")
if game not in ["chel", "pk"]:
    game = random.choice(["chel","pk"])
    print("неопределенный ввод, программа выбрала игру", game)
score = 0
r = 0
if game == "chel":
    level = input("уровень сложности: easy = 0-100, middle = 0-500, hard = 0-1000 ")
    if level not in ["easy","middle","hard"]:
        level = random.choice(["easy","middle","hard"])
        print("неопределенный ввод, программа выбрала сложность", level)
    else:
        while True:
            try:
                chislo = int(input("компьютер загадал число, сможешь угадать?: "))
                     # воспользовался словарем чтобы лучше закрепить, а так можно просто через if
                operachion = {
                        "easy": lambda r:r + random.randint(0, 100),
                        "middle": lambda r:r + random.randint(0, 500), 
                        "hard": lambda r:r + random.randint(0, 1000)}
                if level in operachion:
                        random_ = operachion[level](r)
                while chislo != random_:
                        if chislo > random_:
                            score+=1
                            chislo = int(input("не угадал,число меньше, попробуй еще раз: "))
                        if chislo < random_:
                            score+=1
                            chislo = int(input("не угадал, число больше, попробуй еще раз: "))
               
                print("ты угадал,", "количество попыток:", score+1)
                cursorr.execute('INSERT INTO chel_record VALUES(?,?,?)', (name, level, score+1))
                cursorr.execute('SELECT * FROM chel_record ORDER BY score_player DESC LIMIT 5')
                chel = cursorr.fetchall()
                print("-----------ТАБЛИЦА----------")
                for a, row in enumerate(chel):
                    print(f"TOP {a+1} --> {row}")
                cursorr.execute('DELETE FROM chel_record WHERE score_player < (SELECT MIN(score_player) FROM chel_record ORDER BY score_player DESC LIMIT 5)')
                table.commit()
                table.close()
                break
            except ValueError:
                 print("введенно не число, повторите попытку")
   
if game == "pk":
    mini = 0
    maxi = 1000
    score_pk_game = 0
    while True:
         try:
            chislo_pk = int(input("загадайте число компьютеру До 1000: "))
            if 0 <= chislo_pk <= 1000:
                 break
            else:
                 print("число должно быть от 0 до 1000")
            
         except ValueError or chislo_pk > 1000:
              print("введенно не число, повторите:")
    pk = random.randint(mini, maxi)
    while chislo_pk != pk:
        if pk > chislo_pk:
            score_pk_game+=1
            min = pk+1
            pk = random.randint(mini, maxi)
        if pk < chislo_pk:
            score_pk_game+=1
            max = pk-1
            pk = random.randint(mini, maxi) 
    print("комп угадал твое число:", chislo_pk, "за", score_pk_game+1 ,"попыток")
    cursorr.execute('INSERT INTO pk_record VALUES(?,?)', (name, score_pk_game+1))
    cursorr.execute('SELECT * FROM pk_record ORDER BY score_pk DESC LIMIT 5')
    
    pk_ = cursorr.fetchall()
    print("---------ТАБЛИЦА---------")
    for i, roe in enumerate(pk_):
         print(f"TOP {i+1} -->{roe}")
    cursorr.execute('DELETE FROM pk_record WHERE score_pk < (SELECT MIN(score_pk) FROM pk_record ORDER BY score_pk DESC LIMIT 5)')
    table.commit()
    table.close()
table.close()