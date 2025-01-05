exlist = [1, 2, 3]

def list_sum_av(lst, n=0, leng=0):
    if len(lst)==0:
        return n//leng
    else:
        n+=lst.pop()
        leng+=1
        return list_sum_av(lst, n,leng)

print(list_sum_av(exlist))