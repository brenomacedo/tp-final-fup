
scoreboard = [0,0,0]
cases_plays = [None]*5
who_begins = 0
last_played = [None] * 3

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

def tic_tac_toe():

  board = [[[' ' for i in range(3)] for i in range(3)] for i in range(3)]
  
  for c in range(3):
    last_played[c] = None
  
  turn = 0
  marks = ['O','X']

  def show_mark(x,y,z):
    if last_played[0] == x and last_played[1] == y and last_played[2] == z:
      return YELLOW + BOLD + board[x][y][z] + OKGREEN + BOLD
    else:
      return board[x][y][z]

  def start_game():

    nonlocal marks

    option = '0'

    show_menu()

    print()

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

    begin_option = '0'

    while begin_option != '1' and begin_option != '2':
        begin_option = input(YELLOW + BOLD + 'Quem começa? ' + ENDC + HEADER)

        if begin_option != '1' and begin_option != '2':
            print(FAIL + BOLD + 'Opção inválida! As opções válidas são 1 e 2!' + HEADER + ENDC)

    global who_begins

    if begin_option == '2':
        who_begins = 1

    if option == '1':
      show_board()
    elif option == '2':
      show_board()
      marks = marks[::-1]
      

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

  def cpu_turn(player, cpu):
    nonlocal board
    print(BOLD + '====================== VEZ DA CPU ======================' + ENDC)

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

  def verify_victory(move,mark):

    nonlocal board

    def verify(layer,line,column):

      nonlocal mark

      tile = board[layer][line][column]

      same_mark = (mark == tile)

      return same_mark

    def new_list(listtype,index,new_element):
      new = list(listtype)
      new[index] = new_element
      return(new)
    
    def line_row(axis,coordinates = move,stop = False):

      row = coordinates[axis]
      row = (row+1)%3
      new_position = new_list(coordinates,axis,row)

      if(verify(*new_position)):

        if(not stop): return line_row(axis,new_position,True)
        else:return True
        
    def diagonal_row(axis,coordinates = move):

      plane = list(coordinates)
      del plane[axis]
      x,y = plane[0],plane[1]

      if((x+y)%2 == 0):

        diagonals =[
          [[0,0],[1,1],[2,2]],
          [[0,2],[1,1],[2,0]]
        ] 
        
        for diagonal in diagonals:

          consecutive = True

          for position in diagonal:

            position.insert(axis,coordinates[axis])

            consecutive *= verify(*position)
          
          if(consecutive): return True
      
      return False

    def universal_diagonal(coordinates = move):

      number_of_2s =coordinates.count(1)

      if(number_of_2s == 0):

        opposing_vertex = [0 if i == 2 else 2 for i in coordinates]
        return(verify(1,1,1) and verify(*opposing_vertex))

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

    victory = universal_diagonal()
    axis = 0

    while not victory and axis<3:
      victory = line_row(axis) or diagonal_row(axis)
      axis += 1
    
    return(victory)


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

def show_scoreboard():
  print()
  print('============================= PLACAR =============================')
  print(f'========================= VITORIAS: {scoreboard[0]} ============================')
  print(f'========================= DERROTAS: {scoreboard[2]} ============================')
  print(f'========================= EMPATES: {scoreboard[1]} =============================')
  print('==================================================================')
  print()

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

show_banner()
tic_tac_toe()