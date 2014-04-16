#-*- coding: utf-8 -*-

import json
from glassdoor import get

dest_path = 'company.json'
json_data = open('companies/data.json')
data = json.load(json_data)
com_list = []
for value in data:
  com_list.append(value['name'])
json_data.close()
#remove duplicates
com_list = list(set(com_list))
print 'Len: ', len(com_list)

obj = open(dest_path, 'w')
obj.write('[')
for one in com_list:
  #print one
  info = get(one)
  obj.write('{ "name": "' + one.encode('utf-8') +'",')
  obj.write(' "info": ' + json.dumps(info))
  obj.write('},\n')
  obj.flush()
obj.write(']')
obj.close()
