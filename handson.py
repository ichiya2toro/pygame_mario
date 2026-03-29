import pygame  

# 画面サイズを定義
W, H = 320, 270

# タイル数
TILE_X = 16
TILE_Y = 14


class Mario(pygame.sprite.Sprite):
    ''' マリオのクラス
    '''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('mario.png')
        self.rect = pygame.Rect(150, 200, 20, 20)

    def right(self):
        self.rect.x += 5


def main():
    ''' メイン関数
    '''
    # pygame初期化
    pygame.init()
    # 画面を作成
    win = pygame.display.set_mode((W, H))
    # クロックを生成
    clock = pygame.time.Clock()

    # スプライトグループを定義
    group = pygame.sprite.RenderUpdates()
    # マリオクラスを構築
    mario = Mario()
    # マリオをグループに追加
    group.add(mario)
    
    running = True
    # イベントループ

    while running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False   
            elif e.type == pygame.KEYDOWN:
                if e.key ==  pygame.K_RIGHT:
                    mario.right()

        # キーボードの状態を取得
        keys = pygame.key.get_pressed()
        print(keys[pygame.K_RIGHT]) 

        # 背景を塗りつぶす
        win.fill((135, 206, 235))  
        # グループを更新
        group.update()
        # グループを描画
        group.draw(win)

        # 画面全体を更新
        pygame.display.flip()

        # フレームレートを設定
        clock.tick(30)

if __name__ == '__main__':
    main()