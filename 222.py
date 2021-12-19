def permute(nums):
    size=len(nums)
    if size==0:
        return []
    res=[]
    used=[False for _ in range(size)]
    dfs(nums,size,0,[],used,res)
    return res

def dfs(nums,size,depth,path,used,res):
    if depth==size:
        res.append(path)
        return
    
    for i in range(size):
        if not used[i]:
            used[i]=True
            path.append(used[i])
            dfs(nums,size,depth+1,path,used,res)
            used[i]=False
            path.pop()

if __name__=='__main__':
    nums=[1,2,3]
    res=permute(nums)
    print(res)