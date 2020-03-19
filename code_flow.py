import random
import pygame
from pygame.locals import *
from sys import exit
 
PANEL_width = 1920
PANEL_highly = 1080
FONT_PX = 20
 
pygame.init()
 
# 创建一个可是窗口
winSur = pygame.display.set_mode((PANEL_width, PANEL_highly), RESIZABLE, 32)
 
font = pygame.font.SysFont("123.ttf", 25)
 
bg_suface = pygame.Surface((PANEL_width, PANEL_highly), flags=pygame.SRCALPHA)
 
pygame.Surface.convert(bg_suface)
 
bg_suface.fill(pygame.Color(0, 0, 0, 16))
 
winSur.fill((0, 0, 0))
 
# 数字版
# texts = [font.render(str(i), True, (0, 255, 0)) for i in range(10)]
 
# # 二进制版
# letter = ['1', '0', '1', '1', '1', '0', '0', '0', '1', '0', '1', '0', '1', '0', '0', '1', '1', '0', '0', '0', '1', '1'
#           ,'1', '0', '1', '0', '0', '1', '0', '1']
 
# # 汉字版,你看不到字
# letter = ['我', '爱', '你', '我', '爱你', '我爱你', '我非常爱你', '我爱你', '我爱', '我', '爱', '你',
#           '我爱你', '爱', '我', '爱你', '我', '我爱', '爱你', '你']
#
# #  字母版
letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v'
           ,'w', 'x', 'y', 'z']
 
texts = [
    font.render(str(letter[i]), True, (0, 255, 0)) for i in range(20)
]
 
# 按屏幕的宽带计算可以在画板上放几列坐标并生成一个列表
column = int(PANEL_width / FONT_PX)
drops = [0 for i in range(column)]
 
while True:
    # 从队列中获取事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
 
            chang = pygame.key.get_pressed()
            if (chang[32]):
                exit()
 
    # 将暂停一段给定的毫秒数
    pygame.time.delay(30)
 
    # 重新编辑图像第二个参数是坐上角坐标
    winSur.blit(bg_suface, (0, 0))
 
    for i in range(len(drops)):
        text = random.choice(texts)
 
        # 重新编辑每个坐标点的图像
        winSur.blit(text, (i * FONT_PX, drops[i] * FONT_PX))
 
        drops[i] += 1
        if drops[i] * 10 > PANEL_highly or random.random() > 0.95:
            drops[i] = 0
 
    pygame.display.flip()
