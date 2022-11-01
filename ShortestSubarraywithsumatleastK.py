# A Python program to print all
# combinations of given length
import collections
from itertools import combinations
num = 7999
under_twenty = ['','One', 'Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven',
                'Twelve', 'Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Ninteen']
tens = ['','','Twenty','Thirty','Fourty','Fifty','Sixty','Seventy','Eighty','Ninty']
chunks = ['Thousand','Million','Billion']
def to_words(num):
    if num < 20: return [under_twenty[num]]
    if num <100: return [tens[num//10]] + to_words(num%10)
    if num < 1000:
        quotient, reminder = num//100, num%100
        return [under_twenty[quotient], 'Hundred'] + to_words(reminder)
    for power, chunk in enumerate(chunks, 1):
        if num < 1000** (power+1):
            quotient, reminder = num//1000**power, num%1000**power
            return  to_words(quotient)+[chunk] + to_words(reminder)
print(' '.join(to_words(num)))
