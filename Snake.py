import pygame,sys,random
from pygame.math import Vector2

class SNAKE:

    def __init__(self):

        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(1,0)
        self.new_block = False

        self.head_up = pygame.image.load('Graphics/snake/head/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('Graphics/snake/head/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('Graphics/snake/head/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('Graphics/snake/head/head_left.png').convert_alpha()
		
        self.tail_up = pygame.image.load('Graphics/snake/tail/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('Graphics/snake/tail/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('Graphics/snake/tail/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('Graphics/snake/tail/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('Graphics/snake/body/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('Graphics/snake/body/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('Graphics/snake/body/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('Graphics/snake/body/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('Graphics/snake/body/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('Graphics/snake/body/body_bl.png').convert_alpha()

    
        self.update_head_graphics()

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index,block in enumerate(self.body):
            # 1.rect สำหรับ ตำเเหน่ง
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)
            # 2.ทิศทาง หน้าของหัวงู
            if index == 0: # ถ้าส่วนตำเเหน่งของงู มีค่าเท่ากับ 0 (ส่วนหัว)
                screen.blit(self.head,block_rect) # ให้เเสดง รูปภาพที่เป็น "self.head"
            elif index == len(self.body) - 1: # ถ้าส่วนตำเเหน่งของงู มีค่าเท่ากับ ส่วนทั้งหมดของงู - 1 (ส่วนปลายหาง)
                screen.blit(self.tail,block_rect)  # ให้เเสดง รูปภาพที่เป็น "self.tail"
            else:
                previous_block = self.body[index + 1] - block # บล็อกก่อนหน้า = 
                next_block = self.body[index - 1] - block # บล็อกถัดไป
            else:
                pygame.draw.rect(screen,(150,100,100),block_rect) # ให้เเสดงเป็นตัวงู

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0] # ให้ head_relation เท่ากับการ ที่ Vector ส่วนของงูในตำเเหน่งที่ 0(หัวงู) - Vector ส่วนของงูในตำเเหน่งที่ 1(ก่อนหัวงู) 
        if head_relation == Vector2(1,0): self.head = self.head_left # ถ้า head_relation มีค่าเท่ากับ Vector2(1,0) ให้ self.head เท่ากับ ภาพหัวงูหันด้านซ้าย
        elif head_relation == Vector2(-1,0): self.head = self.head_right # ถ้า head_relation มีค่าเท่ากับ Vector2(-1,0) ให้ self.head เท่ากับ ภาพหัวงูหันด้านขวา 
        elif head_relation == Vector2(0,1): self.head = self.head_up # ถ้า head_relation มีค่าเท่ากับ Vector2(0,1) ให้ self.head เท่ากับ ภาพหัวงูหันด้านบน
        elif head_relation == Vector2(0,-1): self.head = self.head_down # ถ้า head_relation มีค่าเท่ากับ Vector2(0,-1) ให้ self.head เท่ากับ ภาพหัวงูหันด้านล่าง

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1] # ให้ tail_relation เท่ากับการ ที่ Vector ส่วนของงูในตำเเหน่งที่ -2(ก่อนปลายหางงู) - Vector ส่วนของงูในตำเเหน่งที่ 1(ปลายหางงู) 
        if tail_relation == Vector2(1,0): self.tail = self.tail_left # ถ้า tail_relation มีค่าเท่ากับ Vector2(1,0) ให้ self.head เท่ากับ ภาพหางงูหันด้านซ้าย
        elif tail_relation == Vector2(-1,0): self.tail = self.tail_right # ถ้า tail_relation มีค่าเท่ากับ Vector2(-1,0) ให้ self.head เท่ากับ ภาพหางงูหันด้านขวา 
        elif tail_relation == Vector2(0,1): self.tail = self.tail_up # ถ้า tail_relation มีค่าเท่ากับ Vector2(0,1) ให้ self.head เท่ากับ ภาพหางงูหันด้านบน
        elif tail_relation == Vector2(0,-1): self.tail = self.tail_down # ถ้า tail_relation มีค่าเท่ากับ Vector2(0,-1) ให้ self.head เท่ากับ ภาพหางงูหันด้านล่าง






        #for block in self.body:
        #   # สร้าง rect
        #   x_pos = int(block.x * cell_size)
        #   y_pos = int(block.y * cell_size)
        #   block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)
        #   # วาด rectangle
        #   pygame.draw.rect(screen,(183,111,122),block_rect)

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
        screen.blit(apple,fruit_rect)
        #pygame.draw.rect(screen,(126,166,114),fruit_rect)

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
        self.check_fail()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()

    def check_collision(self):# หลักการ กินของงู
        if self.fruit.pos == self.snake.body[0]: # ถ้า ตำเเหน่งของผลไม้ เท่ากับ ตำเเหน่งที่ 0 ของงู  (ถ้า ผลไม้ อยู่ในตำเเหน่งเดียวกันกับ ส่วนหัวของงู)
            # เปลี่ยนตำเเหน่งของผลไม้ใหม่
            self.fruit.randomize()
            # เพิ่มจำนวนบล็อกให้กับงู (เพิ่มความยาวของงู 1 บล็อก)
            self.snake.add_block()
    
    def check_fail(self):
        # กรณีที่งูออกจาก screen
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number: # ถ้าหัวของงู(self.snake.body[0]) ไม่อยู่ระหว่าง 0 กับ 20(cell_number) ทั้งเเกน x เเละ y -> เกมจะจบทันที
            self.game_over()             
        # กรณีที่งูชนกับตัวเอง
        for block in self.snake.body[1:]:   # ให้ block เป็น ตำเเหน่งส่วนตัวของงูทั้งหมดยกเว้นส่วนที่เป็น ตำเเหน่งที่ 0 ของงู(ส่วนหัวของงู)
            if block == self.snake.body[0]: # ถ้า ตำเเหน่งส่วนตัวของงู เท่ากับ ตำเเหน่งที่ 0 ของงู  (ถ้า ส่วนตัวของงู อยู่ในตำเเหน่งเดียวกันกับ ส่วนหัวของงู) -> เกมจะจบทันที
                self.game_over() 

    def game_over(self):
        pygame.quit()
        sys.exit()


pygame.init()
cell_size = 40  # ขนาด cell
cell_number = 20 # จำนวน cell
screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size)) # ขนาดหน้าจอ
clock = pygame.time.Clock() # ตัวกำหนดค่า fps
apple = pygame.image.load('Graphics/fruit/apple.png').convert_alpha() # นำรูปเเอปเปิ้ลเข้า ปล. convert_alpha() ทำให้ pygame ทำงานง่ายขึ้นเฉยๆ

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

            if event.key == pygame.K_UP: # ถ้ามีเหตุการณ์ที่กดลูกศรขึ้น 
                if main_game.snake.direction.y != 1: # ถ้าทิศทางของงู ในพิกัด y ไม่เท่ากับ 1 (งูไม่ได้เคลื่อนไปทางด้านล่าง) 
                    main_game.snake.direction = Vector2(0,-1) # => งูจะเคลื่อนที่ไปทางด้านบน

            if event.key == pygame.K_DOWN: # ถ้ามีเหตุการณ์ที่กดลูกศรลง
                if main_game.snake.direction.y != -1: # ถ้าทิศทางของงู ในพิกัด y ไม่เท่ากับ -1 (งูไม่ได้เคลื่อนไปทางด้านบน)
                    main_game.snake.direction = Vector2(0,1) # => งูจะเคลื่อนที่ไปทางด้านล่าง

            if event.key == pygame.K_RIGHT: # ถ้ามีเหตุการณ์ที่กดลูกศรขวา 
                if main_game.snake.direction.x != -1: # ถ้าทิศทางของงู ในพิกัด x ไม่เท่ากับ -1 (งูไม่ได้เคลื่อนไปทางด้านซ้าย)
                    main_game.snake.direction = Vector2(1,0) # => งูจะเคลื่อนที่ไปทางขวา

            if event.key == pygame.K_LEFT: # ถ้ามีเหตุการณ์ที่กดลูกศรซ้าย
                if main_game.snake.direction.x != 1: # ถ้าทิศทางของงู ในพิกัด x ไม่เท่ากับ 1 (งูไม่ได้เคลื่อนไปทางด้านขวา)
                    main_game.snake.direction = Vector2(-1,0) # => งูจะเคลื่อนที่ไปทางซ้าย
                


    screen.fill((175,215,70)) # กำหนดสีของ screen
    main_game.draw_elements() # อยู่ใน class main
    pygame.display.update() # อยู่ใน class main
    clock.tick(60) # fps = 60