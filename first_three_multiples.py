# Write your first_three_multiples function here
def first_three_multiples(num):
    i=1
    while i<=3:
        curr = i*num
        print(curr)
        i+=1
    return curr
# Uncomment these function calls to test your first_three_multiples function:
first_three_multiples(10)
# should print 10, 20, 30, and return 30
first_three_multiples(0)
# should print 0, 0, 0, and return 0