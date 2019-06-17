# screen.py
# from pygame.graphic import render     # 패스 경로 지정하지 않아서 오류
from . import render


def screen():
    print('screen called')
    render.render()
