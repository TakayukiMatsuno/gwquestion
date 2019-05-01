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
                print("---------------------------------\nプレーヤーの攻撃！\n4のダメージ")
                ehp=ehp-4
                mhp=mhp-3
                if mhp<=0:
                    print("---------------------------------\n残念！死亡してしまいました！")
                    break
                elif ehp>0:
                    print("\n敵の攻撃！\n3のダメージ")
            elif choice=="2":
                l=["ok","failure"]
                away=random.choice(l)
                if away=="ok":
                    print("---------------------------------\n逃げることに成功した！")
                    break
                elif away=="failure":
                    print("---------------------------------\nまわりこまれた！")
                    print("---------------------------------\n敵の攻撃！\n5のダメージ")
                    mhp=mhp-5
                    if mhp<=0:
                        print("---------------------------------\n残念！死亡してしまいました！")
                        break
        else: 
            print("---------------------------------\n敵を倒した！")
    elif happening==cure:
        mhp=mhp+3
    distance=distance-1
    if mhp<=0:
        break
else:
    print("---------------------------------\n出口まで"+str(distance)+"歩\nHP"+str(mhp))
    print("---------------------------------\n1歩進んだ\n---------------------------------")
    print("おめでとう！洞窟を出られました！")
    
