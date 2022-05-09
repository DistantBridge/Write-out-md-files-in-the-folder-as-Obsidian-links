import os
import time
import codecs

FilePath = ''

Time = time.localtime(time.time())
Output_Time = "检索时间为{}年{}月{}日{}点{}分{}秒".format(Time[0],Time[1],Time[2],Time[3],Time[4],Time[5])
This_Document_Name = "All_MD_Files_List.md"

os.listdir()
FileList = os.walk(FilePath)
folders = []
mdFile = []
for Root,Dirs,All_Name in FileList:
    for name in All_Name : 
        j = name.split('.')
        # j的长度为2说明name是文件，若是1说明是文件夹
        if len(j) == 2:
            # 读取特定的文件名
            if j[1] == 'md':
                mdFile.append(name)
        else:
            folders += j    # 或者 folders.append(name)


print(folders)
print(mdFile)

OutputFile = open(This_Document_Name, "w", encoding = 'utf-8')

OutputFile.write("检索的文件夹路径为：")
OutputFile.write(FilePath)
OutputFile.write('\n')
OutputFile.write('\n')

OutputFile.write(Output_Time)
OutputFile.write('\n')
OutputFile.write('\n')

for Single_mdFile in mdFile:
    Output_File_Name = Single_mdFile.split('.')[0]
    if Single_mdFile != This_Document_Name:
        OutputFile.write('[['+ Output_File_Name + ']]')
        OutputFile.write('\n')
        OutputFile.write('\n')

OutputFile.close()



'''
os.path.splitext()
os.path.splitext(文件名)
函数用途：将文件名和扩展名分开。
'''