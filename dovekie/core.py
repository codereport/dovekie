# combinators
b     = lambda f, g:    lambda x:    f(g(x))
phi1 = lambda f, g, h: lambda x, y: g(f(x, y), h(x, y))
l    = lambda x, _: x
r    = lambda _, y: y

# convient unary/binary operations
addl = lambda x: lambda y: x + y

fst = lambda x: x[0]
snd = lambda x: x[1]
