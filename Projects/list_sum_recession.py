exlist=[1,2,3]
def list_sum_recession(list,n=0):
    if len(list)==0:
        return n
    else:
        n+=list.pop()
        return list_sum_recession(list,n)

print(list_sum_recession(exlist))