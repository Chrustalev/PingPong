from pygame import *


# нам нужны такие картинки:
img_ball = "tenis_ball.png" # фон игры
img_racket = "racket.png" # герой

# класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
  # конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # Вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)

        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
  # метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# класс главного игрока
class Player(GameSprite):
    # метод для управления спрайтом стрелками клавиатуры
    def updater(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 100:
            self.rect.y += self.speed

    def updatel(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 100:
            self.rect.y += self.speed


# Создаем окошко
win_width = 700
win_height = 500
display.set_caption("Ping pong")
window = display.set_mode((win_width, win_height))


# создаем спрайты
racket1 = Player(img_racket, 5, win_height/2, 80, 100, 10)
racket2 = Player(img_racket, win_width-70, win_height/2, 80, 100, 10)

# переменная "игра закончилась": как только там True, в основном цикле перестают работать спрайты
finish = False
# Основной цикл игры:
run = True # флаг сбрасывается кнопкой закрытия окна
while run:
    # событие нажатия на кнопку Закрыть
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        # обновляем фон
        window.fill((0,0,0))

        # производим движения спрайтов
        racket1.updater()
        racket2.updatel()


        # обновляем их в новом местоположении при каждой итерации цикла
        racket1.reset()
        racket2.reset()


        display.update()
    # цикл срабатывает каждую 0.05 секунд
    time.delay(50)