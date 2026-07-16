def fold_pattern(n):
    if n == 1:
        return "V"  #base case
    prev = fold_pattern(n - 1) 
    return prev + "V" +  flip_reverse(prev)  
    


def flip_reverse(s):
    flipped = "".join("V" if ch == "M" else "M" for ch in s)  
    return flipped[::-1]  #reverses the order
    


def get_crease(n, x):
    seq = fold_pattern(n)         
    letter = seq[x - 1]        

    if letter == "V":
        return "Valley"
    else:
        return "Mountain"
    
 
    
if __name__ == "__main__":    
    print(get_crease(1, 1))
    print(get_crease(3, 6))
    print(get_crease(5, 16))
    print(get_crease(8, 255))