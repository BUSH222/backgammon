import pygame
import sys
import bghelper
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
w, h = 1200, 800
display = pygame.display.set_mode((w, h))



def game():
    board = bghelper.Board(display)
    temppos1 = []
    temppos2 = []
    cdice = bghelper.roll_dice()
    cnt = 0
    while True:
        boardimg = pygame.image.load('bg2.png').convert()
        display.blit(boardimg, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                temppos1.append(0) if y > 400 else temppos1.append(1)
                if y > 400:
                    if x < 600:
                        temppos1.append((x-35)//94)
                    else:
                        temppos1.append((x-45)//94)
                else:
                    if x < 600:
                        temppos1.append(11 - (x-35)//94)
                    else:
                        temppos1.append(11 - (x-45)//94)


            elif event.type == pygame.MOUSEBUTTONUP:
                
                x, y = pygame.mouse.get_pos()
                temppos2.append(0) if y > 400 else temppos2.append(1)
                if y > 400:
                    temppos2.append((x-45)//92)
                else:
                    temppos2.append(11 -(x-45)//92)
                
                if board.check_move(temppos1[0], temppos1[1], temppos2[0], temppos2[1], cdice):
                    board.move_piece(temppos1[0], temppos1[1], temppos2[0], temppos2[1], cdice[1])
                
                    
                    if len(cdice[1]) == 0:
                        cdice = bghelper.roll_dice()
                        board.movenumber += 1
                        board.movesfromhead = 0
                temppos1 = []
                temppos2 = []
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:
                    cdice = bghelper.roll_dice()
                    board.movenumber += 1
                    board.movesfromhead = 0

        my_font = pygame.font.SysFont('Helvetica', 100)
        text_surface = my_font.render(f'{cdice[0][0]} {cdice[0][1]}', False, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(600, 400))
        display.blit(text_surface, text_rect)
        if board.movenumber % 2 == 1:
            bghelper.dropshadow(display, 'w', 50, 450, 410)
        else:
            bghelper.dropshadow(display, 'b', 50, 450, 410)


        my_font = pygame.font.SysFont('Helvetica', 20)
        text_surface = my_font.render(f'Move:', False, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(450, 370))
        display.blit(text_surface, text_rect)
        
        
        if cnt % 50 == 0:
            if board.movenumber % 2 == 1:
                movec = 'w'
            else:
                movec = 'b'
            outcomes = []
            trueboard = board.board[0] + board.board[1]
            for i in range(len(trueboard)):
                if trueboard[i] != '':
                    if trueboard[i][-1] == movec:
                        for s in cdice[1]:
                            outcomes.append(board.check_move(i//12, i%12, (i+s)//12, (i+s)%12, cdice))
            if True not in outcomes:
                
                cdice = bghelper.roll_dice()
                board.movenumber += 1
                board.movesfromhead = 0





        board.draw_pieces()
        pygame.display.update()
        cnt += 1
        clock.tick(bghelper.FPS)

if __name__ == '__main__':
    game()
    pygame.quit()
    sys.exit()