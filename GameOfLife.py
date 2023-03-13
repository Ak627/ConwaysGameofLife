import pygame
import random

pygame.init()
pygame.display.set_caption("space invader!") # sets the window title
screen = pygame.display.set_mode((800,800)) # creates game screen
clock = pygame.time.Clock() #set up clock
map = [[0]*80 for i in range (80)]

    
# map [2][4] = 1
# map[2][3] = 1
# map [5][10] = 1
# map [5][11] = 1
# map [4] [10] = 1

map =[[random.randrange(0,2)] *80 for i in range(80) ]
print(map)





#game loop-----------------------------------------------
while True:
    clock.tick(60) #FPs
    event = pygame.event.get()#event queue
    
    
    #input section---------------------------------------
    for event in pygame.event.get():
        break
    #update section--------------------------------------
    for i in range (80):
        for j in range(80):
            counter = 0 #reset counter for each cell
            if i<79 and map[i+1] [j] == 1: #check above
                counter+=1
            if i>0 and map[i-1] [j] == 1: #check down
                counter+=1
            if j<79 and map[i][j+1] == 1: #check right
                counter+=1
            if j>0 and map[i][j-1] == 1: #check checks left
                counter+=1
            if i<79 and j<79 and map[i+1][j+1]==1: #check top right corner
                counter+=1
            if i>=0 and j<79 and map[i-1][j+1]==1: #check bottom right corner
                counter+=1
            if i<79 and j>=0 and map[i+1][j-1]==1: #check top left corner
                counter+=1
            if i>=0 and j>=0 and map[i-1][j-1]==1: #check bottom left corner
                counter+=1
                
            #kill, live, or grow cells
            if map[i][j]==1 and counter <=1:
                 map[i][j]=0 #cell dies from lonliness :'(
                 print("i died from lonliness")
            if map[i][j]==1 and counter >=4:
                map[i][j]=0
                print("i died from over crowding")
            if map[i][j]==0 and counter ==3:
                map[i][j]=1
                print("im alive")
    
    
    
    pygame.time.wait(200) #alows the game down a bit (optional)
    
    
    
    #render section----------------------------------------
    screen.fill((0,0,0)) #wipe screen so it doesnt smear
    #draw map
    for i in range (80):
        for j in range(80):
            if map[i][j]==0:
                pygame.draw.rect(screen, (0,0,0), (j*10, i*10, 10, 10))
                pygame.draw.rect(screen, (255,255,255), (j*10, i*10, 10, 10), 1) #uncomment if you want to see grid
            if map[i][j] == 1:
                pygame.draw.rect(screen, (0,200,200), (j*10, i*10, 10, 10))
    #stuff gets drawn here!
    
    pygame.display.flip()
    
    
    
#end game loop--------------------------------------------------
pygame.quit()
