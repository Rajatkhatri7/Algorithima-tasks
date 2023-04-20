import random
from concurrent.futures import ThreadPoolExecutor

def create_file(file_name):
    with open(file_name,'w') as f:
        ran_num = str(random.randint(1, 20))
        f.write(ran_num)
        
    return file_name
        
filelist = []
for i in range(1,6):
    filename = 'randomfile_{}.txt'.format(random.randint(1, 10))
    filelist.append(filename)
    
with ThreadPoolExecutor(max_workers=5) as executor:
    result = executor.map(create_file,filelist)
    for res in result:
        print("file created: ",res)
    