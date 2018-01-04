# 10-1 create list
print [x * (x+1) for x in range(1, 100,2)]


# 10-2
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
def generate_tr(name, score):
if score<60:
return '<tr><td>%s</td><td style="color:red">%s</td></tr>' % (name, score)
else:
return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)

tds = [generate_tr(name, score) for name, score in d.iteritems()]
print '<table border="1">'
print '<tr><th>Name</th><th>Score</th><tr>'
print '\n'.join(tds)
print '</table>'


# 10-3 
def toUppers(L):
return [l.upper() for l in L if isinstance(l, str)]

print toUppers(['Hello', 'world', 101])

# 10-4
print [100*m+10*n+p for m in range(1,10) for n in range(0,10) for p in range(10) if m==p]

