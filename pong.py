# Super Pong
# Game created by Po-Yi Liu (November, 2013)

import simplegui

import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
ball_pos = [WIDTH / 2, HEIGHT / 2]
init_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [-5, 2] 
random_spawn = ['LEFT', 'RIGHT']
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
paddle1_pos = HEIGHT/2 - HALF_PAD_HEIGHT
paddle2_pos = HEIGHT/2 - HALF_PAD_HEIGHT
paddle1_posb = paddle1_pos + 2*HALF_PAD_HEIGHT
paddle2_posb = paddle2_pos + 2*HALF_PAD_HEIGHT
paddle1_vel = 0
paddle2_vel = 0
score1 = 0
score2 = 0
LEFT = False
RIGHT = True

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    global random_spawn
    ball_pos[0] = 300
    ball_pos[1] = 200
   
    if direction == 'RIGHT':
        
        ball_vel[0] = random.randrange(2, 5)
        ball_vel[1] = -random.randrange(2, 5)
    
    elif direction == 'LEFT':
        
        ball_vel[0] = -random.randrange(2, 5)
        ball_vel[1] = random.randrange(2, 5)
    
    
    


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    global random_spawn
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = 0
    score2 = 0
    
    return spawn_ball(random_spawn[random.randrange(0,2)])
    

    

def draw(c):
    global PAD_WIDTH, PAD_HEIGHT, HALF_PAD_WIDTH, HALF_PAD_HEIGHT
    global score1, score2, paddle1_pos, paddle2_pos, paddle1_posb, paddle2_posb
    global ball_pos, ball_vel, vel, time, init_pos
    global paddle1_vel, paddle2_vel
 
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_text('PONG', (190, 350), 80, 'GREY', 'serif')
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]  

    # collide and reflect off of left hand side of canvas
    #if ball_pos[0] <= BALL_RADIUS:
        #ball_vel[0] = - ball_vel[0]  
        
    # collide and reflect off of right hand side of canvas
    #if ball_pos[0] >= 600 - BALL_RADIUS:
        #ball_vel[0] = -ball_vel[0]
    # collide and reflect off of bottom of canvas
    if ball_pos[1] >= 400 - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    # collide and reflect off of top of canvas
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
        
    #if ball touches the left gutter:
    if (ball_pos[0] <= (BALL_RADIUS + 8)) and (ball_pos[1] not in range(paddle1_pos, paddle1_posb)):
        score2 += 1
        return spawn_ball('RIGHT')
    #if the ball touches paddle1:
    if (ball_pos[0] <= (BALL_RADIUS + 8)) and (ball_pos[1] in range(paddle1_pos, paddle1_posb)):
        
        ball_vel[0] = -(ball_vel[0]+(ball_vel[0]*0.1))
           
    
    #if ball touches the right gutter:  
    if (ball_pos[0] >= 600 - (BALL_RADIUS + 8)) and (ball_pos[1] not in range(paddle2_pos, paddle2_posb)):
        score1 += 1
        return spawn_ball('LEFT')
    #if the ball touches paddle2:
    if (ball_pos[0] >= 600 - (BALL_RADIUS + 8)) and (ball_pos[1] in range(paddle2_pos, paddle2_posb)):
        
        ball_vel[0] = -(ball_vel[0]+(ball_vel[0]*0.1))
    
    
    
    
    
        
    # draw ball --------------------------------------------
    c.draw_circle(ball_pos, 20, 5, 'Yellow', 'BLUE')
    
#----------------------------------------------------   
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
    paddle1_posb += paddle1_vel
    paddle2_posb += paddle2_vel
    
    if paddle1_posb >= HEIGHT or paddle1_pos <= 0:
        paddle1_vel = 0
    
    elif paddle2_posb >= HEIGHT or paddle2_pos <= 0:
        paddle2_vel = 0
    
   
        
    
    
    
    # draw paddles
    c.draw_polygon([(0*WIDTH, paddle1_pos), (PAD_WIDTH, paddle1_pos), (PAD_WIDTH, paddle1_posb), (0*WIDTH, paddle1_posb)], 1, 'Purple', 'Purple')
    c.draw_polygon([(WIDTH, paddle2_pos), (WIDTH - PAD_WIDTH, paddle2_pos), (WIDTH - PAD_WIDTH, paddle2_posb), (WIDTH, paddle2_posb)], 1, 'Green', 'Green')
#----------------------------------------------------------
    
    # draw scores
    c.draw_text('P1', (240, 20), 20, 'PURPLE', 'serif')
    c.draw_text('P2', (350, 20), 20, 'GREEN', 'serif')
    c.draw_text(str(score1), (240, 60), 40, 'WHITE', 'serif')
    c.draw_text(str(score2), (350, 60), 40, 'WHITE', 'serif')
    
    
#---------------------------------------------------
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel -= 5
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel += 5
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel -= 5
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel += 5
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    paddle1_vel = 0
    paddle2_vel = 0
        


# create frame ----------------------------
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Reset Game', new_game, 200)


# start frame -----------------------------------------
new_game()
frame.start()
