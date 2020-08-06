# Your code here
import math, random

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

# why don't I create the answers before hand?
print("BUILDING POWERS")
powers = {}
for x in range(2, 15):
    for y in range(3, 7):
        powers[(x, y)] = math.pow(x, y)
print("DONE!")

print("BUILDING FACTORIALS")

factorials = {}

def build_facts(n):
    if n in factorials:
        return factorials[n]
    elif n == 0:
        return 1
    else:
        x = build_facts(n-1) * n
        factorials[n] = x
        return x

for n in range(100000):
    build_facts(n)
    
print("DONE!")

# print(factorials)



def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    
    # what was the old function doing?

    #1) taking n1^n2 and storing that in v
    #2) calculating a factorial for v
        # i.e. v = 4
        # result --> 1 * 2 * 3 * 4 == 24
    #3) taking v (24) and dividing and then flooring by n1 + n2 (4) == 6
    #4) finnaly assigning v to the remainder of 982451653

    v = powers[(x, y)]

    # if (v,'fac') not in cache:
    #     cache[(v, 'fac')] = math.factorial(v)
    # v = cache[(v,'fac')]

    v = factorials[v]

    # if ('dnf', x, y) not in cache:
    #     cache[('dnf', x, y)] //= (x + y)
    # v = cache[('dnf', x, y)]

    # if (x, y, 'mod') not in cache:
    #     cache[(x, y, 'mod')] %= 982451653
    # v = cache[(x, y, 'mod')]

    return v

# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
