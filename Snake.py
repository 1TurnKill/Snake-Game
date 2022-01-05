import pygame,sys,random
from pygame.math import Vector2

class SNAKE:

    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)] # ตัวงู
        self.direction = Vector2(0,0) # ทิศทางที่งูเริ่มเคลื่อนที่
        self.new_block = False

        self.head_up = pygame.image.load('Graphics/snake/head/head_up.png').convert_alpha() # ภาพหัว หันด้านบน
        self.head_down = pygame.image.load('Graphics/snake/head/head_down.png').convert_alpha() # ภาพหัว หันด้านล่าง
        self.head_right = pygame.image.load('Graphics/snake/head/head_right.png').convert_alpha() # ภาพหัว หันด้านขวา
        self.head_left = pygame.image.load('Graphics/snake/head/head_left.png').convert_alpha() # ภาพหัว หันด้านซ้าย
		
        self.tail_up = pygame.image.load('Graphics/snake/tail/tail_up.png').convert_alpha() # ภาพหาง หันด้านบน
        self.tail_down = pygame.image.load('Graphics/snake/tail/tail_down.png').convert_alpha() # ภาพหาง หันด้านล่าง
        self.tail_right = pygame.image.load('Graphics/snake/tail/tail_right.png').convert_alpha() # ภาพหาง หันด้านขวา
        self.tail_left = pygame.image.load('Graphics/snake/tail/tail_left.png').convert_alpha() # ภาพหาง หันด้านซ้าย

        self.body_vertical = pygame.image.load('Graphics/snake/body/body_vertical.png').convert_alpha() # ภาพตัว เเนวตั้ง(พิกัด x เดียวกัน)
        self.body_horizontal = pygame.image.load('Graphics/snake/body/body_horizontal.png').convert_alpha() # ภาพตัว เเนวนอน(พิกัด y เดียวกัน)

        self.body_topright = pygame.image.load('Graphics/snake/body/body_topright.png').convert_alpha() # ภาพตัวของงู ที่มาจากด้านบนเเล้วไปทางขวา
        self.body_topleft = pygame.image.load('Graphics/snake/body/body_topleft.png').convert_alpha() # ภาพตัวของงู ที่มาจากด้านบนเเล้วไปทางซ้าย
        self.body_bottomright = pygame.image.load('Graphics/snake/body/body_bottomright.png').convert_alpha() # ภาพตัวของงู ที่มาจากด้านล่างเเล้วไปทางขวา
        self.body_bottomleft = pygame.image.load('Graphics/snake/body/body_bottomleft.png').convert_alpha() # ภาพตัวของงู ที่มาจากด้านล่างเเล้วไปทางซ้าย
        
        self.eat_sound = pygame.mixer.Sound('Sound/Eat.wav') # เสียงกิน
        self.eat_sound.set_volume(0.3) # ความดังเสียงกิน 
        self.crash_sound = pygame.mixer.Sound('Sound/Crash.wav') # เสียงชน
        self.crash_sound.set_volume(0.3) # ความดังเสียงชน
        self.right_sound = pygame.mixer.Sound('Sound/Right.wav') # เสียงหันขวา
        self.right_sound.set_volume(0.3) # ความดังเหันขวา
        self.up_sound = pygame.mixer.Sound('Sound/Up.wav') # เสียงหันบน
        self.up_sound.set_volume(0.3) # ความดังเหันบน
        self.left_sound = pygame.mixer.Sound('Sound/Left.wav') # เสียงหันซ้าย
        self.left_sound.set_volume(0.3) # ความดังหันซ้าย
        self.down_sound = pygame.mixer.Sound('Sound/Down.wav') # เสียงหันล่าง
        self.down_sound.set_volume(0.3) # ความดังหันล่าง
        # *ปล.เสียงดังสุดคือ 1 เบาสุดคือ 0(ไม่ได้ยิน)

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
                previous_block = self.body[index + 1] - block # บล็อกก่อนหน้า = (ตำเเหน่งตัวของงูปัจจุบัน + 1) - ตำเเหน่งตัวของงูทั้งหมด 
                next_block = self.body[index - 1] - block # บล็อกถัดไป = (ตำเเหน่งตัวของงูปัจจุบัน - 1) - ตำเเหน่งตัวของงูทั้งหมด
                if previous_block.x == next_block.x: # ถ้าพิกัด x ของบล็อกก่อนหน้า มีค่าเท่ากับ พิกัด x ของบล็อกถัดไป
                    screen.blit(self.body_vertical,block_rect) # ให้เเสดง รูปภาพที่เป็น "ภาพตัว เเนวตั้ง(พิกัด x เดียวกัน)"
                elif previous_block.y == next_block.y: # ถ้าพิกัด y ของบล็อกก่อนหน้า มีค่าเท่ากับ พิกัด y ของบล็อกถัดไป
                    screen.blit(self.body_horizontal,block_rect) # ให้เเสดง รูปภาพที่เป็น "ภาพตัว เเนวนอน(พิกัด y เดียวกัน)"
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1: # ถ้า บล็อกก่อนหน้าอยู่ถัดจากบล็อกปัจจุบันด้านซ้าย เเละ บล็อกถัดไปอยู่ถัดจากบล็อกปัจจุบันด้านบน
                                                                                                                       # หรือ บล็อกก่อนหน้าอยู่ถัดจากบล็อกปัจจุบันด้านบน เเละ บล็อกถัดไปอยู่ถัดจากบล็อกปัจจุบันด้านซ้าย
                        screen.blit(self.body_topleft,block_rect) # ให้เเสดง รูปภาพที่เป็น "ภาพตัวของงู ที่มาจากด้านบนเเล้วไปทางซ้าย"

                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1: # ถ้า บล็อกก่อนหน้าอยู่ถัดจากบล็อกปัจจุบันด้านขวา เเละ บล็อกถัดไปอยู่ถัดจากบล็อกปัจจุบันด้านบน
                                                                                                                       # หรือ บล็อกก่อนหน้าอยู่ถัดจากบล็อกปัจจุบันด้านบน เเละ บล็อกถัดไปอยู่ถัดจากบล็อกปัจจุบันด้านขวา
                        screen.blit(self.body_topright,block_rect) # ให้เเสดง รูปภาพที่เป็น "ภาพตัวของงู ที่มาจากด้านบนเเล้วไปทางขวา"

                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1: # ถ้า บล็อกก่อนหน้าอยู่ถัดจากบล็อกปัจจุบันด้านซ้าย เเละ บล็อกถัดไปอยู่ถัดจากบล็อกปัจจุบันด้านล่าง
                                                                                                                       # หรือ บล็อกก่อนหน้าอยู่ถัดจากบล็อกปัจจุบันด้านล่าง เเละ บล็อกถัดไปอยู่ถัดจากบล็อกปัจจุบันด้านซ้าย
                        screen.blit(self.body_bottomleft,block_rect) # ให้เเสดง รูปภาพที่เป็น "ภาพตัวของงู ที่มาจากด้านล่างเเล้วไปทางซ้าย"

                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:   # ถ้า บล็อกก่อนหน้าอยู่ถัดจากบล็อกปัจจุบันด้านขวา เเละ บล็อกถัดไปอยู่ถัดจากบล็อกปัจจุบันด้านล่าง
                                                                                                                       # หรือ บล็อกก่อนหน้าอยู่ถัดจากบล็อกปัจจุบันด้านล่าง เเละ บล็อกถัดไปอยู่ถัดจากบล็อกปัจจุบันด้านขวา
                        screen.blit(self.body_bottomright,block_rect) # ให้เเสดง รูปภาพที่เป็น "ภาพตัวของงู ที่มาจากด้านล่างเเล้วไปทางขวา"
                    
    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0] # ให้ head_relation เท่ากับการ ที่ Vector ส่วนของงูในตำเเหน่งที่ 0(หัวงู) - Vector ส่วนของงูในตำเเหน่งที่ 1(ก่อนหัวงู) 
        if head_relation == Vector2(1,0): self.head = self.head_left # ถ้า head_relation มีค่าเท่ากับ Vector2(1,0) ให้ self.head เท่ากับ "ภาพหัว หันด้านซ้าย"
        elif head_relation == Vector2(-1,0): self.head = self.head_right # ถ้า head_relation มีค่าเท่ากับ Vector2(-1,0) ให้ self.head เท่ากับ "ภาพหัว หันด้านขวา" 
        elif head_relation == Vector2(0,1): self.head = self.head_up # ถ้า head_relation มีค่าเท่ากับ Vector2(0,1) ให้ self.head เท่ากับ "ภาพหัว หันด้านบน"
        elif head_relation == Vector2(0,-1): self.head = self.head_down # ถ้า head_relation มีค่าเท่ากับ Vector2(0,-1) ให้ self.head เท่ากับ "ภาพหัว หันด้านล่าง"

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1] # ให้ tail_relation เท่ากับการ ที่ Vector ส่วนของงูในตำเเหน่งที่ -2(ก่อนปลายหางงู) - Vector ส่วนของงูในตำเเหน่งที่ 1(ปลายหางงู) 
        if tail_relation == Vector2(1,0): self.tail = self.tail_left # ถ้า tail_relation มีค่าเท่ากับ Vector2(1,0) ให้ self.head เท่ากับ "ภาพหาง หันด้านซ้าย"
        elif tail_relation == Vector2(-1,0): self.tail = self.tail_right # ถ้า tail_relation มีค่าเท่ากับ Vector2(-1,0) ให้ self.head เท่ากับ "ภาพหาง หันด้านขวา"
        elif tail_relation == Vector2(0,1): self.tail = self.tail_up # ถ้า tail_relation มีค่าเท่ากับ Vector2(0,1) ให้ self.head เท่ากับ "ภาพหาง หันด้านบน"
        elif tail_relation == Vector2(0,-1): self.tail = self.tail_down # ถ้า tail_relation มีค่าเท่ากับ Vector2(0,-1) ให้ self.head เท่ากับ "ภาพหาง หันด้านล่าง"

        #for block in self.body:
        #   # สร้าง rect
        #   x_pos = int(block.x * cell_size)
        #   y_pos = int(block.y * cell_size)
        #   block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)
        #   # วาด rectangle
        #   pygame.draw.rect(screen,(183,111,122),block_rect)

    def move_snake(self): # ให้ทำความเข้าใจ "การเคลื่อนไหวของตัวงู" ก่อนที่จะไป "การเพิ่มความยาวของงู"
        if self.direction == Vector2(0,0): 
            return # ถ้างูไม่เคลื่อนที่ จะคืนค่ากลับไป เเละหยุดการทำงานของ คำสั่งด้านล่าง
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
    
    def reset(self): # ให้งูกลับไปตำเเหน่งเริ่มต้น เเละ หยุดนิ่ง
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(0,0)

    def add_block(self):
        self.new_block = True

    def play_eat_sound(self):
        self.eat_sound.play()

    def play_crash_sound(self):
        self.crash_sound.play()

    def play_right_sound(self):
        self.right_sound.play()

    def play_up_sound(self):
        self.up_sound.play()

    def play_left_sound(self):
        self.left_sound.play()
    
    def play_down_sound(self):
        self.down_sound.play()

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
        self.musicbackground_sound = pygame.mixer.Sound('Sound/music background.wav') # เสียงเพลงประกอบ
        self.musicbackground_sound.set_volume(0.1) # ความดังเสียงเพลงประกอบ
        self.musicbackground_sound.play(loops = -1) # เสียงเพลงประกอบทำงานไม่หยุด

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def check_collision(self):# หลักการ กินของงู
        if self.fruit.pos == self.snake.body[0]: # ถ้า ตำเเหน่งของผลไม้ เท่ากับ ตำเเหน่งที่ 0 ของงู  (ถ้า ผลไม้ อยู่ในตำเเหน่งเดียวกันกับ ส่วนหัวของงู)
            # ให้มีการเล่นเสียง eat_sound
            self.snake.play_eat_sound()
            # เปลี่ยนตำเเหน่งของผลไม้ใหม่
            self.fruit.randomize()
            # เพิ่มจำนวนบล็อกให้กับงู (เพิ่มความยาวของงู 1 บล็อก)
            self.snake.add_block()

        for block in self.snake.body[1:]: # ให้ block เป็น ส่วนตัวของงูตั้งเเต่ตำเเหน่งที่ 1 จน ถึง ตำเเหน่งสุดท้าย (เอาส่วนตัวของงูทั้งหมดยกเว้น ตำเเหน่งที่ 0,หัว) 
            if block == self.fruit.pos: # ถ้า block เท่ากับ ตำเเหน่งของผลไม้
                self.fruit.randomize() # ให้มีการเปลี่ยนตำเเหน่งของผลไม้ใหม่ใหม่
  
    def check_fail(self):
        # กรณีที่งูออกจาก screen
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number: # ถ้าหัวของงู(self.snake.body[0]) ไม่อยู่ระหว่าง 0 กับ 20(cell_number) ทั้งเเกน x เเละ y -> เกมจะจบทันที
            self.game_over() # ให้งูกลับไปตำเเหน่งเริ่มต้น เเละ หยุดนิ่ง     
        # กรณีที่งูชนกับตัวเอง
        if self.snake.direction == Vector2(0,0): 
            return # ถ้างูไม่เคลื่อนที่ จะคืนค่ากลับไป เเละหยุดการทำงานของคำสั่งด้านล่าง
        for block in self.snake.body[1:]:   # ให้ block เป็น ตำเเหน่งส่วนตัวของงูทั้งหมดยกเว้นส่วนที่เป็น ตำเเหน่งที่ 0 ของงู(ส่วนหัวของงู)
            if block == self.snake.body[0]: # ถ้า ตำเเหน่งส่วนตัวของงู เท่ากับ ตำเเหน่งที่ 0 ของงู  (ถ้า ส่วนตัวของงู อยู่ในตำเเหน่งเดียวกันกับ ส่วนหัวของงู) -> เกมจะจบทันที 
                self.game_over() # ให้งูกลับไปตำเเหน่งเริ่มต้น เเละ หยุดนิ่ง
            
    def game_over(self):
        self.snake.play_crash_sound()
        self.snake.reset() # ให้งูกลับไปตำเเหน่งเริ่มต้น เเละ หยุดนิ่ง

    def draw_grass(self):
        grass_color = (167,209,61) # สีเขียวเข้ม
        for row in range(cell_number): #ให้ เเถวในเเนวนอน เป็น การจัดลำดับตัวเลขของ cell_number (0,1,2,3,4,..,19)
            if row % 2 == 0: # ถ้า เเถวในเเนวนอน หาร 2 เเล้วเหลือเศษ 0 -> เลขคู่
                for col in range(cell_number): #ให้ เเถวในเเนวตั้ง เป็น การจัดลำดับตัวเลขของ cell_number (0,1,2,3,4,..,19)
                    if col % 2 == 0: # ถ้า เเถวในเเนวตั้ง หาร 2 เเล้วเหลือเศษ 0 -> เลขคู่
                        # สร้าง rect
                        grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                        # วาด rectangle
                        pygame.draw.rect(screen,grass_color,grass_rect)
            else:
                for col in range(cell_number): #ให้ เเถวในเเนวตั้ง เป็น การจัดลำดับตัวเลขของ cell_number (0,1,2,3,4,..,19)
                    if col % 2 != 0: # ถ้า เเถวในเเนวตั้ง หาร 2 เเล้วเหลือเศษที่ไม่ใช่ 0 -> เลขคี่
                        # สร้าง rect
                        grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
                        # วาด rectangle
                        pygame.draw.rect(screen,grass_color,grass_rect)

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3) # กำหนดให้คะเเนน มีค่าเท่ากับ ความยาวของตัวงู - 3 รวมถึงกำหนดเป็น string
                                                   # ปล.ที่ลบ 3 เพราะความยาวงูเริ่มต้นคือ 3 บล็อก
        score_surface = game_font.render(score_text,True,(56,74,12)) # ปล.การปรับค่าเป็น True จะทำให้ตัวอักษรลบรอยหยัก -> ตัวอักษรเรียบขึ้น
        score_x = int(cell_size * cell_number - 60) # กำหนดให้ score ที่อยู่ชิดขวาของ screen ขยับมาด้านซ้าน 60 px
        score_y = int(cell_size * cell_number - 40) # กำหนดให้ score ที่อยู่ชิดล่างของ screen ขยับมาด้านบน 40 px
        apple_x = int(cell_size * cell_number - 100) # กำหนดให้ apple ที่อยู่ชิดขวาของ screen ขยับมาด้านซ้าย 100 px
        apple_y = int(cell_size * cell_number - 40) # กำหนดให้ apple ที่อยู่ชิดล่างของ screen ขยับมาด้านบน 40 px
        bg_x    = int(cell_size * cell_number - 125) # กำหนดให้ score ที่อยู่ชิดขวาของ screen ขยับมาด้านซ้าย 125 px
        bg_y    = int(cell_size * cell_number - 60) # กำหนดให้ score ที่อยู่ชิดล่างของ screen ขยับมาด้านบน 60 px       
        # สร้าง rect
        score_rect = score_surface.get_rect(center = (score_x,score_y))
        apple_rect = apple.get_rect(center = (apple_x,apple_y))
        bg_rect = pygame.Rect(bg_x,bg_y,apple_rect.width + score_rect.width + 20,apple_rect.height) # ให้พื้นหลัง มีพิกัดเป็น bg_x,bg_y
                                                                                                    # เเละมีความกว้างเท่ากับ ความกว้างของ apple_rect + score_rect + 20 เเละมีความสูงเท่ากับ apple_rect 
        # วาด rectangle
        pygame.draw.rect(screen,(255,250,250),bg_rect) # พื้นหลัง apple เเละ score
        screen.blit(score_surface,score_rect) # score
        screen.blit(apple,apple_rect) # apple
        pygame.draw.rect(screen,(56,74,12),bg_rect,2) # กรอบพื้นหลัง apple เเละ score

pygame.mixer.pre_init(44100,-16,2,512) # ไม่ทำให้เสียงมีการดีเลย์
pygame.init()
cell_size = 40  # ขนาด cell
cell_number = 20 # จำนวน cell
screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size)) # ขนาดหน้าจอ
clock = pygame.time.Clock() # ตัวกำหนดค่า fps
apple = pygame.image.load('Graphics/fruit/apple.png').convert_alpha() # นำรูปเเอปเปิ้ลเข้า ปล. convert_alpha() ทำให้ pygame ทำงานง่ายขึ้นเฉยๆ
game_font = pygame.font.Font('Font/PressStart2P-vaV7.ttf', 25) # นำ font เข้า --> เป็น Font PressStart2P ขนาด 25px 
                                                               
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
                    main_game.snake.play_up_sound()
                    main_game.snake.direction = Vector2(0,-1) # => งูจะเคลื่อนที่ไปทางด้านบน

            if event.key == pygame.K_DOWN: # ถ้ามีเหตุการณ์ที่กดลูกศรลง
                if main_game.snake.direction.y != -1: # ถ้าทิศทางของงู ในพิกัด y ไม่เท่ากับ -1 (งูไม่ได้เคลื่อนไปทางด้านบน)
                    main_game.snake.play_down_sound()
                    main_game.snake.direction = Vector2(0,1) # => งูจะเคลื่อนที่ไปทางด้านล่าง

            if event.key == pygame.K_RIGHT: # ถ้ามีเหตุการณ์ที่กดลูกศรขวา 
                if main_game.snake.direction.x != -1: # ถ้าทิศทางของงู ในพิกัด x ไม่เท่ากับ -1 (งูไม่ได้เคลื่อนไปทางด้านซ้าย)
                    main_game.snake.play_right_sound()
                    main_game.snake.direction = Vector2(1,0) # => งูจะเคลื่อนที่ไปทางขวา

            if event.key == pygame.K_LEFT: # ถ้ามีเหตุการณ์ที่กดลูกศรซ้าย
                if main_game.snake.direction.x != 1: # ถ้าทิศทางของงู ในพิกัด x ไม่เท่ากับ 1 (งูไม่ได้เคลื่อนไปทางด้านขวา)
                    main_game.snake.play_left_sound()
                    main_game.snake.direction = Vector2(-1,0) # => งูจะเคลื่อนที่ไปทางซ้าย
                


    screen.fill((175,215,70)) # กำหนดสีของ screen -> สีเขียวอ่อน
    main_game.draw_elements() # อยู่ใน class main
    pygame.display.update() # อยู่ใน class main
    clock.tick(60) # fps = 60