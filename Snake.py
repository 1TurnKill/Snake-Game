import pygame,sys,random
from pygame.math import Vector2

class SNAKE:

    def __init__(self):
        # สร้างตัวงู
        # ทิศทางการเคลื่อนที่เริ่มต้นของงู
        # การเพิ่มความยาวของงู
        self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)]
        self.direction = Vector2(1,0)
        self.new_block = False

    def draw_snake(self):
        for block in self.body:
            # สร้าง rect
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)
            # วาด rectangle
            pygame.draw.rect(screen,(183,111,122),block_rect)

    def move_snake(self): # ให้ทำความเข้าใจ "การเคลื่อนไหวของตัวงู" ก่อนที่จะไป "การเพิ่มความยาวของงู"
        if self.new_block == True:
            # การเพิ่มความยาวของงู            
            body_copy = self.body[:] # ให้ body_copy มีค่าเท่ากับ ส่วนตัวของงูทั้งหมด 
                                     # self.body[:] => คัดลอก(:) ส่วนของงูทั้งหมด                                  
            body_copy.insert(0,body_copy[0] + self.direction) # => ในตำเเหน่งที่เป็นส่วนหัว(0) จะมีการเพิ่มบล็อก ตามทิศทางการเคลื่อนที่ของงู(self.direction)
                                                              # ปล.บล็อกที่เพิ่ม จะเอามาจากส่วนหัวของงู(body_copy[0])                                                   
            self.body = body_copy[:] # เป็นการคืนค่า ส่วนของงูทั้งหมด(self.body) กลับไปยัง การคัดลอกอีกครั้ง(body_copy[:])
            self.new_block = False #**ต้องมีบรรทัดนี้ เพื่อให้กลับไป ชุดคำสั่ง "การเคลื่อนไหวของตัวงู"
        else: 
            # การเคลื่อนไหวของตัวงู
            body_copy = self.body[:-1] # ให้ body_copy มีค่าเท่ากับ ส่วนตัวของงูทั้งหมดยกเว้นส่วนปลายหาง
                                       # self.body[:-1] => คัดลอก(:) ส่วนของงูทั้งหมด ยกเว้นส่วนสุดท้าย,ส่วนปลายหาง(-1)
            body_copy.insert(0,body_copy[0] + self.direction) # => ในตำเเหน่งที่เป็นส่วนหัว(0) จะมีการเพิ่มบล็อก ตามทิศทางการเคลื่อนที่ของงู(self.direction)
                                                              # ปล.บล็อกที่เพิ่ม จะเอามาจากส่วนหัวของงู(body_copy[0])                                                        
            self.body = body_copy[:] # เป็นการคืนค่า ส่วนของงูทั้งหมด(self.body) กลับไปยัง การคัดลอกอีกครั้ง(body_copy[:])

    def add_block(self):
        self.new_block = True

class FRUIT:

    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        # สร้าง rect
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
        # วาด rectangle
        pygame.draw.rect(screen,(126,166,114),fruit_rect)

    def randomize(self):
        # สร้าง ตำเเหน่งพิกัด x เเละ y
        # วาด square (ผลไม้)
        # สุ่มการเกิดของผลไม้
        self.x = random.randint(0,cell_number - 1) # -1 เพื่อไม่ให้การสุ่มของผลไม้เกินหน้าจอในเเกน x
        self.y = random.randint(0,cell_number - 1) # -1 เพื่อไม่ให้การสุ่มของผลไม้เกินหน้าจอในเเกน y
        self.pos = Vector2(self.x,self.y)
       
class MAIN:
    # เป็น class ที่รวมคำสั่ง ผลไม้เเละงู 
    def __init__(self):
        self.snake = SNAKE() 
        self.fruit = FRUIT()

    def update(self):
        self.snake.move_snake()
        self.check_collision()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def check_collision(self):# หลักการ กินของงู
        if self.fruit.pos == self.snake.body[0]: # ถ้า ตำเเหน่งของผลไม้ เท่ากับ ตำเเหน่งที่ 0 ของงู  (ถ้า ผลไม้ อยู่ในตำเเหน่งเดียวกันกับ ส่วนหัวของงู)
            # เปลี่ยนตำเเหน่งของผลไม้ใหม่
            self.fruit.randomize()
            # เพิ่มจำนวนบล็อกให้กับงู (เพิ่มความยาวของงู 1 บล็อก)
            self.snake.add_block()

pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size))
clock = pygame.time.Clock()

# ตั้งค่าเวลา(millisecond) การอัพเดตข้อมูลบน screen
SCREEN_UPDATE = pygame.USEREVENT 
pygame.time.set_timer(SCREEN_UPDATE,150)

main_game = MAIN()

while True:
    for event in pygame.event.get():
        # event การออกเกม
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # event การอัพเดตการเคลื่อนไหวของงูบนหน้า screen
        if event.type == SCREEN_UPDATE:
            main_game.update()
        # event การควบคุมเคลื่อนไหวของงู จาก keyboard
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                main_game.snake.direction = Vector2(0,-1) # ถ้ากดลูกศรขึ้น => งูจะเคลื่อนที่ไปทางด้านบน
            if event.key == pygame.K_DOWN:
                main_game.snake.direction = Vector2(0,1) # ถ้ากดลูกศรลง => งูจะเคลื่อนที่ไปทางด้านล่าง
            if event.key == pygame.K_RIGHT:
                main_game.snake.direction = Vector2(1,0) # ถ้ากดลูกศรขวา => งูจะเคลื่อนที่ไปทางขวา
            if event.key == pygame.K_LEFT:
                main_game.snake.direction = Vector2(-1,0) # ถ้ากดลูกศรซ้าย => งูจะเคลื่อนที่ไปทางซ้าย
                


    screen.fill((175,215,70))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)