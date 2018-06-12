# Author:YSY


import winreg,os
import Lnktrans
def get_desktop():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    return winreg.QueryValueEx(key, "Desktop")[0]


def file_Name_noTraversal(file_dir):
    '''
    获取目录下文件列表（不遍历子目录）
    :param file_dir:
    :return:
    '''
    L=[]
    for filename in os.listdir(file_dir):
        #for file in filename:
            #if os.path.splitext(file)[1] == '.lnk':
        m = os.path.join(file_dir, filename)
        if(os.path.isdir(m)):
            print('目录：', os.path.join(filename))
        if(os.path.isfile(m)):
            print('文件：', os.path.join(filename))
        if os.path.splitext(filename)[1] == '.lnk':
            L.append(os.path.join(file_dir,filename))
    return L

def file_Name_Traversal(file_dir):
    '''
    获取目录下文件列表（遍历子目录）
    :param file_dir:
    :return:
    '''
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.lnk':
                L.append(os.path.join(root, file))
    return L

def file_name(file_dir,flag=True):
    '''
    :param file_dir: 需要列举出的路径
    :param flag:    Ture:遍历子目录 False:仅当前目录
    :return:    返回文件列表（包含路径）
    '''
    if flag:
        return file_Name_Traversal(file_dir)
    else:
        return file_Name_noTraversal(file_dir)



filelist = file_name(get_desktop(),True)
for file in filelist:
    print(file)
    print(Lnktrans.MSShortcut(file).localBasePath)
    print(Lnktrans.MSShortcut(file).commandLineArgs)
    print('---------------------------------')

