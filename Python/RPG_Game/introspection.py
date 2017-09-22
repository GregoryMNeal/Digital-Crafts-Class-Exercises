class A:
    @classmethod
    def get_classname(cls):
        return cls.__name__

    def use_classname(self):
        return self.get_classname()

#  Usage:

#  >>> A.get_classname()
#  'A'
#  >>> a = A()
#  >>> a.get_classname()
#  'A'
#  >>> a.use_classname()
#  'A'
