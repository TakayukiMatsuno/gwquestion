MONEY_KIND_LIST = [10000, 5000, 1000, 500, 100, 50, 10, 5, 1]
print("買い物の合計金額を入力してください。")
cost = int(input())
print("支払う金額を入力してください。")
pay = int(input())
if pay < cost:
    print("金額が足りません。")
else:
    change = pay - cost
    print("お釣りは、{0}円で、".format(change))
    for money in MONEY_KIND_LIST:
        unit = ""
        if money > 500:
            unit = "札"
        else:
            unit = "玉"
        print("{0}円{1}が{2}枚".format(money, unit, change // money))
        change -= change // money * money
    print("です。")
