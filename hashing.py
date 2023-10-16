class HashMap:
    def __init__(self, initial_size=10):
        # Inicialização do HashMap com um tamanho inicial
        self.size = initial_size
        # Inicialização do array para armazenar os dados
        self.map = [None] * self.size
        # Limite de fator de carga para acionar o redimensionamento
        self.threshold = 0.7

    def _hash(self, key):
        # Função hash simples para obter o índice com base na chave
        return hash(key) % self.size

    def _resize(self):
        # Redimensionamento da tabela hash para um tamanho maior (número primo próximo ao dobro)
        new_size = self.size * 2
        while not self._is_prime(new_size):
            new_size += 1

        # Criação de uma nova tabela hash
        new_map = [None] * new_size
        # Rehashing de todos os elementos da tabela anterior para a nova tabela
        for bucket in self.map:
            if bucket:
                for key, value in bucket:
                    new_index = hash(key) % new_size
                    if new_map[new_index] is None:
                        new_map[new_index] = []
                    new_map[new_index].append((key, value))

        # Atualização da tabela hash e do tamanho
        self.map = new_map
        self.size = new_size

    def _is_prime(self, n):
        # Verifica se um número é primo
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def insert(self, category, event_name, event_description):
        # Inserção de um novo evento na tabela hash
        if self.load_factor() > self.threshold:
            # Redimensionamento se o fator de carga exceder o limite
            self._resize()

        # Cálculo do índice usando a categoria como chave
        index = self._hash(category)
        # Criação de uma nova lista se o índice estiver vazio
        if self.map[index] is None:
            self.map[index] = []
        # Adição do evento à lista correspondente à categoria
        self.map[index].append((category, event_name, event_description))

    def remove(self, category, event_name):
        # Remoção de um evento da tabela hash
        index = self._hash(category)
        # Verificação se o índice não está vazio
        if self.map[index] is not None:
            # Iteração sobre a lista para encontrar o evento
            for i, (cat, name, desc) in enumerate(self.map[index]):
                if cat == category and name == event_name:
                    # Remoção do evento
                    del self.map[index][i]
                    break

    def search_category(self, category):
        # Busca de eventos por categoria
        index = self._hash(category)
        events = []
        # Verificação se o índice não está vazio
        if self.map[index] is not None:
            # Iteração sobre a lista para encontrar eventos da categoria
            for cat, name, desc in self.map[index]:
                if cat == category:
                    events.append((name, desc))
        return events

    def list_categories(self):
        # Listagem de todas as categorias disponíveis
        categories = []
        for entry in self.map:
            if entry is not None:
                for cat, _, _ in entry:
                    if cat not in categories:
                        categories.append(cat)
        return categories

    def list_all_events(self):
        # Listagem de todos os eventos
        all_events = []
        for entry in self.map:
            if entry is not None:
                all_events.extend(entry)
        return all_events

    def load_factor(self):
        # Cálculo do fator de carga
        used_buckets = sum(1 for bucket in self.map if bucket is not None)
        return used_buckets / self.size


def listar_categorias(hash_map):
    # Função auxiliar para listar todas as categorias
    categories = hash_map.list_categories()
    if not categories:
        print("Nenhuma categoria cadastrada.")
    else:
        print(f"Todas as categorias: {categories}")


def listar_eventos_na_categoria(hash_map, category):
    # Função auxiliar para listar eventos em uma categoria
    events = hash_map.search_category(category)
    if not events:
        print(f"Nenhum evento encontrado na categoria '{category}'.")
    else:
        print(f"Eventos na categoria '{category}':")
        for event in events:
            print(f"Nome do Evento: '{event[0]}'; Descrição: '{event[1]}'")


def buscar_eventos_por_categoria(hash_map):
    # Função para buscar eventos por categoria
    categories = hash_map.list_categories()
    if not categories:
        print("Nenhuma categoria cadastrada. Retornando ao menu principal.")
        return

    listar_categorias(hash_map)
    category = input("Digite a categoria para buscar eventos: ")
    if category not in hash_map.list_categories():
        print(f"A categoria '{category}' não existe.")
        return

    events = hash_map.search_category(category)
    if not events:
        print(f"Nhum evento encontrado na categoria '{category}'.")
    else:
        print(f"Eventos na categoria '{category}':")
        for event in events:
            print(f"Nome do Evento: '{event[0]}'; Descrição: '{event[1]}'")


def remover_evento(hash_map):
    # Função para remover um evento
    categories = hash_map.list_categories()
    if not categories:
        print("Nenhuma categoria cadastrada. Retornando ao menu principal.")
        return

    listar_categorias(hash_map)
    category = input("Digite a categoria do evento a ser removido: ")
    if category not in hash_map.list_categories():
        print(f"A categoria '{category}' não existe.")
        return

    listar_eventos_na_categoria(hash_map, category)
    event_name = input("Digite o nome do evento a ser removido: ")
    if event_name not in [event[0] for event in hash_map.search_category(category)]:
        print(f"O evento '{event_name}' não existe na categoria '{category}'.")
        return

    hash_map.remove(category, event_name)
    print("Evento removido com sucesso!")


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

        if choice == "1":
            # Opção para adicionar um evento
            category = input("Digite a categoria do evento: ")
            event_name = input("Digite o nome do evento: ")
            event_description = input("Digite a descrição do evento: ")
            hash_map.insert(category, event_name, event_description)
            print("Evento adicionado com sucesso!")

        elif choice == "2":
            # Opção para remover um evento
            remover_evento(hash_map)

        elif choice == "3":
            # Opção para buscar eventos por categoria
            buscar_eventos_por_categoria(hash_map)

        elif choice == "4":
            # Opção para listar todos os eventos
            all_events = hash_map.list_all_events()
            if not all_events:
                print("Nenhum evento cadastrado.")
            else:
                print("Todos os eventos:")
                for event in all_events:
                    print(f"Categoria: '{event[0]}'; Nome do Evento: '{event[1]}'; Descrição: '{event[2]}'")

        elif choice == "5":
            # Opção para listar todas as categorias
            listar_categorias(hash_map)

        elif choice == "0":
            # Opção para sair do programa
            print("Saindo do programa. Até mais!")
            break

        else:
            # Mensagem de opção inválida
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
