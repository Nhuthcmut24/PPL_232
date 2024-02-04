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

    def test_complex_array(self):
        """Complex array"""
        input = """func foo() begin
        number x[100]
        x[1,foo(2)]<- "string\\t"
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,2300))

    def test_complex_array2(self):
        """Complex array"""
        input = """func foo() begin
        number x[100]
        x[1,foo(2)]<- "string\\t"
        boolean b 
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,2301))

    def test_complex_string_literal(self):
        """Complex string literal"""
        input = """func convert()
        begin
        number x[10,foo(4)] <- [1,3,4,1+4,foo(3)]
        end
        """
        expect = "Error on line 3 col 20: foo"
        self.assertTrue(TestParser.test(input,expect,2302))

    def test_complex_expression(self):
        """Complex expression"""
        input = """string x <- "be ba ne \\t"
        func foo() begin
        x <- 5 + 5 % 3
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,2303))

    def test_complex_expression2(self):
        """Complex expression"""
        input = """string x <- "be ba ne \\t"
        func foo() begin
        x <- 5 + 5 % 3 - 8 * 12 / 4
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,2304))
        
    def test_complex_expression3(self):
        """Complex expression"""
        input = """string x <- "be ba ne \\t"
        func foo() begin
        x <- 5 + 5 % 3 - 8 * 12 / 4
        y <- "be ba " ... "ne"
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,2305))

    def test_complex_expression4(self):
        """Complex expression"""
        input = """string x <- "be ba ne \\t"
        func foo() begin
        x <- 5 + 5 % 3 - 8 * 12 / 4
        y <- "be ba " ... "ne"
        z <- y=5
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,2306))

    def test_complex_expression5(self):
        """Complex expression"""
        input = """string x <- "be ba ne \\t"
        func foo() begin
        x <- 5 + 5 % 3 - 8 * 12 / 4
        y <- "be ba " ... "ne"
        z <- y = 5
        t <- z != 5
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,2306))

    def test_complex_expression6(self):
        """Complex expression"""
        input = """string x <- "be ba ne \\t"
        func foo() begin
        x <- 5 + 5 % 3 - 8 * 12 / 4
        y <- "be ba " ... "ne"
        z <- y = 5
        t <- z != 5
        var n <- 5 <= 6 
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,2307))

    def test_complex_expression7(self):
        """Complex expression"""
        input = """string x <- "be ba ne \\t"
        func foo() begin
        x <- 5 + 5 % 3 - 8 * 12 / 4
        y <- "be ba " ... "ne"
        z <- y = 5
        t <- z != 5
        var n <- 5 <= 6 
        a[3 + foo(2)] <- a[b[2, 3]] + 4
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,2308))

    def test_complex_expression8(self):
        """Complex expression"""
        input = """string x <- "be ba ne \\t"
        func foo() begin
        x <- 5 + 5 % 3 - 8 * 12 / 4
        y <- "be ba " ... "ne"
        z <- y = 5
        t <- z != 5
        var n <- 5 <= 6 
        a[3 + foo(2)] <- a[b[2, 3]] + 4
        boolean z <- not 5==6
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,2309))

    def test_complex_expression8(self):
        """Complex expression"""
        input = """string x <- "be ba ne \\t"
        func foo() begin
        x <- 5 + 5 % 3 - 8 * 12 / 4
        y <- "be ba " ... "ne"
        z <- y = 5
        t <- z != 5
        var n <- 5 <= 6 
        a[3 + foo(2)] <- a[b[2, 3]] + 4
        boolean z <- not 5==6
        boolean z1 <- not ((4<=6) and (5>5))
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,2309))

    def test_complex_expression9(self):
        """Complex expression"""
        input = """string x <- "be ba ne \\t"
        func foo() begin
        x <- 5 + 5 % 3 - 8 * 12 / 4
        y <- "be ba " ... "ne"
        z <- y = 5
        t <- z != 5
        var n <- 5 <= 6 
        a[3 + foo(2)] <- a[b[2, 3]] + 4
        boolean z <- not 5==6
        boolean z1 <- not ((4<=6) and (5>5))
        dynamic t <- -4
        number a[6]
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,2310))

    def test_complex_expression10(self):
        """Complex expression"""
        input = """string x <- "be ba ne \\t"
        func foo() begin
        x <- 5 + 5 % 3 - 8 * 12 / 4
        y <- "be ba " ... "ne"
        z <- y = 5
        t <- z != 5
        var n <- 5 <= 6 
        a[3 + foo(2)] <- a[b[2, 3]] + 4
        boolean z <- not 5==6
        boolean z1 <- not ((4<=6) and (5>5))
        dynamic t <- -4
        number a[6]
        if (not(a>=4)) 
        a <- a + 5
        elif (a < 0) 
        a <- 0
        else a <-1
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,2311))

    def test_complex_expression11(self):
        """Complex expression"""
        input = """func foo() 
        begin 
        for x until x <= 6 by 1
        arr[x] <- 2 * x
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,2312))

    def test_complex_component(self):
        """Complex component"""
        input = """
            var VoTien <- true and "true" or 1 
            var VoTien <- 1 and 2 and 3 or 4 or 4
            var VoTien <- 1 + 2 - 2 + 3 and 3
            var VoTien <- 1 / 2 * 3 % 4
            var VoTien <- 1 / 2 / 2 * 3 % 4 
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,2400))

    def test_complex_component2(self):
        """Complex component"""
        input = """number VoTien
            ## VO Tien
            number VoTien <- 0
            boolean a[122,15]
            boolean a[122,15] <- [1 + 1/2 * 3]
            string b[3]
            ## 12 
            string b[3] <- [2 ... " tring"]
            var i <- 0
            dynamic i
            dynamic i <- 0
            ## VO Tien
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,2401))

    def test_complex_component3(self):
        """Complex component"""
        input = """
        var Nhut
        """
        expect = """Error on line 2 col 17: 
"""
        self.assertTrue(TestParser.test(input,expect,2402))

    def test_complex_component4(self):
        """Complex component"""
        input = """
        dynamic VoTien[5] <- 3
        """
        expect = """Error on line 2 col 22: ["""
        self.assertTrue(TestParser.test(input,expect,2403))

    def test_complex_component5(self):
        """Complex component"""
        input = """
        boolean a["string"]
        boolean a[[1,2]]
        boolean a[1+1]
        """
        expect = """Error on line 2 col 18: string"""
        self.assertTrue(TestParser.test(input,expect,2404))
    
    def test_complex_component6(self):
        """Complex component"""
        input = """
        boolean a[1,]
        """
        expect = """Error on line 2 col 20: ]"""
        self.assertTrue(TestParser.test(input,expect,2405))

    def test_complex_component7(self):
        """Complex component"""
        input = """
        var a[1]
        """
        expect = """Error on line 2 col 13: ["""
        self.assertTrue(TestParser.test(input,expect,2406))

    def test_complex_component8(self):
        """Complex component"""
        input = """
        func main()
        func main(number f1)
        func main(number a[5],boolean x[5,2,3], boolean a[5,2,3], string b, boolean c)
        func main(number num1, number num2)
        var VoTien <- 1
        func main(number f1 <- c)
        """
        expect = """Error on line 7 col 28: <-"""
        self.assertTrue(TestParser.test(input,expect,2407))

    def test_complex_component9(self):
        """Complex component"""
        input = """
        func main()
        ## VO Tien
        func main() func main(dynamic a) ## VO Tien
        """
        expect = """Error on line 4 col 20: func"""
        self.assertTrue(TestParser.test(input,expect,2408))

    def test_complex_component10(self):
        """Complex component"""
        input = """
        func main()
        ## VO Tien
        func main() func main(dynamic a) ## VO Tien
        """
        expect = """Error on line 4 col 20: func"""
        self.assertTrue(TestParser.test(input,expect,2409))

    def test_complex_component11(self):
        """Complex component"""
        input = """
        func main(var a)
        """
        expect = """Error on line 2 col 18: var"""
        self.assertTrue(TestParser.test(input,expect,2410))

    def test_complex_component12(self):
        """Complex component"""
        input = """
        ##12
        ##12
            
        func main(number a) var c <- 1
        """
        expect = """Error on line 5 col 28: var"""
        self.assertTrue(TestParser.test(input,expect,2411))

    def test_complex_component13(self):
        """Complex component"""
        input = """
            func main(string a) 
                begin 
                    break ## 12
                end
            func main(dynamic a) 
        func main(number a) var c <- 1
        """
        expect = """Error on line 6 col 22: dynamic"""
        self.assertTrue(TestParser.test(input,expect,2412))

    def test_complex_component14(self):
        """Complex component"""
        input = """
            func main(number a[1,2,3]) ##12
                break
        """
        expect = """Error on line 3 col 16: break"""
        self.assertTrue(TestParser.test(input,expect,2413))

    def test_complex_component15(self):
        """Complex component"""
        input = """
        ##12
        func main(number a) 
        ##12
                
        begin 
            break
            end
                
            ##12
            ##12
            func main(number a)
            ##12 
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,2414))

    def test_complex_component16(self):
        """Complex component"""
        input = """
        ## 12
            
        var a <- 1 ## 12
        ## 12
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,2415))

    def test_complex_component17(self):
        """Complex component"""
        input = """var a <- 3"""
        expect = """Error on line 1 col 10: <EOF>"""
        self.assertTrue(TestParser.test(input,expect,2416))

    def test_complex_component18(self):
        """Complex component"""
        input = """var a <- 3"""
        expect = """Error on line 1 col 10: <EOF>"""
        self.assertTrue(TestParser.test(input,expect,2417))

    def test_complex_component19(self):
        """Complex component"""
        input = """var VoTien <- "Vo" ... "Tien"
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,2418))

    def test_complex_component20(self):
        """Complex component"""
        input = """var VoTien <- "Nguyen" ... "Quoc" ... "Nhut"
        """
        expect = """Error on line 1 col 34: ..."""
        self.assertTrue(TestParser.test(input,expect,2419))

    def test_complex_component21(self):
        """Complex component"""
        input ="""
        var VoTien <- true > "true" 
        var VoTien <- true >= "true"
        var VoTien <- true = "true"
        var VoTien <- true == "true"
        var VoTien <- true < "true"
        var VoTien <- true <= "true"
        var VoTien <- true >= "true" ... 1 > 2
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,2420))

    def test_complex_component22(self):
        """Complex component"""
        input ="""
        var VoTien <- true > x >= z
        """
        expect = """Error on line 2 col 31: >="""
        self.assertTrue(TestParser.test(input,expect,2421))

    def test_complex_component23(self):
        """Complex component"""
        input ="""
            var VoTien <- true and "true" or 1 
            var VoTien <- 1 and 2 and 3 or 4 or 4
            var VoTien <- 1 + 2 - 2 + 3 and 3
            var VoTien <- 1 / 2 * 3 % 4
            var VoTien <- 1 / 2 / 2 * 3 % 4
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,2422))

    def test_complex_component24(self):
        """Complex component"""
        input ="""
            var VoTien <- true >= "true" and 1 > 2
        """
        expect = """Error on line 2 col 47: >"""
        self.assertTrue(TestParser.test(input,expect,2423))

    def test_complex_component25(self):
        """Complex component"""
        input ="""
            var VoTien <- -1 * not 1
            var VoTien <- not not not----C
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,2424))
        
    def test_complex_component26(self):
        """Complex component"""
        input ="""
            var VoTien <- - not 1
        """
        expect = """Error on line 2 col 28: not"""
        self.assertTrue(TestParser.test(input,expect,2425))

    def test_complex_component27(self):
        """Complex component"""
        input ="""
            var VoTien <- a[1] + 1
            var VoTien <- array[1,1+2][1][2,3]
            var VoTien <- array[1,(1)...2,array[ar[(1*2) and 1]],array[2]]
            var VoTien <- a[1] + fun()[1,fun()] 
            var VoTien <- 1[1]
        """
        expect = """Error on line 3 col 38: ["""
        self.assertTrue(TestParser.test(input,expect,2426))

    def test_complex_component28(self):
        """Complex component"""
        input ="""
            var VoTien <- a[]
        """
        expect = """Error on line 2 col 28: ]"""
        self.assertTrue(TestParser.test(input,expect,2427))

    def test_complex_component29(self):
        """Complex component"""
        input ="""
            var VoTien <- a()
            var VoTien <- a(1,2)
            var VoTien <- a(x,array[2])[2]
            var VoTien <- a(z,k[3] ... 2)[1,2]
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,2428))

    def test_complex_component30(self):
        """Complex component"""
        input ="""
            var VoTien <- a()()
        """
        expect = """Error on line 2 col 29: ("""
        self.assertTrue(TestParser.test(input,expect,2429))

    def test_complex_component31(self):
        """Complex component"""
        input ="""
            var VoTien <- a() + ++1 / 2 *3 <= 3 ... "v" >= 2
            var VoTien <- a(1,2)[1,2,3 ... 2] + false + true
            var VoTien <- a(z,k[2,3,"2"] ... 2)[true]
            var VoTien <- (a ... 3) ... b and (a >= b) < b[1, b[1]]
            var VoTien <-  ["tr", 2, 3, 4, 5] + [[1, 2 + 2 * 2 / 3, 3], [4, 5, 6]]
            var VoTien <- a(x,array[2])[2,3+2,true,false]
        """
        expect = """Error on line 2 col 32: +"""
        self.assertTrue(TestParser.test(input,expect,2430))

    def test_complex_component32(self):
        """Complex component"""
        input ="""
            var VoTien <- a[1]()
        """
        expect = """Error on line 2 col 30: ("""
        self.assertTrue(TestParser.test(input,expect,2431))

    def test_complex_component33(self):
        """Complex component"""
        input ="""
            ## comment
        func main()

            ## comment
            begin
            aPI <- 3.14
            end
            ## comment
            
        ## comment
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,2432))

    def test_complex_component34(self):
        """Complex component"""
        input ="""
           func main() begin 
        end
        func main() 
            begin 
                ## comment0
            end
        func main()
            ## comment1
            begin
                ## comment2
                
                ## comment3
                VoTien <- 1 + 2 + fun()
                VoTien[1+a] <- 1
                
                ## comment4
                VoTien[3+4,2,4] <- 1
                
                ## comment5
            end
            ## comment
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,2433))

    def test_complex_component35(self):
        """Complex component"""
        input ="""
           func main()
            begin
            aPI + 1 <- 3.14
            end
        """
        expect = """Error on line 4 col 16: +"""
        self.assertTrue(TestParser.test(input,expect,2434))

    def test_complex_component36(self):
        """Complex component"""
        input ="""
           func main()
            begin
            aPI()<- 3.14
            end
        """
        expect = """Error on line 4 col 17: <-"""
        self.assertTrue(TestParser.test(input,expect,2435))

    def test_complex_component37(self):
        """Complex component"""
        input ="""
           func main()
            begin
            (aPI)[2]<- 3.14
            end
        """
        expect = """Error on line 4 col 12: ("""
        self.assertTrue(TestParser.test(input,expect,2436))
        
    def test_complex_component38(self):
        """Complex component"""
        input ="""
           func main()
            begin   
                if(1+1) api <- 1
                ## comment0
                
                if(1+1) 
                    ## comment1
                    
                    api <- 1
                    ## comment2
                else api <- 1
                ## comment3
                
                if (1) api <- 1
                elif (1 ... 2)
                    ## comment1
                    
                    api <- 1
                    ## comment2
                elif (1) api <- 1
                
                if (1) api <- 1
                elif (1 ... 2) api <- 1
                elif (1) api <- 1
                else api <- 1   
            end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,2437))

    def test_complex_component39(self):
        """Complex component"""
        input ="""
           func main()
            begin   
                if (api <- 1)
            end
        """
        expect = """Error on line 4 col 24: <-"""
        
        self.assertTrue(TestParser.test(input,expect,2438))

    def test_complex_component40(self):
        """Complex component"""
        input ="""
           func main()
            begin
            for i until i >= 10 by 1 + 1
                ## comment
                
                a <- 1
            ## comment
            end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,2439))

    def test_complex_component41(self):
        """Complex component"""
        input ="""
           func main()
            begin
            for i[1] until i >= 10 by 1 + 1
                a <- 1
            end
        """
        expect = """Error on line 4 col 17: ["""
        self.assertTrue(TestParser.test(input,expect,2440))

    def test_complex_component42(self):
        """Complex component"""
        input ="""
           func main()
            begin
            for i+1 until i >= 10 by 1 + 1
                a <- 1
            end
        """
        expect = """Error on line 4 col 17: +"""
        self.assertTrue(TestParser.test(input,expect,2441))

    def test_complex_component43(self):
        """Complex component"""
        input ="""
           func main()
        begin 
            break
            continue
            for i until i >= 10 by 1 + 1 ... 3 / 2
                begin
                    break
                    continue
                end
                
            for i until i >= 10 by 1 print(1)
            for i until i >= 10 by 1 
                print(1)
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,2442))

    def test_complex_component44(self):
        """Complex component"""
        input ="""
           func main()
            return 1 + 1
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,2443))

    def test_complex_component45(self):
        """Complex component"""
        input ="""
           func main()
            begin
            main()
            end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,2444))

    def test_complex_component46(self):
        """Complex component"""
        input ="""
        func main()
        begin 
            return ([1,2,3]) + 1
            return main()
            main(1,2)
            fun()
            main([1,2,3], 1+2, a, c ... e)
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,2445))

    def test_complex_component47(self):
        """Complex component"""
        input ="""
        func main()
            return func()
        """
        expect = """Error on line 3 col 19: func"""
        self.assertTrue(TestParser.test(input,expect,2446))

    def test_complex_component48(self):
        """Complex component"""
        input ="""
        func main()
            return break
        """
        expect = """Error on line 3 col 19: break"""
        self.assertTrue(TestParser.test(input,expect,2447))

    def test_complex_component49(self):
        """Complex component"""
        input ="""
        func main()
            begin
                begin
                    begin
                        x <- 1
                    end
                    
                    begin
                        return true
                    end
                    
                    return false
                end
                
                begin
                end
                return true
            end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,2448))

    def test_complex_component50(self):
        """Complex component"""
        input ="""
        func areDivisors(number num1, number num2)
            return (num1 % num2 = 0 ... num2 % num1 = 0)
        func main()
            begin
                var num1 <- readNumber()
                var num2 <- readNumber()
                if (areDivisors(num1, num2)) printString("Yes")
                else printString("No")
            end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,2449))

    def test_complex_component51(self):
        """Complex component"""
        input ="""
        func isPrime(number x)
        func main()
            begin
                number x <- readNumber()
                if (isPrime(x)) printString("Yes")
                else printString("No")
            end
        func isPrime(number x)
        begin
        if (x <= 1) return false
        var i <- 2
        for i until i > x / 2 by 1
        begin
        if (x % i = 0) return false
        end
        return true
        
        
        for i until i > x / 2 by 1 + 1 var c <- 1
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,2450))

    def test_complex_component52(self):
        """Complex component"""
        input ="""
        var Nhut
        """
        expect = """Error on line 2 col 17: \n"""
        self.assertTrue(TestParser.test(input,expect,2451))

    def test_complex_component53(self):
        """Complex component"""
        input ="""
        func main[number x, string y]
        begin
        end
        """
        expect = """Error on line 2 col 17: ["""
        self.assertTrue(TestParser.test(input,expect,2452))

    def test_complex_component54(self):
        """Complex component"""
        input ="""
        func main()
            begin
            for i*i until i >= 10 by 1 + 1
                ## comment
                
                a <- 1
            ## comment
            end
        """
        expect = """Error on line 4 col 17: *"""
        self.assertTrue(TestParser.test(input,expect,2453))

    def test_complex_component55(self):
        """Complex component"""
        input ="""
        func main()
            begin
            for i until arr[i] >= 10 by 1 + 1
                a <- 1
            end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,2453))

    def test_complex_component56(self):
        """Complex component"""
        input ="""
        func main()
            return a <- 1
        """
        expect = """Error on line 3 col 21: <-"""
        self.assertTrue(TestParser.test(input,expect,2454))

    def test_complex_component57(self):
        """Complex component"""
        input ="""
        string b[3] <- [2 ... " tring" + "Nhut ne",foo("NhUT")]
            var i <- 0
            dynamic i
            dynamic i <- 0
            ## VO Tien
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,2455))

    def test_complex_component58(self):
        """Complex component"""
        input ="""
        boolean a[12,2]
        boolean a[[1,2]]
        bool a[1+1]
        """
        expect = """Error on line 3 col 18: ["""
        self.assertTrue(TestParser.test(input,expect,2456))

    def test_complex_component59(self):
        """Complex component"""
        input ="""
        func main(dynamic a)
        """
        expect = """Error on line 2 col 18: dynamic"""
        self.assertTrue(TestParser.test(input,expect,2457))

    def test_complex_component60(self):
        """Complex component"""
        input ="""
        func main(number a[],string x) begin
        arr[1][2] <- 2
        end
        """
        expect = """Error on line 3 col 14: ["""
        self.assertTrue(TestParser.test(input,expect,2458))

    def test_complex_component61(self):
        """Complex component"""
        input ="""
        func main(number a[],string x) begin
        arr[1] <- 2
        dynamic z <- "nhut"..."hi"
        end
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,2459))

    def test_complex_component62(self):
        """Complex component"""
        input ="""
        func main(number a[],string x) begin
        arr[1] <- 2
        dynamic z <- "nhut"..."hi"
        end
        string t <- "Nguyen Quoc Nhut \\'"
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(input,expect,2460))

