# Write your tip function here:
def tip(total, percentage):
    tip = (total/100)*percentage
    return tip
# Uncomment these function calls to test your tip function:
print(tip(10, 25))
# should print 2.5
print(tip(0, 100))
# should print 0.0