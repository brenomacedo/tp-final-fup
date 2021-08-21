#
#    TRABALHO PRÁTICO FINAL DE FUP
#    NOMES DOS MEMBROS DA EQUIPE:
#    Breno Macêdo de Brito - 514513
#    Felipe Vieira Duarte - 509067
#

# Definir o placar (a posição 0 é a quantidade de vitórias,
# 1 é a quantidade de empates e 2 a de derrotas)

scoreboard = [0,0,0]

# Definir as cores
# utilizadas no código

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
YELLOW = '\033[33m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

# Iniciar a função do jogo

def tic_tac_toe():

  # Definir o tabuleiro
  # Definir os casos, A, B, C, D e E do computador, em que a
  # variável cases_plays irá armazenar as possíveis jogadas de cada caso

  board = [[[' ' for i in range(3)] for i in range(3)] for i in range(3)]
  
  cases_plays = [None]*5
  last_played = [None] * 3
  who_begins = 0
  
  # O turno da jogada, será utilizado para saber quem venceu,
  # quem perdeu ou se for empate (se o turno chegar a 27)

  turn = 0

  # Um vetor que, na primeira posição, armazenará o simbolo do jogador e, na segunda posição,
  # armazenará o símbolo da cpu

  marks = ['O','X']

  # A função show_mark irá verificar se o símbolo é o último símbolo jogado
  # e, caso for, irá mostrá-lo destacado no tabuleiro, para evitar que o jogador
  # fique buscando qual foi a jogada do adversário.

  def show_mark(x,y,z):
    if last_played[0] == x and last_played[1] == y and last_played[2] == z:
      return YELLOW + BOLD + board[x][y][z] + OKGREEN + BOLD
    else:
      return board[x][y][z]

  # Iniciar o jogo

  def start_game():

    nonlocal marks

    option = '0'

    show_menu()

    print()

    # Ler o símbolo que o jogador deseja jogar

    while option != '1' and option != '2' and option != '3':
      option = input(YELLOW + BOLD + 'Selecione com qual símbolo deseja jogar: ' + HEADER + ENDC)

      if option != '1' and option != '2' and option != '3':
        print(FAIL + BOLD + 'Opção inválida, tente novamente.' + HEADER + ENDC)

    
    if option == '3':
      show_creditos()
      return(True)

    print(OKBLUE + BOLD + 'Quem deverá começar?')
    print('1 - Eu')
    print('2 - O Computador' + HEADER + ENDC)

    # Ler quem deverá começar

    begin_option = '0'

    while begin_option != '1' and begin_option != '2':
        begin_option = input(YELLOW + BOLD + 'Quem começa? ' + ENDC + HEADER)

        if begin_option != '1' and begin_option != '2':
            print(FAIL + BOLD + 'Opção inválida! As opções válidas são 1 e 2!' + HEADER + ENDC)

    nonlocal who_begins

    if begin_option == '2':
        who_begins = 1

    # Inverter as posições do vetor marks caso o jogador escolha jogar com o
    # símbolo X

    if option == '1':
      show_board()
    elif option == '2':
      show_board()
      marks = marks[::-1]

  # A função show_menu irá simplesmente mostrar o menu

  def show_menu():
    print()
    print(BOLD + OKBLUE + 'Instruções:')
    print('O terminal mostrará as opções disponíves na forma: "NÚMERO - AÇÃO"')
    print('Entre com o número que corresponde a ação que você quer realizar para prosseguir.')
    print()
    print('1 - Jogar com o símbolo O')
    print('2 - Jogar com o símbolo X')
    print('3 - Sair' + HEADER + ENDC)
    print()

  # A função show_board irá pegar o vetor board e mostrar ele na forma
  # de um jogo da velha 3D

  def show_board():
    print()
    print(OKGREEN + BOLD + '============== TABULEIRO ATUAL ==============')
    print()
    print('  CAMADA  1       CAMADA  2       CAMADA  3  ')
    print('  1   2   3       1   2   3       1   2   3  ')
    print(f'1 {show_mark(0,0,0)} | {show_mark(0,0,1)} | {show_mark(0,0,2)} 1   1 {show_mark(1,0,0)} | {show_mark(1,0,1)} | {show_mark(1,0,2)} 1   1 {show_mark(2,0,0)} | {show_mark(2,0,1)} | {show_mark(2,0,2)} 1')
    print(' ---+---+---     ---+---+---     ---+---+--- ')
    print(f'2 {show_mark(0,1,0)} | {show_mark(0,1,1)} | {show_mark(0,1,2)} 2   2 {show_mark(1,1,0)} | {show_mark(1,1,1)} | {show_mark(1,1,2)} 2   2 {show_mark(2,1,0)} | {show_mark(2,1,1)} | {show_mark(2,1,2)} 2')
    print(' ---+---+---     ---+---+---     ---+---+--- ')
    print(f'3 {show_mark(0,2,0)} | {show_mark(0,2,1)} | {show_mark(0,2,2)} 3   3 {show_mark(1,2,0)} | {show_mark(1,2,1)} | {show_mark(1,2,2)} 3   3 {show_mark(2,2,0)} | {show_mark(2,2,1)} | {show_mark(2,2,2)} 3' + ENDC + HEADER)
    print()

  # A função error mostrará um erro de entrada, de acordo com o tipo
  # de erro na função player_turn.

  def error(index):

    if(index == 0):
      print(FAIL + BOLD + "\nENTRADA INVÁLIDA\n")
      print("\nNúmeros de 1 a 3, separados por vírgula")
      print("Exemplo: 3,1,2" + ENDC + HEADER)

    elif(index == 1):
      print(FAIL + BOLD + "\nNão há coordenadas o suficiente, insira os três eixos" + HEADER + ENDC)

    elif(index == 2):
      print(FAIL + BOLD + "\nPosição não existente, reinsira o valor" + HEADER + ENDC)

    elif(index == 3):
      print(FAIL + BOLD + "\nEssa casa já está preenchida, insira uma nova posição" + HEADER + ENDC)

  # A função move coloca o elemento em sua devida posição

  def move(layer,line,column):

    nonlocal turn
    nonlocal board

    elemento = marks[(turn + who_begins)%2]
    turn += 1
    board[layer][line][column] = elemento

    last_played[0] = layer
    last_played[1] = line
    last_played[2] = column

    show_board()

  # A função player_turn recebe os inputs do player para uma jogada e retorna a jogada
  # para a análise de vitória

  def player_turn():

      print('\nSelecione onde será sua jogada:')

      try: coordinates = [int(i.strip()) for i in input().split(',')]

      except: return(error(0))

      if(len(coordinates)!=3):return(error(1))

      find_element = board

      for index,coordinate in enumerate(coordinates):

        coordinate-=1

        coordinates[index] = coordinate

        if(coordinate<0 or 2<coordinate): return(error(2))

        find_element = find_element[coordinate]

      if(find_element in ["O","X"]): return(error(3))

      move(*coordinates)

      return coordinates

  # A função cpu_turn recebe o marcador do player e da cpu e percorre o vetor board
  # para verificar os possíveis casos em cada linha, coluna e diagonal e, em seguida,
  # realiza a jogada no caso encontrado que tiver maior prioridade

  def cpu_turn(player, cpu):
    nonlocal board
    print(BOLD + '====================== VEZ DA CPU ======================' + ENDC)

    x = 0

    for c in range(5):
        cases_plays[c] = None

    # Percorrer o vetor board para encontrar cada caso possível em linhas, colunas e diagonais

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

    # Após enumerar os casos, realizar a jogada no caso que tiver maior prioridade.

    if cases_plays[0] != None:
      board[cases_plays[0][0]][cases_plays[0][1]][cases_plays[0][2]] = cpu

      last_played[0] = cases_plays[0][0]
      last_played[1] = cases_plays[0][1]
      last_played[2] = cases_plays[0][2]
    elif cases_plays[1] != None:
      board[cases_plays[1][0]][cases_plays[1][1]][cases_plays[1][2]] = cpu

      last_played[0] = cases_plays[1][0]
      last_played[1] = cases_plays[1][1]
      last_played[2] = cases_plays[1][2]
    elif cases_plays[2] != None:
      board[cases_plays[2][0]][cases_plays[2][1]][cases_plays[2][2]] = cpu

      last_played[0] = cases_plays[2][0]
      last_played[1] = cases_plays[2][1]
      last_played[2] = cases_plays[2][2]
    elif cases_plays[3] != None:
      board[cases_plays[3][0]][cases_plays[3][1]][cases_plays[3][2]] = cpu

      last_played[0] = cases_plays[3][0]
      last_played[1] = cases_plays[3][1]
      last_played[2] = cases_plays[3][2]
    else:
      board[cases_plays[4][0]][cases_plays[4][1]][cases_plays[4][2]] = cpu

      last_played[0] = cases_plays[4][0]
      last_played[1] = cases_plays[4][1]
      last_played[2] = cases_plays[4][2]

    nonlocal turn
    turn += 1

    show_board()

  # A função verify_case irá receber, nos valores x, y e z, um vetor de duas posições,
  # contendo na primeira posição, o marcador, e na segunda posição suas coordenadas,
  # em que x, y e z serão uma linha, coluna ou diagonal

  # em seguida, a função verificará os casos em que essa sequência se encaixa

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
      elif y[0] == ' ':
        cases_plays[0] = y[1]
      else:
        cases_plays[0] = z[1]
      
      nonlocal winner
      winner = True

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

  # A função verify_victory, recebe a posição da última jogada do jogador, e, a partir dela,
  # analisa todas as retas que ela pode completar, retornando vitoria caso exista.

  def verify_victory(move,mark):

    nonlocal board


    # A função verify verifica se o elemento na posição é o mesmo elemento usado pelo jogador.

    def verify(layer,line,column):

      nonlocal mark

      tile = board[layer][line][column]

      same_mark = (mark == tile)

      return same_mark

    # A função new_list é usada para criar uma nova coordenada mudando apenas
    # o valor de uma coordenada prévia.

    def new_list(listtype,index,new_element):
      new = list(listtype)
      new[index] = new_element
      return(new)

    # A função line_row fixa o eixo e examina se as outras duas posições 
    # nessa reta também pertencem ao jogador.

    def line_row(axis,coordinates = move,stop = False):

      #row é a posição na reta, new_position sua sucessão no loop (1=>2=>3=>1)

      row = coordinates[axis]
      new_position = new_list(coordinates,axis,(row+1)%3)

      if(verify(*new_position)):

        #Se essa nova posição é do jogador, verifica-se o elemento que a sucede
        #caso seja também do jogador, retorna verdadeiro

        if(not stop): return line_row(axis,new_position,True)
        else:return True

    # Fixa um dos três planos que intersectam o elemento da coordenada e analisa as duas diagonais
        
    def diagonal_row(axis,coordinates = move):

      #retira o eixo
      plane = list(coordinates)
      del plane[axis]
      x,y = plane[0],plane[1]

      if((x+y)%2 == 0):

        diagonals =[
          [[0,0],[1,1],[2,2]],
          [[0,2],[1,1],[2,0]]
        ] 
        
        #vê se uma das duas diagonais está preenchida
        for diagonal in diagonals:

          consecutive = True

          for position in diagonal:
            
            #adiciona o eixo a posição da diagonal
            position.insert(axis,coordinates[axis])

            consecutive *= verify(*position)
          
          if(consecutive): return True
      
      return False

    # Verifica as diagonais que possuem 3 dimensões (diagonais internas do cubo) para
    # saber se elas possuem 3 símbolos do jogador.

    def universal_diagonal(coordinates = move):

      number_of_2s =coordinates.count(1)

      #vértices do cubo
      if(number_of_2s == 0):

        opposing_vertex = [0 if i == 2 else 2 for i in coordinates]
        return(verify(1,1,1) and verify(*opposing_vertex))

      #centro do cubo
      elif(number_of_2s == 3):

        diagonal_origins = [
          [0,0,0],
          [0,0,2],
          [0,2,2],
          [0,2,2]
          ]

        for k in range(4):

          origin = diagonal_origins[k]
          opposing_vertex = [0 if i == 2 else 2 for i in origin]

          if(verify(*origin) and verify(*opposing_vertex)): 
            return True   

      return False

    #Verifica-se linhas 3d.
    victory = universal_diagonal()
    axis = 0

    #Verifica-se as diagonais e linhas 2d em cada um dos eixos e planos que eles definem.

    while not victory and axis<3:
      victory = line_row(axis) or diagonal_row(axis)
      axis += 1
    
    return(victory)

  # A função show_creditos irá mostrar os creditos do trabalho ao sair do jogo.

  def show_creditos():
    print()
    print()
    print(OKCYAN + BOLD + '==================================================================')
    print()
    print()
    print('                    ⡿⠋⠄⣀⣀⣤⣴⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣌⠻⣿⣿')
    print('                    ⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠹⣿')
    print('                    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠹')
    print('                    ⣿⣿⡟⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡛⢿⣿⣿⣿⣮⠛⣿⣿⣿⣿⣿⣿⡆')
    print('                    ⡟⢻⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣣⠄⡀⢬⣭⣻⣷⡌⢿⣿⣿⣿⣿⣿')
    print('                    ⠃⣸⡀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠈⣆⢹⣿⣿⣿⡈⢿⣿⣿⣿⣿')
    print('                    ⠄⢻⡇⠄⢛⣛⣻⣿⣿⣿⣿⣿⣿⣿⣿⡆⠹⣿⣆⠸⣆⠙⠛⠛⠃⠘⣿⣿⣿⣿')
    print('                    ⠄⠸⣡⠄⡈⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠁⣠⣉⣤⣴⣿⣿⠿⠿⠿⡇⢸⣿⣿⣿')
    print('                    ⠄⡄⢿⣆⠰⡘⢿⣿⠿⢛⣉⣥⣴⣶⣿⣿⣿⣿⣻⠟⣉⣤⣶⣶⣾⣿⡄⣿⡿⢸')
    print('                    ⠄⢰⠸⣿⠄⢳⣠⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣼⣿⣿⣿⣿⣿⣿⡇⢻⡇⢸')
    print('                    ⢷⡈⢣⣡⣶⠿⠟⠛⠓⣚⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⢸⠇⠘')
    print('                    ⡀⣌⠄⠻⣧⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠛⠛⢿⣿⣿⣿⣿⣿⡟⠘⠄⠄')
    print('                    ⣷⡘⣷⡀⠘⣿⣿⣿⣿⣿⣿⣿⣿⡋⢀⣠⣤⣶⣶⣾⡆⣿⣿⣿⠟⠁⠄⠄⠄⠄')
    print('                    ⣿⣷⡘⣿⡀⢻⣿⣿⣿⣿⣿⣿⣿⣧⠸⣿⣿⣿⣿⣿⣷⡿⠟⠉⠄⠄⠄⠄⡄⢀')
    print('                    ⣿⣿⣷⡈⢷⡀⠙⠛⠻⠿⠿⠿⠿⠿⠷⠾⠿⠟⣛⣋⣥⣶⣄⠄⢀⣄⠹⣦⢹⣿')
    print()
    print()
    print('                      Criado por: Felipe e Breno!')
    print('                          OBRIGADO POR JOGAR!')
    print()
    print()
    show_scoreboard()
    print('==================================================================' + HEADER + ENDC)

  # Finaliza o jogo no turno recebido.

  def end_game(turn):

    if(turn == 27): 
      scoreboard[1] += 1
      print(OKCYAN + BOLD + '\n==================== EMPATE ====================')
      show_scoreboard()
      print('\n==================== EMPATE ====================' + HEADER + ENDC)
    elif((turn + who_begins)%2 - 1 == 0):
      scoreboard[0] += 1
      print(OKCYAN + BOLD + '\n================ 🎉✨🎉 VITORIA 🎉✨🎉 ================')
      show_scoreboard()
      print('\n================ 🎉✨🎉 VITORIA 🎉✨🎉 ================' + HEADER + ENDC)
    else:
      scoreboard[2] += 1
      print(OKCYAN + BOLD + '\n================ 😢😢😭 PERDESTE 😭😢😢 ================')
      show_scoreboard()
      print('\n================ 😢😢😭 PERDESTE 😭😢😢 ================' + HEADER + ENDC)
    
    print(YELLOW + BOLD + '\nJogar Novamente?\n')
    print('1 - Sim\n2 - Não' + HEADER + ENDC)

    action = '0'

    while action != '1' and action != '2':
      action = input(YELLOW + BOLD + 'Deseja jogar novamente? ' + ENDC + HEADER)

      if action != '1' and action != '2':
        print(FAIL + BOLD + 'Opção inválida, as opções disponíveis são 1 ou 2!' + ENDC + HEADER)

    if action == '1':
      return tic_tac_toe()

    return(show_creditos())

  end = start_game()

  if(end == True): return(None)

  print(OKGREEN + '\nOrdem: Camada , Linha, Coluna' + HEADER)
  print(OKGREEN + '\nValores de 1 a 3 para as posições' + HEADER)

  winner = False

  while turn<27 and not winner:

    if((turn + who_begins)%2 == 0):

      play = player_turn()

      if(play != None):

        player = marks[(turn -1+ who_begins)%2]

        winner = verify_victory(play,player)

    else:
      cpu_turn(marks[0], marks[1])

    if(winner): end_game(turn)

# A função show_scoreboard irá mostrar o placar de vitórias, derrotas e de empates
# contabilizados durante as partidas

def show_scoreboard():
  print()
  print('============================= PLACAR =============================')
  print(f'========================= VITORIAS: {scoreboard[0]} ============================')
  print(f'========================= DERROTAS: {scoreboard[2]} ============================')
  print(f'========================= EMPATES: {scoreboard[1]} =============================')
  print('==================================================================')
  print()

# A função show_banner irá mostrar uma tela de boas-vindas para o jogador, mostrando
# o título do jogo e os criadores

def show_banner():
  print(BOLD + OKBLUE + '==================================================================')
  print('      _                         _                   _ _             _____ ____  ')
  print('     | | ___   __ _  ___     __| | __ _  __   _____| | |__   __ _  |___ /|  _ \ ')
  print('  _  | |/ _ \ / _` |/ _ \   / _` |/ _` | \ \ / / _ \ | \'_ \ / _` |   |_ \| | | |')
  print(' | |_| | (_) | (_| | (_) | | (_| | (_| |  \ V /  __/ | | | | (_| |  ___) | |_| |')
  print('  \___/ \___/ \__, |\___/   \__,_|\__,_|   \_/ \___|_|_| |_|\__,_| |____/|____/ ')
  print('              |___/                                                             ')
  print()
  print()
  print('                    ⡆⣐⢕⢕⢕⢕⢕⢕⢕⢕⠅⢗⢕⢕⢕⢕⢕⢕⢕⠕⠕⢕⢕⢕⢕⢕⢕⢕⢕⢕')
  print('                    ⢐⢕⢕⢕⢕⢕⣕⢕⢕⠕⠁⢕⢕⢕⢕⢕⢕⢕⢕⠅⡄⢕⢕⢕⢕⢕⢕⢕⢕⢕')
  print('                    ⢕⢕⢕⢕⢕⠅⢗⢕⠕⣠⠄⣗⢕⢕⠕⢕⢕⢕⠕⢠⣿⠐⢕⢕⢕⠑⢕⢕⠵⢕')
  print('                    ⢕⢕⢕⢕⠁⢜⠕⢁⣴⣿⡇⢓⢕⢵⢐⢕⢕⠕⢁⣾⢿⣧⠑⢕⢕⠄⢑⢕⠅⢕')
  print('                    ⢕⢕⠵⢁⠔⢁⣤⣤⣶⣶⣶⡐⣕⢽⠐⢕⠕⣡⣾⣶⣶⣶⣤⡁⢓⢕⠄⢑⢅⢑')
  print('                    ⠍⣧⠄⣶⣾⣿⣿⣿⣿⣿⣿⣷⣔⢕⢄⢡⣾⣿⣿⣿⣿⣿⣿⣿⣦⡑⢕⢤⠱⢐')
  print('                    ⢠⢕⠅⣾⣿⠋⢿⣿⣿⣿⠉⣿⣿⣷⣦⣶⣽⣿⣿⠈⣿⣿⣿⣿⠏⢹⣷⣷⡅⢐')
  print('                    ⣔⢕⢥⢻⣿⡀⠈⠛⠛⠁⢠⣿⣿⣿⣿⣿⣿⣿⣿⡀⠈⠛⠛⠁⠄⣼⣿⣿⡇⢔')
  print('                    ⢕⢕⢽⢸⢟⢟⢖⢖⢤⣶⡟⢻⣿⡿⠻⣿⣿⡟⢀⣿⣦⢤⢤⢔⢞⢿⢿⣿⠁⢕')
  print('                    ⢕⢕⠅⣐⢕⢕⢕⢕⢕⣿⣿⡄⠛⢀⣦⠈⠛⢁⣼⣿⢗⢕⢕⢕⢕⢕⢕⡏⣘⢕')
  print('                    ⢕⢕⠅⢓⣕⣕⣕⣕⣵⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣷⣕⢕⢕⢕⢕⡵⢀⢕⢕')
  print('                    ⢑⢕⠃⡈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢃⢕⢕⢕')
  print('                    ⣆⢕⠄⢱⣄⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢁⢕⢕⠕⢁')
  print('                    ⣿⣦⡀⣿⣿⣷⣶⣬⣍⣛⣛⣛⡛⠿⠿⠿⠛⠛⢛⣛⣉⣭⣤⣂⢜⠕⢑⣡⣴⣿')
  print()
  print()
  print('                      Criado por: Felipe e Breno!')
  print()
  print()
  print()
  print('==================================================================')

# Mostrar o banner e iniciar o jogo

show_banner()
tic_tac_toe()