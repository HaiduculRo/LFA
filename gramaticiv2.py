def verifGramatici(gramatica, start, cuv):
    if len(cuv) == 0 and '@' in gramatica[start]:
        #conditie de final
        print("Cuvantul gasit este acceptat")
        return True

    for aux in gramatica[start]:
        if cuv and cuv[0] == aux[0] and aux[0].islower():
            if verifGramatici(gramatica, aux[1], cuv[1:]):
                return True

        elif aux[0].isupper():
            verifGramatici(gramatica, aux[0], aux[1] + cuv)
    return False

gramatica = {'S': [('a', 'A'), ('d', 'E')], 'A': [('a', 'B'), ('a', 'S')], 'B': [('b', 'C')],
           'C': [('b', 'D'), ('b', 'B')], 'D': [('c', 'D'), '@'], 'E': ['@']}
start = 'S'
string = "aab"
print(verifGramatici(gramatica, 'S', string))
