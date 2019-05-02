MONEY_KIND_LIST = [10000, 5000, 1000, 500, 100, 50, 10, 5]
money_count_list = []
print("買い物の合計金額を入力してください。")
cost = int(input())
print("支払う金額を入力してください。")
pay = int(input())
if pay < cost:
    print("金額が足りません。")
else:
    change = cost - pay
    for money in MONEY_KIND_LIST:
        money_count_list.append(change // money)
        change -= change // money * money

    print("お釣りは、{0}円で、".format(cost - pay))
    print("10000円札が{0}枚".format(money_count_list[0]))
    print("5000円札が{0}枚".format(money_count_list[1]))
    print("1000円札が{0}枚".format(money_count_list[2]))
    print("500円玉が{0}枚".format(money_count_list[3]))
    print("100円玉が{0}枚".format(money_count_list[4]))
    print("50円玉が{0}枚".format(money_count_list[5]))
    print("10円玉が{0}枚".format(money_count_list[6]))
    print("5円玉が{0}枚".format(money_count_list[7]))
