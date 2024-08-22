

class detention:
    '''
    类的构造方法
    当一个类的实例被创建时，__init__方法会自动被调用。它允许你在对象创建时为其设置初始状态。
    可以在这个方法中初始化实例变量，为对象赋予特定的属性值。
    示例：
       class Person:
            def __init__(self, name, age):
                self.name = name
                self.age = age
    当创建Person类的实例时，可以传入name和age两个参数，__init__方法会将这两个参数的值分别赋给实例变量self.name和self.age。

    除了设置属性值，还可以在__init__方法中执行其他必要的设置操作。可以打开文件、建立数据库连接等。
    '''

    def __init__(self) -> None:
        pass


    def Detention_gun(self,gun_list):
        # 违禁品
        contraband_list = ['ak', 'm4a1', 'skr']
        count = 0
        for gun in gun_list:
            for contraband in contraband_list:
                if contraband in gun:  #简单模糊匹配；字符串gun中查找是否完整地包含字符串contraband
                    count += 1
                    break

        return count



if __name__ == '__main__':

    #收缴物品
    n = int(input('请输入物品数量:'))
    gun_list = []
    for i in range(n):
        gun_list.append(input('请输入收缴物品：'))
    # print(gun_list)
    count = detention.Detention_gun(None,gun_list)
    print(count)







