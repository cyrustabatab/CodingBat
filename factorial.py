import unittest



memo = {}
def factorial(n):

    if n <= 1:
        return 1
    

    
    return n * factorial(n - 1)








class Test(unittest.TestCase):


    def setUp(self):
        self.sol = factorial


    def test_case_1(self):

        self.assertEqual(self.sol(1),1)

    def test_case_2(self):

        self.assertEqual(self.sol(5),120)

    def test_case_3(self):
        self.assertEqual(self.sol(4),24)


    def test_case_4(self):
        self.assertEqual(self.sol(2),2)

    def test_case_5(self):
        self.assertEqual(self.sol(0),1)




if __name__ == "__main__":
    
    unittest.main(verbosity=2)

    print(memo)
