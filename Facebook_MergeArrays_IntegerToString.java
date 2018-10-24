
/*Welcome to Facebook!

This is just a simple shared plaintext pad, with no execution capabilities.

When you know what language you'd like to use for your interview,
simply choose it from the dropdown in the top bar.

Enjoy your interview!
*/  
1. 
  
a = [1, 3, 4]

b = [2, 4, 5, _, _, _]

b = [2, 4, 5, 4, 4, 5]

a = [4,5,6]
b = [1,2,3]

// [2, 4 ,5, _, _, 5]
//Increment compare index for both arrays
public int[] mergeSortedArrays(int[] a, int lengthA, int[] b, int lengthB, int fullLengthB){
  
  int indA = lengthA - 1, indB = lengthB - 1, indC = fullLengthB - 1;
  
  while (indA >= 0 && indB >= 0) {
    if (a[indA] <  b[indB]){
      b[indC--] = b[indB--];
    } else {
      b[indC--] = a[indA--];
    }
  }
  
  
  while (indA >= 0){
    b[indC--] = a[indA--];
  }
  while (indB >= 0){
    b[indC--] = b[indB--];
  }

}


2. Integer value to English representation

12 -> "twelve"
123 -> "one hundred twenty three"
Input: Integer input
Output: String
  
String[] onesDigit = new String[]{"zero", "one", ...}
String[] teensDigit = new String[]{"", "eleven", "twelve", ...}
String[] tensDigit = new String[] {"","", "twenty", "thirty", ...}


String[] tensPower = new String[]{"hundred", "thousand"..."billion"}

String inputStr = String(input);


if (inputStr.length == 1){
  return onesDigit[inputStr - '0'];
}

int digitInd = 0;
int len = inputStr.length;
String result = "";
while (digitInd < len){
  if (len >= 3) {
    if (inputStr[x] - '0' != 0){
      result.append += oneDigit[num[x] - '0']
      result.append += tensPower[x];
    }
    
  }
  
  x++;
  if (input[x] - '0' != 0){
    //if one -> teens
      //grab the one's digit to determine which "teen"
    //else tensDigit and append it
      //increment x and get the ones digit
  }
  
}