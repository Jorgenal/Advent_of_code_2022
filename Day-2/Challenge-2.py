if __name__ == '__main__':
    # A = rock, B = Paper, C = Scissor
    # X = loss, Y = draw, Z = win
    # Rock = 1, Paper = 2, Scissor = 3, loss = 0, draw = 3, win = 6
    scores = {'rock': 1, 'paper': 2, 'scissor': 3}
    translate = {'A': 'rock', 'X': 'loss', 'B': 'paper', 'Y': 'draw', 'C': 'scissor', 'Z': 'win'}

    opponent = []
    result = []

    # Parse file and create list of moves
    with open('input.txt', 'r') as f:  
        lines = [line.rstrip().split(' ') for line in f]   # Strip newline as it messes up reading of file

        for line in lines:
            opponent.append(line[0])
            result.append(line[1])
    
    my_score = 0
    for i in range(len(opponent)):
        # Translate to rock/paper/scissor and result  
        opp_val = translate[opponent[i]]
        res = translate[result[i]]

        if(res == 'loss'):
            if(opp_val == 'rock'):
                my_score += scores['scissor']
            elif (opp_val == 'paper'):
                my_score += scores['rock']
            else:
                my_score += scores['paper']
            # My_score += 0

        elif(res == 'draw'):
            my_score += scores[opp_val]
            my_score += 3
        
        else:
            if(opp_val == 'rock'):
                my_score += scores['paper']
            elif(opp_val == 'scissor'):
                my_score += scores['rock']
            else:
                my_score += scores['scissor']
            my_score += 6

    print(my_score)
