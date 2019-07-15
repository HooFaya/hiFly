# '''
# 线程不安全的单例
# '''
#
#
# class Singleton:
#     def __new__(cls):
#         if not hasattr(cls,"_instance"):
#             cls._instance=super().__new__(cls)
#         return cls._instance
#
# class Myclass(Singleton):
#     def __init__(self):
#         pass
# p1=Myclass()
# p2=Myclass()
# print(id(p1))
# print(id(p2))
#
class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,"_instance"):
            cls._instance=super().__new__(cls)
        return cls._instance
class Myclass(Singleton):
    def __init__(self):
        pass
p1=Myclass()
p2=Myclass()
print(id(p1))
print(id(p2))