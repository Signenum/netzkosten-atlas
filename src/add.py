import json,sys
f,key,val=sys.argv[1],sys.argv[2],json.loads(sys.argv[3])
d=json.load(open(f)); d.setdefault(key,{}).update(val); json.dump(d,open(f,'w'),ensure_ascii=False,indent=0)
