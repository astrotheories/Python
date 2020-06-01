import base64

with open("importantes.txt", "rb") as importantissimo:
    ler = importantissimo.read()
    creep = base64.b64encode(ler)
    desb = creep.decode("utf-8")
    
with open("importantes.txt", "w") as replacement:
   replacement.write(desb)