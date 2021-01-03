numbers = dict()
user_numbers = [input('Please,start to type the numbers:')]
for numbers_together in user_numbers :
    numbers_split = numbers_together.split()
    for str_number in numbers_split :
        int_number = int(str_number)
        numbers[int_number] = numbers.get(int_number, 0) + 1

print('YOUR RESULTS:')
bignumber = None
mostnumber = None
for most_number,big_number in numbers.items() :
    if bignumber is None or big_number > bignumber :
        mostnumber = most_number
        bignumber = big_number
print(f'The number that most apper is : {mostnumber} ,because it appers {bignumber} many times')  #ps:if there are 2numbers reapeting the same amount it doesnt show,try to solve using sort(michigan 2,week 4 chapter 9)
total = 0
count = 0  #print(inte,bers,i,findi,txt,line) #inte=the big number among all the numbers,ex:45\bers=1(dn why)\i=bignumber\findi=list\line=numbers withoutlist
for number in numbers_split:
    x = int(number)
    total = total + x
    count = len(numbers_split)
    average = total / count
    counting =  count % 2
if counting == 0 :
    print('the amount of numbers you gave me are even')

if counting != 0 :
    print('the amount of numbers you gave me are odd')

print('the average of the numbers you gave me is:',average)
