numbers = dict()
txt = [input('Please,start to type the numbers:')]
for line in txt :
    findi = line.split()
    for i in findi :
        inte = int(i)
        numbers[inte] = numbers.get(inte, 0) + 1
print('YOUR RESULTS:')
bignumber = None
mostnumber = None
for inte,bers in numbers.items() :
    if bignumber is None or bers > bignumber :
        mostnumber = inte
        bignumber = bers
print(f'the number that most apper is : {mostnumber} ,because it appers {bignumber} many times')  #ps:if there are 2numbers reapeting the same amount it doesnt show,try to solve using sort(michigan 2,week 4 chapter 9)
total = 0
count = 0  #print(inte,bers,i,findi,txt,line) #inte=the big number among all the numbers,ex:45\bers=1(dn why)\i=bignumber\findi=list\line=numbers withoutlist
for number in findi:
    x = int(number)
    total = total + x
    count = len(findi)
    average = total / count
    counting =  count % 2
if counting == 0 :
    print('the amount of numbers you gave me are even')

if counting != 0 :
    print('the amount of numbers you gave me are odd')

print('the average of the numbers you gave me is:',average)




