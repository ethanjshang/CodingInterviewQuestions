/*
"10 + 2 * 6"            ---> 22
10 + 12
22

"100 * 2 + 12"          ---> 212


"100 * ( 2 + 12)"      ---> 1400 

"100 * ( 2 + 12 * 3)"      ---> 1400 

.split(" ")


["10", "+", "2", "*", "6"]

PE . MD . AS

md = ["*", "/"]

if char in md:

if char in as:



100 * 2 + 12

"10 + 2 * 6"            ---> 22

values stack: 10 2
operator stack: + 
*/

public int calc(String input) {
    String[] tokens = input.split(" ");
    Stack values = new Stack();
    Stack operators = new Stack();
    Map op_val = new HashMap();
    op_val.put("*", 2);
    op_val.put("/", 2);
    op_val.put("+", 1);
    op_val.put("-", 1);
    
    

for (token : tokens) {
    if (token is a number){
        values.push(token)    
    } else {
        if hasHigherPrecedence(token, operators.peek()) {
	        int RHS_num = values.pop
	        int LHS_num = values.pop
	        String op = operators.pop
            values.push(Apply(num, num, op))
            operators.push(token)

        }
    }
}


public int hasHigherPrecedence(String op1, String op2){
    return op_val.get(op1) > op_val.get(op2);
}


