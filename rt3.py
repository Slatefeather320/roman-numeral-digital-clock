import datetime, time, pygame 

window = pygame.display.set_mode((1100,100))
pygame.init()

pygame.display.set_caption("Digital Roman Clock")

font = pygame.font.Font("freesansbold.ttf",100)
text = font.render("TEST", True, (255,255,255))
compiled_m = font.render("TEST", True, (255,255,255))

def drawFrame():
     global text, compiled_m
     window.fill((0,0,0))
     window.blit(text, (0,0))
     window.blit(compiled_m, (900, 0))
     pygame.display.update()

def roman(x):
    out = ""
    guide = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
    if x >= 50:
        out += "L"
        x -= 50
    elif x >= 40:
        out += "XL"
        x -= 40
    else:
        while x >= 10:
            x -= 10
            out += "X"
    
    out += guide[x]
    return out

def findTime():
    global text, compiled_m
    now = datetime.datetime.now()
    minute = now.minute
    second = now.second
    hour = now.hour
    if hour > 12:
        m = "pm"
        hour -= 12
    else:
        m = "am"
    hour = roman(hour)
    minute = roman(minute)
    second = roman(second)
    compiled_time = str(hour + " : " + minute + " : " + second)
    text = font.render(compiled_time, True, (255,255,255))
    compiled_m = font.render(m, True, (255,255,255))


#active loop 
active = True

while active:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         active = False
    

   #maingameloop
   drawFrame()
   findTime()







