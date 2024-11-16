numbers=[10,45,23,67,99,12,34]
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i]<numbers[j]:
            numbers[i],numbers[j]=numbers[j],numbers[i]
print("The largest number is:",numbers[0])
print("The smallest number is:",numbers[-1])