from GUI_Core import *

def printMenu():
    print("1.登陆 2.开户 ")
    choice =int(input("请选择菜单选项: "))
    if choice==1:
        if login():
            go_second_menu()
        else:
            print("账号或者密码不正确")

    elif choice == 2:
        create()
    else:
        print("输入错误")
    return

print("欢迎来到ATM")

count =0
while( count < 1):
    printMenu()
    
    




