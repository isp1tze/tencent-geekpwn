f = open('trace2/process-data/chinese.txt',encoding="utf-8")
r = f.readline()
list_key = []
while(r):
    tmp = r.split("'")
    if len(tmp) > 1:
        list_key.append(tmp[1])
    r = f.readline()
f.close()

f = open('trace2/process-data/chinese-all.txt',encoding="utf-8")
r = f.readline()
list_key_all = []
while(r):
    tmp = r.split("'")
    if len(tmp) > 1:
        list_key_all.append(tmp[1])
    r = f.readline()
f.close()

f = open('trace2/process-data/last-section.txt', encoding='utf-8')
r = f.readline()
list_last_section = []
while(r):
    r = r.replace("\n", "")
    list_last_section.append(r)
    r = f.readline()

f.close()


f = open('trace2/process-data/noUse.txt', encoding='utf-8')
r = f.readline()
list_no_use_domain,list_no_use_domain_all = [],[]
while(r):
    r = r.replace("\n", "")
    tmp = r.split(".")
    if len(tmp) > 3:
        list_no_use_domain.append(r)
    else:
        list_no_use_domain.append(tmp[0])
    list_no_use_domain_all.append(r)
    r = f.readline()
f.close()