#temp_l = [1 1 2 3 3 4 7]
T = int(input())
count_l = []
if T>=1 and T<= 10:
    for test in range(T):
        seq = int(input())
        ne = []
        arr = list(map(int, input().split()))
        if seq>= 1 and seq <= 10**5:
            new_arr = []
            count = 0
            for i in range(len(arr)+1):

                new_arr.clear()
                for j in range(len(arr)+1):

                    
                    new_arr = arr[i:j+1]
                    if len(new_arr)>=2:
                        
                        
                        ne.append(new_arr)

                
                ne = [flist for flist in ne if flist != []]
            # print(ne)
            for ele in ne:
                # print(ele)
                if ele[0] != ele[-1] or ele[0] != ele[-2]:

                    count+=1


            
            count_l.append(count)
    c = 0

for i in count_l:
    c += 1
    print(f"Case {c}: {i}")