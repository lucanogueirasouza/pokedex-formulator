pokedex = [] #lista dos pokemons
while True: 
    print ("----Pokedex----")
    escolha = int(input("1 - Add Pokemon\n2 - Ver Todos\n3 - Filtrar Elementos\n4 - Sair\nDigite: "))
    if escolha == 1: 
        pokemon = str(input("Digite o nome do Pokemon: ")).capitalize()
        elemento = str(input("Digite o Elemento: ")).capitalize()
        pokedex.append({"Pokemon": pokemon , "Elemento": elemento}) #dicionario
        print(f"{pokemon} Adicionado!")
    if escolha == 2: 
        print (pokedex)       
    if escolha == 3: 
        elementoescolha = str(input("Digite o elemento para elemento para filtar: ")).capitalize()
        filtrados = [p for p in pokedex if p["Elemento"] == elementoescolha]  # filtragem
        if filtrados:
            print(f"Pokémon com elemento: {elementoescolha}")
            for p in filtrados:
                print (f"Pokémon com o elemento escolhido: {[pokemon]}")
        else:
            print("Não existe pokémons com este elemento.") 
    elif escolha == 4: 
        print ("Saindo...")
        break  
    elif escolha > 4:
        print ("Opção Inválida!") 
