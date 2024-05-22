# 导入json模块
import json

# 准备符合格式json格式要求的python数据，本质上是python数据
data = [{"name": "老王", "age": 16}, {"name": "张三", "age": 20}]

# 通过 json.dumps(data) 方法把python数据转化为了 json数据
json_data = json.dumps(data)
# 如果有中文可以带上：ensure_ascii=False参数来确保中文正常转换，如下
# json_data = json.dumps(data, ensure_ascii=False)

# 通过 json.loads(data) 方法把json数据转化为了 python数据
python_data = json.loads(json_data)

print(data)
print(json_data)
print(python_data)
