def length(x): return len(x)
def first(x): return x[0]
def last(x): return x[-1]
def push(x,value): x.append(value); return x
def map_values(fn,values): return [fn(v) for v in values]
def filter_values(fn,values): return [v for v in values if fn(v)]
