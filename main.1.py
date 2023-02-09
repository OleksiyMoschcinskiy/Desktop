import random as rnd
def start():
    Level = int(1)
    HP = float(0)
    MP = float(0)
    Damage = float(0)
    Def = float(0)
    Crit_Rate = float(0)
    abilities_character = list()
    abilities_list = list()
    while True:
        try:
            abilities_character.clear()
            print('#>-------------------------<#')
            print('#>     вітаю вас в грі     <#')
            print('#>=========================<#')
            print('#>      Hogwarts wars      <#')
            print('#>=========================<#')
            print('#>                         <#')
            print("#>    Виберіть персонажа   <#")
            print('#>                         <#')
            print('#>_________________________<#')
            print()
            print()
            print('  ______________________________            _________________________________   ')
            print(" /             : HP = 11        \          /             : HP = 9            \  ")
            print(" |    Гарі     : Damage = 3     |          |    Рон      : Damage = 3        |  ")
            print(" |   Поттер    : def = 3        |          |   Візлі     : def = 5           |  ")
            print(' |             : Crit_Rate = 10 |          |             : Crit_Rate = 10    |  ')
            print(' \______________________________/          \_________________________________/  ')
            print('                                                                                ')
            print('                                                                                ')
            print('  ______________________________            _________________________________   ')
            print(" /             : HP = 8         \          /             : HP = 8            \  ")
            print(" |  Герміона   : Damage = 2     |          |    Невіл    : Damage = 2        |  ")
            print(' |  Грейнджер  : def = 7        |          |  Лонгботом  : def = 4           |  ')
            print(' |             : Crit_Rate = 10 |          |             : Crit_Rate = 10    |  ')
            print(" \______________________________/          \_________________________________/  ")
            print()
            print()
            print('/======================================================\ ')
            class_character = str(input('| Зробіть ваш вибір:'))
            print('\======================================================/ ')
            if class_character.lower() == 'гарі поттер':
                HP = 11
                MP = 4
                Damage = 3
                Def = 3
                Crit_Rate = 10
                abilities_list.append('імперіус')
                abilities_list.append('аваде кедавра')
                abilities_list.append('інсендіо')
                abilities_list.append('експекто патронум')
                x = 'імперіус' , 'аваде кедавра'  ,  'інсендіо'  ,  'експекто патронум'
                for i in range(0, 2):
                    ability = abilities_list[rnd.randint(0, len(abilities_list)-1)]
                    if ability in abilities_character:
                        i -= 1
                    else:
                        abilities_character.append(ability)
                print(abilities_character)
                break
            elif class_character.lower() == 'рон візлі':
                HP = 9
                MP = 4
                Damage = 3
                Def = 5
                Crit_Rate = 10
                abilities_list.append('редукто')
                abilities_list.append('конюктивітіс')
                abilities_list.append('конфрінго')
                abilities_list.append('експекто патронум')

                for i in range(0, 2):
                    ability = abilities_list[rnd.randint(0, len(abilities_list) - 1)]
                    if ability in abilities_character:
                        i -= 1
                    else:
                        abilities_character.append(ability)
                print(abilities_character)
                break
            elif class_character.lower() == 'герміона грейнджер':
                HP = 8
                MP = 4
                Damage = 2
                Def = 7
                Crit_Rate = 10
                abilities_list.append('ферула')
                abilities_list.append('сектумсепра')
                abilities_list.append('епіксі')
                abilities_list.append('експекто патронум')
                for i in range(0, 2):
                    ability = abilities_list[rnd.randint(0, len(abilities_list) - 1)]
                    if ability in abilities_character:
                        i -= 1
                    else:
                        abilities_character.append(ability)
                print(abilities_character)
                break
            elif class_character.lower() == 'невіл лонгботом':
                HP = 8
                MP = 4
                Damage = 2
                Def = 4
                Crit_Rate = 10
                abilities_list.append('круціатус')
                abilities_list.append('локомотор мортіс')
                abilities_list.append('петрифікус тоталус')
                abilities_list.append('експекто патронум')
                for i in range(0, 2):
                    ability = abilities_list[rnd.randint(0, len(abilities_list) - 1)]
                    if ability in abilities_character:
                        i -= 1
                    else:
                        abilities_character.append(ability)
                print(abilities_character)
                break
            else:
                raise Exception('Невідомий персонаж! Повторіть спробу!')
        except Exception as e:print(e)
    game_process(HP, MP, Damage, Def, Crit_Rate, abilities_character, class_character)
def game_process(HP, MP, Damage, Def, Crit_Rate, abilities_character, class_character):
    start = False
    e_Level = 1
    e_HP = 0
    e_MP = 0
    e_Damage = 0
    e_Def = 0
    e_Crit_Rate = 0
    list_enemy = ['драко малфой', 'дементор', 'волан де морт']
    for i in range(0, 3):
        enemy_name = str(list_enemy[rnd.randint(0, len(list_enemy)-1)])
        if enemy_name.lower() == 'драко малфой':
            e_HP = 5
            e_MP = 4
            e_Damage = 2
            e_Def = 1
            e_Crit_Rate = 5
        elif enemy_name.lower() == 'дементор':
            e_HP = 5
            e_MP = 3
            e_Damage = 2
            e_Def = 0
            e_Crit_Rate = 4
        elif enemy_name.lower() == 'волан де морт':
            e_HP = 8
            e_MP = 2
            e_Damage = 2
            e_Def = 3
            e_Crit_Rate = 2
        start = bool(rnd.randint(0, 2))
        print('............................')
        print(f"Хвиля №{i+1} ")
        print(':...........................:')
        while True:
            print(' __________________________')
            print("(   Інформація про ворога  )")
            print(' --------------------------')
            print()
            print('========================')
            print(f"|Назва: {enemy_name}")
            print(f"[HP: {e_HP}           ")
            print(f"<Damage: {e_Damage}    ")
            print(f"(Def: {e_Def}          ")
            print("========================")
            print()
            print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
            print("#Статус персонажа:                  ")
            print(f"0 персонаж: {class_character}      ")
            print(f"# HP: {HP}                         ")
            print(f"0 MP: {MP}                         ")
            print(f"# Damage: {Damage}                 ")
            print(f"0 Def: {Def}                       ")
            print(f"# Crit Rate: {Crit_Rate}           ")
            print(f"0 Здібності: {abilities_character} ")
            print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
            Crit_Rate_Bonus = 0
            if start == True: #user
                print('Ваш хід:')
                x = input('закляття - >')
                if x == 'імперіус':
                    Crit_Rate_Bonus = 30
                    print(f'Crit_Rate + {Crit_Rate_Bonus} = {Crit_Rate} + {Crit_Rate_Bonus}')
                if x == 'аваде кедавра':
                    Crit_Rate_Bonus = 40
                    print(f'Crit_Rate + {Crit_Rate_Bonus} = {Crit_Rate} + {Crit_Rate_Bonus}')
                if x == 'інсендіо':
                    Crit_Rate_Bonus = 20
                    print(f'Crit_Rate + {Crit_Rate_Bonus} = {Crit_Rate} + {Crit_Rate_Bonus}')
                if x == 'експекто патронум':
                    Crit_Rate_Bonus = 60
                    print(f'Crit_Rate + {Crit_Rate_Bonus} = {Crit_Rate} + {Crit_Rate_Bonus}')
                if x == 'редукто':
                    Crit_Rate_Bonus = 30
                    print(f'Crit_Rate + {Crit_Rate_Bonus} = {Crit_Rate} + {Crit_Rate_Bonus}')
                if x == 'конюктивітіс':
                    Crit_Rate_Bonus = 40
                    print(f'Crit_Rate + {Crit_Rate_Bonus} = {Crit_Rate} + {Crit_Rate_Bonus}')
                if x == 'конфрінго':
                    Crit_Rate_Bonus = 50
                    print(f'Crit_Rate + {Crit_Rate_Bonus} = {Crit_Rate} + {Crit_Rate_Bonus}')
                if x == 'епіксі':
                    Crit_Rate_Bonus = 30
                    print(f'Crit_Rate + {Crit_Rate_Bonus} = {Crit_Rate} + {Crit_Rate_Bonus}')
                if x == 'сектумсепра':
                    Crit_Rate_Bonus = 40
                    print(f'Crit_Rate + {Crit_Rate_Bonus} = {Crit_Rate} + {Crit_Rate_Bonus}')
                if x == 'ферула':
                    Crit_Rate_Bonus = 50
                    print(f'Crit_Rate + {Crit_Rate_Bonus} = {Crit_Rate} + {Crit_Rate_Bonus}')
                if x == 'круціатус':
                    Crit_Rate_Bonus = 50
                    print(f'Crit_Rate + {Crit_Rate_Bonus} = {Crit_Rate} + {Crit_Rate_Bonus}')
                if x == 'локомотор мортіс':
                    Crit_Rate_Bonus = 20
                    print(f'Crit_Rate + {Crit_Rate_Bonus} = {Crit_Rate} + {Crit_Rate_Bonus}')
                if x == 'петрифікус тоталус':
                    Crit_Rate_Bonus = 40
                    print(f'Crit_Rate + {Crit_Rate_Bonus} = {Crit_Rate} + {Crit_Rate_Bonus}')
                input()
                start = False
                Crit = (Damage*(Crit_Rate + Crit_Rate_Bonus)/100)
                result_damege_by_user = Damage + Crit
                print('#>------------------------------------<#')
                print(f'Bonus Crit: {Crit}                     ')
                print(f'Summary Damage: {result_damege_by_user}')
                print('#>------------------------------------<#')
                if result_damege_by_user > e_Def:
                    current_damage = result_damege_by_user - e_Def
                    e_Def = 0
                    e_HP -= current_damage
                    if e_HP < 0:
                        e_HP = 0
                        print('<#########################>')
                        print(f"|ви вбили {enemy_name}!  ")
                        print(' |    flawless victory    ')
                        print('<#########################>')
                        break
                else:
                    e_Def -= result_damege_by_user
            else: #enemy
                start = True
                result_damege_by_enemy = e_Damage + (e_Damage*e_Crit_Rate/100)
                if result_damege_by_enemy > Def:
                    current_damage = result_damege_by_enemy - Def
                    Def = 0
                    HP -= current_damage
                    if HP < 0:
                        HP = 0
                        print('...........................')
                        print(":  Вас вбили! Кінець гри! :")
                        print(':         you lose        :')
                        print(':.........................:')
                        break
                        end()
                else:
                    Def -= result_damege_by_enemy
        input()
def end():
    print('Exit')
if __name__ == "__main__":
    try:
        start()
    except Exception as e:
        print(e)

