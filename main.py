import hashlib
s='tashkentdev'
print('short:'+hashlib.md5(s.encode()).hexdigest()[:8])
