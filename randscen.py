import json, random, time, datetime, os

can_be_disabled = [
    9,
    4,
    2,
    11,
    13,
    6,
    5,
    1,
    3,
    7,
    8,
    10,
    12
  ]

items = [[9, 12], [9, 13], [9, 5], [9, 9], [4, 11], [4, 17], [4, 18], [4, 20], [4, 26], [4, 25], [4, 16], [4, 15], [4, 6], [4, 9], [4, 19], [2, 8], [2, 11], [2, 17], [2, 2], [2, 18], [2, 12], [2, 13], [2, 5], [2, 16], [2, 15], [2, 6], [2, 9], [2, 14], [11, 12], [11, 13], [11, 5], [11, 9], [13, 11], [13, 12], [13, 13], [13, 9], [6, 11], [6, 17], [6, 18], [6, 12], [6, 13], [6, 5], [6, 16], [6, 15], [6, 6], [6, 9], [6, 19], [5, 17], [5, 18], [5, 20], [5, 26], [5, 25], [5, 16], [5, 15], [5, 6], [5, 9], [5, 19], [1, 11], [1, 17], [1, 18], [1, 12], [1, 13], [1, 5], [1, 16], [1, 15], [1, 6], [1, 1], [1, 9], [1, 14], [3, 8], [3, 11], [3, 17], [3, 18], [3, 12], [3, 13], [3, 5], [3, 16], [3, 15], [3, 6], [3, 9], [3, 14], [7, 11], [7, 12], [7, 13], [7, 5], [7, 9], [7, 14], [10, 11], [10, 17], [10, 18], [10, 12], [10, 13], [10, 5], [10, 16], [10, 15], [10, 10], [10, 9], [8, 11], [8, 17], [8, 18], [8, 12], [8, 13], [8, 5], [8, 16], [8, 15], [8, 6], [8, 9], [8, 14], [12, 10], [12, 11], [12, 18], [12, 12], [12, 13]]

system_targets = 13
print("""Генерация

1 - Случайный сид времени, но своя сложность
2 - Статичный сид времени, но своя сложность
3 - Статичный сид и выбор сложности
4 - Случайно всё
      
5 - Ежедневный полёт""")
removed_predmet = 0
timedurka = 0.0
if (q_f:=input("===> ")) == "1":
    seed = int(time.time())
    random.seed(seed)
    # Q2
    print("""Сложность (Сколько вещей не будет, кроме: Реактора, Балон CO2, Балон O2, Балон Азота, Балон Жидкого Азота):
    1 - Легко (0-25 вещей) (5-10 минут)
    2 - Средне (25-45 вещей) (10-20 минут)
    3 - Тяжело (45-65 вещей) (20-30 минут)
    4 - Хардкор (65-85 вещей) (30-50 минут)
    5 - Полный ноль (113 вещей) (50-120 минут)
    """)
    while True:
        if (mode1:=input("===> "))=="1":
            removed_predmet = random.randint(0,25)
            timedurka = round(random.uniform(5.0,10.0),1)
            break
        elif mode1 == "2":
            removed_predmet = random.randint(45,65)
            timedurka = round(random.uniform(20.0,30.0),1)
            break
        elif mode1 == "3":
            removed_predmet = random.randint(65,85)
            timedurka = round(random.uniform(30.0,50.0),1)
            break
        elif mode1 == "4":
            removed_predmet = random.randint(85,113)
            timedurka = round(random.uniform(30.0,50.0),1)
            break
        elif mode1 == "5":
            removed_predmet = 113
            timedurka = round(random.uniform(50.0,120.0),1)
            break
        else:
            print("Не то что нужно...")
    print()
elif q_f == "2":
    seed = int(input("Сид времени: "))
     # Q2
    print("""Сложность (Сколько вещей не будет, кроме: Реактора, Балон CO2, Балон O2, Балон Азота, Балон Жидкого Азота):
    1 - Легко (0-25 вещей) (5-10 минут)
    2 - Средне (25-45 вещей) (10-20 минут)
    3 - Тяжело (45-65 вещей) (20-30 минут)
    4 - Хардкор (65-85 вещей) (30-50 минут)
    5 - Полный ноль (113 вещей) (50-120 минут)
    """)
    while True:
        if (mode1:=input("===> "))=="1":
            removed_predmet = random.randint(0,25)
            timedurka = round(random.uniform(5.0,10.0),1)
            break
        elif mode1 == "2":
            removed_predmet = random.randint(25,65)
            timedurka = round(random.uniform(10.0,20.0),1)
            break
        elif mode1 == "3":
            removed_predmet = random.randint(65,85)
            timedurka = round(random.uniform(20.0,30.0),1)
            break
        elif mode1 == "4":
            removed_predmet = random.randint(85,113)
            timedurka = round(random.uniform(30.0,50.0),1)
            break
        elif mode1 == "5":
            removed_predmet = 113
            timedurka = round(random.uniform(50.0,120.0),1)
            break
        else:
            print("Не то что нужно...")
    print()
elif q_f == "3":
    inp = input("Введите полный сид: ").split("_")
    mode1 = inp[1]
    seed = int(inp[0])
    random.seed(seed)
    if  mode1 == "1":
        removed_predmet = random.randint(0,25)
        timedurka = round(random.uniform(5.0,10.0),1)
    elif mode1 == "2":
        removed_predmet = random.randint(25,45)
        timedurka = round(random.uniform(10.0,20.0),1)
    elif mode1 == "3":
        removed_predmet = random.randint(45,65)
        timedurka = round(random.uniform(20.0,30.0),1)
    elif mode1 == "4":
        removed_predmet = random.randint(65,85)
        timedurka = round(random.uniform(30.0,50.0),1)
    elif mode1 == "5":
        removed_predmet = 113
        timedurka = round(random.uniform(50.0,120.0),1)
elif q_f == "4":
    seed = int(time.time())
    mode1 = str(random.randint(1,5))
    random.seed(seed)
    if  mode1 == "1":
        removed_predmet = random.randint(0,25)
        timedurka = round(random.uniform(5.0,10.0),1)
    elif mode1 == "2":
        removed_predmet = random.randint(25,45)
        timedurka = round(random.uniform(10.0,20.0),1)
    elif mode1 == "3":
        removed_predmet = random.randint(45,65)
        timedurka = round(random.uniform(20.0,30.0),1)
    elif mode1 == "4":
        removed_predmet = random.randint(65,85)
        timedurka = round(random.uniform(30.0,50.0),1)
    elif mode1 == "5":
        removed_predmet = 113
        timedurka = round(random.uniform(50.0,120.0),1)
elif q_f == "5":
    seed = round(time.mktime(datetime.datetime.strptime(datetime.datetime.now().strftime("%Y-%m-%d"), "%Y-%m-%d").timetuple()))
    random.seed(seed)
    mode1 = str(random.randint(1,5))
    if  mode1 == "1":
        removed_predmet = random.randint(0,25)
        timedurka = round(random.uniform(5.0,10.0),1)
    elif mode1 == "2":
        removed_predmet = random.randint(25,45)
        timedurka = round(random.uniform(10.0,20.0),1)
    elif mode1 == "3":
        removed_predmet = random.randint(45,65)
        timedurka = round(random.uniform(20.0,30.0),1)
    elif mode1 == "4":
        removed_predmet = random.randint(65,85)
        timedurka = round(random.uniform(30.0,50.0),1)
    elif mode1 == "5":
        removed_predmet = 113
        timedurka = round(random.uniform(50.0,120.0),1)

# STATIC
sd = {}
pereriv = random.randint(1,30)
sd["ScenarioName"] = f"SEED: {seed}_{mode1}"
sd["CreatedDate"] = f"12.16.2024 00:56:07"
sd["CreatedBy"] =  76561197960287930
sd["DamagePrct"] = 0
sd["RemovedPrct"] = 0
sd["StockagePrct"] = 0
sd["RemovedSystems"] = []
sd["DisabledCompomentsInPod"] = []
sd["ComponentNeeded"] = []
sd["NoGeneratedComponent"] = []


removedd = []
for i in range(removed_predmet):
    r_c = random.choice(items)
    items.pop(items.index(r_c))
    removedd.append({
        "SystemTypeTarget": r_c[0],
        "Component": r_c[1]
    })

# Q3
assus=[]
#README: dodelat

phaserand = (0,0)
phasedur = (0,0)
if mode1 == "1":
    phaserand = (2,5)
    phasedur = (8,15)
elif mode1 == "2":
    phaserand = (5,10)
    phasedur = (10,20)
elif mode1 == "3":
    phaserand = (10,20)
    phasedur = (14,25)
elif mode1 == "4":
    phaserand = (20,40)
    phasedur = (17,28)
elif mode1 == "5":
    phaserand = (40,60)
    phasedur = (17,28)
awaitphase = round(timedurka/20)
phasest = ["|"]
for _ in range(random.randint(phaserand[0], phaserand[1])):
    rrrr = random.randint(1,5)
    if rrrr == 1:
        assus.append({
        "Evenement": 1,
        "StartTime": awaitphase,
        "Duration": random.randint(phasedur[0],phasedur[1]),
        "StrikeDelay": 0,
        "ComponentImpacted": None
        })
        phasest.append("Астеройды |")
    elif rrrr == 2:
        assus.append({
      "Evenement": 2,
      "StartTime": awaitphase,
      "Duration": random.randint(phasedur[0],phasedur[1]),
      "StrikeDelay": 0,
      "ComponentImpacted": None
        })
        phasest.append("Холодное облако |")
    elif rrrr == 3:
        assus.append({
      "Evenement": 3,
      "StartTime": awaitphase,
      "Duration": random.randint(phasedur[0],phasedur[1]),
      "StrikeDelay": 0,
      "ComponentImpacted": None
    })
        phasest.append("Электрическое облако |")
    elif rrrr == 4:
        assus.append({
      "Evenement": 4,
      "StartTime": awaitphase,
      "Duration": 0,
      "StrikeDelay": 0,
      "ComponentImpacted": None
    })
        phasest.append("Горячая звезда |")
    elif rrrr == 5:
        assus.append({
      "Evenement": 5,
      "StartTime": awaitphase,
      "Duration": 0,
      "StrikeDelay": 0,
      "ComponentImpacted": None
    })
        phasest.append("Чёрная дыра |")
    

sd["EvenementsSettings"] = assus
# POLNYI RANDOM
sd["TimeDuration"] = timedurka
sd["DisabledCompomentsInSystem"] = removedd
sd["TimePreparation"] = round(random.uniform(0.5, 3.0),1)
sd["DisabledSystems"] = random.choices(can_be_disabled, k=random.randint(1,13))
sd["StarshipCompStockPrct"] = random.randint(1,100)

# sd["StockagePrct"] = random.randint(1,100)
print("==================================")
print(f"""Сид: {seed}_{mode1}
Сид времени: {seed}
Сложность: {"Легко" if mode1 == "1" else "Средне" if mode1 == "2" else "Тяжело" if mode1 == "3" else "Хардкор" if mode1 == "4" else "Полный ноль"}

Время которое нужно выжить: {timedurka} минут(ы)
Время подготовки: {sd["TimePreparation"]} минуты

Процент компонентов в изначальном корабле: {sd["StarshipCompStockPrct"]}
Отсутствующих компонентов из модулей: {removed_predmet}
Изначально отключено модулей: {len(sd["DisabledSystems"])}

Время между событиями: {awaitphase} минут(ы)
Событий: {len(sd["EvenementsSettings"])} ({" ".join(phasest)})""")
print("==================================")
# Процент компонентов внутри корабля: {sd["StockagePrct"]}
try:
    with open(f"{seed}_{mode1}.json", "x") as fl:
        fl.write(json.dumps(sd, indent=1))
except FileExistsError:
    os.remove(f"{seed}_{mode1}.json")
    with open(f"{seed}_{mode1}.json", "x") as fl:
        fl.write(json.dumps(sd, indent=1))