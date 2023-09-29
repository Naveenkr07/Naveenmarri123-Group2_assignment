"""
Title           : Fermat’s Last Theorem Near Misses
File            : relativemiss.py
Programmer      : Naveen Kumar Marri  
                  Vyshnavi Duppekar
Email           : naveenkumarmarri@lewisu.edu
                  vyshnaviduppekar@lewisu.edu
Course Number   : CPSC 60500
Section Number  : 2
Date            : 23-09-2023
Explanation     : This provided Python program is to find Fermat's last theorem which is a famous mathematical conjecture that has no three positive integers a, b, and c which satisfy the equation a^n +b^n =c^n for any integer value of n greater than 2

"""

#Calculate the relative miss
def calculate_miss(x, y, z, n):
    result = (x ** n) + (y ** n)
    z = z ** n
    nextZ = (z + 1) ** n

    miss = abs(result - z)
    relativeMiss = miss / result
    return relativeMiss

#Main function
def main():
    #print welcome message
    print("\nFermat's Last Theorem Near Misses\n")  
    
    #Get input from User
    n = int(input("Enter the value of n (2 < n < 12): "))
    k = int(input("\nEnter the value of k (k > 10): "))

    minimumRelativeMissValues = float('inf')
    minX,minY=0,0;
    
    # Check if input values are valid or not
    if 2 < n < 12 and k > 10:
        for x in range(10, k + 1):
            for y in range(10, k + 1):
                for z in range(1, k + 1):
                    if x != y:  
                        relativeMiss = calculate_miss(x, y, z, n)
                        
                        if relativeMiss < minimumRelativeMissValues:
                            minimumRelativeMissValues = relativeMiss
                            minX = x
                            minY = y
    
        #Print Result
        print("\nRelative miss:")
        print(f"x = {minX}, y = {minY}")
        print(f"Relative diff = {minimumRelativeMissValues:.7f}")
    else:
        #Print Invalid input
        print("Invalid input. Please make sure n is (2 < n < 12), and k > 10")

if __name__ == "__main__":
    main()
    input("\nPress Enter to exit...")
