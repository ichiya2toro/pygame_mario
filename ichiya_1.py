import pyxel

# キャラクターを描く関数 (ｘ座標，ｙ座標、体の色、輪郭線の色、顔の色)
def draw_character(x, y, body_color, outline_color, face_color):
   pyxel.circ(x, y, 8, body_color)
   pyxel.circb(x, y, 8, outline_color)
   pyxel.line(x - 4, y - 3, x - 4, y, face_color)
   pyxel.line(x + 2, y - 3, x + 2, y, face_color)
   pyxel.line(x - 4, y + 3, x + 2, y + 3, face_color)
   pyxel.pset(x - 5, y + 2, face_color)
   pyxel.pset(x + 3, y + 2, face_color) 


pyxel.init(160, 120, title="pyxel Drawing")
# 線
for i in range(40):
   pos = i * 4 + 1 
   pyxel.line(pos, 0, pos, 119, 2)
   pyxel.line(0, pos, 159, pos, 2)

# キャラクター
for _ in range(50):
   x = pyxel.rndi(0, 159)
   y = pyxel.rndi(0, 119)
   body_color = pyxel.rndi(6, 11)
   outline_color = pyxel.rndi(12, 15)
   face_color = pyxel.rndi(0, 5)

   draw_character(x, y, body_color, outline_color, face_color)
   

# for i in range(8):
#    x = i * 18 + 7
#    y = i * 10 + 25
#    draw_character(x, y, 10, 9, 8)

pyxel.show()



# pyxel.init(160, 120, title="pyxel Drawing")

# x = 45 # キャラクターの基準位置のｘ座標
# y = 40 # キャラクターの標準位置のy座標
# body_color = 3 # 体の色
# outline_color = 7 # 輪郭線の色
# face_color = 0 # 顔パーツの色

# pyxel.circ(x, y, 8, body_color)
# pyxel.circb(x, y, 8, outline_color)
# pyxel.line(x - 4, y - 3, x - 4, y, face_color)
# pyxel.line(x + 2, y - 3, x + 2, y, face_color)
# pyxel.line(x - 4, y + 3, x + 2, y + 3, face_color)
# pyxel.pset(x - 5, y + 2, face_color)
# pyxel.pset(x + 3, y + 2, face_color)

# x = 115# キャラクターの基準位置のｘ座標
# y = 80
#  # キャラクターの標準位置のy座標
# body_color = 8 # 体の色
# edge_color = 15 # 輪郭線の色
# face_color = 0 # 顔パーツの色

# pyxel.circ(x, y, 8, body_color)
# pyxel.circb(x, y, 8, edge_color)
# pyxel.line(x - 4, y - 3, x - 4, y, face_color)
# pyxel.line(x + 2, y - 3, x + 2, y, face_color)
# pyxel.line(x - 4, y + 3, x + 2, y + 3, face_color)
# pyxel.pset(x - 5, y + 2, face_color)
# pyxel.pset(x + 3, y + 2, face_color)

# キャラクターを描く関数 (ｘ座標，ｙ座標、体の色、輪郭線の色、顔の色)
# def draw_character(x, y, body_color, outline_color, face_color):
#    pyxel.circ(x, y, 8, body_color)
#    pyxel.circb(x, y, 8, outline_color)
#    pyxel.line(x - 4, y - 3, x - 4, y, face_color)
#    pyxel.line(x + 2, y - 3, x + 2, y, face_color)
#    pyxel.line(x - 4, y + 3, x + 2, y + 3, face_color)
#    pyxel.pset(x - 5, y + 2, face_color)
#    pyxel.pset(x + 3, y + 2, face_color) 



# draw_character(45, 40, 3, 7, 0)
# draw_character(55, 40, 3, 8, 0)
# draw_character(65, 40, 3, 9, 0)
# draw_character(75, 40, 3, 10, 0)

# for i in range(40):
#    pos = i * 18 + 17 * i
#    pyxel.line = i * 10 + 25 * i
#    pyxel.line(0, pos, 159, pos, 2)

#    draw_character(x, y, 3, 7, 0)


# pyxel.show()