# 封装
class Phone:
    IMEI = None         # 序列号
    producer = None     # 厂商
    __current_voltage = 0.5    # 当前电压；私有成员变量

    def call_by_5g(self):
        if self.__current_voltage >= 1:     # 在成员方法内可以访问其他私有成员
            print("5G通话已开启")
        else:
            self.__keep_single_core()       # 在成员方法内可以访问其他私有成员
            print("通话失败，电量不足")

    def __keep_single_core(self):
        print("让CPU以单核模式运行以节省电量")   # 私有成员方法


phone = Phone()
phone.call_by_5g()

# print(phone.__current_voltage)   # 获取私有变量值；报错，无法使用
# phone.__keep_single_core()       # 使用私有方法；报错，无法使用

phone.__current_voltage = 33       # 私有变量赋值；不报错，但无效
print(phone.__current_voltage)     # 不报错，但实际上输出的不是类内部定义的私有变量
