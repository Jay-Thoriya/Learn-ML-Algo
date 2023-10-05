

def Least_common_multiple(num1,num2):
    maxNum = max(num1,num2)
    while(True):
        if(maxNum % num1 == 0 and maxNum % num2 == 0):
            break
        maxNum += 1
    return maxNum


def  Highest_common_factor(num1 , num2):
    minMum = num2 > num1 and num1 or num2
    print("min ", minMum)
    for i in range(1, minMum+1):
        if num1 % i == 0 and num2 % i == 0:
            hcf = i
    return hcf


def main():
    num1 = int(input("Enter First Number : "))
    num2 = int(input("\nEnter Second Number : "))
    operation = int(input("\nEnter 1 to Find LCM & 2 to Find HCF : ")) 

    if( operation == 1): print( f"\nThe LCM of {num1} and {num2} is : {Least_common_multiple(num1,num2)}")
    else : print( f"\nThe HCF of {num1} and {num2} is : {Highest_common_factor(num1,num2)} ")

if __name__=="__main__":
    main()