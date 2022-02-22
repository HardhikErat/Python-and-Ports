mark=[]
total=0
print("Enter Marks Obtained in all 5 subjects: ")
for i in range (5):
    mark.insert(i, int(input()))
for i in range (5):
    total = total + mark[i]

average=total/5
percentage=(total/500)*100
print("Average Marks = ", average)
print("Percentage Mark = ", percentage)