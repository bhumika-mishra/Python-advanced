keypad = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
def printcombination(combination,cur,output,n):
    if(cur == n):
        print(*output,sep=",")
        return
    for i in range(len(keypad[combination[cur]])):
        output.append(keypad[combination[cur]][i])
        printcombination(combination,cur+1,output,n)
        output.pop()
        if (combination[cur]==0 or combination[cur]==1):
            return
combination = [2,7,3]        
n = len(combination)
printcombination(combination,0,[],n)
