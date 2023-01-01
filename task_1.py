def is_palindrome(text):
       x1 = text.replace(" ", "")
       x1 = x1.lower()
       x2 = x1[::-1]
       if x1==x2:
        return(True)
       else:
        return(False)
