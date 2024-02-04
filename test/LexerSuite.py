import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_simple_string(self):
        """test simple string"""
        self.assertTrue(TestLexer.test("\"Yanxi Palace - 2018\"","Yanxi Palace - 2018,<EOF>",101))

    def test_complex_string(self):
        """test complex string"""
        self.assertTrue(TestLexer.test("\"isn''t\"","isn''t,<EOF>",102))

    def test_complex_string2(self):
        """test complex string"""
        input = ''' "tabcdefg\\" '''
        expectedOutput = '''Illegal Escape In String: tabcdefg\\"'''
        self.assertTrue(TestLexer.test(input,expectedOutput,103))

    def test_complex_string3(self):
        """test complex string2"""
        self.assertTrue(TestLexer.test("\"PPL is the '\"best'\"\"","PPL is the '\"best'\",<EOF>",104))
        
    def test_simple_number(self):
        """test simple number"""
        self.assertTrue(TestLexer.test("2024","2024,<EOF>",105))
    
    def test_simplex_number(self):
        """test simplex number"""
        self.assertTrue(TestLexer.test("123a123","123,a123,<EOF>",106))
        
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
        
    def test_keyword2(self):
        """test keyword"""
        self.assertTrue(TestLexer.test("boolean continue else","boolean,continue,else,<EOF>",207))
        
    def test_operator(self):
        """test operator"""
        self.assertTrue(TestLexer.test("+ - * / % <= =","+,-,*,/,%,<=,=,<EOF>",208))

    def test_separator(self):
        """test keyword"""
        self.assertTrue(TestLexer.test("()","(,),<EOF>",209))

    def test_integer(self):
        """test integer"""
        self.assertTrue(TestLexer.test("123","123,<EOF>",210))

    def test_real_number(self):
        """test real number"""
        self.assertTrue(TestLexer.test("12.","12.,<EOF>",301))

    def test_real_number2(self):
        """test real number2"""
        self.assertTrue(TestLexer.test("12.3","12.3,<EOF>",302))
        
    def test_real_number_lit(self):
        """test real number scientist"""
        self.assertTrue(TestLexer.test("12.3e30","12.3e30,<EOF>",303))
        
    def test_real_number_lit2(self):
        """test real number scientist"""
        self.assertTrue(TestLexer.test("12.3e30","12.3e30,<EOF>",304))

    def test_real_number_lit3(self):
        """test real number scientist2"""
        self.assertTrue(TestLexer.test("12.3e-40","12.3e-40,<EOF>",305))
        
    def test_real_number_lit4(self):
        """test real number scientist2"""
        self.assertTrue(TestLexer.test("0003121.e00321132  0e-432 001.11011000","0003121.e00321132,0e-432,001.11011000,<EOF>",306))

    def test_invalid_real_number_lit(self):
        """test invalid real number scientist2"""
        self.assertTrue(TestLexer.test("1e 123e e123 e-132 -e123","1,e,123,e,e123,e,-,132,-,e123,<EOF>",307))
        
    def test_bool_lit(self):
        """test boolean literals"""
        self.assertTrue(TestLexer.test("true false","true,false,<EOF>",401))

    def test_invalid_bool_lit(self):
        """test invalid boolean literals"""
        self.assertTrue(TestLexer.test("TRUE False FALSE","TRUE,False,FALSE,<EOF>",402))

    def test_boolean_type(self):
        """test boolean type"""
        self.assertTrue(TestLexer.test("boolean","boolean,<EOF>",403))

    def test_number_type(self):
        """test number type"""
        self.assertTrue(TestLexer.test("number","number,<EOF>",404))
        
    def test_valid_identifiers(self):
        """test valid identifiers"""
        self.assertTrue(TestLexer.test("mssv ID _id 24id 29I_D 4_id","mssv,ID,_id,24,id,29,I_D,4,_id,<EOF>",405))

    def test_valid_identifiers2(self):
        """test valid identifiers"""
        self.assertTrue(TestLexer.test("id bool_id long_id int_id string_int void_int","id,bool_id,long_id,int_id,string_int,void_int,<EOF>",406))
        
    def test_valid_identifiers3(self):
        """test valid identifiers"""
        self.assertTrue(TestLexer.test("c cse a232 c_ a_bc a_bc232 a_13 _abc _123 _ab123 _abc_123 _ ___ ____123____","c,cse,a232,c_,a_bc,a_bc232,a_13,_abc,_123,_ab123,_abc_123,_,___,____123____,<EOF>",407))
        
    def test_valid_identifiers4(self):
        """test valid identifiers"""
        self.assertTrue(TestLexer.test("hcmut HCMUT go __abcd KK __abc___________________dd A___1 69D1 AB nhut b cse","hcmut,HCMUT,go,__abcd,KK,__abc___________________dd,A___1,69,D1,AB,nhut,b,cse,<EOF>",408))

    def test_invalid_identifiers(self):
        """test invalid identifiers"""
        self.assertTrue(TestLexer.test("mssv-43 id?1","mssv,-,43,id,Error Token ?",501))

    def test_invalid_identifiers2(self):
        """test invalid identifiers"""
        self.assertTrue(TestLexer.test("22cs 2212_mt 003_123abc id_id 1ct 21ids 8hc_id 89_____________id3 id___2 90___abc__ppl___sba____abc____dba ds#a","22,cs,2212,_mt,003,_123abc,id_id,1,ct,21,ids,8,hc_id,89,_____________id3,id___2,90,___abc__ppl___sba____abc____dba,ds,Error Token #",502))
        
    def test_inline_comment(self):
        """test inline comment"""
        self.assertTrue(TestLexer.test("##this is an inline comment","<EOF>",503)) 

    def test_invalid_comment(self):
        """test invalid comment"""
        self.assertTrue(TestLexer.test("#inline comment","Error Token #" ,504)) 
        
    def test_invalid_int_lit(self):
        """test invalid int literal"""
        self.assertTrue(TestLexer.test("0 1 2 3 4 123 123456789 001 0x123","0,1,2,3,4,123,123456789,001,0,x123,<EOF>" ,601)) 

    def test_invalid_int_lit2(self):
        """test invalid int literal"""
        self.assertTrue(TestLexer.test("0x223 0X69BC 0xffffff xCSE 0X32","0,x223,0,X69BC,0,xffffff,xCSE,0,X32,<EOF>" ,602)) 

    def test_string_lit(self):
        """test string literal"""
        self.assertTrue(TestLexer.test("\"\" \"String\" \" \" \"?\" \"_\" \"\\\\\" \"Multiple Characters\" ",",String, ,?,_,\\\\,Multiple Characters,<EOF>" ,603))

    def test_mix_lit(self):
        """test mix literal"""
        self.assertTrue(TestLexer.test("\"\" 12 32.43 43.E12 4e-1 true \"false\" false \"012\" 1.32 1. \"String\"",",12,32.43,43.E12,4e-1,true,false,false,012,1.32,1.,String,<EOF>" ,701))  

    def test_unclose_string(self):
        """test unclose string"""
        self.assertTrue(TestLexer.test("\"Hello Be Ba","Unclosed String: Hello Be Ba" ,801)) 

    def test_unclose_string2(self):
        """test unclose string"""
        input = ''' "38n"Ffs0ED"0.""T7n'''
        expect = "38n,Ffs0ED,0.,Unclosed String: T7n"
        self.assertTrue(TestLexer.test(input,expect,802)) 

    def test_unclose_multi_line(self):
        """test unclose multi line"""
        input='''"Hello Be Ba\\Hello CSE"'''
        output= '''Illegal Escape In String: Hello Be Ba\\H'''
        self.assertTrue(TestLexer.test(input,output ,803)) 

    def test_escape(self):
        """test escape"""
        input=''' ""\\"cse"'''
        output = "\\,cse,<EOF>"
        self.assertTrue(TestLexer.test("\"\\\"cse","\\,cse,<EOF>" ,804))
        
    def test_unclose_string2(self):
        """test unclose string"""
        self.assertTrue(TestLexer.test("s=\"String PPL","s,=,Unclosed String: String PPL" ,806))
        
    def test_error_token(self):
        """test error token"""
        self.assertTrue(TestLexer.test("!= = &","!=,=,Error Token &" ,901))
        
    def test_error_token2(self):
        """test error token"""
        self.assertTrue(TestLexer.test("x = x ! y","x,=,x,Error Token !" ,902))

    def test_error_token3(self):
        """test error token"""
        self.assertTrue(TestLexer.test("@_abc","Error Token @" ,903))
        
    def test_error_token4(self):
        """test error token"""
        self.assertTrue(TestLexer.test("_abc?","_abc,Error Token ?" ,904))

    def test_error_token5(self):
        """test error token"""
        self.assertTrue(TestLexer.test("*(*)()_(()$)","*,(,*,),(,),_,(,(,),Error Token $" ,905))

    def test_invalid_keyword(self):
        """test invalid keyword"""
        self.assertTrue(TestLexer.test("bOOLEAN INt 0.12INTEGER sTRIng 12and","bOOLEAN,INt,0.12,INTEGER,sTRIng,12,and,<EOF>" ,1000))
        
    def test_invalid_operator(self):
        """test invalid operator"""
        self.assertTrue(TestLexer.test("*= /= %=","*,=,/,=,%,=,<EOF>" ,1001))

    def test_invalid_operator2(self):
        """test invalid operator"""
        self.assertTrue(TestLexer.test("++ -- += -= ^","+,+,-,-,+,=,-,=,Error Token ^" ,1002))

    def test_invalid_operator3(self):
        """test invalid operator"""
        self.assertTrue(TestLexer.test("!xyz <> % # &a","Error Token !" ,1003))

    def test_invalid_operator4(self):
        """test invalid operator"""
        self.assertTrue(TestLexer.test("x=(4+3i)(2+i)?-i","x,=,(,4,+,3,i,),(,2,+,i,),Error Token ?" ,1004))

    def test_sensitive_keyword(self):
        """test sensitive keyword"""
        self.assertTrue(TestLexer.test("true TRUE false FALSE","true,TRUE,false,FALSE,<EOF>" ,1005))
    
    def test_unclose_string3(self):
        """test unclose string"""
        self.assertTrue(TestLexer.test("69a\"[#baS!8fD\"5.\"A`7n","69,a,[#baS!8fD,5.,Unclosed String: A`7n" ,1006))

    def test_unclose_string4(self):
        """test unclose string"""
        self.assertTrue(TestLexer.test("\"q|F&)CSX\"+>X+\"#CSE","q|F&)CSX,+,>,X,+,Unclosed String: #CSE" ,1007))

    def test_random(self):
        """test random """
        self.assertTrue(TestLexer.test("a=5##a is an integer","a,=,5,<EOF>" ,1100))

    def test_random2(self):
        """test random """
        self.assertTrue(TestLexer.test("for (int a ; b = 2 && c = 2; 2**2)","for,(,int,a,Error Token ;" ,1101))
    def test_random3(self):
        """test random """
        self.assertTrue(TestLexer.test("str abc[] = {1,2,3}","str,abc,[,],=,{,1,,,2,,,3,},<EOF>" ,1102))
    def test_random4(self):
        """test random """
        self.assertTrue(TestLexer.test("$no idea","Error Token $" ,1103))

    def test_random5(self):
        """test random """
        self.assertTrue(TestLexer.test("INT abc = 12;","INT,abc,=,12,Error Token ;" ,1104))

    def test_random6(self):
        """test random """
        self.assertTrue(TestLexer.test("[,<>,( k01 begin,],true","[,,,<,>,,,(,k01,begin,,,],,,true,<EOF>" ,1105))
        
    def test_random7(self):
        """test random """
        self.assertTrue(TestLexer.test("\" \"  \"a?"," ,Unclosed String: a?",1106))

    def test_random8(self):
        """test random """
        self.assertTrue(TestLexer.test("if flag then a:=1","if,flag,then,a,Error Token :",1107))

    def test_random9(self):
        """test random """
        self.assertTrue(TestLexer.test("void print(string str){io.writeString(str)","void,print,(,string,str,),{,io,Error Token .",1108))
    
    def test_simple_array(self):
        """test simple array """
        self.assertTrue(TestLexer.test("number arr[5] = {1,2}","number,arr,[,5,],=,{,1,,,2,},<EOF>",1200))

    def test_simplex(self):
        """test simplex"""
        self.assertTrue(TestLexer.test("hh + 0000 >= 12.E-00 - FALSE","hh,+,0000,>=,12.E-00,-,FALSE,<EOF>",1300))

    def test_simplex2(self):
        """test simplex"""
        self.assertTrue(TestLexer.test("1+2==3 ? Return True","1,+,2,==,3,Error Token ?",1301))

    def test_simplex3(self):
        """test simplex"""
        self.assertTrue(TestLexer.test("0ox123 0X89? true","0,ox123,0,X89,Error Token ?",1302))

    def test_simplex4(self):
        """test simplex"""
        self.assertTrue(TestLexer.test("Var: s=\"haha\",\"qweqweqwe\"","Var,Error Token :",1303))

    def test_simplex5(self):
        """test simplex"""
        input = '''This is a raw string
        With a newline'''
        expectedOut = '''This,is,a,raw,string,\n,With,a,newline,<EOF>'''
        self.assertTrue(TestLexer.test(input,expectedOut,1304))

    def test_simplex_6(self):
        """unterminated multi"""
        input='''## not hate me \ndon't care much ..'''
        expectedOut='''
,don,Error Token \''''
        self.assertTrue(TestLexer.test(input,expectedOut,1305))

    def test_escape(self):
        """test invalid escape"""
        input=''' "not hate me \m don't care much .." '''
        expectedOut='''Illegal Escape In String: not hate me \m'''
        self.assertTrue(TestLexer.test(input,expectedOut,1306))

    def test_escape2(self):
        """test invalid escape"""
        input=''' not hate me \n  \t \\u don't care much ..'''
        expectedOut='''not,hate,me,\n,Error Token \\'''
        self.assertTrue(TestLexer.test(input,expectedOut,1307))

    def test_mix(self):
        """test mix"""
        input=''' "string"
        'string' 
        '''
        expectedOut='''string,\n,Error Token \''''
        self.assertTrue(TestLexer.test(input,expectedOut,1401))

    def test_mix2(self):
        """test mix"""
        input='''"\\a"'''
        expectedOut='''Illegal Escape In String: \\a'''
        self.assertTrue(TestLexer.test(input,expectedOut,1402))

    def test_mix3(self):
        """test mix"""
        input='''"abcz\\t"'''
        expectedOut='''abcz\\t,<EOF>'''
        self.assertTrue(TestLexer.test(input,expectedOut,1403))

    def test_mix_string(self):
        input = """a:="Hello world1 \b Hello World1 " """
        expect = """a,Error Token :"""
        self.assertTrue(TestLexer.test(input, expect, 1500))
        
    def test_mix4(self):
        input = """for (number x ; x = 2 && c = 2; 5**2)
        break
        """
        expect = """for,(,number,x,Error Token ;"""
        self.assertTrue(TestLexer.test(input, expect, 1501))

    def test_mix5(self):
        input = """ x + z = c
        x * y = c * 2
        y / 2 = 15
        z % 3 >= 6
        a # 2 = 0.6
        a && a == 1
        """
        expect = """x,+,z,=,c,\n,x,*,y,=,c,*,2,\n,y,/,2,=,15,\n,z,%,3,>=,6,\n,a,Error Token #"""
        self.assertTrue(TestLexer.test(input, expect, 1502))

    def test_mix6(self):
        input = """ ## // */ acc
        a++
        string a = "a";
        """
        expect = """\n,a,+,+,\n,string,a,=,a,Error Token ;"""
        self.assertTrue(TestLexer.test(input, expect, 1503))
        
    def test_program(self):
        """test program"""
        input='''void print(string str){io.writeString(str);}
        void main(){this.print(\"\";}}  
        '''
        expectedOut='''void,print,(,string,str,),{,io,Error Token .'''
        self.assertTrue(TestLexer.test(input,expectedOut,1600))

    def test_program2(self):
        """test program"""
        input='''if flag then
            a=1
        else
            a=2 
        '''
        expectedOut='''if,flag,then,\n,a,=,1,\n,else,\n,a,=,2,\n,<EOF>'''
        self.assertTrue(TestLexer.test(input,expectedOut,1601))

    def test_program3(self):
        """test program"""
        input='''func isPrime(number x)
        
        func main()
        begin 
        '''
        expectedOut='''func,isPrime,(,number,x,),\n,\n,func,main,(,),\n,begin,\n,<EOF>'''
        self.assertTrue(TestLexer.test(input,expectedOut,1602))
        
    def test_program4(self):
        """test program"""
        input='''
        begin
            number x <- readNumber()
            if (isPrime(x)) printString("Yes")
            else printString("No")
        end
        '''
        expectedOut='''\n,begin,\n,number,x,<-,readNumber,(,),\n,if,(,isPrime,(,x,),),printString,(,Yes,),\n,else,printString,(,No,),\n,end,\n,<EOF>'''
        self.assertTrue(TestLexer.test(input,expectedOut,1603))

    def test_program5(self):
        """test program"""
        input='''a[3 + foo(2)] <- a[b[2, 3]] + 4'''
        expectedOut='''a,[,3,+,foo,(,2,),],<-,a,[,b,[,2,,,3,],],+,4,<EOF>'''
        self.assertTrue(TestLexer.test(input,expectedOut,1604))
        
    def test_complex_lit(self):
        """test complex literal"""
        input='''12.'''
        expectedOut='''12.,<EOF>'''
        self.assertTrue(TestLexer.test(input,expectedOut,1605))

    def test_complex_mix(self):
        """test complex mix"""
        input='''##nhddjnadh\na<-5'''
        expectedOut='''\n,a,<-,5,<EOF>'''
        self.assertTrue(TestLexer.test(input,expectedOut,1606))

    def test_complex_mix2(self):
        """test complex mix"""
        input='''a<5+6=7<=8'''
        expectedOut='''a,<,5,+,6,=,7,<=,8,<EOF>'''
        self.assertTrue(TestLexer.test(input,expectedOut,1607))
        
    def test_complex_mix3(self):
        """test complex mix"""
        input='''12.56E+03'''
        expectedOut='''12.56E+03,<EOF>'''
        self.assertTrue(TestLexer.test(input,expectedOut,1608))

    def test_complex_mix4(self):
        """test complex mix"""
        input='''1E+0333'''
        expectedOut='''1E+0333,<EOF>'''
        self.assertTrue(TestLexer.test(input,expectedOut,1609))

    def test_complex_mix5(self):
        """test complex mix"""
        input='''
        .33
        '''
        expectedOut='''\n,Error Token .'''
        self.assertTrue(TestLexer.test(input,expectedOut,1610))

    def test_complex_lit2(self):
        """test complex literal"""
        input='''"He said:'"How old are you?'""'''
        expectedOut='''He said:'"How old are you?'",<EOF>'''
        self.assertTrue(TestLexer.test(input,expectedOut,1700))

    def test_complex_lit3(self):
        """test complex literal"""
        input='''l[3] <- value * aPi\\n'''
        expectedOut='''l,[,3,],<-,value,*,aPi,Error Token \\'''
        self.assertTrue(TestLexer.test(input,expectedOut,1701))

    def test_complex_lit4(self):
        """test complex literal"""
        input='''l[3] <- value * aPi\n'''
        expectedOut='''l,[,3,],<-,value,*,aPi,\n,<EOF>'''
        self.assertTrue(TestLexer.test(input,expectedOut,1702))
        
    def test_complex_lit5(self):
        """test complex literal"""
        input='''s="String literal'''
        expectedOut='''s,=,Unclosed String: String literal'''
        self.assertTrue(TestLexer.test(input,expectedOut,1703))

    def test_complex_lit6(self):
        """test complex literal"""
        input='''"abc\n'''
        expectedOut='''Unclosed String: abc
'''
        self.assertTrue(TestLexer.test(input,expectedOut,1704))

    def test_complex_lit7(self):
        """test complex literal"""
        input='''"Hello \\\\ \\"'''
        expectedOut='''Illegal Escape In String: Hello \\\\ \\"'''
        self.assertTrue(TestLexer.test(input,expectedOut,1705))

    def test_complex_escape(self):
        """test complex escape"""
        input='''"Hello \\\\ \\t"'''
        expectedOut='''Hello \\\\ \\t,<EOF>'''
        self.assertTrue(TestLexer.test(input,expectedOut,1800))
        
    def test_complex_escape2(self):
        """test complex escape"""
        input='''"Hello \\\\ \\t \\w"'''
        expectedOut='''Illegal Escape In String: Hello \\\\ \\t \\w'''
        self.assertTrue(TestLexer.test(input,expectedOut,1801))

    def test_complex_escape3(self):
        """test complex escape"""
        input='''"Hello \\\\ \\t \\'"'''
        expectedOut='''Hello \\\\ \\t \\',<EOF>'''
        self.assertTrue(TestLexer.test(input,expectedOut,1802))
        
    def test_complex_literal(self):
        """test complex literal"""
        input=''' 4 -5 '''
        expectedOut='''4,-,5,<EOF>'''
        self.assertTrue(TestLexer.test(input,expectedOut,1803))

    def test_complex_literal_and_escape(self):
        """test complex literal and escape"""
        input='''"Nhut \\G"'''
        expectedOut='''Illegal Escape In String: Nhut \\G'''
        self.assertTrue(TestLexer.test(input,expectedOut,1804))

    def test_complex_literal_and_escape2(self):
        """test complex literal and escape"""
        input='''"Nhut \\t \\f \\r \\z"'''
        expectedOut='''Illegal Escape In String: Nhut \\t \\f \\r \\z'''
        self.assertTrue(TestLexer.test(input,expectedOut,1805))

    def test_complex_literal_and_escape3(self):
        """test complex literal and escape"""
        input=""" "He asked me: \'"Where is John?\'"" """
        expectedOut='''He asked me: '"Where is John?'",<EOF>'''
        self.assertTrue(TestLexer.test(input,expectedOut,1806))
