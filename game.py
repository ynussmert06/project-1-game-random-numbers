import random

r = 0
score = 0


level = input("уровень сложности: easy = 0-100, middle = 0-500, hard = 0-1000 ")
chislo = int(input("компьютер загадал число, сможешь угадать?: "))
        # воспользовался словарем чтобы лучше закрепить, а так можно просто через if
operachion = {
            "easy": lambda r: r + random.randint(0, 100),
            "middle": lambda r: r + random.randint(0, 500), 
            "hard": lambda r: r + random.randint(0, 1000)}
if level in operachion:
            random_ = operachion[level](r)
while chislo != random_:
            if chislo > random_:
                score+=1
                chislo = int(input("не уагадал,число меньше, попробуй еще раз: "))
            if chislo < random_:
                score+=1
                chislo = int(input("не уагадал, число больше, попробуй еще раз: "))
print(f"ты угадал", "количество попыток:", score+1)
