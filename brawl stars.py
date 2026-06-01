import pyxel
import math
import random

WIDTH = 240
HEIGHT = 160


# =========================
# 壁
# =========================
class Wall:
    def __init__(self, x, y, w, h):
        self.x, self.y, self.w, self.h = x, y, w, h

    def draw(self):
        pyxel.rect(self.x, self.y, self.w, self.h, 4)


# =========================
# 草むら
# =========================
class Bush:
    def __init__(self, x, y, w, h):
        self.x, self.y, self.w, self.h = x, y, w, h

    def draw(self):
        pyxel.rect(self.x, self.y, self.w, self.h, 3)


# =========================
# 弾（プレイヤー）
# =========================
class Bullet:
    def __init__(self, x, y, angle, speed, dmg, color):
        self.x, self.y = x, y
        self.dx = math.cos(angle) * speed
        self.dy = math.sin(angle) * speed
        self.dmg = dmg
        self.color = color
        self.r = 2
        self.alive = True

    def update(self, walls):
        nx = self.x + self.dx
        ny = self.y + self.dy

        for w in walls:
            if w.x < nx < w.x + w.w and w.y < ny < w.y + w.h:
                self.alive = False
                return

        self.x, self.y = nx, ny

        if not (0 < self.x < WIDTH and 0 < self.y < HEIGHT):
            self.alive = False

    def draw(self):
        pyxel.circ(self.x, self.y, self.r, self.color)


# =========================
# 敵弾
# =========================
class EnemyBullet:
    def __init__(self, x, y, angle):
        self.x, self.y = x, y
        self.dx = math.cos(angle) * 2.5
        self.dy = math.sin(angle) * 2.5
        self.r = 2
        self.alive = True

    def update(self, walls):
        nx = self.x + self.dx
        ny = self.y + self.dy

        for w in walls:
            if w.x < nx < w.x + w.w and w.y < ny < w.y + w.h:
                self.alive = False
                return

        self.x, self.y = nx, ny

        if not (0 < self.x < WIDTH and 0 < self.y < HEIGHT):
            self.alive = False

    def draw(self):
        pyxel.circ(self.x, self.y, self.r, 8)


# =========================
# 敵
# =========================
class Enemy:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.hp = 5
        self.speed = 0.6
        self.r = 6
        self.reload = 0
        self.range = 70
        self.alive = True

    def update(self, player, walls):
        bullets = []

        dx = player.x - self.x
        dy = player.y - self.y
        dist = math.sqrt(dx*dx + dy*dy)

        if self.reload > 0:
            self.reload -= 1

        # 追跡
        if dist > self.range:
            if dist > 0:
                dx /= dist
                dy /= dist

            nx = self.x + dx * self.speed
            ny = self.y + dy * self.speed

            if not any(w.x < nx < w.x + w.w and w.y < ny < w.y + w.h for w in walls):
                self.x, self.y = nx, ny

        # 攻撃
        else:
            if self.reload == 0:
                ang = math.atan2(player.y - self.y, player.x - self.x)
                bullets.append(EnemyBullet(self.x, self.y, ang))
                self.reload = 60

        return bullets

    def damage(self, d):
        self.hp -= d
        if self.hp <= 0:
            self.alive = False

    def draw(self):
        pyxel.circ(self.x, self.y, self.r, 8)
        pyxel.rect(self.x-6, self.y-10, 12, 2, 1)
        pyxel.rect(self.x-6, self.y-10, max(0, self.hp*2), 2, 11)


# =========================
# 仮想スティック
# =========================
class Stick:
    def __init__(self, x, y, r):
        self.cx, self.cy = x, y
        self.r = r
        self.x, self.y = x, y
        self.vx = 0
        self.vy = 0

    def update(self):
        self.vx = 0
        self.vy = 0

        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            mx, my = pyxel.mouse_x, pyxel.mouse_y
            dx, dy = mx - self.cx, my - self.cy
            dist = math.sqrt(dx*dx + dy*dy)

            if dist < self.r * 2:
                if dist > 0:
                    self.vx = dx / self.r
                    self.vy = dy / self.r

                if dist > self.r:
                    dx /= dist
                    dy /= dist
                    dx *= self.r
                    dy *= self.r

                self.x = self.cx + dx
                self.y = self.cy + dy
        else:
            self.x, self.y = self.cx, self.cy

    def draw(self):
        pyxel.circb(self.cx, self.cy, self.r, 7)
        pyxel.circ(self.x, self.y, 6, 7)


# =========================
# プレイヤー
# =========================
class Player:
    def __init__(self):
        self.x, self.y = 60, 60
        self.r = 6
        self.hp = 10
        self.reload = 0
        self.character = 0
        self.in_bush = False

    def move(self, vx, vy, walls):
        nx = self.x + vx * 2
        ny = self.y + vy * 2

        if not any(w.x < nx < w.x + w.w and w.y < ny < w.y + w.h for w in walls):
            self.x, self.y = nx, ny

    def shoot(self, ax, ay):
        if self.reload > 0:
            return []

        ang = math.atan2(ay, ax)
        bullets = []

        # Shelly
        if self.character == 0:
            for s in [-0.2, 0, 0.2]:
                bullets.append(Bullet(self.x, self.y, ang+s, 4, 1, 10))
            self.reload = 20

        # Colt
        elif self.character == 1:
            bullets.append(Bullet(self.x, self.y, ang, 6, 1, 9))
            self.reload = 5

        # Brock
        else:
            bullets.append(Bullet(self.x, self.y, ang, 3, 3, 14))
            self.reload = 40

        return bullets

    def update(self, walls, bushes):
        if self.reload > 0:
            self.reload -= 1

        self.in_bush = any(
            b.x < self.x < b.x + b.w and b.y < self.y < b.y + b.h
            for b in bushes
        )

    def draw(self):
        color = 11 if not self.in_bush else 5
        pyxel.circ(self.x, self.y, self.r, color)


# =========================
# GAME
# =========================
class App:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT)

        self.player = Player()
        self.move = Stick(40, 130, 18)
        self.aim = Stick(200, 130, 18)

        self.walls = [
            Wall(90, 40, 20, 80),
            Wall(150, 20, 20, 80)
        ]

        self.bushes = [
            Bush(120, 100, 40, 20)
        ]

        self.enemies = [Enemy(200, 40), Enemy(180, 120)]
        self.bullets = []
        self.ebullets = []

        pyxel.run(self.update, self.draw)

    def update(self):
        self.move.update()
        self.aim.update()

        self.player.move(self.move.vx, self.move.vy, self.walls)
        self.player.update(self.walls, self.bushes)

        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.bullets += self.player.shoot(self.aim.vx, self.aim.vy)

        for b in self.bullets:
            b.update(self.walls)

        for e in self.enemies:
            self.ebullets += e.update(self.player, self.walls)

        for eb in self.ebullets:
            eb.update(self.walls)

        # 当たり判定
        for b in self.bullets:
            for e in self.enemies:
                if math.hypot(b.x-e.x, b.y-e.y) < b.r + e.r:
                    b.alive = False
                    e.damage(b.dmg)

        for eb in self.ebullets:
            if math.hypot(eb.x-self.player.x, eb.y-self.player.y) < eb.r + self.player.r:
                eb.alive = False
                self.player.hp -= 1

        self.bullets = [b for b in self.bullets if b.alive]
        self.ebullets = [b for b in self.ebullets if b.alive]
        self.enemies = [e for e in self.enemies if e.alive]

    def draw(self):
        pyxel.cls(3)

        for b in self.bushes:
            b.draw()

        for w in self.walls:
            w.draw()

        for b in self.bullets:
            b.draw()

        for eb in self.ebullets:
            eb.draw()

        for e in self.enemies:
            e.draw()

        self.player.draw()

        self.move.draw()
        self.aim.draw()

        pyxel.text(5, 5, f"HP:{self.player.hp}", 7)


App()