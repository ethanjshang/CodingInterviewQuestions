# Take a list of strings, serialize them into a singleString then deserialize back into a list of Strings
# INPUT: List of strings
# OUTPUT: SAME list of strings
# Goal: Serialize list of strings into a single string then deserialize back into a list of strings



# serialize ([Ethan6, 22Foo, -Shang, "", "--", null, "100", "101"]) => result-string
# "Ethan66-Shang-100-101"
# "6--Shang5-22Foo
# "6-Ethan65-22Foo6--Shang0-n-"
# 
# 
# 
# deserialize (result-string) => [Ethan, Shang, "", null]
# ["Ethan", "Shang", "100", "101"]
# //iterate through the list and replace sentinel values
# 
# //Ethan-Shang-"sentinel value for """-"sentinel value for null"
# 
# String serialize(List<String> input) {
#   if (input.empty) {
#     return ""
#   }
#   
#   for (String str : input) {
#     
#   }
#   
# } 
# 
# List<String> deserialize(String input) { … }
# 


def serialize(lst):
    returnStr = ""
    for item in lst:
        if item is None:
            returnStr += "n"   
            returnStr += "-"

        else:
            returnStr += str(len(item))
            returnStr += "-"
            returnStr += item
    return returnStr
    
def deserialize(serStr):    
    
    returnLst = []
    i = 0
    #Turns out i doesn't get modified during for loop
    while i < len(serStr):
        lenSubStringStr = ""
        lenSubString = 0
        subString = ""
        null = False
        
        #Get the length of the subString in string form
        #i will be at the delimiter (one char before the string we want)
        while serStr[i] != "-":
            lenSubStringStr += serStr[i]
            i += 1
        #Cast the length of the SubString to an int if it's not null
        if lenSubStringStr == "n":
            null = True
        else:
            lenSubString = int(lenSubStringStr)
        i += 1 #Must move the index to character after delim
        if (not null):
            for j in range(lenSubString):
                subString += serStr[i]
                i += 1
            returnLst.append(subString)
        else:
            returnLst.append(None)
            
    return returnLst
            
            
            
lst_basic = ["Ethan", "Shang", "100", "101"]    
print("Before: ", lst_basic)
serialized_basic = serialize(lst_basic)
print("Serialized: ", serialized_basic)
print("Deserialized:", deserialize(serialized_basic), "\n")

list_None_Delimiter_MoreThan10_Empty = [None, "-Ethan-", "0123456789", "", "222", "222", "n"] 
print(list_None_Delimiter_MoreThan10_Empty)
serialized_None_Delimiter_MoreThan10_Empty = serialize(list_None_Delimiter_MoreThan10_Empty)
print(serialized_None_Delimiter_MoreThan10_Empty)
print(deserialize(serialized_None_Delimiter_MoreThan10_Empty))
        
            
    
    
    
    