# 2 public, 3 private, 2 objs and display all attributes of the object

class Activity:
    def __init__(self,pub1,pub2,priv1,priv2,priv3):
        self.pub1 = pub1
        self.pub2 = pub2
        self.__priv1 = priv1
        self.__priv2 = priv2
        self.__priv3 = priv3

    def get_priv1(self):
      return self.__priv1

    def get_priv2(self):
      return self.__priv2
    
    def get_priv3(self):
      return self.__priv3
    
    
    def set_priv1(self,prival1):
        self.__priv1 = prival1

    def set_priv2(self,prival2):
        self.__priv2 = prival2

    def set_priv3(self,prival3):
        self.__priv3 = prival3

values = Activity("1st Public", "2nd Public","1st Private","2nd Private","3rd Private",)
print("pub1 =", values.pub1)
print("pub2 =", values.pub2)
print("priv1 =", values.get_priv1())
print("priv2 =", values.get_priv2())
print("priv3 =", values.get_priv3())