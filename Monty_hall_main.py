import pygame
import time
import random
import pickle

pygame.init()

# Variables statiques

white = (255,255,255)
curious=(237,155,120)
curious2=(255,255,128)
cDark=(200,200,128)
black = (0,0,0)
red = (255,0,0)
redClear=(155,0,0)
redbordeau=(170,105,70)
fakegray=(195,195,195)
lavande=(200,191,231)
blue = (0,0,255)
green= (0,255,0)
greenClear=(0,55,0)
blueDark=(0,0,55)
yellow=(255,249,0)
violet=(255,90,255)
smallfont=pygame.font.SysFont("comicsansms",30) 
largefont2=pygame.font.SysFont("comicsanms",50)
largefont=pygame.font.SysFont("ardelaneymoyen",38)
Markers=[(65,386),(433,386),(800,386)]
Max_x=1104
Max_y=600


     
gameDisplay = pygame.display.set_mode((Max_x,Max_y))
pygame.display.set_caption('Monty Hall Game')
pygame.display.update


# Fonctions utiles

def message_to_screen(message,color, x, y):
    text=largefont.render(message, True, color)
    gameDisplay.blit(text, [x,y])

def message_to_screen2(message,color, x, y):
    text=largefont2.render(message, True, color)
    gameDisplay.blit(text, [x,y])



def Setbackground(img):
    bg=pygame.image.load(img)
    gameDisplay.blit(bg, (0,0))


def SetImage(img, x, y):
    im=pygame.image.load(img)
    gameDisplay.blit(im, (x,y))


def SetScore(scr):
    succes_chang, nb_chang, succes_conser, nb_conser=scr[0][0], scr[0][1], scr[1][0], scr[1][1]
    if nb_chang!=0:
        perc_chang=round((succes_chang/nb_chang)*100, 1)

    else:
        perc_chang=101
        
    if nb_conser!=0:
        perc_conser=round((succes_conser/nb_conser)*100, 1)

    else:
        perc_conser=101
        
    message_to_screen2(str(succes_chang), black, 640 ,270 ) 
    message_to_screen2(str(nb_chang), black, 822 ,270  )
    if perc_chang!=101:
        
        message_to_screen2(str(perc_chang), black, 1000 ,270  )
    message_to_screen2(str(succes_conser), black,640 ,480  ) 
    message_to_screen2(str(nb_conser), black, 822 ,480  )
    
    if perc_conser!=101:
        
        message_to_screen2(str(perc_conser), black, 1000  ,480  )


def dialogue(msg,color):
    x=(Max_x)/2-(len(msg)/2)*10
    y=561
    message_to_screen(msg, color, x, y)

def set_randomnly():
    L=[['opened_door_sheep.jpg'], ['opened_door_treasure.jpg'], ['opened_door_sheep.jpg']]
    random.shuffle(L)
    for i in range(3):
        if L[i]==['opened_door_treasure.jpg']:
            treasure=i
        
    L[0].extend([2,31])
    L[1].extend([372,31])
    L[2].extend([737,31])

    return L, treasure
    

gameExit=False
IntroExit=False
PlayExit=True
StatsExit=True




#Boucle principale

Setbackground('make_a_deal.jpg')
while not gameExit:
    event=pygame.event.poll()
    if event.type == pygame.QUIT :
        gameExit = True
        break

        
    Mouse_x=0; Mouse_y=0
    while not IntroExit :
            
            event=pygame.event.poll()
            if event.type == pygame.QUIT :
                gameExit = True
                break
            if event.type==pygame.MOUSEMOTION:
                Mouse_x, Mouse_y=event.pos
                
            if Mouse_x>=830 and Mouse_x<=1063:
                            if Mouse_y<=353 and Mouse_y>=296:
                                
                                 SetImage('buttonHighlightPlay.png', 809, 285)
                            
                                
                            elif Mouse_y<=482 and Mouse_y>=424:
                                
                                 SetImage('buttonHighlightStats.png', 809, 415)

                            else:
                
                                Setbackground('make_a_deal.jpg')
                                pygame.display.update()
            else:
                
                Setbackground('make_a_deal.jpg')
                pygame.display.update()                
            

            

            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                Mouse_x, Mouse_y=event.pos
                
                if Mouse_x>=830 and Mouse_x<=1063:
                    
                            if Mouse_y<=353 and Mouse_y>=296:
                                
                                 SetImage('buttonPressedPlay.png', 809, 285)
                                 pygame.display.update()
                                 time.sleep(0.2)
                                 Setbackground('make_a_deal.jpg')
                                 time.sleep(0.2)
                                 IntroExit=True
                                 PlayExit=False
                                 with open('score.txt', 'rb') as scoref:
                                    score_d=pickle.Unpickler(scoref)
                                    score=score_d.load()
                                 
                                 start=True
                                 
                                 
                                 
                                
                            if Mouse_y<=482 and Mouse_y>=424:
                                
                                 SetImage('buttonPressedStats.png', 809, 415)
                                 pygame.display.update()
                                 time.sleep(0.2)
                                 Setbackground('make_a_deal.jpg')
                                 StatsExit=False
                                 IntroExit=True
                                 score_set=False

                            
            

            pygame.display.update()
                
                
                
       
        
    while not PlayExit:
        
        
            
            if event.type == pygame.QUIT :
                gameExit = True
                
                break

            pygame.display.update()

            if start:
               dialogue1=False
               dialogue2=True  #ou presque lol
               dialogue3=True
               start=False
               choisi=False
               ouvert=True
               rechoisi=True
               oui=False
               non=False
               dialogue4=True
               Liste, voiture=set_randomnly()
               Setbackground('closed_doors3.png')
       
            if not dialogue1:
               dialogue('Choisir une porte par son numero', redbordeau)
               pygame.display.update()
               dialogue1=True
               
            event=pygame.event.poll()
            if not choisi:
       
               if event.type==pygame.KEYDOWN:
                   if event.unicode=='1':
                       choix=1
                       choisi=True
                       ouvert=False
                       dialogue('Choisir une porte par son numero', lavande)
                       SetImage('marker.jpg', 63, 386)
                       

                   elif event.unicode=='2':
                       choix=2
                       choisi=True
                       ouvert=False
                       dialogue('Choisir une porte par son numero', lavande)
                       SetImage('marker.jpg', 433, 386) 

                   elif event.unicode=='3':
                       choix=3
                       choisi=True
                       ouvert=False
                       dialogue('Choisir une porte par son numero', lavande)
                       SetImage('marker.jpg', 800, 386)
            if not ouvert:
                 nbL=[0,1,2]
                 if choix-1==voiture:
                     nbL.remove(choix-1)
                     x=random.choice(nbL)
                 else:
                    nbL.remove(choix-1)
                    nbL.remove(voiture)
                    x=nbL[0]

                 pygame.display.update()   
                 time.sleep(1.5)  
                 SetImage('opened_door_sheep.png',Liste[x][1],Liste[x][2])
                 pygame.display.update()
                 ouvert=True
                 dialogue2=False
            if not dialogue2:
                dialogue('Voulez-vous changez de porte? Oui (O) ou Non (N) ?', redbordeau)
                pygame.display.update()
                dialogue2=True
                rechoisi=False

            if not rechoisi:
               if event.type==pygame.KEYDOWN:
                   print(event.unicode)
                   if event.unicode=='o':
                       oui=True
                       dialogue('Voulez-vous changez de porte? Oui (O) ou Non (N) ?', lavande)
                       pygame.display.update()
                       time.sleep(0.3)
                       rechoisi=True

                   elif event.unicode=='n':
                       non=True
                       dialogue('Voulez-vous changez de porte? Oui (O) ou Non (N) ?', lavande)
                       pygame.display.update()
                       time.sleep(0.3)
                       rechoisi=True
                   
                   
                   L2=[0,1,2]
                   L2.remove(choix-1)
                   L2.remove(x)
                   y=L2[0]
                   
            if oui:
            
               Setbackground('closed_doors3.png')
               SetImage('opened_door_sheep.png',Liste[x][1],Liste[x][2])
               SetImage('marker.jpg', Markers[y][0], Markers[y][1])
               pygame.display.update()
               time.sleep(1.5)
               score[0][1]=score[0][1]+1
               if choix-1==voiture:
                   #SetImage('opened_door_sheep.png',Liste[choix-1][1],Liste[choix-1][2])
                   #pygame.display.update()
                   #time.sleep(1)
                   SetImage('opened_door_sheep.png',Liste[y][1],Liste[y][2])
                   dialogue('Vous avez PERDU',redbordeau)
               else:
                   
                   SetImage('opened_door_treasure.png',Liste[voiture][1],Liste[voiture][2])
                   dialogue('Vous avez GAGNE', redbordeau)
                   score[0][0]=score[0][0]+1 
                   
               pygame.display.update()   
               oui=False
               dialogue3=False
               PlayExit=True
               IntroExit=False
               with open('score.txt', 'wb') as scoref:
                     score_p=pickle.Pickler(scoref)
                     score_p.dump(score)
               time.sleep(3)
           
            if non:
                score[1][1]=score[1][1]+1
                time.sleep(1.5)
                if choix-1==voiture:
                   #SetImage('opened_door_sheep.png',Liste[y][1],Liste[y][2])
                   #pygame.display.update()
                   
                   SetImage('opened_door_treasure.png',Liste[voiture][1],Liste[voiture][2])
                   dialogue('Vous avez GAGNE', redbordeau)
                   score[1][0]=score[1][0]+1
                   

                else:
                   SetImage('opened_door_sheep.png',Liste[choix-1][1],Liste[choix-1][2])
                   dialogue('Vous avez PERDU', redbordeau)

                pygame.display.update()   
                non=False
                dialogue3=False
                PlayExit=True
                IntroExit=False
                with open('score.txt', 'wb') as scoref:
                     score_p=pickle.Pickler(scoref)
                     score_p.dump(score)
                time.sleep(3)

            #if not dialogue3:
    
    while not StatsExit:
        event=pygame.event.poll()
        if event.type == pygame.QUIT :
                gameExit = True
                StatsExit=True
                
        if event.type == pygame.KEYDOWN :
                
                if event.unicode=='e':
                    StatsExit=True
                    IntroExit=False
        if not score_set:
            with open('score.txt', 'rb') as scoref:
                 score_d=pickle.Unpickler(scoref)
                 score=score_d.load()
            Setbackground('stats.jpg')
            SetScore(score)
            score_set=True
            pygame.display.update()
            
     
pygame.quit()
quit()
                
            

        

         
                       
