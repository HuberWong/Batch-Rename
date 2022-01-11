import os


config = eval(open("./config.json","r").read())
csv = open(config['csvPath'],'r',encoding='utf-8').read()
csvList = csv.split('\n')
workList = []
oldDocList = []
newDocList = []
docFlag = 0
workSpace = os.getcwd()
# print(workSpace)

# 制作旧文件名列表
# csv 文件切割
for i in range(len(csvList)):
    csvList[i] = csvList[i].split(',')
# 确定 docFlag
for i in range(len(csvList[2]) - 1):
    if 'https://wj.qq.com/api/files/download' in csvList[2][i]:
        docFlag = i
        break

for i in range(1,len(csvList) - 1):
    oldDocList.append(csvList[i][12].split("，")[1].strip('")'))
# print(oldDocList)


# 制作新文件名列表
for i in range(len(oldDocList)):
    newDocList.append('')


for subname in config['subname']:
    if  not (len(newDocList[0]) == 0) :
        for i in range(len(newDocList)):
            newDocList[i] += config['separator'] 
    for i in range(len(newDocList)):
        newDocList[i] += csvList[i+1][subname].strip('"\t')
for i in range(len(oldDocList)):
    newDocList[i] += "." + oldDocList[0].split(".")[1]
    
# print(oldDocList)
# print(newDocList)
for i in range(len(oldDocList)):
    oldDocList[i] = workSpace + "\\" + config['needRename'] + oldDocList[i]
    newDocList[i] = workSpace + "\\" + config['renamed'] + newDocList[i]

for i in range(len(oldDocList)):
    os.system("copy "+oldDocList[i]+" "+newDocList[i])
print(newDocList)


print(oldDocList[0].split(".")[1])
