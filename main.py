from hashing import *

def main():
    # Função principal
    hash_map = HashMap()

    while True:
        print("\nMenu:")
        print("1. Adicionar Evento")
        print("2. Remover Evento")
        print("3. Buscar Eventos por Categoria")
        print("4. Listar Todos os Eventos")
        print("5. Listar Todas as Categorias")
        print("0. Sair")

        choice = input("Escolha uma opção: ")

        # Opção para adicionar um evento
        if choice == "1":
            # Opção para adicionar um evento
            category = input("Digite a categoria do evento: ")
            event_name = input("Digite o nome do evento: ")
            event_description = input("Digite a descrição do evento: ")
            hash_map.insert(category, event_name, event_description)
            print("Evento adicionado com sucesso!")

        # Opção para remover um evento
        elif choice == "2":
            remover_evento(hash_map)

        # Opção para buscar eventos por categoria
        elif choice == "3":
            buscar_eventos_por_categoria(hash_map)

        # Opção para listar todos os eventos
        elif choice == "4":
            all_events = hash_map.list_all_events()
            if not all_events:
                print("Nenhum evento cadastrado.")
            else:
                print("Todos os eventos:")
                for event in all_events:
                    print(f"Categoria: '{event[0]}'; Nome do Evento: '{event[1]}'; Descrição: '{event[2]}'")

        # Opção para listar todas as categorias
        elif choice == "5":
            listar_categorias(hash_map)

        # Opção para sair do programa
        elif choice == "0":
            print("Saindo do programa. Até mais!")
            break

        else:
            # Mensagem de opção inválida
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
