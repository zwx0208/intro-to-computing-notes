sentence=list(input().split(';'))
a,b,c='0','0','0'
for s in sentence:
    if s.startswith('a:='):
        a=s[-1]
    if s.startswith('b:='):
        b=s[-1]
    if s.startswith('c:='):
        c=s[-1]
a=int(a)
b=int(b)
c=int(c)
print(a,b,c)





s = input().strip()
vars = {'a': 0, 'b': 0, 'c': 0}
for statement in s.split(';'):
    if statement:
        var, value = statement.split(':=')
        vars[var] = int(value)
print(vars['a'], vars['b'], vars['c'])

