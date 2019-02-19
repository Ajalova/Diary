import os
import sys
import pygame

pygame.init()
pygame.key.set_repeat(200, 70)


WIDTH = 650
HEIGHT = 600
STEP = 50
n = -1

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
background_image = pygame.image.load('data/fonus.jpg')

player = None
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
bonusi = pygame.sprite.Group()


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert_alpha()

    if color_key is not None:
        if color_key is -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    return image


def load_level(filename):
    filename = "data/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    # и подсчитываем максимальную длину    
    max_width = max(map(len, level_map))

    # дополняем каждую строку пустыми клетками ('.')    
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def generate_level(level):
    new_player, x, y = None, None, None
    
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == '=':
                Tile('stik', x, y)
            elif level[y][x] == 'b':
                Tile('stik', x, y)
                b = Player(x, y, tile_images['stik'])
            elif level[y][x] == '1':
                Tile('empty', x, y)
                s1 = Player(x, y, tile_images['star'])
            elif level[y][x] == '2':
                Tile('empty', x, y)
                s2 = Player(x, y, tile_images['star'])
            elif level[y][x] == '3':
                Tile('empty', x, y)
                s3 = Player(x, y, tile_images['star'])            
            elif level[y][x] == '@':
                Tile('empty', x, y)            
                new_player = Player(x, y, player_image)
    # вернем игрока, а также размер поля в клетках            
    return new_player, x, y, s1, s2, s3,b


def terminate():
    pygame.quit()
    sys.exit()


tile_images = {'wall': load_image('66.png'),'st': load_image('st.png'), 'empty': load_image('grass.png'),'star': load_image('star.png'),  'stik': load_image('stik.png')}
player_image = load_image('1.png')
tile_width = tile_height = 50


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        if tile_type!='many' and tile_type!='star':
            super().__init__(tiles_group, all_sprites)
        else:
            super().__init__(bonusi, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)
    
        

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y,im):
        super().__init__(player_group, all_sprites)
        self.image = im
        self.rect = self.image.get_rect().move(tile_width * pos_x , tile_height * pos_y)
            


player, level_x, level_y, s1, s2, s3,bb = generate_level(load_level("levelex.txt"))
running = True
x = False
up = False
Tile('st', 10, 0)

while running:
    b = False
    FPS = 70
    if load_level("levelex.txt")[(player.rect.y+50)//50][(player.rect.x)//50] != '=' and load_level("levelex.txt")[(player.rect.y+50)//50][(player.rect.x)//50] != '#':
        player.rect.y += STEP
        b = True
    if x==True:
        Tile('star', 10+n, 0)
        #print(n)
        x=False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if up is True:
                b = False
                up = False
            if load_level("levelex.txt")[(player.rect.y)//50][(player.rect.x-50)//50] == '1' and s1 in all_sprites:
                s1.kill()
                n+=1
                x = True
            if load_level("levelex.txt")[(player.rect.y+50)//50][(player.rect.x+50)//50] == '2' and s2 in all_sprites:
                s2.kill()
                n+=1
                x = True
            if load_level("levelex.txt")[(player.rect.y)//50][(player.rect.x+50)//50] == '3' and s3 in all_sprites:
                s3.kill()
                n+=1
                x = True
            if  load_level("levelex.txt")[(player.rect.y)//50][(player.rect.x+50)//50] == 'b' :
                bb.kill()
            if event.key == pygame.K_LEFT and load_level("levelex.txt")[(player.rect.y)//50][(player.rect.x-50)//50] != '='  and load_level("levelex.txt")[(player.rect.y)//50][(player.rect.x-50)//50] != '#':
                player.rect.x -= STEP
            if event.key == pygame.K_RIGHT and load_level("levelex.txt")[(player.rect.y)//50][(player.rect.x+50)//50] != '=' and load_level("levelex.txt")[(player.rect.y)//50][(player.rect.x+50)//50] != '#':
                player.rect.x += STEP
            if (event.key == pygame.K_UP) and (load_level("levelex.txt")[(player.rect.y-50)//50][(player.rect.x)//50] != '=') and (load_level("levelex.txt")[(player.rect.y-50)//50][(player.rect.x)//50] != '#'):
                player.rect.y -= STEP
                up = True
            if (event.key == pygame.K_SPACE) and (load_level("levelex.txt")[(player.rect.y-50)//50][(player.rect.x)//50] != '=') and (load_level("levelex.txt")[(player.rect.y-50)//50][(player.rect.x)//50] != '#'):
                if load_level("levelex.txt")[((player.rect.y-50)//50)-1][(player.rect.x)//50] != '#' and load_level("levelex.txt")[((player.rect.y-50)//50)-1][(player.rect.x)//50] != '=':
                    player.rect.y -= STEP*2
                else:
                    player.rect.y -= STEP
                up = True
                
    if b is False:
        FPS -= 40
    else:
        FPS += 100
    
    screen.blit(background_image, (0, 0)) 
    tiles_group.draw(screen)
    bonusi.draw(screen)
    player_group.draw(screen)
    if n==2:
        screen.blit(pygame.image.load('ura.jpg'), (0, 0))
    pygame.display.flip()
    pygame.display.update()
    clock.tick(FPS)
terminate()
