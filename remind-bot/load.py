import json
import time


async def load_in(path):
    """读取文件的数据，以dic形式返回"""
    with open(path, 'r') as f:
        try:
            jsonData = json.load(f)
        except:
            jsonData = {}
    return jsonData


async def write_in(path, jsondata):
    """传入需写入的信息"""
    dic = await load_in(path)
    dic.update(jsondata)
    with open(path, 'w') as f:
        json.dump(dic, f)
    return


async def del_in(path, user_id):
    """删除该学生的一条信息"""
    data = await load_in(path)
    try:
        del data[user_id]
        with open(path, 'w') as f:
            json.dump(data, f)
        return 1
    except:
        return 0


async def got_path(string):
    """将路径格式化返回"""
    dic = {'一': '0', '二': '1', '三': '2', '四': '3', '五': '4', '六': '5', '日': '6'}
    flat = 0
    for i in ['一', '二', '三', '四', '五', '六', '日']:
        for j in ['一', '二', '三', '四', '五']:
            if f'周{i}第{j}节' == string:
                path = f'./timeable/loadmmy/{dic[i]}-{dic[j]}.json'
                flat = 1
                return path
            else:
                pass
    if flat == 0:
        raise UserWarning


async def got_next_lesson():
    """将课程数字格式化输出
    返回类型：int"""
    now = time.ctime()[11:19]
    if now < '08:30:00':
        return 0
    elif now < '10:25:00':
        return 1
    elif now < '14:00:00':
        return 2
    elif now < '15:55:00':
        return 3
    elif now < '18:40:00':
        return 4
    else:
        raise UserWarning
