if __name__ == '__main__':
    # Parse file
    with open('input.txt', 'r') as f:  
        lines = [line.rstrip() for line in f]   # Strip newline as it messes up reading of file

        count = 0
        for line in lines:
            pair = line.split(",")
            a = pair[0].split("-")
            b = pair[1].split("-")
            
            # Convert char to int and compare ranges
            if (int(a[0]) <= int(b[0])) & (int(a[1]) >= int(b[1])):
                count += 1
            
            # Compare opposite range
            elif (int(b[0]) <= int(a[0])) & (int(b[1]) >= int(a[1])):
                count += 1
        
        print(count)