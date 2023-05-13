import pygame
import button
pygame.init()

#
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
black = (0, 0, 0)
mainscreencolour = (99, 155, 255)

#screen
screen_width = 900
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill(white)
pygame.display.set_caption("Kaas")


#afbeeldingen laden
mainscreen = pygame.image.load("C:/Users/Guido/Desktop/pythonProject2/sprites/UI/mainscreen.png").convert_alpha()
wood = pygame.image.load("C:/Users/Guido/Desktop/pythonProject2/sprites/resources/log.png").convert_alpha()
stone = pygame.image.load("C:/Users/Guido/Desktop/pythonProject2/sprites/resources/stone.png").convert_alpha()
house = pygame.image.load("C:/Users/Guido/Desktop/pythonProject2/sprites/buildings/house.png").convert_alpha()

houses = pygame.image.load("C:/Users/Guido/Desktop/pythonProject2/sprites/city/houses.png").convert_alpha()
city = pygame.transform.scale(houses, (150, 150))

wood_button = button.Button(0, 780, wood, 2)
stone_button = button.Button(60, 780, stone, 2)
house_button = button.Button(450, 780, house, 2)

#font
font = pygame.font.Font("Minecraft.ttf", 25)

#resources
wood_amount = 0
stone_amount = 0

screen.blit(mainscreen, (0, 0))
#main loop
run = True
while run:
    if wood_button.draw(screen):
        pygame.draw.rect(screen, mainscreencolour, [0, 0, 150, 30])
        wood_amount += 1
        text = font.render(" Wood " + str(wood_amount), True, black, mainscreencolour)
        woodRect = text.get_rect()
        screen.blit(text, (0, 0))

    if stone_button.draw(screen):
        pygame.draw.rect(screen, mainscreencolour, [0, 40, 150, 30])
        stone_amount += 1
        text2 = font.render(" Stone " + str(stone_amount), True, black, mainscreencolour)
        stoneRect = text2.get_rect()
        screen.blit(text2, (0, 40))

    if house_button.draw(screen):
        if wood_amount >= 10:
            print("je hebt genoeg hout")
            screen.blit(city, (500, 500))
            wood_amount -= 10
            pygame.draw.rect(screen, mainscreencolour, [0, 0, 150, 30])
            text = font.render(" Wood " + str(wood_amount), True, black, mainscreencolour)
            screen.blit(text, (0, 0))
        else:
            print("je hebt niet genoeg hout")


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()
