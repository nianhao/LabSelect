import random

all_mem=["邢光辉","肖年浩","邹远晨","常晨","张慧","孙小东","尹小涵"]
select=[]
ans={}
ans["张慧"]=0
ans["尹小涵"]=1
ans["邹远晨"]=4
ans["孙小东"]=3
for i in range(7):
    select.append(0)
for i in range(7):
    if i in [0,1,3,4]:
        continue
    selectIndex=-1
    while True:
        selectIndex=random.randint(0,6)
        if select[selectIndex]==0 and not all_mem[selectIndex]in ans.keys():
            break
    select[selectIndex]=1
    ans[all_mem[selectIndex]]=i
for key in ans.keys():
    print("{}翻译第{}~{}段".format(key,ans[key]*2+1,ans[key]*2+2))
