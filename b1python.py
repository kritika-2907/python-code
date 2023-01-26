class reverse:
    s=""
    def __init__(self,s):
        self.s=" ".join(reversed(s.split()))
print("Enter the 3 Strings")
dict={}
objArr=[]
vowelsCount=[0,0,0]

for i in range(3):
    objArr.append(reverse(input()))
    for j in range(len(objArr[i].s)):
        if objArr[i].s[j].lower() in ['a','e','i','o','u']:
            vowelsCount[i]+=1

    dict.update({objArr[i].s: vowelsCount[i]})

print(*sorted(dict.items(),key=lambda x: x[1], reverse=True), sep="\n")
