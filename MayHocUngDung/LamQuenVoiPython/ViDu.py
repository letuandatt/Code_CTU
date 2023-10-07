"""
import numpy as np

a = np.array([0, 1, 2, 3, 4, 5])

print(a)

print("Số chiều của mảng a: ", a.ndim)

print("Kích thước ma trận a là: ", a.shape)

print("In ra các phần trử có giá trị > 3 trong mảng a: ", a[a > 3])

a[a > 3] = 10

b = a.reshape((3, 2))

print("Mảng b là: ", b)

print("Số chiều của mảng b: ", b.ndim)

print("Kích thước ma trận b là: ", b.shape)

print(b[2][1])

b[2][0] = 50

print("B là: ", b)

c = b * 2

print("C là: ", c)
"""
"""
import numpy as np
import matplotlib.pyplot as plt

X = np.array([1, 2, 4])
Y = np.array([2, 3, 6])

plt.axis([0, 5, 0, 8])
plt.plot(X, Y, "ro", color = "red")
plt.xlabel("Giá trị thuộc tính X")
plt.ylabel("Giá trị thuộc tính Y")
plt.show()
"""
"""
import scipy as sp
import numpy as np

data = np.genfromtxt('web_traffic.tsv', delimiter="\t")

print(data.shape)

x = data[:,0]

y = data[:,1]

print(len(~np.isnan(y)))

x = x[~np.isnan(y)]

y = y[~np.isnan(y)]

import matplotlib.pyplot as plt

plt.scatter(x, y)
plt.title("Web traffic over the last month")
plt.xlabel("Time")
plt.ylabel("Hits/Hours")
plt.xticks([w * 7 * 24 for w in range(10)], ['week %i'%w for w in range(10)])
plt.autoscale(tight=True)
plt.grid()
plt.show()
"""
"""
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("play_tennis.csv", delimiter=",")
a = data.head(5) #lấy 5 dòng đầu
b = data.tail(5) #lấy 5 dòng cuối
d46 = data.iloc[3:7] #hàng thứ 3 đến 6, bắt đầu từ 0
c1 = data.iloc[:,0:1] #cột đầu tiên, cột 0
c15 = data.iloc[:,0:6] #cột đầu tiên (0) đến cột thứ 5
c3 = data.iloc[:,2] #cột thứ 2, bắt đầu từ 0
c453 = data.iloc[4:6,2] #giá trị dòng 4, 5 cột 2 (tính từ 0)
print(data.outlook) #In dữ liệu cột outlook
"""
"""
import pandas as pd
dt = pd.read_csv("play_tennis.csv", delimiter=',')
dt.head()
dt.tail(7)

dt.loc[3:8]
dt.iloc[:,3:6]
dt.iloc[5:10,3:4]
print(dt.outlook)
"""

import pygame
import random

pygame.init()

gadget_pair = 1
ch = int(input("Enter your choice for gadget pair: "))
if ch == 1:
    gadget_pair = 1
elif ch == 2:
    gadget_pair = 2

# INITIALS
WIDTH, HEIGHT = 1000, 600
wn = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong_But_Better")
run = True
player_1 = player_2 = 0
direction = [0, 1]
angle = [0, 1, 2]

# colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# for the ball
radius = 15
ball_x, ball_y = WIDTH / 2 - radius, HEIGHT / 2 - radius
ball_vel_x, ball_vel_y = 0.7, 0.7
dummy_ball_x, dummy_ball_y = WIDTH / 2 - radius, HEIGHT / 2 - radius
dummy_ball_vel_x, dummy_ball_vel_y = 0.7, 0.7

# paddle dimensions
paddle_width, paddle_height = 20, 120
left_paddle_y = right_paddle_y = HEIGHT / 2 - paddle_height / 2
left_paddle_x, right_paddle_x = 100 - paddle_width / 2, WIDTH - (100 - paddle_width / 2)
second_left_paddle_y = second_right_paddle_y = HEIGHT / 2 - paddle_height / 2
second_left_paddle_x, second_right_paddle_x = 100 - paddle_width / 2, WIDTH - (100 - paddle_width / 2)
right_paddle_vel = left_paddle_vel = 0
second_right_paddle_vel = second_left_paddle_vel = 0

# gadgets
left_gadget = right_gadget = 0
left_gadget_remaining = right_gadget_remaining = 5

# main loop
while run:
    wn.fill(BLACK)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP:
                right_paddle_vel = -0.9
                second_right_paddle_vel = -0.9
            if i.key == pygame.K_DOWN:
                right_paddle_vel = 0.9
                second_right_paddle_vel = 0.9
            if i.key == pygame.K_RIGHT and right_gadget_remaining > 0:
                right_gadget = 1
            if i.key == pygame.K_LEFT and right_gadget_remaining > 0:
                right_gadget = 2
            if i.key == pygame.K_w:
                left_paddle_vel = -0.9
                second_left_paddle_vel = -0.9
            if i.key == pygame.K_s:
                left_paddle_vel = 0.9
                second_left_paddle_vel = 0.9
            if i.key == pygame.K_d and left_gadget_remaining > 0:
                left_gadget = 1
            if i.key == pygame.K_a and left_gadget_remaining > 0:
                left_gadget = 2

        if i.type == pygame.KEYUP:
            second_right_paddle_vel = 0
            right_paddle_vel = 0
            second_left_paddle_vel = 0
            left_paddle_vel = 0

    # ball's movement controls
    if ball_y <= 0 + radius or ball_y >= HEIGHT - radius:
        ball_vel_y *= -1
    if dummy_ball_y <= 0 + radius or dummy_ball_y >= HEIGHT - radius:
        dummy_ball_vel_y *= -1
    if ball_x >= WIDTH - radius:
        player_1 += 1
        ball_x, ball_y = WIDTH / 2 - radius, HEIGHT / 2 - radius
        dummy_ball_x, dummy_ball_y = WIDTH / 2 - radius, HEIGHT / 2 - radius
        second_left_paddle_y = left_paddle_y
        second_right_paddle_y = right_paddle_y
        dir = random.choice(direction)
        ang = random.choice(angle)
        if dir == 0:
            if ang == 0:
                ball_vel_y, ball_vel_x = -1.4, 0.7
                dummy_ball_vel_y, dummy_ball_vel_x = -1.4, 0.7
            if ang == 1:
                ball_vel_y, ball_vel_x = -0.7, 0.7
                dummy_ball_vel_y, dummy_ball_vel_x = -0.7, 0.7
            if ang == 2:
                ball_vel_y, ball_vel_x = -0.7, 1.4
                dummy_ball_vel_y, dummy_ball_vel_x = -0.7, 1.4

        if dir == 1:
            if ang == 0:
                ball_vel_y, ball_vel_x = 1.4, 0.7
                dummy_ball_vel_y, dummy_ball_vel_x = 1.4, 0.7
            if ang == 1:
                ball_vel_y, ball_vel_x = 0.7, 0.7
                dummy_ball_vel_y, dummy_ball_vel_x = 0.7, 0.7
            if ang == 2:
                ball_vel_y, ball_vel_x = 0.7, 1.4
                dummy_ball_vel_y, dummy_ball_vel_x = 0.7, 1.4
        ball_vel_x *= -1
        dummy_ball_vel_x *= -1

    if ball_x <= 0 + radius:
        player_2 += 1
        ball_x, ball_y = WIDTH / 2 - radius, HEIGHT / 2 - radius
        dummy_ball_x, dummy_ball_y = WIDTH / 2 - radius, HEIGHT / 2 - radius
        second_right_paddle_y = right_paddle_y
        second_left_paddle_y = left_paddle_y
        dir = random.choice(direction)
        ang = random.choice(angle)
        if dir == 0:
            if ang == 0:
                ball_vel_y, ball_vel_x = -1.4, 0.7
                dummy_ball_vel_y, dummy_ball_vel_x = -1.4, 0.7
            if ang == 1:
                ball_vel_y, ball_vel_x = -0.7, 0.7
                dummy_ball_vel_y, dummy_ball_vel_x = -0.7, 0.7
            if ang == 2:
                ball_vel_y, ball_vel_x = -0.7, 1.4
                dummy_ball_vel_y, dummy_ball_vel_x = -0.7, 1.4

        if dir == 1:
            if ang == 0:
                ball_vel_y, ball_vel_x = 1.4, 0.7
                dummy_ball_vel_y, dummy_ball_vel_x = 1.4, 0.7
            if ang == 1:
                ball_vel_y, ball_vel_x = 0.7, 0.7
                dummy_ball_vel_y, dummy_ball_vel_x = 0.7, 0.7
            if ang == 2:
                ball_vel_y, ball_vel_x = 0.7, 1.4
                dummy_ball_vel_y, dummy_ball_vel_x = 0.7, 1.4

    # paddle's movement controls
    if left_paddle_y >= HEIGHT - paddle_height:
        left_paddle_y = HEIGHT - paddle_height
    if left_paddle_y <= 0:
        left_paddle_y = 0
    if right_paddle_y >= HEIGHT - paddle_height:
        right_paddle_y = HEIGHT - paddle_height
    if right_paddle_y <= 0:
        right_paddle_y = 0

    if second_left_paddle_y >= HEIGHT - paddle_height:
        second_left_paddle_y = HEIGHT - paddle_height
    if second_left_paddle_y <= 0:
        second_left_paddle_y = 0
    if second_right_paddle_y >= HEIGHT - paddle_height:
        second_right_paddle_y = HEIGHT - paddle_height
    if second_right_paddle_y <= 0:
        second_right_paddle_y = 0

    # paddle collisions
    # left paddle
    if second_left_paddle_y == left_paddle_y:
        if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
            if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
                ball_x = left_paddle_x + paddle_width
                dummy_ball_x = left_paddle_x + paddle_width
                ball_vel_x *= -1
                dummy_ball_vel_x *= -1

    if second_left_paddle_y != left_paddle_y:
        if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
            if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
                ball_x = left_paddle_x + paddle_width
                dummy_ball_x = left_paddle_x + paddle_width
                ball_vel_x *= -1
                dummy_ball_vel_x *= -1

        if second_left_paddle_x <= ball_x <= second_left_paddle_x + paddle_width:
            if second_left_paddle_y <= ball_y <= second_left_paddle_y + paddle_height:
                ball_x = left_paddle_x + paddle_width
                dummy_ball_x = left_paddle_x + paddle_width
                ball_vel_x *= -1
                dummy_ball_vel_x *= -1

    # right paddle
    if second_right_paddle_y == right_paddle_y:
        if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
            if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
                ball_x = right_paddle_x
                dummy_ball_x = right_paddle_x
                ball_vel_x *= -1
                dummy_ball_vel_x *= -1

    if second_right_paddle_y != right_paddle_y:
        if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
            if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
                ball_x = right_paddle_x
                dummy_ball_x = right_paddle_x
                ball_vel_x *= -1
                dummy_ball_vel_x *= -1

        if second_right_paddle_x <= ball_x <= second_right_paddle_x + paddle_width:
            if second_right_paddle_y <= ball_y <= second_right_paddle_y + paddle_height:
                ball_x = right_paddle_x
                dummy_ball_x = right_paddle_x
                ball_vel_x *= -1
                dummy_ball_vel_x *= -1

    # gadgets in action
    if gadget_pair == 1:
        if left_gadget == 1:
            if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
                if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
                    ball_x = left_paddle_x + paddle_width
                    ball_vel_x *= -3.5
                    dummy_ball_vel_x *= -3.5
                    left_gadget = 0
                    left_gadget_remaining -= 1
        elif left_gadget == 2:
            left_paddle_y = ball_y
            left_gadget = 0
            left_gadget_remaining -= 1

        if right_gadget == 1:
            if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
                if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
                    ball_x = right_paddle_x
                    ball_vel_x *= -3.5
                    dummy_ball_vel_x *= -3.5
                    right_gadget = 0
                    right_gadget_remaining -= 1

        elif right_gadget == 2:
            right_paddle_y = ball_y
            right_gadget = 0
            right_gadget_remaining -= 1

    # second pair
    elif gadget_pair == 2:
        if left_gadget == 1:
            if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
                if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
                    ball_x = left_paddle_x + paddle_width
                    dummy_ball_x = left_paddle_x + paddle_width
                    ball_vel_x *= -1
                    dummy_ball_vel_x *= -1
                    dummy_ball_vel_y *= -1
                    left_gadget = 0
                    left_gadget_remaining -= 1

        elif left_gadget == 2:
            second_left_paddle_y = left_paddle_y + 200
            left_gadget = 0
            left_gadget_remaining -= 1

        if right_gadget == 1:
            if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
                if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
                    ball_x = right_paddle_x
                    dummy_ball_x = right_paddle_x
                    ball_vel_x *= -1
                    dummy_ball_vel_x *= -1
                    dummy_ball_vel_y *= -1
                    right_gadget = 0
                    right_gadget_remaining -= 1

        elif right_gadget == 2:
            second_right_paddle_y = right_paddle_y + 200
            right_gadget = 0
            right_gadget_remaining -= 1

    # movements
    ball_x += ball_vel_x
    ball_y += ball_vel_y
    dummy_ball_x += dummy_ball_vel_x
    dummy_ball_y += dummy_ball_vel_y
    right_paddle_y += right_paddle_vel
    left_paddle_y += left_paddle_vel
    second_left_paddle_y += second_left_paddle_vel
    second_right_paddle_y += second_right_paddle_vel

    # scoreboard
    font = pygame.font.SysFont('callibri', 32)
    score_1 = font.render("Player_1:" + str(player_1), True, WHITE)
    wn.blit(score_1, (25, 25))
    score_2 = font.render("Player_2:" + str(player_2), True, WHITE)
    wn.blit(score_2, (825, 25))
    gad_left_1 = font.render("Gad Left:" + str(left_gadget_remaining), True, WHITE)
    wn.blit(gad_left_1, (25, 65))
    gad_left_2 = font.render("Gad Left:" + str(right_gadget_remaining), True, WHITE)
    wn.blit(gad_left_1, (825, 65))

    # OBJECTS
    pygame.draw.circle(wn, BLUE, (ball_x, ball_y), radius)
    pygame.draw.rect(wn, RED, pygame.Rect(left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(wn, RED, pygame.Rect(right_paddle_x, right_paddle_y, paddle_width, paddle_height))

    # dummy ball section
    pygame.draw.circle(wn, BLUE, (dummy_ball_x, dummy_ball_y), radius)

    # second paddles
    pygame.draw.rect(wn, RED, pygame.Rect(second_left_paddle_x, second_left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(wn, RED, pygame.Rect(second_right_paddle_x, second_right_paddle_y, paddle_width, paddle_height))

    # gadget indication
    if left_gadget == 1:
        pygame.draw.circle(wn, WHITE, (left_paddle_x + 10, left_paddle_y + 10), 4)
    if right_gadget == 1:
        pygame.draw.circle(wn, WHITE, (right_paddle_x + 10, right_paddle_y + 10), 4)

    # endscreen
    winning_font = pygame.font.SysFont('callibri', 100)
    if player_1 >= 3:
        wn.fill(BLACK)
        endscreen = winning_font.render("PLAYER_1 WON!!!!", True, WHITE)
        wn.blit(endscreen, (200, 250))

    if player_2 >= 3:
        wn.fill(BLACK)
        endscreen = winning_font.render("PLAYER_2 WON!!!!", True, WHITE)
        wn.blit(endscreen, (200, 250))

    pygame.display.update()