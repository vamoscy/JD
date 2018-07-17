import os
list_dirs=os.walk('D://女装//')
attrdict={}
for root,dirs,files in list_dirs:
    for file in files:
        if file.endswith('.csv'):
            path=os.path.join(root,file)
            fopen=open(path)
            cat_list =fopen.readline().strip().split(',')
            name_list =fopen.readline().strip().split(',')
            for i in name_list:
                i=i.split('，')
            for i in cat_list:
                if i not in attrdict:
                    attrdict[i]=name_list[cat_list.index(i)]
                else:
                    for detail in name_list[cat_list.index(i)]:
                        if detail not in attrdict[i]:
                            attrdict[i].append(detail)
            fopen.close()
for i in attrdict:
    print(i)
'''
fwrite=open('D://female_clothing.csv', 'a+')
for i in attrdict:
    for detail in i:
        fwrite.write(i + detail)
'''