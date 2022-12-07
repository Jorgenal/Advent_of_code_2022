if __name__ == '__main__':
    # Parse file
    with open('input.txt', 'r') as f:  
        lines = [line.rstrip() for line in f]   # Strip newline as it messes up reading of file

        cargo = {}
        inputs = []

        # Manually change range to match figure
        for i in range(1, 10):
            cargo[i] = []
        
        figure = True
        for line in lines:
            if(line == ""):
                figure = False
                pass
            
            # Append figure into cargo dict based on columns
            elif(figure == True):
                idx = 0
                for i in range(len(line)):
                    # Always spaces/chars between each letter in a figure
                    if i % 4 == 1:
                        idx+=1  # the amount of times 4 letters are parsed is an increment to index and the column letter belongs to
                        if((line[i] != " ") & (line[i].isalpha())):
                            cargo[idx].append(line[i])
            
            # Append inputs after figure
            elif(figure == False):
                inputs.append(line)

        

        # Reverse the list for each "column" to use pop and append operators to match doing one at a time
        for key in cargo.keys():
            cargo[key].reverse()

        # Parse inputs
        for input in inputs:
            lst = input.split(' ')

            count = int(lst[1])
            src = int(lst[3])
            dst = int(lst[5])

            # When popping items from a "column" the original order is reversed
            # By then using a temporary list and popping from that,
            # the original order is restored, mimicking moving x items at once 
            tmp = []

            for i in range(count):
                tmp.append(cargo[src].pop())

            for i in range(count):
                cargo[dst].append(tmp.pop())

                

        str = ""
        for key in cargo.keys():
            str += cargo[key].pop()
        
        print(str)