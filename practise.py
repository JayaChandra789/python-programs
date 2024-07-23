def data_analyze(s):
    capitals=sum(1 for c in s if c.isupper())
    lowers=sum(1 for c in s if c.islower())
    digits=sum(1 for c in s if c.isdigit())
    word=len(s.split())
    return capitals,lowers,digits,word
s=input("Enter any name number with spaces:")
capitals,lowers,digits,words=data_analyze(s)
print(f"capitals:{capitals},lowers={lowers},digits={digits},words={words}")
    
