# 基础数据类型注解
var_1: int = 10
var_2: float = 3.1415926
var_3: bool = True
var_4: str = "lawliet"

# 类对象类型注解
class Student:
    pass
stu: Student = Student()

# 基础容器类型注解
my_list: list = [1, 2, 3]
my_tuple: tuple = (1, 2, 3)
my_set: set = {1, 2, 3}
my_dict: dict = {"lawliet": 666}
my_str: str = "lawliet"

# 容器类型详细注解
my_list: list[int] = [1, 2, 3]
my_tuple: tuple[str, int, bool] = (1, 2, 3)
my_set: set[int] = {1, 2, 3}
my_dict: dict[str, int] = {"lawliet": 666}
# 注意：
# 元组类型设置类型详细注解，需要将每一个元素都标记出来
# 字典类型设置类型详细注解，需要2个类型，第一个是key第二个是value
