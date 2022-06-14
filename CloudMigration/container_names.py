list_of_files=['rohit-jsona9ee9062-be14-49cc-9ae1-c6f395a81d0a/rohit.json0-10',
 'rohit-jsona9ee9062-be14-49cc-9ae1-c6f395a81d0a/rohit.json10-20',
 'rohit-jsona9ee9062-be14-49cc-9ae1-c6f395a81d0a/rohit.json100-110',
 'rohit-jsona9ee9062-be14-49cc-9ae1-c6f395a81d0a/rohit.json110-120',
 'rohit-jsona9ee9062-be14-49cc-9ae1-c6f395a81d0a/rohit.json120-130',
 'rohit-jsona9ee9062-be14-49cc-9ae1-c6f395a81d0a/rohit.json130-137',
 'rohit-jsona9ee9062-be14-49cc-9ae1-c6f395a81d0a/rohit.json20-30',
 'rohit-jsona9ee9062-be14-49cc-9ae1-c6f395a81d0a/rohit.json30-40',
 'rohit-jsona9ee9062-be14-49cc-9ae1-c6f395a81d0a/rohit.json40-50',
 'rohit-jsona9ee9062-be14-49cc-9ae1-c6f395a81d0a/rohit.json50-60',
 'rohit-jsona9ee9062-be14-49cc-9ae1-c6f395a81d0a/rohit.json60-70',
 'rohit-jsona9ee9062-be14-49cc-9ae1-c6f395a81d0a/rohit.json70-80',
 'rohit-jsona9ee9062-be14-49cc-9ae1-c6f395a81d0a/rohit.json80-90',
 'rohit-jsona9ee9062-be14-49cc-9ae1-c6f395a81d0a/rohit.json90-100']
container_group_name=[]
j=1
for i in range(0,len(list_of_files)):
    container_group_name.append("container_group_"+str(j))
    if j==5:
        j=1
    else:
        j+=1