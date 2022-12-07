if __name__ == '__main__':
    lower = 96  # Conversion with ord() function
    UPPER = 38  

    # Parse file
    with open('input.txt', 'r') as f:  
        lines = [line.rstrip().split(' ') for line in f]   # Strip newline as it messes up reading of file

        sum = 0
        for line in lines:
            a_freq = {}
            b_freq = {}

            string = line[0]
            a = string[0:len(string)//2]
            b = string[len(string)//2:]

            common = list(set(a)&set(b))
            
            for char in common:
                if char.isupper() == True:
                    sum += ord(char)-UPPER
                else:
                    sum += ord(char)-lower
        
        print(sum)