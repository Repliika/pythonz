
def find_it(seq):
    odds = []
    double_odd = []
    for i in seq:
        if i % 2 != 0:
            odds.append(i) 
    
    for num in odds:
        if odds.count(num) % 2 !=0 and num not in double_odd:
            double_odd.append(num)
    print(double_odd)
    return None



seq= (1,1,2,3,3,3,5,6,6,7)
find_it(seq)