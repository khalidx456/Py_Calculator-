# Normal Calculator Project
while True:
    print("Project : Py_Calculator ________ [by] Khalid_Saif" )
    print("github link_____( https://github.com/Khalidx456 )")
    print("_________________________________________________")
    print()
    n1 = int(input(">> Enter Your First Value => "))
    n2 = int(input(">> Enter Your Second Value => "))
    op = input(">> Enter Operator => ")
    #condition checking for Operators
    if op == "+":
        print("🔴 Final Output => ", n1+n2)
    elif op == "-":
        print("🔴 Final Output => ",n1-n2)    
    elif op == "*" or op == "×":
        print("🔴 Final Output => ", n1*n2)
    elif op == "/" or op == "÷":
        print("🔴 Final Output => ", n1/n2) 
    elif op == "**" or op ==  "××":
        print("🔴 Final Output => ", n1**n2) 
    elif op == "%":
        print("🔴 Final Output => ", n1/n2*100)    
    else :
        print("***___________Invalid Operation____________***")    