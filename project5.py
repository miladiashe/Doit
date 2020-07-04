money = 10000

print("{0}원의 금액이 적립되어있습니다.".format(money))

while (money > 1500):
    print(""" 다음 메뉴에 해당하는 번호를 입력하세요.
 1. 아메리카노  1500
 2. 카페라떼    2000
 3. 에스프레소  1800
 4. 주문을 끝냅니다.""")
    number = input("-->")
    if (number == "1"):
        money = money - 1500
        print("손님께서는 아메리카노를 주문하셨습니다.\n잔돈은 {0}입니다.".format(money))
    elif (number == "2"):
        money = money - 2000
        print("손님께서는 카페라떼를 주문하셨습니다.\n잔돈은 {0}입니다.".format(money))
    elif (number == "3"):
        money = money - 1800
        print("손님께서는 에스프레소를 주문하셨습니다.\n잔돈은 {0}입니다.".format(money))
    elif (number == "4"):
        break
    else:
        print("잘못된 입력입니다.")

    
