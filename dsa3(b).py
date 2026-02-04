# Postfix Expression Evaluation using Stack 
 
stack = [] 
 
expr = raw_input("Enter postfix expression (Example: 23+): ") 
 
for ch in expr: 
    if ch.isdigit(): 
        stack.append(int(ch)) 
    else: 
        operand2 = stack.pop() 
        operand1 = stack.pop() 
 
        if ch == '+': 
            stack.append(operand1 + operand2) 
        elif ch == '-': 
            stack.append(operand1 - operand2) 
        elif ch == '*': 
            stack.append(operand1 * operand2) 
        elif ch == '/': 
            stack.append(operand1 / operand2) 
 
result = stack.pop() 
print "Result of the postfix expression is:", result 
