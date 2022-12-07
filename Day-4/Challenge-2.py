if __name__ == '__main__':
    # Parse file
    with open('input.txt', 'r') as f:  
        lines = [line.rstrip() for line in f]   # Strip newline as it messes up reading of file

        count = 0
        for line in lines:
            pair = line.split(",")
            a = int(pair[0].split("-")[0])
            b = int(pair[0].split("-")[1])
            c = int(pair[1].split("-")[0])
            d = int(pair[1].split("-")[1])
            
            #a-b, c-d
            if(b >= c) & (d >= a):
                count += 1

        
        print(count)