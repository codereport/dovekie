_phi1_ = lambda f, g, h: lambda x, y: g(f(x, y), h(x, y))
_l_    = lambda x, _: x
_r_    = lambda _, y: y
