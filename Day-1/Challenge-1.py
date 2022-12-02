# input.txt file needs to be created from advent of code day 1 website. 

if __name__ == '__main__':
    with open('input.txt') as f:
        all_food = [line.rstrip() for line in f]    # Strip newline as it messes up reading of file

        calorie_count = []

        sum = 0
        for item in all_food:
            if item != '':
                sum += int(item)
            else:
                calorie_count.append(sum)
                sum = 0
        
        calorie_count.append(sum)   # Append last sum

        print("Max: ", max(calorie_count))
        
            