# documentation: https://ru.it-brain.online/tutorial/python3/os_stat/
import os
from datetime import datetime

path = '/Users/USER/Desktop/My_best_summary_about_python/summary/Django/2. Обработка запросов/request-handling/file_server/files'
print(os.sep.join([path, 'server.01']))
# /Users/USER/Desktop/My_best_summary_about_python/summary/Django/2. Обработка запросов/request-handling/file_server/files/server.01


stat = os.stat(os.sep.join([path, 'server.01']))
print(stat)
"""
os.stat_result(
st_mode=33188, 
st_ino=37461565, 
st_dev=16777220, 
st_nlink=1, 
st_uid=501, 
st_gid=20, 
st_size=537, 
st_atime=1621146726, 
st_mtime=1613818392, 
st_ctime=1621146723)
"""

