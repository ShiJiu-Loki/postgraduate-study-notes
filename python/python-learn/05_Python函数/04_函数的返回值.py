# 函数的返回值
def add(x, y):
    return x + y


result = add(1, 2)
print(f"result={result}")
print(type(result))
# ============================================================================
# ============================================================================


# 不写return或者只写return不写具体返回值是同样效果，都是return一个None类型值
def add(x, y):
    return


result = add(1, 2)
print(result)
print(type(result))
# ============================================================================
# ============================================================================


# None的使用场景,None在if判断中值为False
def check_age(age):
    if age >= 18:
        return "SUCCESS"
    return None


result = check_age(17)   # 通过更改参数值测试
if not result:
    print("未成年，不可进入")
else:
    print("已成年，可以进入")
