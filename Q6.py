import random

distance = 5
player_hp = 20
while distance > 1:
    print("---------------------------------")
    print("出口まで{0}歩".format(distance))
    print("HP: {0}".format(player_hp))
    print("---------------------------------")
    print("1歩進んだ")
    print("---------------------------------")
    battle = "敵が現れた！"
    cure = "HPが3回復した！"
    nothing = "何もおきなかった"
    event = [battle, cure, nothing]
    happening = random.choice(event)
    print(happening)
    if happening == battle:
        enemy_hp = 5
        while enemy_hp > 0:
            print("---------------------------------")
            print("敵のHP: {0}".format(enemy_hp))
            print("自分のHP: {0}".format(player_hp))
            print("---------------------------------")
            print("コマンドを選択")
            print("1:たたかう")
            print("2:にげる")
            choice = input()
            if choice == "1":
                print("---------------------------------")
                print("プレーヤーの攻撃！")
                print("4のダメージ")
                print("敵の攻撃！")
                print("3のダメージ")
                enemy_hp = enemy_hp - 4
                player_hp = player_hp - 3
            elif choice == "2":
                escape_result = ["ok", "failure"]
                away = random.choice(escape_result)
                if away == "ok":
                    print("逃げることに成功した！")
                    break
                elif away == "failure":
                    print("まわりこまれた！")
        else:
            print("敵を倒した！")
    elif happening == cure:
        player_hp = player_hp + 3
    distance = distance - 1
else:
    print("---------------------------------")
    print("出口まで{0}歩".format(distance))
    print("HP: {0}".format(player_hp))
    print("---------------------------------")
    print("1歩進んだ")
    print("---------------------------------")
    print("おめでとう！洞窟を出られました！")
