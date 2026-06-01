import pyxel


# ウサギさんを描く関数
def draw_rabbit(x, y, color):
    pyxel.line(x + 2, y, x + 2, y + 2, color)
    pyxel.line(x + 4, y, x + 4, y + 4, color)
    pyxel.rect(x + 2, y + 3, 4, 3, color)
    pyxel.rect(x + 1, y + 6, 4, 3, color)
    pyxel.line(x, y + 9, x + 2, y + 9, color)
    pyxel.line(x + 4, y + 9, x + 5, y + 9, color)
    pyxel.pset(x + 3, y + 4, 8)
    pyxel.pset(x + 5, y + 4, 8)


pyxel.init(80, 60, title="ichiyas cute rabbit ") 

rabbit_x = 37 # ウサギさんのⅹ座標
rabbit_y = 10 # ウサギさんのｙ座標
rabbit_vy = 0 #ウサギさんのｘ方向の速度
rabbit_height = 10 # ウサギさんの高さ
rabbit_color = 15 # ウサギさんの色

while True:

    rabbit_y += rabbit_vy
    rabbit_vy += 0.1

    rabbit_bounce_y = pyxel.height - rabbit_height
    if rabbit_y >= rabbit_bounce_y:
        rabbit_y = rabbit_bounce_y
        rabbit_vy *= -0.95

    pyxel.cls(1)
    draw_rabbit(rabbit_x, rabbit_y, rabbit_color)
    pyxel.flip()

    # rabbit_x += rabbit_vx
    # rabbit_vx += 0.1

    # if rabbit_x >= pyxel.width:
    #     rabbit_x = -6
    #     rabbit_vx = 0

    # pyxel.cls(1)
    # draw_rabbit(rabbit_x, 25, 15)

    # pyxel.flip()
    # rabbit_x += 1
