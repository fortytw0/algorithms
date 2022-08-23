def merge(data, start, mid, end) : 


    temp = []
    i = start
    j = mid
    

    while (i<mid) and (j<end) : 

        if data[i] < data[j] : 
            temp.append(data[i])
            i += 1 

        else : 
            temp.append(data[j])
            j += 1 

    if i<mid : 
        temp += data[i:mid]
    
    else : 
        temp += data[j:end]

    data[start:end] = temp

    
def merge_sort(data, start, end) : 
    
    # print('Merge Sort Called')
    # print('data : ' , data)
    # print('start : ' , start)
    # print('end : ' , end)
    if start<end-1 : 
        mid = (start+end)//2
        
        merge_sort(data, start, mid)
        merge_sort(data, mid, end)
        merge(data, start, mid, end)


merge_sort([-3, 20, 7, 5, 9, -5] , 0 , 6)