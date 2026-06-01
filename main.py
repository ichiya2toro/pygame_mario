import pygame

#　画面サイズを定義
W, H = 320, 270

# タイル数
TILE_X = 16
TILE_Y = 14


class Mario(pygame.sprite.Sprite):
    ''' マリオのクラス
    '''
    WALK_ANIME_IDX = [0, 0, 0, 1, 1, 1]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # 左右どちら向きかのフラグを定義
        self.__isleft = False
        # 歩くフラグ
        self.__walkidx = 0
        # y輪方向移動距離
        self.__vy = 0
        # マリオが地面にいるかどうか
        self.__on_ground = True

        # マリオの画像を読み込んでおく
        self.__imgs = [
            pygame.image.load('mario001.png'),
            pygame.image.load('mario002.png')
        ]
            
        self.image = self.__imgs[0]
        self.rect = pygame.Rect(150, 180, 20, 208)
    
    
    def __right(self):
        self.rect.x += 5
        self.__isleft = False
        self.__walkidx += 1

    def __left(self):
        self.rect.x -= 5
        self.__isleft = True
        self.__walkidx += 1

    def __jump(self):
        if self.__on_ground:
            self.__vy = -15
            self.__on_ground = False
       


    def update(self):
        # キーボードの状態を取得
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.__right()
        if keys[pygame.K_LEFT]:
            self.__left()

        if keys[pygame.K_SPACE]:
            self.__jump()   

        # y軸方向に移動
        if not self.__on_ground:
            self.rect.y += self.__vy
            self.__vy += 1

            if self.rect.y >= 180:
                self.rect.y = 180
                self.__on_ground = True
       
        self.image = pygame.transform.flip(self.__imgs[self.WALK_ANIME_IDX[self.__walkidx % 6]], self.__isleft, False)

def main():
    ''' メイン関数
    '''
    # pygame初期化
    pygame.init()
    # 画面を作成
    win = pygame.display.set_mode((W, H))
    # クロックを作成
    clock = pygame.time.Clock()

    #　スプライトグループを定義
    group = pygame.sprite.RenderUpdates()
    # マリオクラスを構築
    mario = Mario()
    # マリオをグループに追加
    group.add(mario)

    # イベントループ
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
         

        # 背景を塗りつぶす
        win.fill((135, 206, 235))  

        # グループを更新
        group.update()

        #  グループを描画
        group.draw(win) 

        # 画面全体を更新    
        pygame.display.flip()

        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()