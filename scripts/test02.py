"""
目标：unittest skip 与skipIf 功能
语法：
@unittest.skip("原因")
@unittest.skipIf(条件，原因)

"""

#导包
import unittest



class Test01(unittest.TestCase):

    def test01(self):
        print("test01")

    def test02(self):
        print("test02")

    def test03(self):
        print("test03")

