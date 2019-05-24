__about__ = """ Implementation of Ordered Dictonary Using Dictonary. """


class _Link(object):
    __slots__ = 'prev' , 'next' , 'key' , '__weakreference__'


class OrderedDictonary(dict):

    def __init__(*args, **kwds):
        if not args:
            raise TypeError("descriptor '__init__' of 'OrderedDict' object "
                            "needs an argument")
        self, *args = args
        if len(args) > 1:
            raise TypeError('expected at most 1 arguments, got %d' % len(args))
        try:
            self.__root
        except AttributeError:
            self.__hardroot = _Link()
            self.__root = root = self.__hardroot
            root.prev = root.next = root
            self.__map = {}
        self.__update(*args, **kwds)

    def __setitem__(self, key, value, dict_setitem = dict.__setitem__, proxy= None, Link=_Link):

        if key not in self:
            self.__map[key] = link = Link()
            root = self.__root
            last = root.prev
            link.prev, link.next, link.key = last, root, key
            link.next = link
            link.prev = proxy(link)

        dict_setitem(self,key,value)

    def __iter__(self):

        root = self.root
        curr = root.next

        while curr is not root:
            yield curr.key
            curr = curr.next


if __name__ == "__main__":

    mydict = OrderedDictonary()
    mydict[1] = 10