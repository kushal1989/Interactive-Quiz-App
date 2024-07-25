Updates to keyboard shortcuts … On Thursday, August 1, 2024, Drive keyboard shortcuts will be updated to give you first-letters navigation.Learn more
import tkinter as tk
from tkinter import *
import random
import sqlite3 
import time
import webbrowser

def loginPage(logdata):
    sup.destroy()
    global login
    login = Tk()
    
    user_name = StringVar()
    password = StringVar()
    
    login_canvas = Canvas(login,width=1000,height=1000,bg="blue")
    login_canvas.pack()

    login_frame = Frame(login_canvas,bg="white")
    login_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    heading = Label(login_frame,text="Quiz App Login",fg="black",bg="white")
    heading.config(font=('calibri 40'))
    heading.place(relx=0.2,rely=0.1)

    #USER NAME
    ulabel = Label(login_frame,text="Username",fg='black',bg='white')
    ulabel.place(relx=0.21,rely=0.4)
    uname = Entry(login_frame,bg='#d3d3d3',fg='black',textvariable = user_name)
    uname.config(width=42)
    uname.place(relx=0.31,rely=0.4)
    
    #PASSWORD
    plabel = Label(login_frame,text="Password",fg='black',bg='white')
    plabel.place(relx=0.215,rely=0.5)
    pas = Entry(login_frame,bg='#d3d3d3',fg='black',show="*",textvariable = password)
    pas.config(width=42)
    pas.place(relx=0.31,rely=0.5)

    def check():
        for a,b,c in logdata:
            if b == uname.get() and c == pas.get():
                menu()
                break
        else:
            error = Label(login_frame,text="Wrong Username or Password!",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
    
    #LOGIN BUTTON
    log = Button(login_frame,text='Login',padx=5,pady=5,width=5,command=check)
    log.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    log.place(relx=0.4,rely=0.6)
    
    
    login.mainloop()

def signUpPage():
    root.destroy()
    global sup
    sup = Tk()
    
    fname = StringVar()
    uname = StringVar()
    passW = StringVar()
    
    
    
    sup_canvas = Canvas(sup,width=1000,height=1000,bg="blue")
    sup_canvas.pack()

    sup_frame = Frame(sup_canvas,bg="white")
    sup_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    heading = Label(sup_frame,text="Quiz App SignUp",fg="black",bg="white")
    heading.config(font=('calibri 40'))
    heading.place(relx=0.2,rely=0.1)

    #full name
    flabel = Label(sup_frame,text="Full Name",fg='black',bg='white')
    flabel.place(relx=0.21,rely=0.4)
    fname = Entry(sup_frame,bg='#d3d3d3',fg='black',textvariable = fname)
    fname.config(width=42)
    fname.place(relx=0.31,rely=0.4)

    #username
    ulabel = Label(sup_frame,text="Username",fg='black',bg='white')
    ulabel.place(relx=0.21,rely=0.5)
    user = Entry(sup_frame,bg='#d3d3d3',fg='black',textvariable = uname)
    user.config(width=42)
    user.place(relx=0.31,rely=0.5)
    
    
    #password
    plabel = Label(sup_frame,text="Password",fg='black',bg='white')
    plabel.place(relx=0.215,rely=0.6)
    pas = Entry(sup_frame,bg='#d3d3d3',fg='black',show="*",textvariable = passW)
    pas.config(width=42)
    pas.place(relx=0.31,rely=0.6)
    
    
    
    
    def addUserToDataBase():
        
        fullname = fname.get()
        username = user.get()
        password = pas.get()
        
        conn = sqlite3.connect('quiz.db')
        create = conn.cursor()
        create.execute('CREATE TABLE IF NOT EXISTS userSignUp(FULLNAME text, USERNAME text,PASSWORD text)')
        create.execute("INSERT INTO userSignUp VALUES (?,?,?)",(fullname,username,password)) 
        conn.commit()
        create.execute('SELECT * FROM userSignUp')
        z=create.fetchall()
        print(z)
#        L2.config(text="Username is "+z[0][0]+"\nPassword is "+z[-1][1])
        conn.close()
        loginPage(z)
    def gotoLogin():
        conn = sqlite3.connect('quiz.db')
        create = conn.cursor()
        conn.commit()
        create.execute('SELECT * FROM userSignUp')
        z=create.fetchall()
        loginPage(z)
    #signup BUTTON
    sp = Button(sup_frame,text='SignUp',padx=5,pady=5,width=5,command = addUserToDataBase,bg='green')
    sp.configure(width = 15,height=1, activebackground = "#33B5E5", relief = FLAT)
    sp.place(relx=0.4,rely=0.8)

    log = Button(sup_frame,text='Already have a Account?',padx=5,pady=5,width=5,command = gotoLogin,bg="white",fg='blue')
    log.configure(width = 16,height=1, activebackground = "#33B5E5", relief = FLAT)
    log.place(relx=0.4,rely=0.9)

    sup.mainloop()

def menu():
    login.destroy()
    global menu 
    menu = Tk()
    
    
    menu_canvas = Canvas(menu,width=1000,height=1000,bg="blue")
    menu_canvas.pack()

    menu_frame = Frame(menu_canvas,bg="white")
    menu_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    
    wel = Label(menu_canvas,text=' W E L C O M E  T O  Q U I Z  S T A T I O N ',fg="white",bg="#101357") 
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1,rely=0.02)
    
    
    level = Label(menu_frame,text='Select Language to write Quiz !!',bg="white",font="calibri 18")
    level.place(relx=0.25,rely=0.3)
    
    
    var = IntVar()
    cR = Radiobutton(menu_frame,text='C',bg="white",font="calibri 16",value=1,variable = var)
    cR.place(relx=0.25,rely=0.4)
    
    cppR = Radiobutton(menu_frame,text='C++',bg="white",font="calibri 16",value=2,variable = var)
    cppR.place(relx=0.25,rely=0.5)
    
    JAVAR = Radiobutton(menu_frame,text='JAVA',bg="white",font="calibri 16",value=3,variable = var)
    JAVAR.place(relx=0.25,rely=0.6)
    
    PYTHONR = Radiobutton(menu_frame,text='PYTHON',bg="white",font="calibri 16",value=4,variable = var)
    PYTHONR.place(relx=0.25,rely=0.7)
    
    
    def navigate():
        
        x = var.get()
        print(x)
        if x == 1:
            menu.destroy()
            c()
        elif x == 2:
            menu.destroy()
            cpp()
        
        elif x == 3:
            menu.destroy()
            JAVA()
            
        elif x == 4:
            menu.destroy()
            PYTHON()
        else:
            pass
    letsgo = Button(menu_frame,text="Let's Go",bg="white",font="calibri 12",command=navigate)
    letsgo.place(relx=0.25,rely=0.8)
    menu.mainloop()
    

def c():
    
    global e
    e = Tk()
    
    c_canvas = Canvas(e,width=1000,height=1000,bg="#101357")
    c_canvas.pack()

    c_frame = Frame(c_canvas,bg="white")
    c_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    def countDown():
        check = 0
        for k in range(20, 0, -1):
            
            if k == 1:
                check=-1
            timer.configure(text=k)
            c_frame.update()
            time.sleep(1)
            
        timer.configure(text="Times up!")
        if check==-1:
            return (-1)
        else:
            return 0
    global score
    score = 0
    
    global cQ
    
    cQ = [
                 [
                     "Every C Program should contain which function?",
                     "printf()",
                     "show()",
                     "scanf()",
                     "main()",
                     "https://www.w3schools.com/c/c_functions.php"
                     
                 ] ,
                 [
                     "Data structure used to implement recursive function calls _____________" ,
                    "Array",
                    "Linked list",
                    "Binary tree",
                    "Stack",
                    "https://www.w3schools.com/c/c_functions_recursion.php"
                    

                     
                 ],
                [
                    "What is the output of this program?\n#include <stdio.h>\nint main(){\nFILE *fp;\nchar *str;\nfp=fopen(demo.txt,r);while(fgets(str,6,fp)!=NULL)\nputs(str);\nfclose(fp);\nreturn 0;}" ,
                    "you are a good programmer",
                    "e a good programmer",
                    "you ar",
                    "you are",
                    "https://www.w3schools.com/c/c_files.php"
                    

                ],
                [
                    " What is the output of this program?\n#include <stdio.h>\nint main(){\nstruct simp\n{\nint i = 6;\nchar city[] = chennai;\n};\nstruct simp s1;\nprintf(%d,s1.city);\nprintf(%d, s1.i);\nreturn 0;\n}\n" ,
                    "chennai 6",
                    "Nothing will be displayed",
                    "Runtime Error",
                    "Compilation Error",
                    "https://www.w3schools.com/c/c_structs.php"
                    

                ],
                [
                    "While loop terminates when conditional expression returns?",
                    "One",
                    "Zero",
                    "Non - zero",
                    "None of the above",
                    "https://www.w3schools.com/c/c_functions_decl.php"
                    

                ] ,
                [
                   "For loop in a C program, if the condition is missing?" ,
                   "it is assumed to be present and taken to be false",
                   "it is assumed to be present and taken to the true",
                   "it result in a syntax error",
                   "execution will be terminated abruptly",
                   "https://www.w3schools.com/c/c_while_loop.php"
                   

                    
                ],
               [
                   "Array can be considered as set of elements stored in consecutive memory locations but having __________." ,
                   "Same data type",
                   "Different data type",
                   "Same scope",
                   "None of these",
                   "https://www.w3schools.com/c/c_for_loop.php"
                   


               ],
               [
                   "  Which of the following statements are correct ?\n1: A string is a collection of characters terminated by .\n2: The format specifier %s is used to print a string.\n3: The length of the string can be obtained by strlen().\n4: The pointer CANNOT work on string." ,
                   "1,2,3",
                   "1,2",
                   "2,4",
                   "3,4",
                   "https://www.w3schools.com/c/c_arrays.php"
                   


               ],
               
                [
                    " Address stored in the pointer variable is of type __________." ,
                    "Integer",
                    "Float",
                    "Array",
                    "Character",
                    "https://www.w3schools.com/c/c_strings.php"


                ],
                [
                    "  Select a function which is used to write a string to a file?" ,
                    "pits()",
                    "putc()",
                    "fputs()",
                    "fgets()",
                    "https://www.w3schools.com/c/c_pointers.php"



                ]
            ]
    answer = [
                "main()",
                "Stack",
                "e a good programmer",
                "Compilation Error",
                "Zero",
                "is assumed to be present and taken to the true",
                "Same data type",
                "1,2,3",
                "Integer",
                "fputs()",
                "^"
             ]
    global li
    li = ['',0,1,2,3,4,5,6,7,8,9]
    x = random.choice(li[1:])
    
    
    ques = Label(c_frame,text =cQ[x][0],font="calibri 12",bg="white")
    ques.place(relx=0.5,rely=0.2,anchor=CENTER)

    var = StringVar()
    
    a = Radiobutton(c_frame,text=cQ[x][1],font="calibri 10",value=cQ[x][1],variable = var,bg="white")
    a.place(relx=0.5,rely=0.42,anchor=CENTER)

    b = Radiobutton(c_frame,text=cQ[x][2],font="calibri 10",value=cQ[x][2],variable = var,bg="white")
    b.place(relx=0.5,rely=0.52,anchor=CENTER)

    c = Radiobutton(c_frame,text=cQ[x][3],font="calibri 10",value=cQ[x][3],variable = var,bg="white")
    c.place(relx=0.5,rely=0.62,anchor=CENTER) 

    d = Radiobutton(c_frame,text=cQ[x][4],font="calibri 10",value=cQ[x][4],variable = var,bg="white")
    d.place(relx=0.5,rely=0.72,anchor=CENTER) 
    
    li.remove(x)
    
    timer = Label(e)
    timer.place(relx=0.8,rely=0.82,anchor=CENTER)
    
    
    
    def display():
        
        if len(li) == 1:
                e.destroy()
                wrong1()
        if len(li) == 2:
               showMark(mark)
               nextQuestion.configure(text='End',command=calc)
                
        if li:
            x = random.choice(li[1:])
            ques.configure(text =cQ[x][0])
            
            a.configure(text=cQ[x][1],value=cQ[x][1])
      
            b.configure(text=cQ[x][2],value=cQ[x][2])
      
            c.configure(text=cQ[x][3],value=cQ[x][3])
      
            d.configure(text=cQ[x][4],value=cQ[x][4])
            
            li.remove(x)
            print(li)
            y = countDown()
            if y == -1:
                display()

            
    def calc():
            if (var.get() not in answer):
                wrong1()
            if(var.get() in answer):
                global score
                score = 0
                score+=1
       
    submit = Button(c_frame,command=calc,text="Submit")
    submit.place(relx=0.5,rely=0.82,anchor=CENTER)
    
    nextQuestion = Button(c_frame,command=display,text="Next")
    nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER)
    
    y = countDown()
    if y == -1:
        display()
    e.mainloop()
    
    
   
    
def cpp():
    
    global m
    m = Tk()
    
    cpp_canvas = Canvas(m,width=1000,height=1000,bg="#101357")
    cpp_canvas.pack()

    cpp_frame = Frame(cpp_canvas,bg="white")
    cpp_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    def countDown():
        check = 0
        for k in range(20, 0, -1):
            
            if k == 1:
                check=-1
            timer.configure(text=k)
            cpp_frame.update()
            time.sleep(1)
            
        timer.configure(text="Times up!")
        if check==-1:
            return (-1)
        else:
            return 0
        
    global score
    score = 0
    
    global cppQ
    
    cppQ = [
                [
                    " Which among the following can be used together in a single class?",
                    "Only private",
                    "Private and Protected together",
                    "Private and Protected together",
                    "All three together",
                    "https://www.w3schools.com/cpp/cpp_user_input.asp"
                  
                ],
                [
                    "What is use of eof() ?",
                    "Returns true if a file open for reading has reached the next character.",
                    "Returns true if a file open for reading has reached the next word.",
                    "Returns true if a file open for reading has reached the end.",
                    "Returns true if a file open for reading has reached the middle.",
                    "https://www.w3schools.com/cpp/cpp_conditions.asp"

                ],
                [
                  " What will be the output of the following code snippet?\n#include <iostream>\nusing namespace std;\nint main()\n{\nint arr[] = { 4, 5, 6, 7 },*ptr,*ptr1;\nptr=&arr[0];ptr1=arr[1];\ncout << a= << ptr1;return 0;\n}",
                    "5",
                    "6",
                    "4",
                    "Compiler error",
                    "https://www.w3schools.com/cpp/cpp_oop.asp"

                ],
                [
                   " What is the output of the following program?\n#include <iostream>\nusing namespace std;\nint main()\n{\nint i,j=0;\nfor(i=10;i>0;i/=2)\n{\nj++;\ncout<<j;\n}\ncout<<j;\n return 0;\n}",
                        "0123456789",
                        "123456789",
                        "12344",
                        "12345",
                        "https://www.w3schools.com/cpp/cpp_classes.asp"

                ],
                [
                                    "What is the output of the following code?\n#include <iostream>\nusing namespace std;\nvoid find()\nvoid find()\n{\n    cout<<course;\n}\nint main()\n{\n    find();\n    return 0;\n} \n",
                                    "course",
                                    "coursecourse",
                                    "compile time error",
                                    "none of the mentioned",
                                    "https://www.w3schools.com/cpp/cpp_constructors.asp"

                ], 
                
                [
                   " Destructor has the same name as the constructor and it is preceded by __ .",
                                "!",
                                "?",
                                "~",
                                "$",
                                "https://www.w3schools.com/cpp/cpp_function_param.asp"

                    ],
                [
                     "Predict the output of following C++ program\n#include<iostream>\nusing namespace std;\nclass Empty {};\nint main()\n{\ncout << sizeof(Empty);\nreturn 0;\n}",
                                  "non-zero value",
                                  "0",
                                  "Compiler Error",
                                  "Runtime Error",
                                  "https://www.w3schools.com/cpp/cpp_for_loop.asp"

                    
                    ],
                [
                   " Which of the following is true statement?",

                        "Friend function can access public data only",
                        
                       " Scope of friend function is limited within the class where it is declared.",
                        
                       " A friend function can't be called using the object of the class",
                        
                       " Like class member, it can access the class members directly.",
                       "https://www.w3schools.com/cpp/cpp_access_specifiers.asp"

                    
                    ],
                [
                    "Which of the following shows the correct syntax for an if statement?",
                                    "if expression",
                                    "if { expression",
                                    "if ( expression )",
                                    "expression if",
                                    "https://www.w3schools.com/cpp/cpp_files.asp"

                    
                    ],
                [
                    
                    "What will be the output of the following C++ code by manipulating the text file?\n #include <stdio.h> \nint main ()\n{\nif (remove( myfile.txt ) != 0 )\nperror( Error ) \n else\nputs( Success );\nreturn 0;\n}",
                                           
                                           "Error",
                                            "Success",
                                            "Runtime Error",
                                            "Can’t say",
                                            "https://www.w3schools.com/cpp/cpp_exceptions.asp"

                    
                    ]
            ]
    answer = [
            "All three together",
            "Returns true if a file open for reading has reached the end.",
            "Compiler error",
            "12344",
            "compile time error",
            "~",
            "non-zero value",
            " A friend function can't be called using the object of the class",
            "if ( expression )",
            "Can’t say"
            ]
    
    global li
    li = ['',0,1,2,3,4,5,6,7,8,9]
    x = random.choice(li[1:])
    
    
    ques = Label(cpp_frame,text =cppQ[x][0],font="calibri 12",bg="white")
    ques.place(relx=0.5,rely=0.2,anchor=CENTER)

    var = StringVar()
    
    a = Radiobutton(cpp_frame,text=cppQ[x][1],font="calibri 10",value=cppQ[x][1],variable = var,bg="white")
    a.place(relx=0.5,rely=0.42,anchor=CENTER)

    b = Radiobutton(cpp_frame,text=cppQ[x][2],font="calibri 10",value=cppQ[x][2],variable = var,bg="white")
    b.place(relx=0.5,rely=0.52,anchor=CENTER)

    c = Radiobutton(cpp_frame,text=cppQ[x][3],font="calibri 10",value=cppQ[x][3],variable = var,bg="white")
    c.place(relx=0.5,rely=0.62,anchor=CENTER) 

    d = Radiobutton(cpp_frame,text=cppQ[x][4],font="calibri 10",value=cppQ[x][4],variable = var,bg="white")
    d.place(relx=0.5,rely=0.72,anchor=CENTER) 
    
    li.remove(x)
    
    timer = Label(m)
    timer.place(relx=0.8,rely=0.82,anchor=CENTER)
    
    
    
    def display():
        
        if len(li) == 1:
                m.destroy()
                wrong2()
        if len(li) == 2:
            nextQuestion.configure(text='End',command=calc)
                
        if li:
            x = random.choice(li[1:])
            ques.configure(text =cppQ[x][0])
            
            a.configure(text=cppQ[x][1],value=cppQ[x][1])
      
            b.configure(text=cppQ[x][2],value=cppQ[x][2])
      
            c.configure(text=cppQ[x][3],value=cppQ[x][3])
      
            d.configure(text=cppQ[x][4],value=cppQ[x][4])
            
            li.remove(x)
            print(li)
            y = countDown()
            if y == -1:
                display()

            
    def calc():
        if (var.get() not in answer):
            wrong2()
    submit = Button(cpp_frame,command=calc,text="Submit")
    submit.place(relx=0.5,rely=0.82,anchor=CENTER)
    
    nextQuestion = Button(cpp_frame,command=display,text="Next")
    nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER)
    
    y = countDown()
    if y == -1:
        display()
    m.mainloop()
    
    
    
def JAVA():
    
       
    global h
    h = Tk()
    
    JAVA_canvas = Canvas(h,width=1000,height=1000,bg="#101357")
    JAVA_canvas.pack()

    JAVA_frame = Frame(JAVA_canvas,bg="white")
    JAVA_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    
    def countDown():
        check = 0
        for k in range(20, 0, -1):
            
            if k == 1:
                check=-1
            timer.configure(text=k)
            JAVA_frame.update()
            time.sleep(1)
            
        timer.configure(text="Times up!")
        if check==-1:
            return (-1)
        else:
            return 0
        
    global score
    score = 0
    
    global JAVAQ
    
    JAVAQ=[
       [
        "Implicit Type Conversion in java is also called__",
        "Narrowing Type Conversion",
        "Widening Type Conversion",
        "No Type Conversion",
        "None of the above",
        "https://www.w3schools.com/java/java_type_casting.asp"
        ],
       [
        "What will be the result of the following code?\nint j=0;\nwhile(j<1000){\nj=j-1;\n} ",
        "j=-999",
        "j=999",
        "Compiler Error",
        "Endless loop",
        "https://www.w3schools.com/java/java_while_loop.asp"
        ],
       [
        "public class Test{\n\tpublic static void main(String[] args){\n\t\tint i=0\n\t\tfor(;i<10;i++){\n\t\t\tbreak;\n\t\t}\nSystem.out.println(i);\n\t}\n}",
        "0",
        "1",
        "10",
        "compilation error",
        "https://www.w3schools.com/java/java_for_loop.asp"
        ],
       [
        "A java array that would have rows and columns is called a ____array?",
        "Two-dimensional Sequence",
        "Three-dimensional Cubic",
        "Uni dimensional Sequence",
        "None",
        "https://www.w3schools.com/java/java_arrays.asp"
        ],
       [
        "Which of the following is not relevant to OOPS?",
        "Object and Class",
        "Encapsulation and Inheritance",
        "Enumerated type and Structure",
        "Constructor and Method",
        "https://www.w3schools.com/java/java_scope.asp"
        ],
       [
        "Which keyword is used to inherit a class in java?",
        "inherit",
        "extend",
        "extends",
        "implement"
        "https://www.w3schools.com/java/java_oop.asp"
        ],
       [
        "What is an access modifier in java ?",
        "An access modifier controls the visibility of variables, constants and methods of a class",
        "An access modifier can hide or show a variable or method to outside classesArithmeticError",
        "Access modifiers help in implementing the Encapsulation feature of Object-Oriented Programming (OOPsArithmeticError",
        "All the above",
        "https://www.w3schools.com/java/java_class_attributes.asp"
        ],
       [
        " Which method returns the elements of the Enum class?",
        "getEnum()",
        "getEnumList()",
        "getEnums()",
        "getEnumConstants()",
        "https://www.w3schools.com/java/java_modifiers.asp"
        ],
       [
        "Which of the following is not a class of java.util.regex?",
        "Pattern class",
        "matcher class",
        "PatternSyntaxException",
        "Regex class",
        "https://www.w3schools.com/java/java_enums.asp"
        ],
       [
        "What is the output of following program code? \npublic static void main(String[] args){\ntry\n{int i;\nreturn;\n}\ncatch(Exception e)\n{\nSytem.out.println('in_catch_Block');\n}\nfinally\n{\nSystem.out.println('in_finally block');\n}\n}",
        "in_Catch_Block",
        "in_Catch_bock in_finally_block",
        "in_finally_block",
        "The program will return without printing anything",
        "https://www.w3schools.com/java/java_abstract.asp"
        ],
       [
        "What will be the output of the following program code?\npublic class Test Runnable{\n public static void main(String[] args){\n  Thread t= new Thread(this);\n  t.start();\n}\n\npublic void run(){\n   System.out.println('test');\n   }\n}",
        "The program does not compile because this cannot be referenced in a static method",
        "The program compiles fine, but it does not print anything because t does not invoke the run() method",
        "The program compiles and runs fine and displays test on the console",
        "None of the above",
        "https://www.w3schools.com/java/java_regex.asp"
        ]
       ]

    answer=[
        "Widening Type Conversion",
        "Endless loop",
        "0",
        "Two-dimensional Sequence",
        "Enumerated type and Structure",
        "extends",
        "All the above",
        "getEnumConstants()",
        "Regex class",
        "in_finally_Block",
        "The program does not compile because this cannot be referenced in a static method."
        ]
    
    global li
    li = ['',0,1,2,3,4,5,6,7,8,9]
    x = random.choice(li[1:])

    
    ques = Label(JAVA_frame,text =JAVAQ[x][0],font="calibri 12",bg="white")
    ques.place(relx=0.5,rely=0.2,anchor=CENTER)

    var = StringVar()
    
    a = Radiobutton(JAVA_frame,text=JAVAQ[x][1],font="calibri 10",value=JAVAQ[x][1],variable = var,bg="white")
    a.place(relx=0.5,rely=0.42,anchor=CENTER)

    b = Radiobutton(JAVA_frame,text=JAVAQ[x][2],font="calibri 10",value=JAVAQ[x][2],variable = var,bg="white")
    b.place(relx=0.5,rely=0.52,anchor=CENTER)

    c = Radiobutton(JAVA_frame,text=JAVAQ[x][3],font="calibri 10",value=JAVAQ[x][3],variable = var,bg="white")
    c.place(relx=0.5,rely=0.62,anchor=CENTER) 

    d = Radiobutton(JAVA_frame,text=JAVAQ[x][4],font="calibri 10",value=JAVAQ[x][4],variable = var,bg="white")
    d.place(relx=0.5,rely=0.72,anchor=CENTER) 
    
    li.remove(x)
    
    timer = Label(h)
    timer.place(relx=0.8,rely=0.82,anchor=CENTER)
    
    
    
    def display():
        
        if len(li) == 1:
                h.destroy()
                wrong3()
        if len(li) == 2:
            nextQuestion.configure(text='End',command=calc)
                
        if li:
            x = random.choice(li[1:])
            ques.configure(text =JAVAQ[x][0])
            
            a.configure(text=JAVAQ[x][1],value=JAVAQ[x][1])
      
            b.configure(text=JAVAQ[x][2],value=JAVAQ[x][2])
      
            c.configure(text=JAVAQ[x][3],value=JAVAQ[x][3])
      
            d.configure(text=JAVAQ[x][4],value=JAVAQ[x][4])
            
            li.remove(x)
            print(li)
            y = countDown()
            if y == -1:
                display()

            
    def calc():
        if (var.get() not in answer):
            wrong3()
    
    submit = Button(JAVA_frame,command=calc,text="Submit")
    submit.place(relx=0.5,rely=0.82,anchor=CENTER)
    
    nextQuestion = Button(JAVA_frame,command=display,text="Next")
    nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER)
    
    y = countDown()
    if y == -1:
        display()
    h.mainloop()
    
def PYTHON():
        
           
        global p
        p = Tk()
        
        PYTHON_canvas = Canvas(p,width=1000,height=1000,bg="#101357")
        PYTHON_canvas.pack()

        PYTHON_frame = Frame(PYTHON_canvas,bg="white")
        PYTHON_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

        
        def countDown():
            check = 0
            for k in range(20, 0, -1):
                
                if k == 1:
                    check=-1
                timer.configure(text=k)
                PYTHON_frame.update()
                time.sleep(1)
                
            timer.configure(text="Times up!")
            if check==-1:
                return (-1)
            else:
                return 0
            
        global score
        score = 0
        
        global PYTHONQ
        
        PYTHONQ = [
                    [
                      "Predict the output of the following code\ncodes = [1, 2, 3, 4] \ncodes.append([5,6,7,8]) \nprint(codes)",
                      "[1,2,3,4,5,6,7,8]",
                      "[1,2,3,4]",
                      "[1,2,3,4,[5,6,7,8]]",
                      "[1,2,3,4][5,6,7,8]",
                      "https://www.w3schools.com/python/python_lists_join.asp"

                 ],
        [
           " What is the out put of following code \nT = 'geeks'\na, b, c, d, e = T \nb = c = '*'\nT = (a, b, c, d, e) \nprint(T) ",
            "(‘g’, ‘*’, ‘*’, ‘k’, ‘s’)",
            "(‘g’, ‘e’, ‘e’, ‘k’, ‘s’)",
            "(‘geeks’,‘*’,‘*’)",
            "Key Error",
            "https://www.w3schools.com/python/python_tuples_update.asp"


        ],
        [
         "Which of the following is a Python tuple?",
            "[1, 2, 3]",
            "(1, 2, 3)",
            "{1, 2, 3}",
            "{}"   ,
            "https://www.w3schools.com/python/python_casting.asp"
        ],
        [
            "Which function overloads the >> operator?",
            "more()",
            "gt()",
            " ge()",
            "None of the above",
            "https://www.w3schools.com/python/python_operators.asp"

        ],
        [
            "What will be the output of print(math.factorial(4.5))?",
            "24",
            "120",
            "error",
            "24.0",
            "https://www.w3schools.com/python/python_for_loops.asp"
        ] ,
        [
                 " What is the output of the following program?\nT = (2e-04, True, False, 8, 1.001, True)\nval = 0\nfor x in T:\n\tval += int(x)\n\tprint(val)",

                        "12",

                        "11",

                        "11.001199999999999",

                        "TypeError",
                        "https://www.w3schools.com/python/python_regex.asp"

                  ],
              [
                  "Which of the following creates a pattern object?",
                  "re.create(str)",
                  "re.regex(str)",
                  "re.compile(str)",
                  "re.assemble(str)",
                  "https://www.w3schools.com/python/python_file_handling.asp"

                  ],
              
              [
                 " If you are having trouble remembering what methods the regex library contains, which command can you use to find said methods?",
                 "help()",
                 "dir(regex)",
                 "dir(re)",
                 "import re",
                 "https://www.w3schools.com/python/python_file_write.asp"


                  
                  ],
              
              [
                 " Select the correct mode to open a file for appending as well as reading?",
                  "a+",
                  "ar",
                  "rw",
                  "ar+",
                  "https://www.w3schools.com/python/python_modules.asp"

                  
                  ],
              
              [
                 " Select the correct method to write a list of lines to a file?",
                 "write(list)",
                 "writelines(list)",
                 "writelist(list)",
                 "writelines(lines)",
                 "https://www.w3schools.com/python/python_try_except.asp"
                  
                  ]
    ]
        answer = [
                "[1,2,3,4,[5,6,7,8]]",
                "(‘g’, ‘*’, ‘*’, ‘k’, ‘s’)",
                "(1, 2, 3)",
                "None of the above",
                "error",
                "11",
                "re.compile(str)",
                "dir(re)",
                "a+",
                "writelines(list)"
                
                ]
        
        global li
        li = ['',0,1,2,3,4,5,6,7,8,9]
        x = random.choice(li[1:])
        
        
        ques = Label(PYTHON_frame,text =PYTHONQ[x][0],font="calibri 12",bg="white")
        ques.place(relx=0.5,rely=0.2,anchor=CENTER)

        var = StringVar()
        
        a = Radiobutton(PYTHON_frame,text=PYTHONQ[x][1],font="calibri 10",value=PYTHONQ[x][1],variable = var,bg="white")
        a.place(relx=0.5,rely=0.42,anchor=CENTER)

        b = Radiobutton(PYTHON_frame,text=PYTHONQ[x][2],font="calibri 10",value=PYTHONQ[x][2],variable = var,bg="white")
        b.place(relx=0.5,rely=0.52,anchor=CENTER)

        c = Radiobutton(PYTHON_frame,text=PYTHONQ[x][3],font="calibri 10",value=PYTHONQ[x][3],variable = var,bg="white")
        c.place(relx=0.5,rely=0.62,anchor=CENTER) 

        d = Radiobutton(PYTHON_frame,text=PYTHONQ[x][4],font="calibri 10",value=PYTHONQ[x][4],variable = var,bg="white")
        d.place(relx=0.5,rely=0.72,anchor=CENTER) 
        
        li.remove(x)
        
        timer = Label(p)
        timer.place(relx=0.8,rely=0.82,anchor=CENTER)
        
        
        
        def display():
            
            if len(li) == 1:
                    p.destroy()
                    wrong4()
            if len(li) == 2:
                nextQuestion.configure(text='End',command=calc)
                    
            if li:
                x = random.choice(li[1:])
                ques.configure(text =PYTHONQ[x][0])
                
                a.configure(text=PYTHONQ[x][1],value=PYTHONQ[x][1])
          
                b.configure(text=PYTHONQ[x][2],value=PYTHONQ[x][2])
          
                c.configure(text=PYTHONQ[x][3],value=PYTHONQ[x][3])
          
                d.configure(text=PYTHONQ[x][4],value=PYTHONQ[x][4])
                
                li.remove(x)
                print(li)
                y = countDown()
                if y == -1:
                    display()

                
        def calc():
            if (var.get() not in answer):
                wrong4()
        
        submit = Button(PYTHON_frame,command=calc,text="Submit")
        submit.place(relx=0.5,rely=0.82,anchor=CENTER)
        
        nextQuestion = Button(PYTHON_frame,command=display,text="Next")
        nextQuestion.place(relx=0.87,rely=0.82,anchor=CENTER)
        
        y = countDown()
        if y == -1:
            display()
        p.mainloop()

def wrong1():
    global wr1
    wr1 = Tk()
    
    wrong_canvas = Canvas(wr1,width=500,height=250,bg="#101357")
    wrong_canvas.pack()

    wrong_frame = Frame(wrong_canvas,bg="white")
    wrong_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
    
    st = "You have selected wrong option !!\n Use the Below link "
    mlabel = Label(wrong_canvas,text=st,fg="black")
    mlabel.place(relx=0.5,rely=0.2,anchor=CENTER)
    
    global no1
    no1=random.choice(li[1:])
    
    print(no1)
    mlabel = Label(wrong_canvas,text=cQ[no1][5],fg="black")
    mlabel.place(relx=0.5,rely=0.3,anchor=CENTER)
    global link1
    webbrowser.open(cQ[no1][5])
    li.remove(no1)
    wr1.mainloop()
    
def wrong2():
        global wr2
        wr2 = Tk()
        
        wrong_canvas = Canvas(wr2,width=500,height=250,bg="#101357")
        wrong_canvas.pack()

        wrong_frame = Frame(wrong_canvas,bg="white")
        wrong_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
        
        st = "You have selected wrong option !!\n Use the Below link "
        mlabel = Label(wrong_canvas,text=st,fg="black")
        mlabel.place(relx=0.5,rely=0.2,anchor=CENTER)
        
        global no2
        no2=random.choice(li[1:])
        
        print(no2)
        mlabel = Label(wrong_canvas,text=cppQ[no2][5],fg="black")
        mlabel.place(relx=0.5,rely=0.3,anchor=CENTER)
        global link2
        webbrowser.open(cppQ[no2][5])
        li.remove(no2)
        wr2.mainloop()

def wrong3():
        global wr3
        wr3 = Tk()
        
        wrong_canvas = Canvas(wr3,width=500,height=250,bg="#101357")
        wrong_canvas.pack()

        wrong_frame = Frame(wrong_canvas,bg="white")
        wrong_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
        
        st = "You have selected wrong option !!\n Use the Below link "
        mlabel = Label(wrong_canvas,text=st,fg="black")
        mlabel.place(relx=0.5,rely=0.2,anchor=CENTER)
        
        global no3
        no3=random.choice(li[1:])
        
        print(no3)
        mlabel = Label(wrong_canvas,text=JAVAQ[no3][5],fg="black")
        mlabel.place(relx=0.5,rely=0.3,anchor=CENTER)
        global link3
        webbrowser.open(JAVAQ[no3][5])
        li.remove(no3)
        wr3.mainloop()
        
def wrong4():
                global wr4
                wr4 = Tk()
                
                wrong_canvas = Canvas(wr4,width=500,height=250,bg="#101357")
                wrong_canvas.pack()

                wrong_frame = Frame(wrong_canvas,bg="white")
                wrong_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
                
                st = "You have selected wrong option !!\n Use the Below link "
                mlabel = Label(wrong_canvas,text=st,fg="black")
                mlabel.place(relx=0.5,rely=0.2,anchor=CENTER)
                
                global no4
                no4=random.choice(li[1:])
                
                print(no4)
                mlabel = Label(wrong_canvas,text=PYTHONQ[no4][5],fg="black")
                mlabel.place(relx=0.5,rely=0.3,anchor=CENTER)
                global link4
                webbrowser.open(PYTHONQ[no4][5])
                li.remove(no4)
                wr2.mainloop()


def showMark(score):
    global sh
    sh = Tk()
    
    show_canvas = Canvas(sh,width=1000,height=1000,bg="#101357")
    show_canvas.pack()

    show_frame = Frame(show_canvas,bg="white")
    show_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
    
    st = "Your score is "+str(mark)
    mlabel = Label(show_canvas,text=st,fg="black")
    mlabel.place(relx=0.5,rely=0.2,anchor=CENTER)
    
    
    
    sh.mainloop()
def start():
    global root 
    root = Tk()
    canvas = Canvas(root,width = 720,height = 440)
    canvas.grid(column = 0 , row = 1)
    

    button = Button(root, text='Start',command = signUpPage) 
    button.configure(width = 102,height=2, activebackground = "#33B5E5", bg ='green', relief = RAISED)
    button.grid(column = 0 , row = 2)

    root.mainloop()
    
    
if _name=='__main_':
    start()
final.py
