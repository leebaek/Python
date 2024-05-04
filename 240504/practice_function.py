# def open_account(): # 함수는 정의 후 호출되기 전에는 동작하지 않는다.
#     print("새로운 계좌가 생성되었습니다.")

# open_account() # 함수 호출

def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money): # 입금함수, balance : 잔액, money : 입금할 금액
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money): # 출금함수
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 불가능합니다. 잔액은 {0}원입니다.".format(balance))
        return balance
    
def withdraw_night(balance, money): # 야간 출금 수수료
    commission = 100 # 수수료 100원
    return commission, balance - money - commission # 두개의 값을 튜플로 반환도 가능하다

balance = 0 # 잔액
money = 12310
balance = deposit(balance, money)
withdraw(151, 293)
commission, balance = withdraw_night(balance, 500)
print("수수료 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))