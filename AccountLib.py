import json
import tool


class Account(object):

    def __init__(self, name, password, balance):
        self.name = name
        self.password = password
        self.balance = balance
        pass

    def add(self, money):
        self.balance += money
        pass

    def save(self):
        print("用户名："+ self.name+"进行存储 ......")
        tool.save_account(self)

    def is_exist(username, password):
        return tool.validate(username, password)
        pass
