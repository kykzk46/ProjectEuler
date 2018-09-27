# Answer
# The "pythonic" way

def s(n): return n*(n+1)/2
def r(n): return s(n/3)*3 + s(n/5)*5 - s(n/15)*15

print '\n'.join(str(r(int(raw_input())-1)) for i in xrange(int(raw_input())))











