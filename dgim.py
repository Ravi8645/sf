import math

data = [0,0,0,1,1,1,1,0,1,0,1,1,0,0,1,1,1,0,1,1,0,1,1,0,0,0,0,1,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,0,0,1]

buckets = []
bucket_size = 1
bucket_size_pow = 0
used_twice = False

index = len(data)-1
temp_bucket = []
while index>=0:
 if data[index]==0:
   index-=1
   continue
 if len(temp_bucket)<bucket_size:
   temp_bucket.append(index)
 if len(temp_bucket)==bucket_size:
   if used_twice:
     bucket_size_pow += 1
     bucket_size = math.pow(2, bucket_size_pow)
     used_twice = False
   else:
     used_twice = True
   buckets.append([len(data)-temp_bucket[0]-1, len(temp_bucket)])
   temp_bucket.clear()
 index-=1

k = int(input("Enter the query range: "))
while k!=-1:
 index = 0
 ans = 0
 while index<len(buckets)-1 and k>=buckets[index+1][0]:
   ans+=buckets[index][1]
   # print(index, ans)
   index+=1
 if k>=buckets[index][0]:
   ans+=buckets[index][1]/2
 print("number of 1's in the strean: ", ans)
 k = int(input("Enter the query range: "))
