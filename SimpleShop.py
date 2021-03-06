
# if __name__ == "__main__":
#     print("请输入打折折扣：")
#     a = input()
#     print("请输入总金额：")
#     price = input()
#     if (a == "9折"):
#         print(float(price) * 0.9)
#     elif (a == "8折"):
#         print(float(price) * 0.1)
#     elif (a == "7折"):
#         pass
#     else:
#         pass
 
 
# 简单工厂模式
# 一个工厂、一个实体类（含抽象方法）、多个抽象方法的实现类
# 经常变动的为打折、不变的为总额、两者有关联关系
# 则总额为实体类、打着为抽象方法的实现类
 
 
# 抽象类，参数为商品原价，返回结果为实付价格
# 即将返回结果进行抽象化
class cashSuper():
    # 抽象类，子类必须实现该类
    @abc.abstractmethod
    def acceptCash(self,money):
        pass
 
 
# 正常收费类
class cashNormal(cashSuper):
    def acceptCash(self,money):
        return money
 
 
# 打折类
class cashRebate(cashSuper):
    # 打折数
    moneyRebat=0
    # init函数等同与构造函数
    def __init__(self, moneyRebate):
        self.moneyRebate = moneyRebate
 
    def acceptCash(self,money):
        return float(money) * float(self.moneyRebate)
 
 
# 满减类
class cashReturn(cashSuper):
    # 满足金额
    moneyCondition = 0
    # 返利
    moneyCondition = 0
 
    def __init__(self, moneyCondition, moneyReturn):
        self.moneyCondition = moneyCondition
        self.moneyReturn = moneyReturn
 
    def acceptCash(self,money):
        result = float(self.money)
        if (result >= self.conditionPirce):
            result = money - math.floor(money / self.moneyCondition) * self.moneyReturn
        return result
 
# 优惠工厂类
class createCashAccept():
    # 运算类的静态方法
    @staticmethod
    def createCash(cashType):
        cash = None
        # 这里可以添加其他运算方法
        if (cashType == "正常收费"):
            cash = cashNormal()
        elif (cashType == "满300减100"):
            cash = cashReturn(300,100)
        elif (cashType == "打8折"):
            cash = cashRebate(0.8)
        else:
            pass
        return cash
 
 
# #使用工厂方式实现需求
# if __name__ == "__main__":
#     print("请输入消费金额：")
#     price = input()
#     print("请输入优惠类型：")
#     type = input()
#     cash = createCashAccept.createCash(type)
#     print("总金额：",cash.acceptCash(price))
 
 
#
# 策略模式和简单工厂模式组合
class CashContext():
    #声明一个现金收费父类对象
    cs=cashSuper()
    #设置策略行为，参数为具体的现金收费子类（正常，打折或返利）
    def __init__(self,type):
        if (type == "正常收费"):
            self.cs = cashNormal()
        elif (type == "满300减100"):
            self.cs = cashReturn(300, 100)
        elif (type == "打8折"):
            self.cs = cashRebate(0.8)
        else:
            pass
 
    #得到现金促销计算结果（利用了多态机制，不同的策略行为导致不同的结果）
    def GetResult(self,money):
        return self.cs.acceptCash(money)
 
 
 
# # #使用策略模式实现需求
if __name__ == "__main__":
    print("请输入消费金额：")
    price = input()
    print("请输入优惠类型：")
    type = input()
    cashSuper=CashContext(type)
    print("价格为：",cashSuper.GetResult(price))
 
