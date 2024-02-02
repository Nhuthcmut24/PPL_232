import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """func main () return 1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1900))
        
    def test_simple_program2(self):
        """Simple program"""
        input = """func main (number a, string b) return a+b
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1901))
        
    def test_simple_program3(self):
        """Simple program"""
        input = """number a[1,2] <- [1,2,3,4]
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1902))
        
    def test_simple_program4(self):
        """Simple program"""
        input = """number x<- [1,2,3,4]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1903))
        
    def test_simple_program5(self):
        """Simple program"""
        input = """number x[2,3]<- [[1,2,4],[1,9,0]]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1904))
        
    def test_simple_program6(self):
        """Simple program"""
        input = """var x<- [[1,2,4],[1,9,0]]
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1905))
    
    def test_simple_program7(self):
        """Simple program"""
        input = """dynamic x
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1906))
    
    def test_simple_program8(self):
        """Simple program"""
        input = """func foo()
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1907))
    
    def test_simple_program9(self):
        """Simple program"""
        input = """func isPrime(number x)
        begin
        if (x <= 1) return false
        var i <- 2
        for i until i > x / 2 by 1
        begin
        if (x % i = 0) return false
        end
        return true
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1908))

    def test_simple_assign_statement(self):
        """Simple program"""
        input = """ func foo()
        begin
        x <- "string literal\t"
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,2000))
    
    def test_simple_assign_statement2(self):
        """Simple program"""
        input = """ func foo()
        begin
        x[3] <- "string literal\t" + foo(2)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,2001))
        
    def test_simple_if_statement2(self):
        """Simple program"""
        input = """func foo()
        begin
        if (x) 
        
        begin
        
        y<-"string literal\t" + foo(2)
        
        end
        end
        
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,2100))
    
    def test_simple_if_statement3(self):
        """Simple program"""
        input = """func foo()
        begin
        if (x+y) y<-"string literal\t" + foo(2)
        elif a b<-5
        else number x
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,2101))
        
    def test_simple_for_statement(self):
        """Simple program"""
        input = """func foo()
        begin
        for y until 5 by y+1 y<-"string literal\t" + foo(2)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,2102))
    
    def test_simple_for_statement2(self):
        """Simple program"""
        input = """var i <- 0
        func foo()
        begin
        for i until i >= 10 by 1
        return
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,2103))
    
    def test_simple_break_statement(self):
        """Simple program"""
        input = """var i <- 0
        func foo() begin
        break
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,2104))
    
    def test_simple_continue_statement(self):
        """Simple program"""
        input = """var i <- 0
        func foo() begin
        continue
        return
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,2105))
    
    def test_simple_return_statement(self):
        """Simple program"""
        input = """var i <- 0
        func foo(number x) begin
        for i until i >= 10 by 1
        break
        continue
        return
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,2106))
        
    def test_function_call_statement(self):
        """Simple program"""
        input = """var i <- 0
        func foo() begin
        for i until i >= 10 by 1
        foo(i)
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,2107))

    def test_block_statement(self):
        """Simple program"""
        input = """func foo()
        begin
        x <- "abx" + 5
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,2108))
        
    def test_complex_program(self):
        """Complex program"""
        input = """func foo()
        begin
        x <- arr[1] + 5.03e-4
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,2200))

    def test_complex_program2(self):
        """Complex program"""
        input = """func foo()
        begin
        x[2+foo(3,4)] <- arr[b[12]] + 5.04e-12
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,2201))

    def test_complex_program3(self):
        """Complex program"""
        input = """func foo()
        begin
        x[2+foo(3,4)] <- arr[b[12]] + 5.04e-12
        y[2+foo(3,4),5] <- 5.04e-12
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,2202))

    def test_complex_program4(self):
        """Complex program"""
        input = """func foo()
        begin
        x[2+foo(3,4)] <- arr[b[12]] + 5.04e-12
        y[2+foo(3,4),5] <- 5.04e-12
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,2203))

    def test_complex_program5(self):
        """Complex program"""
        input = """func foo()
        begin
        x[2+foo(3,4)] <- arr[b[12]] + 5.04e-12
        y[2+foo(3,4),5] <- 5.04e-12
        z <- "string literal\t"
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,2204))

    def test_complex_program5(self):
        """Complex program"""
        input = """func foo()
        begin
        x[2+foo(3,4)] <- arr[b[12]] + 5.04e-12
        y[2+foo(3,4),5] <- 5.04e-12
        z <- "string literal\t"
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,2204))




    



