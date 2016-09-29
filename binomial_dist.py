'''
Calculate binamial dist probability
'''

from math import factorial as fact

def prob_binomial(k, n, p):
    '''calculate the probability using k, n, and p'''
    return fact(n)/(fact(k)*fact(n-k)) * p**k * (1-p)**(n-k)
    
for num in [0, 1, 2, 3]:
    print("Probability of having {0} 6 is: {1}".format(num, prob_binomial(num, 3, 1.0/6)))