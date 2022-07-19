from email import message
import os, sys,re,body,time
def fpath(path,genpath,titles,tage):
    global filepath,bokepath,title,tages
    filepath = path
    bokepath = genpath
    title=titles
    tages=tage
    print(filepath)
    file = open(filepath,'r+',encoding='utf-8')
    writefile = open(genpath+'\\source\\_posts'+'\\'+title+'.txt','w+',encoding='utf-8')
    a=file.readlines()#读取所有记录
    num=0
    localtime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 

    main=['title: '+title,'data: '+localtime,'tags:','   -'+tages]
    writefile.write('---\n')
    for i in main:
        i=str(i)
        writefile.write(i+'\n')
    writefile.write('---\n')
    for i in a:
        if '{标题}'in i:
            num+=1
            star=i.find('}')
            stop=i[star+1:].find('{')
            i=i[star+1:stop+1+star]
            writefile.write(num*'# '+i+'\n')
        elif '{图片}'in i:
            star=i.find('}')
            stop=i[star+1:].find('{')
            i=i[star+1:stop+1+star]
            writefile.write('![alt 图标]('+i+')')
        else:
            writefile.write(i)
    writefile.close()
    os.chdir(genpath+'\\source\\_posts')
    filename=title+'.txt'
    newname= title+'.md'
    os.rename(filename,newname)
    os.chdir(bokepath)
    writefile.close()
    os.system('hexo g')
    os.system('hexo d')
    print('上传结束！')
        
