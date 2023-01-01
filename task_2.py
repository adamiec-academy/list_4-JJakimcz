
def my_split(text):
    s=[]
    s1=""
    
    for l in text:
        if l != " ":
            s1+=l
        elif s1 != "":
            s.append(s1)
            s1=""
    if s1!="":
        s.append(s1)
    
    return s
