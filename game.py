import random
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
                break

            except ValueError:
                 print("введенно не число, повторите попытку")
   
if game == "pk":
    mini = 0
    maxi = 1000
    score_pk = 0
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
            score_pk+=1
            min = pk+1
            pk = random.randint(mini, maxi)
        if pk < chislo_pk:
            score_pk+=1
            max = pk-1
            pk = random.randint(mini, maxi)
        
    print("комп угадал твое число:", chislo_pk, "за", score_pk+1 ,"попыток")
