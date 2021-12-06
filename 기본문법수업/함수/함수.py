def open_account():
    print("새로운 계좌가 생성되었습니다.") #함수정의만. 출력은 따로


open_account() #함수호출

def deposit(balance, money): #입금
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money): #출금
    if balance >= money: #잔액이 출금보다 많을때
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance-money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
        return balance


def withdraw_night(balance, money): #저녁에 출금
    commission = 100 #수수료 100원
    return commission, balance-money-commission #튜플형식으로 여러개 반환가능


balance = 0 #잔액
balance = deposit(balance, 1000)
balance = withdraw(balance,500)

commission,balance = withdraw_night(balance,300)
print("수수료 {0}원이며, 잔액은 {1}원입니다.".format(commission,balance))