# 函数：print_file_info(file_name)，
# 接收传入文件的路径，打印文件的全部内容，
# 如文件不存在则捕获异常，输出提示信息，
# 通过finally关闭文件对象
def print_file_info(file_name):
    f = None
    try:
        f = open(file_name, 'r', encoding="UTF-8")
        print(f.read())
    except Exception as e:
        # 如果文件不存在，r方式无法打开，可以采用w方式进行新建，但新建文件没有信息，所以对于输出来说没有意义
        # f = open(file_name, 'w', encoding="UTF-8")
        print(e)
        print("您要打印的文件不存在，请重新确认文件路径和文件名称")
    finally:
        # 文件存在时f不为None，需要关闭（不这么做程序会报错）
        if f:
            f.close()


# 函数：append_to_file(file_name, data)，
# 接收文件路径以及传入数据，将数据追加写入到文件中
def append_to_file(file_name, data):
    f = None
    try:
        f = open(file_name, 'a', encoding="UTF-8")
        f.write('\n'+data)
        f.flush()
    except Exception as e:
        print(e)
        print("要追加内容的目标文件不存在，请重新确认文件路径和文件名")
    finally:
        # 跟上述一样，如果文件存在，需要关闭；否则直接返回即可（不这么做程序会报错）
        if not f:
            return
        f.close()
