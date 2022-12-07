if __name__ == '__main__':
    lower = 96  # Conversion with ord() function
    UPPER = 38  

    # Parse file
    with open('input.txt', 'r') as f:  
        lines = [line.rstrip().split(' ') for line in f]   # Strip newline as it messes up reading of file, forgot to remove split, cba fixing

        sum = 0
        for i in range(0, len(lines), 3):
            a = lines[i][0]
            b = lines[i+1][0]
            c = lines[i+2][0]

            common = list(set(a)&set(b)&set(c))

            for char in common:
                if char.isupper() == True:
                    sum += ord(char)-UPPER
                else:
                    sum += ord(char)-lower
        
        print(sum)