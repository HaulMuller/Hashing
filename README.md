# Hashing

## Objetivo
Criar um sistema que permita o gerenciamento de eventos organizados por categorias, utilizando uma estrutura de hash map para otimizar a busca e recuperação dos eventos.

## Requisitos Funcionais
1. Inserir Evento: O usuário pode inserir um novo evento, especificando a categoria do evento, o nome do evento e sua descrição.
2. Remover Evento: O usuário pode remover um evento existente, informando a categoria e o nome do evento.
3. Buscar Eventos por Categoria: O usuário pode visualizar todos os eventos de uma determinada categoria.
4. Listar Todas as Categorias: O usuário pode listar todas as categorias de eventos disponíveis.

## Implementação

1. Hash Map para Armazenamento: Implemente uma tabela hash onde a chave será a categoria do evento e o valor será uma lista de eventos para essa categoria.
2. Operações de Inserção e Remoção: Para inserção, calcule o hash da categoria e insira o evento na lista correspondente.
3. Para remoção, encontre a categoria na tabela hash e remova o evento da lista.
4. Operação de Busca por Categoria: Calcule o hash da categoria e acesse a lista correspondente para obter todos os eventos relacionados àquela categoria.
5. Operação de Listagem de Categorias: Percorra a tabela hash e liste todas as categorias disponíveis.
6. Redimensionamento da tabela hash: quando o fator de carga da tabela hash hash estiver entre 0,7 e 0,8, realize o redimensionamento da tabela que envolve aumentar o tamanho da tabela hash para um novo tamanho apropriado ( número primo próximo ao dobro do tamanho original) e todos os elementos precisam ser rehashing e inseridos na nova tabela.

## Restrições

1. O programa deve ser implementado em Python e deve utilizar uma estrutura de dados HashMap.
2. Construa sua implementação do TAD HashMap ou adapte a implementação apresentada em sala de aula. Não utilize algo pronto da linguagem ou disponível da web.

## Integrantes
* [Ian Jairo T. Gonzales](github.com/IanJairo)
* [João Gabriel S. Dantas](github.com/gabrielDantas10)
* [Haul Muller](https://github.com/HaulMuller)

## Comentários sobre a solução
* ### Aprendizado Constante

Durante o desenvolvimento do Sistema de Gerenciamento de Eventos com HashMap, houve um aprendizado constante sobre como implementar uma estrutura de hash map eficiente, bem como entender como organizar eventos por categorias.

* ### Satisfação na Resolução de Problemas

O projeto de Sistema de Gerenciamento de Eventos apresentou desafios interessantes, como a criação de uma estrutura de hash map, a implementação das operações de inserção, remoção e busca, e a gestão das categorias de eventos. Superar esses desafios trouxe uma sensação de satisfação.

* ### Testando e Depurando
Assim como em qualquer desenvolvimento de software, o projeto exigiu testes e depuração para garantir que as operações de inserção, remoção, busca e redimensionamento funcionassem corretamente. Encontrar e corrigir erros foi fundamental para a qualidade do sistema.

* ### A Diversão da Programação

O objetivo do Sistema de Gerenciamento de Eventos é fornecer uma solução eficiente e útil, e o desenvolvimento do projeto também foi uma experiência divertida. A criação de uma solução que pode facilitar a organização de eventos e o acesso a informações sobre eles é uma recompensa por si só.

# Relatório Técnico: Implementação do Sistema de Gerenciamento de Eventos com HashMap em Python

## Introdução

Este relatório técnico descreve a estrutura de hash map utilizada na implementação do Sistema de Gerenciamento de Eventos em Python. O sistema tem como objetivo organizar e gerenciar eventos em diferentes categorias, utilizando uma estrutura de hash map para otimizar a busca e recuperação de informações sobre os eventos.

## Classe HashMap

A classe HashMap é a base da implementação e fornece métodos para criar, redimensionar e gerenciar a tabela hash. Aqui estão os principais aspectos da implementação:

- Construtor e Inicialização: O construtor permite que o usuário especifique um tamanho inicial para o HashMap. Ele inicializa o tamanho, a tabela hash e um limite de fator de carga.

- Função Hash: A função _hash é responsável por calcular o índice com base na chave usando uma função de hash simples.

- Redimensionamento: A função _resize redimensiona a tabela hash para um tamanho maior quando o fator de carga excede um limite. Ela também garante que o novo tamanho seja um número primo.

- Métodos de Inserção e Remoção: insert permite adicionar eventos ao HashMap. Se o fator de carga for excedido, a tabela é redimensionada. remove permite remover eventos com base na categoria e nome.

- Métodos de Busca: search_category permite buscar eventos por categoria, e list_categories lista todas as categorias disponíveis. list_all_events lista todos os eventos.

- Fator de Carga: A função load_factor calcula o fator de carga, o que ajuda a determinar quando redimensionar a tabela.

## Funções Auxiliares

Há também funções auxiliares que auxiliam na interação com o HashMap:

- listar_categorias: Lista todas as categorias disponíveis.
- listar_eventos_na_categoria: Lista eventos em uma categoria específica.
- buscar_eventos_por_categoria: Permite a busca de eventos por categoria.
- remover_evento: Permite a remoção de eventos.

## Implementação da Aplicação

A aplicação main.py é a interface de usuário que permite interagir com o HashMap. Aqui estão os principais aspectos da implementação:

1. Menu Interativo: O programa exibe um menu interativo com opções para adicionar eventos, remover eventos, buscar eventos por categoria, listar todos os eventos, listar todas as categorias e sair.

2. Adicionar e Remover Eventos: Os eventos podem ser adicionados fornecendo a categoria, nome e descrição do evento. Eles podem ser removidos especificando a categoria e nome do evento.

3. Listar Eventos e Categorias: As opções para listar eventos e categorias permitem visualizar os eventos registrados e as categorias disponíveis.

4. Saída do Programa: A opção "0" permite sair do programa.

## Conclusão

A implementação do HashMap e a aplicação em Python fornecem uma maneira eficiente de organizar e gerenciar eventos por categoria. A estrutura do código é modular, permitindo a adição de funcionalidades adicionais ou melhorias. Essa implementação pode ser útil em várias aplicações que envolvam a organização de dados por categorias, como calendários, sistemas de gerenciamento de eventos e muito mais.
