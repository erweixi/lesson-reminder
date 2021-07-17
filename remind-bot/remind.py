import nonebot
import time
from .load import *

'''
In this part,you need to change the time to fit in with your needs.
Every nonebot.scheduler.scheduled_job means a pre-class reminder.
If it's not five classes a day, please change the numbers of nonebot.scheduler.scheduled_job and its internal "now"
'''


@nonebot.scheduler.scheduled_job('cron', day='*', hour='8', minute='10')
async def one():
    bot = nonebot.get_bot()
    weday = time.gmtime()[6]  # 今天是周几
    now = 0
    dic = await load_in(f'./timeable/loadmmy/{weday}-{now}.json')
    for i in dic:
        await bot.send_private_msg(user_id=i, message=f'叮铃铃~~检测到下节课为{dic[i][0]}，起床准备上课啦！！！')


@nonebot.scheduler.scheduled_job('cron', day='*', hour='10', minute='05')
async def two():
    bot = nonebot.get_bot()
    weday = time.gmtime()[6]  # 今天是周几
    now = 1
    dic = await load_in(f'./timeable/loadmmy/{weday}-{now}.json')
    for i in dic:
        await bot.send_private_msg(user_id=i, message=f'叮铃铃~~检测到下节课为{dic[i][0]}，记得好好上课哟~')


@nonebot.scheduler.scheduled_job('cron', day='*', hour='13', minute='40')
async def three():
    bot = nonebot.get_bot()
    weday = time.gmtime()[6]  # 今天是周几
    now = 2
    dic = await load_in(f'./timeable/loadmmy/{weday}-{now}.json')
    for i in dic:
        await bot.send_private_msg(user_id=i, message=f'叮铃铃~~检测到下节课为{dic[i][0]}，准备好迎接一个清爽的下午了吗！')


@nonebot.scheduler.scheduled_job('cron', day='*', hour='15', minute='35')
async def four():
    bot = nonebot.get_bot()
    weday = time.gmtime()[6]  # 今天是周几
    now = 3
    dic = await load_in(f'./timeable/loadmmy/{weday}-{now}.json')
    for i in dic:
        await bot.send_private_msg(user_id=i, message=f'叮铃铃~~检测到下节课为{dic[i][0]}，这个下午过得还开心吗~')


@nonebot.scheduler.scheduled_job('cron', day='*', hour='18', minute='20')
async def five():
    bot = nonebot.get_bot()
    weday = time.gmtime()[6]  # 今天是周几
    now = 4
    dic = await load_in(f'./timeable/loadmmy/{weday}-{now}.json')
    for i in dic:
        await bot.send_private_msg(user_id=i, message=f'叮铃铃~~检测到主人下节课为{dic[i][0]}，这是最后一节课啦，主人加油哦！')
