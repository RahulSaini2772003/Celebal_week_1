def pyr_pattern(n):
    """This is Progam to print Pyramid tringle Patterns on the basis of Input no."""
    try:
        n = int(n)
        print("Here are the Demanded Pattern of Pyramid Tringle",end="\n")
        for i in range(1,n+1):
            print(" "*(n-i)+"*"*(2*i-1))
    except ValueError:
        print("Enter a valid integer Input")
    except Exception as e:
        print("Error Occured",e)
        
        
if __name__ == "__main__":
    N = input("Enter the no. of Row: ")
    pyr_pattern(N)