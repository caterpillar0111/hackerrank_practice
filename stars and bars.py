#如果是|***| [1~5] 答案是 底4-頭0-1
#|**|*|* [1~5] 答案是 底3-0-1
#|**|*|* [1~6] 答案是 底5-0-1-中間有一根1
#要知道底再哪，底即最後一根sub array，另外頭尾確定切下來的字串，中間有|要再扣一
#公式：頭-尾-1-頭尾中間的"|"個數

s='|**|*|*'
start=[1,1]
end=[5,6]
key_list=[]

for i in range(len(s)):
    if s[i]=='|':
        key_list.append(i)
# loop 一次，存入所有"|"再S中的位置
for a in range(len(start)):
    sub_array=s[start[a]-1:end[a]]
    start_point=0
    end_point=0
    
    #頭
    for i in range(len(sub_array)):
        if sub_array[i]=="|":
            start_point=i
            break
    #尾    
    for j in range(len(sub_array)-1,0,-1):
        if sub_array[j]=="|":
            end_point=j
            break
    
    #中間 
    between=0
    for index in key_list:
        if index>start_point and index<end_point:
            between+=1
        
    print(end_point-start_point-1-between)

#這個還要加，如果start_point=end_point要handle，不然會變-1，只要算出來的值<0 return 0 就好

