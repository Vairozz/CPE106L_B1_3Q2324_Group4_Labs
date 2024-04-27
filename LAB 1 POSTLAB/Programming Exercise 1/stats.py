def mode(arr):
    modes = []
    max_count = 0
    for item in arr:
        count = arr.count(item) 
        if count > max_count:
            max_count = count
            modes = [item]  
        elif count == max_count and item not in modes:
            modes.append(item) 

    print(int(modes))
            
def mean(arr):
    ave=sum(arr)/len(arr)
    print(ave)

def median(arr):
    arr.sort()
    mid = len(arr) // 2
    print(arr[mid])
    
    
lst = []
while True:
    first_input = input("Enter numbers from the list; type 'stop' if you're finished: ")
    first_input = first_input.lower()
    if first_input == 'stop':
        break
    else:
        lst.append(float(first_input))


x = int(input("Enter 1 to get mode\nEnter 2 to get mean\nEnter 3 to get median\n"))

if x == 1:
    mode(lst)
elif x == 2:
    mean(lst)
elif x == 3:
    median(lst)
