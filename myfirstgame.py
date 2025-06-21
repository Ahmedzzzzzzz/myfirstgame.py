import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My first game screen")

white = (255, 255, 255)
blue = (0, 0, 255)

screen.fill(white)

rect_width = 200
rect_height = 100
rect_x = (640 - rect_width) // 2
rect_y = (480 - rect_height) // 2
pygame.draw.rect(screen, blue, (rect_x, rect_y, rect_width, rect_height))

font = pygame.font.SysFont(None, 48)
text = font.render("hello pygame", True, (0, 0, 0))
text_rect = text.get_rect(center=(320, 240))
screen.blit(text, text_rect)

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
