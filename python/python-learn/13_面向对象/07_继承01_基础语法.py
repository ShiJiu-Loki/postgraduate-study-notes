# 继承
class Phone:
    IMEI = None         # 序列号
    producer = None     # 厂商

    def call_by_5g(self):
        print("5g通话")


class NFCReader:
    nfc_type = "第五代"
    producer = "HM"

    def read_card(self):
        print("读取NFC卡")

    def write_card(self):
        print("写入NFC卡")


class RemoteControl:
    rc_type = "红外遥控"

    def control(self):
        print("红外遥控开启")


class MyPhone(Phone, NFCReader, RemoteControl):     # 多继承
    pass


phone = MyPhone()
phone.call_by_5g()
phone.read_card()
phone.write_card()
phone.control()
# 输出同名成员属性
print(phone.producer)   # 优先级从左到右，所以是Phone类中的producer，不是NFCReader类中的producer
