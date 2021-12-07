import pygame
from random import *

# 레벨에 맞게 설정
def setup(level):
    # 얼마동안 숫자를 보여줄지
    global display_time
    display_time = 5 - (level // 4)
    display_time = max(display_time, 1) # 1초 미만이면 1초로 처리

    # 얼마나 많은 숫자를 보여줄 것인가?
    number_count = (level // 2) + 3
    number_count = min(number_count, 40) # 만약 40을 초과하면 40으로 처리

    # 실제 화면에 grid 형태로 숫자를 랜덤으로 배치
    shuffle_grid(number_count)

# 숫자 섞기
def shuffle_grid(number_count):
    rows = 5
    columns = 9

    cell_size = 130 # 각 Grid cel별 가로, 세로 크기
    button_size = 110 # Grid cell 내에 실제로 그려질 버튼 크기
    screen_left_margin = 55 # 전체 스크린 왼쪽 여백
    screen_top_margin = 20 # 전체 스크린 위쪽 여백

    # [0, 0, 0, 0, 0, 0, 0, 0, 0] X 5
    grid = [[0 for col in range(columns)] for row in range(rows)] # 5 X 9

    number = 1 # 숫자를 1부터 number_count까지, 만약 5라면 5까지 숫자를 랜덤하게 배치
    while number <= number_count:
        row_idx = randrange(0, rows) #0, 1, 2, 3, 4 중에서 랜덤으로 뽑기
        col_idx = randrange(0, columns) # 0 ~ 8 중에서 랜덤으로 뽑기

        if grid[row_idx][col_idx] == 0:
            grid[row_idx][col_idx] = number # 숫자 지정
            number += 1

            # 현재 grid cell 위치 기준으로 x, y 위치를 구함
            center_x = screen_left_margin + (col_idx * cell_size) + (cell_size / 2)
            center_y = screen_top_margin + (row_idx * cell_size) + (cell_size /2)

            # 숫자 버튼 만들기
            button = pygame.Rect(0, 0, button_size, button_size)
            button.center = (center_x, center_y)
            

            number_buttons.append(button)

    # 배치된 랜덤 숫자 확인


# 시작 화면 보여주기
def display_start_screen():# 여기서 easy: 1단계  normal:5단계 hard: 8단계 
    global lives, curr_level

    pygame.draw.rect(screen,WHITE , start_button,5)
    # 흰색 사각형 그림 - 중심 좌표: start_button.center
    # 좌표 150,150, 가로:150.세로:40.두께 5 빈상자
    msgmemory=game_font.render(f"Press the START button to start.", True, WHITE)
    msgmemory_rect=msgmemory.get_rect(center=(screen_width/2, screen_height/2 -240 ))
    screen.blit(msgmemory, msgmemory_rect)

    msgStart=game_font.render(f"START", True, WHITE)
    msgStart_rect=msgStart.get_rect(center=(screen_width/2, screen_height/2 +60 ))
    screen.blit(msgStart, msgStart_rect)

#난이도 조절 화면 보여주기
def display_lvselect_screen():

    pygame.draw.rect(screen, WHITE, rank_button, 5)
    msg_rank = rank_font.render("RANK", True, WHITE)
    msg_rank_rect = msg_rank.get_rect(center=(screen_width - 150 , screen_height - 110))
    screen.blit(msg_rank, msg_rank_rect)

    pygame.draw.rect(screen, WHITE, hard_button, 5)
    msg2 = game_font.render(f"HARD", True, WHITE)   # 하드  lv8 7개 
    msg2_rect = msg2.get_rect(center=(screen_width/2 , screen_height/2 + 240))
    screen.blit(msg2, msg2_rect)

    pygame.draw.rect(screen, WHITE, normal_button, 5)
    msg1 = game_font.render(f"NORMAL", True, WHITE) # 노말 lv 4 5개
    msg1_rect = msg1.get_rect(center=(screen_width/2 , screen_height/2 + 60))
    screen.blit(msg1, msg1_rect)

    pygame.draw.rect(screen, WHITE, easy_button, 5)
    msg4 = game_font.render(f"EASY", True, WHITE)   #이지 lv 1 3개
    msg4_rect = msg4.get_rect(center=(screen_width/2, screen_height/2 - 120))
    screen.blit(msg4, msg4_rect)

    msg_title = title_font.render("MEMORY GAME", True, WHITE)
    msg_title_rect = msg_title.get_rect(center=(screen_width/2, screen_height/2 - 280))
    screen.blit(msg_title, msg_title_rect)

def display_end_screen():
    global curr_level

    end_button = pygame.Rect(screen_width/2 - 61, screen_height - 143, 125, 60)
    msg1 = game_font.render("Your Score is",True,WHITE)
    msg1_rect = msg1.get_rect(center=(screen_width/2, screen_height - 500))
    screen.blit(msg1,msg1_rect)

    msg2 = game_font.render(f"level {curr_level - 1}",True,WHITE)
    msg2_rect = msg1.get_rect(center=(screen_width/2 + 100, screen_height - 400))
    screen.blit(msg2,msg2_rect)

    pygame.draw.rect(screen, WHITE, end_button, 5)
    msg_end = rank_font.render("END", True, WHITE)
    msg_end_rect = msg_end.get_rect(center=(screen_width/2 , screen_height - 110))
    screen.blit(msg_end, msg_end_rect)

def display_rank_screen():
    score = []
    click_pos = None
    pygame.draw.rect(screen, WHITE, back_button, 5)

    msg1 = game_font.render("RANKING",True,WHITE)
    msg1_rect = msg1.get_rect(center=(screen_width/2, screen_height - 665))
    screen.blit(msg1,msg1_rect)

    msg2 = ranking_font.render("back",True,WHITE)
    msg2_rect = msg2.get_rect(center=(75, 50))
    screen.blit(msg2,msg2_rect)

    msg_line = line_font.render("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ",True,WHITE)
    msg_line_rect = msg_line.get_rect(center=(screen_width/2, screen_height - 620))
    screen.blit(msg_line,msg_line_rect)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP: # 사용자가 마우스를 클릭했을 때
            click_pos = pygame.mouse.get_pos()

    if click_pos:
        check_buttions(click_pos)

    with open("rank.txt", "r", encoding= 'utf-8(한글로 인코딩)') as rk :
        line = 1
        while True :
            row = rk.readline()
            if not row:
                break
            score.append(int(row))
            line += 1

        score.sort(reverse=True)

        for i in range (len(score)) :
            if i < 5 :
                # score = rk.readline()
                msg_score = score_font.render(f"{i+1}등 : level {score[i]}",True,WHITE)
                msg_score_rect = msg_score.get_rect(center=(screen_width/4, screen_height - (530 - 100 * i)))
                screen.blit(msg_score,msg_score_rect)
            elif i < 10 :
                # score = rk.readline()
                msg_score = score_font.render(f"{i+1}등 : level {score[i]}",True,WHITE)
                msg_score_rect = msg_score.get_rect(center=(screen_width/2 + screen_width/4, screen_height - (530 - 100 * (i-5))))
                screen.blit(msg_score,msg_score_rect)
            else :
                break

# 게임 화면 보여주기
def display_game_screen():
    global hidden, curr_level, lives, display_time, start_ticks

    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 -1
    
    if hidden == False:
        times = display_time - elapsed_time
        if int(times) >= 0:
            timer = curr_font.render(str(int(times)),True,WHITE)
            screen.blit(timer,(screen_width - 100, screen_height - 715))
    else :
        timer = curr_font.render("START!",True,WHITE)
        screen.blit(timer,(screen_width - 100, screen_height - 715))

    #현재 상태 표시
    level_msg = curr_font.render(f"현재 단계: level {curr_level} / 남은 목숨: {lives}개",True,WHITE)
    level_msg_rect = level_msg.get_rect(center=(screen_width/2, screen_height-705))
    screen.blit(level_msg,level_msg_rect)

    if not hidden:
        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # ms -> s
        if elapsed_time > display_time or elapsed_time == display_time :
            hidden = True

    for idx, rect in enumerate(number_buttons, start=1):
        if hidden: # 숨김 처리
            # 버튼 사각형 그리기
            pygame.draw.rect(screen, GRAY, rect)
        else:
            # 실제 숫자 텍스트 (버튼 중간에 위치하도록)
            cell_text = game_font.render(str(idx), True, WHITE)
            text_rect = cell_text.get_rect(center=rect.center)
            screen.blit(cell_text, text_rect)

# pos에 해당하는 위치가 버튼 안쪽인지 확인
def check_buttions(pos):
    global start, start_ticks,curr_level
    test_sound = pygame.mixer.Sound("C:/Users/Administrator/Desktop/Project/button.mp3")

    if start==1:
        check_number_buttons(pos)
        
    elif start == 0 :
        if start_button.collidepoint(pos):
            test_sound.play()
            start = 1
            start_ticks = pygame.time.get_ticks() # 타이머 시작 (현재 시간을 저장
    elif start == 3 :
        if easy_button.collidepoint(pos):
            test_sound.play()
            start=0
            curr_level=1 # lv =1 , 카드는 총 3장
            setup(curr_level)
        elif normal_button.collidepoint(pos):
            test_sound.play()
            start=0
            curr_level=4  # lv = 4, 카드는 총 5장
            setup(curr_level)
        elif hard_button.collidepoint(pos):
            test_sound.play()
            start=0
            curr_level=8 #lv = 8, 카드는 총 7장
            setup(curr_level)
        elif rank_button.collidepoint(pos) : #랭크 화면
            test_sound.play()
            start = 2
    elif start == 2 :
        if back_button.collidepoint(pos):#백 버튼을 누르면 난이도 선택창
            test_sound.play()
            start=3
    elif start == 4 :
        if end_button.collidepoint(pos) :#종료버튼을 누르면 프로그램종료
            game_over()

def check_number_buttons(pos):
    global start, curr_level, hidden, level_fail, lives
    fail_sound = pygame.mixer.Sound("C:/Users/Administrator/Desktop/Project/fail.mp3") #틀렸을 때 효과음 선언
    ok_sound = pygame.mixer.Sound("C:/Users/Administrator/Desktop/Project/ok.mp3") #올바른 숫자 클릭 효과음 선언

    for button in number_buttons:
        if button.collidepoint(pos):
            if button == number_buttons[0]: # 올바른 숫자 클릭
                del number_buttons[0]
                if not hidden:
                    hidden = True # 숫자 숨김 처리
                ok_sound.play()
            else: # 잘못된 숫자 클릭
                if lives <= 1:
                    #Game Over
                    fail_sound.play()
                    start = 4
                    # game_over()
                    #running = False
                else:
                    level_fail = True
                    number_buttons.clear()
            break
    
    # 모든 숫자 맞추면 다음 레벨, 실패하면 목숨 깎고 같은 레벨 다시 도전
    if len(number_buttons) == 0:
        start = 0
        hidden = False
        if level_fail == True:
            fail_sound.play()
            lives -= 1
            level_fail = False
            setup(curr_level)
        else:
            ok_sound.play()
            curr_level += 1
            setup(curr_level)

# 게임 종료 처리, 메세지도 보여줌
def game_over():
    global running

    rank_save()

    running = False
 
def rank_save() :
    global curr_level

    with open("rank.txt", "a", encoding= 'utf-8(한글로 인코딩)') as rk :
        rk.write(f"{curr_level - 1}\n")

# 초기화
pygame.init()
screen_width = 1280 # 가로 크기
screen_height = 720 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")
game_font = pygame.font.Font(None, 80) # 폰트 정의
title_font = pygame.font.Font(None, 100)
rank_font = pygame.font.Font(None, 80) # 랭킹 화면 들어가는 버튼 폰트
ranking_font = pygame.font.Font(None,60) # back, reset 버튼 폰트
line_font = pygame.font.SysFont("malgungothic",60) # "ㅡㅡㅡㅡㅡㅡㅡㅡ" 폰트
score_font = pygame.font.SysFont("malgungothic", 70) # 랭킹 순위 폰트
curr_font = pygame.font.SysFont("malgungothic", 18) # 현재 상태 폰트
#배경 이미지불러오기
background =pygame.image.load("C:/Users/Administrator/Desktop/Project/image/bg2.png")


start_button = pygame.Rect(screen_width/2 - 100, screen_height/2 +30, 200,60)
easy_button=pygame.Rect(screen_width/2 - 100,screen_height/2 - 150,200,60)
normal_button=pygame.Rect(screen_width/2 - 130,screen_height/2 + 30,260,60)
hard_button=pygame.Rect(screen_width/2 - 100,screen_height/2 + 210,200,60)
rank_button = pygame.Rect(screen_width - 240, screen_height - 148, 182, 70)
back_button = pygame.Rect(20, 20, 110, 60)
end_button = pygame.Rect(screen_width/2 - 61, screen_height - 143, 125, 60)

# 색깔 (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (125, 125, 125)

number_buttons = [] # 플레이어가 눌러야 하는 버튼들

display_time = None # 숫자를 보여주는 시간
start_ticks = None # 시간 계산
lives = 3 # 목숨

test_sound=pygame.mixer.Sound("C:/Users/Administrator/Desktop/Project/BGM3.wav")
test_sound.play(-1)

# 게임 시작 여부  start=0 , 게임시작화면  |start=1, 게임 화면 |start =2, 랭킹화면 |start =3 난이도 설정화면 
start = 3

# 숫자 숨김 여부 (사용자가 1을 클릭했거나, 보여주는 시간 초과했을 떄)
hidden = False

# 레벨 통과 여부
level_fail = False


# 게임 루프
running = True # 게임이 실행중인가?
while running:
    click_pos = None

    # 이벤트 루프
    for event in pygame.event.get(): # 이떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트인가?
            running = False # 게임이 더 이상 실행중이 아님

        elif event.type == pygame.MOUSEBUTTONUP: # 사용자가 마우스를 클릭했을 때
            click_pos = pygame.mouse.get_pos()
            #print(click_pos)

    # 화면 그리기
    screen.blit(background, (0,0))

    # 화면 표시 제어
    if start==1:
        display_game_screen() # 게임 화면 표시
    elif start ==0 :
        display_start_screen() # 시작 화면 표시
    elif start==2:
        display_rank_screen()# 랭크 화면 
    elif start==3:
        display_lvselect_screen()#난이도 선택화면
    elif start == 4:
        display_end_screen()#게임종료화면
        
    # 사용자가 클릭한 좌표값이 있다면 (어딘가 클릭했다면)
    if click_pos: #시작화면 버튼 
      check_buttions(click_pos)


    # 화면 업데이트
    pygame.display.update()

# 게임 종료
pygame.quit()