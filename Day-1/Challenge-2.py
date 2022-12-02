# input.txt file needs to be created from advent of code day 1 website. 

if __name__ == '__main__':
    with open('input.txt') as f:
        all_food = [line.rstrip() for line in f]    # Strip newline as it messes up reading of file

        calorie_count = []

        sum_person = 0
        for item in all_food:
            if item != '':
                sum_person += int(item)
            else:
                calorie_count.append(sum_person)
                sum_person = 0
        
        calorie_count.append(sum_person)   # Append last sum

        # To find top 3, simply sort the lost in reverse order and extrat first three elements
        calorie_count.sort(reverse=True)
        tmp = calorie_count[:3]
        
        print(sum(tmp))
        
            