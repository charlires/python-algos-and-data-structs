class Person:
    def __init__(self, name: str, know: list[str]):
        self.name = name
        self.know = know

def findCelebrity(persons: list[Person]) -> str:
    m = {}
    for p in persons:
        for k in p.know:
            if k in m:
                m[k] += 1
            else:
                m[k] = 1
    
    for p in persons:
        if len(p.know) == 0 and p.name in m and m[p.name] == len(persons) -1:
            return p.name
    return ""

persons = [
    Person("juan", ["mary"]),
    Person("carlos", ["jose", "mary"]),
    Person("jose", ["mary"]),
    Person("mary", []),
]
print(findCelebrity(persons))