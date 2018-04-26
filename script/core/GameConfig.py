import core.data as data
import os
from core.pycfg import gamepath
import core.ValueHandle as valuehandle

# 读取配置数据
def configData():
    configPath = os.path.join(gamepath,'data','core_cfg.json')
    configData = data._loadjson(configPath)
    return configData

# 读取字体样式配置数据
def getFontData(listId):
    FontPath = os.path.join(gamepath,'data','FontConfig.json')
    FontData = data._loadjson(FontPath)
    return FontData[listId]

# 读取字体样式配置列表
def getFontDataList():
    FontPath = os.path.join(gamepath, 'data', 'FontConfig.json')
    FontData = data._loadjson(FontPath)
    fontList = valuehandle.dictKeysToList(FontData)
    return fontList

#配置数据定义
game_name = configData()['game_name']
verson = configData()['verson']
author = configData()['author']
verson_time = configData()['verson_time']
background_color = configData()['background_color']
language = configData()['language']
window_width = configData()['window_width']
window_hight = configData()['window_hight']
textbox_width = configData()['textbox_width']
textbox_hight = configData()['textbox_hight']
text_width = int(configData()['text_width'])
text_hight = int(configData()['text_hight'])
cursor = configData()['cursor']
year = configData()["year"]
month = configData()["month"]
day = configData()["day"]
hour = configData()["hour"]
minute = configData()["minute"]
max_save = configData()['max_save']
save_page = configData()['save_page']
playerlist_show = configData()['playerlist_show']
text_wait = configData()['text_wait']