import AccountLib
import msvcrt
import tool

CURRENT_ACCOUNT = None


def login():
    global CURRENT_ACCOUNT
    username = input("请输入用户名: ")
    password = input('密码:')
    acc = AccountLib.Account.is_exist(username, password)
    if acc is not None:
        CURRENT_ACCOUNT = AccountLib.Account(acc["name"], acc["password"], acc["balance"])
        print("用户名:" + CURRENT_ACCOUNT.name + ", 余额:" + CURRENT_ACCOUNT.balance.__str__())
        return True
    else:
        return False


def create():
    print("开户")
    username = input("请输入用户名: ")
    while tool.is_exist(username):
        username = input("用户名已经存在,请继续输入")
    password = input("请输入密码: ")
    account = AccountLib.Account(username, password, 0)
    account.save()
    return


def go_second_menu():
    choice = int(input("1 存款 2 取款 3 转账 4 查余额 5 查流水 0 退出"))
    while choice != 0:
        menu_values[choice]()
        choice = int(input("1 存款 2 取款 3 转账 4 查余额 5 查流水 0 退出"))
    pass


def go_save():
    global CURRENT_ACCOUNT
    print("进入存款界面")
    money = float(input("请输入存款金额"))
    choice = input("请确认存入金额" + money.__str__() + "?(Y/N)")
    if choice.upper() == "Y":
        if CURRENT_ACCOUNT is not None:
            CURRENT_ACCOUNT.balance += money
            tool.save_account(CURRENT_ACCOUNT)
            print("存款成功")
            pass
    else:
        print("取消存款 ")
    pass


def go_draw():
    print("进入取款界面")
    money = float(input("请输入取款金额"))
    choice = input("请确认取款金额" + money.__str__() + "?(Y/N)")
    if choice.upper() == "Y":
        if CURRENT_ACCOUNT is not None and CURRENT_ACCOUNT.balance> money:
            CURRENT_ACCOUNT.balance -= money
            tool.save_account(CURRENT_ACCOUNT)
            print("取款成功")
            pass
        else:
            print('取款金额大于余额,存款失败 ')
    else:
        print("取消取款 ")
    pass


def show_balance():
    global CURRENT_ACCOUNT
    print("用户名:" + CURRENT_ACCOUNT.name + ", 余额:" + CURRENT_ACCOUNT.balance.__str__())
    pass


menu_values = {
    1: go_save,
    2: go_draw,
    4: show_balance
}
