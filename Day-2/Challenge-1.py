if __name__ == '__main__':
    # A = rock, B = Paper, C = Scissor
    # X = rock, Y = Paper, Z = Scissor
    # Rock = 1, Paper = 2, Scissor = 3, loss = 0, draw = 3, win = 6
    scores = {'rock': 1, 'paper': 2, 'scissor': 3}
    translate = {'A': 'rock', 'X': 'rock', 'B': 'paper', 'Y': 'paper', 'C': 'scissor', 'Z': 'scissor'}

    opponent = []
    myself = []

    # Parse file and create list of moves
    with open('input.txt', 'r') as f:  
        lines = [line.rstrip().split(' ') for line in f]   # Strip newline as it messes up reading of file

        for line in lines:
            opponent.append(line[0])
            myself.append(line[1])
        
    my_score = 0
    for i in range(len(opponent)):
        # Translate to rock/paper/scissor
        my_val = translate[myself[i]]
        opp_val = translate[opponent[i]]

        # Draw
        if(my_val == opp_val):
            my_score += 3
        
        # I have rock
        if(my_val == 'rock'):
            if(opp_val == 'paper'):
                pass
            elif(opp_val == 'scissor'):
                my_score += 6
        
        # I have paper
        elif(my_val == 'paper'):
            if(opp_val == 'scissor'):
                pass
            elif(opp_val == 'rock'):
                my_score += 6
        
        # I have scissor
        elif(my_val == 'scissor'):
            if(opp_val == 'rock'):
                pass
            elif(opp_val == 'paper'):
                my_score += 6
        
        # Add score for choosing certain value
        my_score += scores[my_val]

    print(my_score)





