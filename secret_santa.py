import random

def assignSantas(participants):
    santas = {}    
    receiversAssigned = set()
    giversAssigned = set()
    
    while len(participants) > len(giversAssigned):
        receiver = ""
        giver = ""
        ir = random.randint(0, len(participants) -1)
        while participants[ir] in receiversAssigned:
            ir = random.randint(0, len(participants) -1)
        receiver = participants[ir]
        
        ig = random.randint(0, len(participants) -1)
        while participants[ig] in giversAssigned or participants[ig] == receiver:
            ig = random.randint(0, len(participants) -1)
        giver = participants[ig]
        
        receiversAssigned.add(receiver)
        giversAssigned.add(giver)
        
        santas[giver] = receiver
        
    return santas

# santas = [
#   "Rodrigo",
#   "Mateo",
#   "Paola",
#   "Frank",
#   "Mary",
#   "Jimmy",
#   "Carlos"
# ]

# print(assignSantas(santas))

# santas = [
#   "Rodrigo",
#   "Mateo",
#   "Paola"
# ]

# print(assignSantas(santas))

# santas = [
#   "Rodrigo",
#   "Mateo"
# ]

# print(assignSantas(santas))