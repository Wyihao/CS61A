class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]

    def __len__(self):
        return 1 + len(self.rest)

    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(self.first, rest_str)

    # def __str__(self):
    #     if self.rest:
    #         rest_str = ', ' + str(self.rest)
    #     else:
    #         rest_str = ''
    #     return '{0}{1}'.format(self.first, rest_str)

def map_link(f, s):
    """Apply f to each element of s."""
    if s is Link.empty:
        return s
    else:
        return Link(f(s.first), map_link(f, s.rest))

def filter_link(f, s):
    """Return a Link with elements of s for which f returns True."""
    if s is Link.empty:
        return s
    else:
        filtered = filter_link(f, s.rest)
        if f(s.first):
            return Link(s.first, filtered)
        else:
            return filtered

def join_link(s, separator):
    """Return a string of all elements in s separated by separator."""
    if s is Link.empty:
        return ""
    elif s.rest is Link.empty:
        return str(s.first)
    else:
        return str(s.first) + separator + join_link(s.rest, separator)

def partitions(n, m):
    """Return a linked list of partitions of n & parts of up to m.
    Each partition is represented as a linked list.
    """
    if n == 0:
        return Link(Link.empty)
    elif n < 0 or m == 0:
        return Link.empty
    else:
        using_m = partitions(n-m, m)
        with_m = map_link(lambda p: Link(m, p), using_m) #注意这里，lambda函数的作用就是将划分出来的using_m再构成一个Link_list
        without_m = partitions(n, m-1)
        return extend_link(with_m, without_m)

def print_partitions(n, m):
    """Print the partitions of n using parts up to size m."""
    links = partitions(n, m)
    lines = map_link(lambda s: join_link(s, " + "), links)
    map_link(print, lines)

def extend_link(s, t):
    """Return a Link with elements of s followed by those of t."""
    if s is Link.empty:
        return t
    else:
        return Link(s. first, extend_link(s.rest, t))
