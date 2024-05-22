def low_pattern(n):
    """This is Progam to print lower tringle Patterns on the basis of Input no."""
    try:
        n = int(n)
        print("Here are the Demanded Pattern of Lower Trangle",end="\n")
        for i in range(n):
            print("*"*(i+1))
    except ValueError:
        print("Enter a valid integer Input")
    except Exception as e:
        print("Error Occured",e)
        
 
if __name__ == "__main__":     
    N = input("Enter the no. of Row: ")
    low_pattern(N)