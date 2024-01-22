import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_simple_string(self):
        """test simple string"""
        self.assertTrue(TestLexer.test("\"Yanxi Palace - 2018\"","Yanxi Palace - 2018,<EOF>",101))

    def test_complex_string(self):
        """test complex string"""
        self.assertTrue(TestLexer.test("\"isn''t\"","isn''t,<EOF>",102))
        
    def test_simple_number(self):
        """test simple number"""
        self.assertTrue(TestLexer.test("2024","2024,<EOF>",103))
    
    def test_simplex_number(self):
        """test simplex number"""
        self.assertTrue(TestLexer.test("123a123","123,a123,<EOF>",104))
        
    def test_simple_func(self):
        """test simple func"""
        self.assertTrue(TestLexer.test("func main () return 1","func,main,(,),return,1,<EOF>",201))

    def test_simplex_func(self):
        """test simplex func"""
        self.assertTrue(TestLexer.test("int main () {putIntLn(4);}","int,main,(,),{,putIntLn,(,4,),Error Token ;",202))

    def test_simplex_func2(self):
        """test simplex func2"""
        self.assertTrue(TestLexer.test("int main( {}","int,main,(,{,},<EOF>",203))
        
    def test_comment(self):
        """test comment"""
        self.assertTrue(TestLexer.test("##this is a comment","<EOF>",204))
        
    def test_identifier(self):
        """test identifier"""
        self.assertTrue(TestLexer.test("abc_12 _ab12","abc_12,_ab12,<EOF>",205))

    def test_keyword(self):
        """test keyword"""
        self.assertTrue(TestLexer.test("func var","func,var,<EOF>",206))
        
    def test_operator(self):
        """test operator"""
        self.assertTrue(TestLexer.test("+ - * / %","+,-,*,/,%,<EOF>",207))

    def test_separator(self):
        """test keyword"""
        self.assertTrue(TestLexer.test("()","(,),<EOF>",208))

    def test_integer(self):
        """test integer"""
        self.assertTrue(TestLexer.test("123","123,<EOF>",209))

    def test_real_number(self):
        """test real number"""
        self.assertTrue(TestLexer.test("12.","12.,<EOF>",301))

    def test_real_number2(self):
        """test real number2"""
        self.assertTrue(TestLexer.test("12.3","12.3,<EOF>",302))
        
    def test_real_number_scientist(self):
        """test real number scientist"""
        self.assertTrue(TestLexer.test("12.3e30","12.3e30,<EOF>",303))
        
    def test_real_number_scientist(self):
        """test real number scientist"""
        self.assertTrue(TestLexer.test("12.3e30","12.3e30,<EOF>",303))
        