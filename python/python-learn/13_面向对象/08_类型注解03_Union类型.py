# Union类型
my_list: list[int] = {1, 2, 3}                      # √
my_dict: dict[str, int] = {"age": 11, "num": 3}     # √

my_list = [1, 2, "lawliet", "yangtzeu"]               # ?
my_dict = {"name": "周杰轮", "age": 31}              # ?

from typing import Union
my_list: list[Union[str, int]] = [1, 2, "lawliet", "yangtzeu"]
my_dict: dict[str, Union[str, int]] = {"name": "周杰轮", "age": 31}


def func(data: Union[int, str]) -> Union[int, str]:
    pass
