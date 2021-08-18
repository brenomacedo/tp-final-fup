board = [[[' ' for i in range(3)] for i in range(3)] for i in range(3)]
scoreboard = [0, 0, 0]
cases_plays = [None]*5

def start_game():
    
    reset_board()

    player = ''
    cpu = ''

    turn = 0

    option = '0'

    show_menu()

    print()

    while option != '1' and option != '2' and option != '3':
        option = input('Selecione com qual símbolo deseja jogar: ')

        if option != '1' and option != '2' and option != '3':
            print('Opção inválida, tente novamente.')

    if option == '1':
        player = 'O'
        cpu = 'X'

        player_turn(player, cpu, turn)
    elif option == '2':
        player = 'X'
        cpu = 'O'

        player_turn(player, cpu, turn)
    else:
        show_creditos()

    

def show_menu():
    print('======================== JOGO DA VELHA 3D ========================')
    print('Criado por: Felipe e Breno!')
    print('==================================================================')
    print()
    print('Instruções:')
    print('O terminal mostrará as opções disponíves na forma: "NÚMERO - AÇÃO"')
    print('Entre com o número que corresponde a ação que você quer realizar para prosseguir.')
    print()
    print('1 - Jogar com o símbolo O')
    print('2 - Jogar com o símbolo X')
    print('3 - Sair')
    print()

def show_board():
    print()
    print('============== TABULEIRO ATUAL ==============')
    print()
    print('  CAMADA  1       CAMADA  2       CAMADA  3  ')
    print('  1   2   3       1   2   3       1   2   3  ')
    print(f'1 {board[0][0][0]} | {board[0][0][1]} | {board[0][0][2]} 1   1 {board[1][0][0]} | {board[1][0][1]} | {board[1][0][2]} 1   1 {board[2][0][0]} | {board[2][0][1]} | {board[2][0][2]} 1')
    print(' ---+---+---     ---+---+---     ---+---+--- ')
    print(f'2 {board[0][1][0]} | {board[0][1][1]} | {board[0][1][2]} 2   2 {board[1][1][0]} | {board[1][1][1]} | {board[1][1][2]} 2   2 {board[2][1][0]} | {board[2][1][1]} | {board[2][1][2]} 2')
    print(' ---+---+---     ---+---+---     ---+---+--- ')
    print(f'3 {board[0][2][0]} | {board[0][2][1]} | {board[0][2][2]} 3   3 {board[1][2][0]} | {board[1][2][1]} | {board[1][2][2]} 3   3 {board[2][2][0]} | {board[2][2][1]} | {board[2][2][2]} 3')
    print()

def player_turn(player, cpu, turn):
    print()
    print('==================== VEZ DO JOGADOR ====================')
    print('OBS: Para jogar, insira a casa no formato: "x, y, z"')
    print('em que x é a camada, y é a linha e z é a coluna. Ex: "2, 1, 1"')
    
    readLines = True

    while readLines:
        try:

            x, y, z = [int(i) for i in input('Insira a casa que você quer jogar: ')
                .replace(' ', '').split(',')]

            if (1 <= x <= 3) and (1 <= y <= 3) and (1 <= z <= 3):
                
                if board[x-1][y-1][z-1] == ' ':
                    readLines = False
                else:
                    print('Erro: essa coordenada já foi ocupada!')

            else:
                print('Erro: coordenadas inválidas. Cada coordenada deve estar entre 1 e 3.')
        except:
            print('Erro: coordenadas inválidas.')
            print('As coordenadas devem ser apenas 3 números inteiros separados por vírgula.')
    
    board[x-1][y-1][z-1] = player

    if verify_board(board, turn, player, cpu):
        cpu_turn(player, cpu, turn + 1)
    else:
        end_game()

def cpu_turn(player, cpu, turn):
    print('====================== VEZ DA CPU ======================')

    x = 0

    for c in range(5):
        cases_plays[c] = None

    while x < 3 and cases_plays[0] == None:
        y = 0
        while y < 3 and cases_plays[0] == None:

            verify_case([board[x][y][0], [x,y,0]], [board[x][y][1], [x,y,1]], [board[x][y][2], [x,y,2]], cpu, player)
            verify_case([board[x][0][y], [x,0,y]], [board[x][1][y], [x,1,y]], [board[x][2][y], [x,2,y]], cpu, player)
            verify_case([board[0][x][y], [0,x,y]], [board[1][x][y], [1,x,y]], [board[2][x][y], [2,x,y]], cpu, player)

            y +=1

        verify_case([board[x][0][0], [x,0,0]], [board[x][1][1], [x,1,1]], [board[x][2][2], [x,2,2]], cpu, player)
        verify_case([board[x][0][2], [x,0,2]], [board[x][1][1], [x,1,1]], [board[x][2][0], [x,2,0]], cpu, player)
        verify_case([board[0][x][0], [0,x,0]], [board[1][x][1], [1,x,1]], [board[2][x][2], [2,x,2]], cpu, player)
        verify_case([board[0][x][2], [0,x,2]], [board[1][x][1], [1,x,1]], [board[2][x][0], [2,x,0]], cpu, player)
        verify_case([board[0][0][x], [0,0,x]], [board[1][1][x], [1,1,x]], [board[2][2][x], [2,2,x]], cpu, player)
        verify_case([board[0][2][x], [0,2,x]], [board[1][1][x], [1,1,x]], [board[2][0][x], [2,0,x]], cpu, player)

        x += 1

    if cases_plays[0] == None:
        verify_case([board[0][0][0], [0,0,0]], [board[1][1][1], [1,1,1]], [board[2][2][2], [2,2,2]], cpu, player)
        verify_case([board[0][0][2], [0,0,2]], [board[1][1][1], [1,1,1]], [board[2][2][0], [2,2,0]], cpu, player)
        verify_case([board[0][2][0], [0,2,0]], [board[1][1][1], [1,1,1]], [board[2][0][2], [2,0,2]], cpu, player)
        verify_case([board[0][2][2], [0,2,2]], [board[1][1][1], [1,1,1]], [board[2][0][0], [2,0,0]], cpu, player)

    if cases_plays[0] != None:
        board[cases_plays[0][0]][cases_plays[0][1]][cases_plays[0][2]] = cpu
    elif cases_plays[1] != None:
        board[cases_plays[1][0]][cases_plays[1][1]][cases_plays[1][2]] = cpu
    elif cases_plays[2] != None:
        board[cases_plays[2][0]][cases_plays[2][1]][cases_plays[2][2]] = cpu
    elif cases_plays[3] != None:
        board[cases_plays[3][0]][cases_plays[3][1]][cases_plays[3][2]] = cpu
    else:
        board[cases_plays[4][0]][cases_plays[4][1]][cases_plays[4][2]] = cpu

    if verify_board(board, turn, player, cpu):
        player_turn(player, cpu, turn + 1)
    else:
        end_game()

def verify_case(x, y, z, cpu, player):

    blank_occ = 0
    cpu_occ = 0
    player_occ = 0

    if x[0] == cpu:
        cpu_occ += 1
    elif x[0] == player:
        player_occ += 1
    else:
        blank_occ += 1

    if y[0] == cpu:
        cpu_occ += 1
    elif y[0] == player:
        player_occ += 1
    else:
        blank_occ += 1
    
    if z[0] == cpu:
        cpu_occ += 1
    elif z[0] == player:
        player_occ += 1
    else:
        blank_occ += 1

    if blank_occ == 1 and cpu_occ == 2:
        if x[0] == ' ':
            cases_plays[0] = x[1]
            return
        elif y[0] == ' ':
            cases_plays[0] = y[1]
            return
        else:
            cases_plays[0] = z[1]
            return

    if blank_occ == 1 and player_occ == 2:
        if x[0] == ' ':
            cases_plays[1] = x[1]
            return
        elif y[0] == ' ':
            cases_plays[1] = y[1]
            return
        else:
            cases_plays[1] = z[1]
            return

    if blank_occ == 2 and cpu_occ == 1:
        if x[0] == ' ':
            cases_plays[2] = x[1]
            return
        elif y[0] == ' ':
            cases_plays[2] = y[1]
            return

    if blank_occ == 3:
        cases_plays[3] = x[1]
        return

    if x[0] == ' ':
        cases_plays[4] = x[1]
        return
    elif y[0] == ' ':
        cases_plays[4] = y[1]
        return
    elif z[0] == ' ':
        cases_plays[4] = z[1]
        return

        

def verify_board(board, turn, player, cpu):
    
    win = False
    lose = False

    x = 0

    while x < 3 and win == False and lose == False:
        y = 0
        while y < 3 and win == False and lose == False:
            if board[x][y][0] == board[x][y][1] == board[x][y][2] == player:
                win = True
            
            if board[x][y][0] == board[x][y][1] == board[x][y][2] == cpu:
                lose = True
                
            if board[x][0][y] == board[x][1][y] == board[x][2][y] == player:
                win = True

            if board[x][0][y] == board[x][1][y] == board[x][2][y] == cpu:
                lose = True

            if board[0][x][y] == board[1][x][y] == board[2][x][y] == player:
                win = True

            if board[0][x][y] == board[1][x][y] == board[2][x][y] == cpu:
                lose = True

            y += 1
        
        if board[x][0][0] == board[x][1][1] == board[x][2][2] == player:
            win = True

        if board[x][0][0] == board[x][1][1] == board[x][2][2] == cpu:
            lose = True

        if board[x][0][2] == board[x][1][1] == board[x][2][0] == player:
            win = True

        if board[x][0][2] == board[x][1][1] == board[x][2][0] == cpu:
            lose = True

        if board[0][x][0] == board[1][x][1] == board[2][x][2] == player:
            win = True

        if board[0][x][0] == board[1][x][1] == board[2][x][2] == cpu:
            lose = True

        if board[0][x][2] == board[1][x][1] == board[2][x][0] == player:
            win = True

        if board[0][x][2] == board[1][x][1] == board[2][x][0] == cpu:
            lose = True

        if board[0][0][x] == board[1][1][x] == board[2][2][x] == player:
            win = True

        if board[0][0][x] == board[1][1][x] == board[2][2][x] == cpu:
            lose = True

        if board[0][2][x] == board[1][1][x] == board[2][0][x] == player:
            win = True

        if board[0][2][x] == board[1][1][x] == board[2][0][x] == cpu:
            lose = True

        x += 1

    if win == False and lose == False:
        if board[0][0][0] == board[1][1][1] == board[2][2][2] == player:
            win = True

        if board[0][0][0] == board[1][1][1] == board[2][2][2] == cpu:
            lose = True

        if board[0][0][2] == board[1][1][1] == board[2][2][0] == player:
            win = True

        if board[0][0][2] == board[1][1][1] == board[2][2][0] == cpu:
            lose = True

        if board[0][2][0] == board[1][1][1] == board[2][0][2] == player:
            win = True

        if board[0][2][0] == board[1][1][1] == board[2][0][2] == cpu:
            lose = True

        if board[0][2][2] == board[1][1][1] == board[2][0][0] == player:
            win = True

        if board[0][2][2] == board[1][1][1] == board[2][0][0] == cpu:
            lose = True

    if win:
        scoreboard[0] = scoreboard[0] + 1
        print('=================== VITÓRIA ====================')
        show_board()
        print('=================== VITÓRIA ====================')

        return False

    if lose:
        scoreboard[1] = scoreboard[1] + 1
        print('=================== DERROTA ====================')
        show_board()
        print('=================== DERROTA ====================')

        return False

    if turn == 27:
        scoreboard[2] = scoreboard[2] + 1
        print()
        print('=================== EMPATE ====================')
        show_board()
        print('=================== EMPATE ====================')
        print()
        return False

    print()
    show_board()
    print()
    return True

def reset_board():
    for x in range(3):
        for y in range(3):
            for z in range(3):
                board[x][y][z] = ' '

def end_game():
    print('=================== PLACAR ===================')
    print(f'===== VITÓRIAS: {scoreboard[0]}')
    print(f'===== DERROTAS: {scoreboard[1]}')
    print(f'===== EMPATES: {scoreboard[2]}')
    print('==============================================')
    if scoreboard[0] > scoreboard[1]:
        print('PARABÉNS, VOCÊ POSSUI CAPACIDADE CEREBRAL O SUFICIENTE PARA GANHAR DE UMA CPU MAL FEITA')
    else:
        print('TA PASSANDO FOME PRA UMA CPU MEIA BOCA? VC NASCEU COM O CEREBRO DERRETIDO OU ESCUTOU MUITO KPOP?')
    print('==============================================')

    print('1 - Sim')
    print('2 - Não')

    option = '0'

    while option != '1' and option != '2':
        option = input('Deseja jogar novamente? ')

    if option == '1':
        start_game()
    else:
        show_creditos()

def show_creditos():
    print()
    print()
    print('============== OBRIGADO POR JOGAR! ===============')
    print('=========== FEITO POR FELIPE E BRENO! ============')
    print('==================================================')

start_game()