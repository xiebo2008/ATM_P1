import json


def convert_2_builtin_type(objs):
    d = {}
    d.update(objs.__dict__)
    return d


def save_account(o):
    account_list=load_account_dict()
    isexist = False
    for obj in account_list:
        if obj["name"] == o.name :
            obj["balance"]= o.balance
            isexist = True
            break
        pass
    if isexist == False:
        account_list.append(o)
    p =json.dumps(account_list,default=convert_2_builtin_type)
    fo = open("data/account.txt", "w")
    fo.write(p)
    fo.close()
    pass

def load_account_dict():
    #读取文件中的json字符串
    fo = open("data/Account.txt","r")
    python_obj=json.load(fo)
    fo.close()
    return list(python_obj)
    pass


def is_exist(account):
    account_list= load_account_dict()
    for obj in account_list:
        if obj.name == account.name:
            return True
    return False
    pass


def validate(username,password):
    account_list = load_account_dict()
    for obj in account_list:
        if obj["name"] == username and obj["password"] == password:
            return obj
    return None
    pass

def is_exist(username):
    account_list = load_account_dict()
    for obj in account_list:
        if obj["name"] == username :
            return True
    return False
    pass