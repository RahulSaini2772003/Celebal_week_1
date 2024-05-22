def up_pattern(n):
    """This is Progam to print Upper tringle Patterns on the basis of Input no."""
    try:
        n = int(n)
        print("Here are the Demanded Pattern of Upper Tringle",end="\n")
        for i in range(n,0,-1):
            print("*"*(i))
    except ValueError:
        print("Enter a valid integer Input")
    except Exception as e:
        print("Error Occured",e)
            
if __name__ == "__main__":    
    N = input("Enter the no. of Row: ")
    up_pattern(N)