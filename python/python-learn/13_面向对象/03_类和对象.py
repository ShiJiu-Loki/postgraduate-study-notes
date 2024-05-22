class clock:
    id = None       # 序列号
    price = None    # 零售价

    def ring(self):     # 响铃
        import winsound
        winsound.Beep(2000, 3000)


clock1 = clock()        # 基于类创建对象
clock1.id = '003032'
clock1.price = 19.99
print(f"闹钟ID：{clock1.id}，价格：{clock1.price}")
clock1.ring()           # 使用对象的属性和行为

clock2 = clock()        # 基于类创建对象
clock2.id = '003033'
clock2.price = 21.99
print(f"闹钟ID：{clock2.id}，价格：{clock2.price}")
clock2.ring()           # 使用对象的属性和行为
