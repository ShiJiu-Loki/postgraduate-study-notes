# 复写和使用父类成员
class Phone:
    IMEI = None             # 序列号
    producer = "ITCAST"     # 厂商

    def call_by_5g(self):
        print("父类的5g通话")


class MyPhone(Phone):     # 单继承
    producer = "ITHEIMA"    # 复写父类属性

    def call_by_5g(self):   # 复写父类方法
        # 方式1调用父类成员
        print(f"父类的品牌是：{Phone.producer}")
        Phone.call_by_5g(self)

        # 方式2调用父类成员
        print(f"父类的品牌是：{super().producer}")
        super().call_by_5g()

        print("子类的5g通话")


phone = MyPhone()
print(phone.producer)
phone.call_by_5g()
