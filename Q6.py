import random
distance=5
mhp=20
while distance>1:
    print("---------------------------------\n出口まで"+str(distance)+"歩\nHP"+str(mhp))
    print("---------------------------------\n1歩進んだ\n---------------------------------")
    battle="敵が現れた！"
    cure="HPが3回復した！"
    nothing="何もおきなかった"
    event=[battle,cure,nothing]
    happening=random.choice(event)
    print(happening)
    if happening==battle:
        ehp=5
        while ehp>0:
            print("---------------------------------\n敵のHP"+str(ehp)+"\n自分のHP"+str(mhp))
            print("---------------------------------\nコマンドを選択\n1:たたかう\n2:にげる")
            choice=input()
            if choice=="1":
                print("---------------------------------\nプレーヤーの攻撃！\n4のダメージ\n敵の攻撃！\n3のダメージ")
                ehp=ehp-4
                mhp=mhp-3
            elif choice=="2":
                l=["ok","failure"]
                away=random.choice(l)
                if away=="ok":
                    print("逃げることに成功した！")
                    break
                elif away=="failure":
                    print("まわりこまれた！")
        else: 
            print("敵を倒した！")
    elif happening==cure:
        mhp=mhp+3
    distance=distance-1
else:
    print("---------------------------------\n出口まで"+str(distance)+"歩\nHP"+str(mhp))
    print("---------------------------------\n1歩進んだ\n---------------------------------")
    print("おめでとう！洞窟を出られました！")
