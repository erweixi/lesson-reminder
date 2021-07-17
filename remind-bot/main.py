import nonebot
from nonebot import CommandSession
from .load import *
import time

'''
作者：尔威希
注意：  星期一从0开始，到星期日结束为6
        第一节课从0开始，到第五节课以4结束
'''
__plugin_name__ = '课表'
__plugin_help__ = '''
导入你的课表，需要一节课一节课的输入，可以私聊
输入下节课获取下一节课是什么
格式：载入 周%第%节 %课程名称% %课程持续周长%
例如：载入 周一第一节 高等数学 20
如若不填入持续周长则默认20
删除课表格式：删除 周%第%节
'''



@nonebot.on_command('课程表帮助')
async def help(session: CommandSession):
    await session.finish(__plugin_help__)


@nonebot.on_command('载入')
async def reload(session: CommandSession):
    ev = session.event
    name = str(ev.message).split()
    if len(name) == 3:
        name.append('20')
    string = name[1]
    try:
        path = await got_path(string)
    except:
        await session.finish("您的输入似乎有误，请重新输入，输入“课程表帮助”获取进一步帮助")
        return
    data = {ev.user_id: [name[2], int(name[3])]}
    msg = f'''好哒我记住了~
    主人在{name[1]}的时候有一节{name[2]}课
    需持续{name[3]}周
    加油哦'''
    await write_in(path, data)
    await session.finish(msg)


@nonebot.on_command('下节课')
async def next_lesson(session: CommandSession):
    ev = session.event
    weday = time.gmtime()[6]  # 今天是周几
    nextlesson0 = await got_next_lesson()
    dic = await load_in(f'./timeable/loadmmy/{weday}-{nextlesson0}.json')
    #await session.send(str(dic)+f'user_id为{ev.user_id}')
    if str(ev.user_id) not in dic:
        await session.finish(f'''您下一节似乎没有课''')
    nextlesson = dic[str(ev.user_id)][0]
    await session.finish(f'''您的下一节课为:
    {nextlesson}
    不要忘记哦~''')

        



@nonebot.on_command('删除')
async def del_lesson(session: CommandSession):
    ev = session.event
    string = str(ev.message).split()
    try:
        path = await got_path(string[1])
    except:
        await session.finish(f'您的输入似乎有误，请重新输入，输入“课程表帮助”获取进一步帮助')
    if not await del_in(path, str(ev.user_id)):
        await session.finish("您这一时段似乎没课呢")
    await session.finish(f"删除{string[1]}成功！")

