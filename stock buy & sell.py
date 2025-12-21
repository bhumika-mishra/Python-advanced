def profit(arr,arr_size):
    profit = 0
    for i in range(1,arr_size):
        if arr[i] > arr[i-1]:
         profit += arr[i] - arr[i-1]
        return profit
prices = [200,345,665,229,667,405,324]
profit = profit(prices,len(prices))  
print("Maximum Profit : ",profit)  