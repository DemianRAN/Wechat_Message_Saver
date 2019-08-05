# 导入模块
from wxpy import *
from time import gmtime, strftime

# 初始化机器人，扫码登陆
bot = Bot()

#指定群
group = bot.groups().search('XXXXXX')[0]


# 打印所有群成员
for member in group:
    print(member)
    
    
@bot.register(group) 
def print_messages(msg):
    file = 'C://Work//Chat_' + strftime("%Y%m%d", gmtime()) + '.txt'
    line = str(msg.member) + ':' + msg.text
    print(line)
    with open(file,'a', encoding='UTF-8') as f:
        f.write(line + '\n')

#堵塞线程
bot.join()
