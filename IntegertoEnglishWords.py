class Solution:
    def numberToWords(self, num: int) -> str:
        
        # dumy datas
        under_twenty = ['','One', 'Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven',
                'Twelve', 'Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
        tens = ['','','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
        chunks = ['Thousand','Million','Billion']

        def toWords(num):
            if num==0:
                return []
            if num < 20:
                return [under_twenty[num]]
            if num < 100:
                return [tens[num//10]] + toWords(num%10)
            if num < 1000:
                q,r = num//100, num%100
                return [under_twenty[q]]+['Hundred'] + toWords(r)
            for power, chunk in enumerate(chunks, 1):
                if num < 1000**(power+1):
                    q,r = num//1000**power, num%1000**power
                    return toWords(q) +[chunk] +toWords(r)

        return ' '.join(toWords(num)) or 'Zero'
        
