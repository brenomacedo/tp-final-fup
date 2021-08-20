
scoreboard = [0,0,0]
cases_plays = [None]*5

def tic_tac_toe():

  board = [[[' ' for i in range(3)] for i in range(3)] for i in range(3)]

  turn = 0
  marks = ['O','X']

  def start_game():

      nonlocal marks

      player = ''
      cpu = ''

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
      elif option == '2':
          player = 'X'
          cpu = 'O'
          marks = marks[::-1]
      else:
          show_creditos()
          return(True)
      

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

  def error(index):

    if(index == 0):
      print("\nENTRADA INVÁLIDA\n")
      print("\nNúmeros de 1 a 3, separados por vírgula")
      print("Exemplo: 3,1,2")

    elif(index == 1):
      print("\nNão há coordenadas o suficiente, insira os três eixos")

    elif(index == 2):
      print("\nPosição não existente, reinsira o valor")

    elif(index == 3):
      print("\nEssa casa já está preenchida, insira uma nova posição")

  def move(layer,line,column):

    nonlocal turn
    nonlocal board

    elemento = marks[turn%2]
    turn += 1
    board[layer][line][column] = elemento

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
    print('============== OBRIGADO POR JOGAR! ===============')
    print('=========== FEITO POR FELIPE E BRENO! ============')
    print('==================================================')

  def end_game(turn):

    if(turn == 27): 
      scoreboard[1] += 1
      print('\nEMPATE')
    elif(turn%2 - 1 == 0):
      scoreboard[0] += 1
      print('\nVITORIA')
    else:
      scoreboard[2] += 1
      print('\nALÁ O PERDEDOR KKKKKKKKKKKKKKKKKKKKKKK')
    
    print('\nJogar Novamente?\n')
    print('1 - Sim\nQualquer outra tecla - Não')

    escolha = int(input())

    if(escolha == 1):return(tic_tac_toe())

    return(show_creditos())

  end = start_game()

  if(end == True): return(None)

  print('\nOrdem: Camada , Linha, Coluna')
  print('\nValores de 1 a 3 para as posições')

  winner = False

  while turn<27 and not winner:

    if(turn%2 == 0):

      play = player_turn()

      if(play != None):

        player = marks[(turn-1)%2]

        winner = verify_victory(play,player)

    else:
      cpu_turn(marks[0], marks[1])

    if(winner): end_game(turn)

tic_tac_toe()