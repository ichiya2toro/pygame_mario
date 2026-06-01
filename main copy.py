import pygame
import sys

# 1. 初期化
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Move the Square!")

# 2. 四角形の初期設定
# [x座標, y座標, 幅, 高さ]
player_pos = [400, 300]
player_size = 50
player_speed = 10

# フレームレート（FPS）を管理する時計
clock = pygame.time.Clock()

# 3. メインループ
running = True
while running:
    # --- A. イベント処理 ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- B. キー入力の取得 ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT]:
        player_pos[0] += player_speed
    if keys[pygame.K_UP]:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN]:
        player_pos[1] += player_speed

    # --- C. 描画処理 ---
    screen.fill((0, 0, 0))  # 画面を黒でクリア

    # 四角形を描く (描く場所, 色, [x, y, 幅, 高さ])
    pygame.draw.rect(screen, (255, 0, 0), (player_pos[0], player_pos[1], player_size, player_size))

    # 画面を更新
    pygame.display.flip()

    # --- D. フレームレートの設定 (1秒間に60回ループさせる) ---
    clock.tick(60)

pygame.quit()
sys.exit()