
print("買い物の合計金額を入力してください。")
cost=input()
print("支払う金額を入力してください。")
pay=input()
change=int(pay)-int(cost)
tth=change//10000
fth=(change-tth*10000)//5000
th=(change-tth*10000-fth*5000)//1000
fh=(change-tth*10000-fth*5000-th*1000)//500
h=(change-tth*10000-fth*5000-th*1000-fh*500)//100
ft=(change-tth*10000-fth*5000-th*1000-fh*500-h*100)//50
t=(change-tth*10000-fth*5000-th*1000-fh*500-h*100-ft*50)//10
f=(change-tth*10000-fth*5000-th*1000-fh*500-h*100-ft*50-t*10)//5
o=change-tth*10000-fth*5000-th*1000-fh*500-h*100-ft*50-t*10-f*5
print("お釣りは、"+str(change)+"で、\n10000円札が"+str(tth)+"枚\n5000円札が"+str(fth)+"枚\n1000円札が"+str(th)+"枚\n500円玉が"+str(fh)+"枚\n100円玉が"+str(h)+"枚\n50円玉が"+str(ft)+"枚\n10円玉が"+str(t)+"枚\n5円玉が"+str(f)+"枚\n1円玉が"+str(0)+"枚です。")

