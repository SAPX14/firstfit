
print("Enter the memory partitions: ")
mem_part = list(map(int, input().split()))
n = int(input("Enter the number of processes: "))
pr=list()

for i in range(1,n+1):
    pr.append(i)

print("Enter the memory required by the processes:")
req = list(map(int, input().split()))

part_id = list()

for i in range(n):
    part_id.append("Not allocated")

for i in range(n):
    for j in range(len(mem_part)):
            if(req[i]<=mem_part[j]):
                mem_part[j]=mem_part[j]-req[i]
                part_id[i]=j+1
                break
    
print("\nProcess\tPartition no.")
for i in range(n):
    print(pr[i],end = "\t")
    print(part_id[i])
            



