import hashlib
s='plusdev'
print('short:'+hashlib.md5(s.encode()).hexdigest()[:8])
