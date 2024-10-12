from baseGraph import baseGraph
import random

class weightedGraph(baseGraph):
    def add_edge(self, u, v, w):
        """ Додає зважене ребро (u <--w--> v). """
        if u in self.graph and v in self.graph:
            # Перевірка, чи вже існує ребро
            if not any(x[0] == v for x in self.graph[u]) and u != v:
                self.graph[u].append((v, w))
                self.graph[v].append((u, w))
            else:
                print(f"Ребро між {u} і {v} вже існує або це петля.")
        else:
            print(f"Одна з вершин {u} або {v} не існує.")
    
    def del_edge(self, u, v):
        """ Видаляє зважене ребро (u <--w--> v). """
        if u in self.graph and v in self.graph:
            # Перевірка, чи існує ребро перед видаленням
            if any(x[0] == v for x in self.graph[u]):
                # Видаляємо ребро (u -> v)
                self.graph[u] = [x for x in self.graph[u] if x[0] != v]
                # Видаляємо ребро (v -> u)
                self.graph[v] = [x for x in self.graph[v] if x[0] != u]
            else:
                print(f"Ребра між {u} і {v} не існує.")
        else:
            print(f"Одна з вершин {u} або {v} не існує.")

class randomWeightedGraph(weightedGraph):
    def __init__(self, n, p, min_weight=1, max_weight=10):
        """
        Ініціалізує випадковий зважений граф у моделі Ердеша-Шеньї.
        
        n - кількість вершин
        p - ймовірність наявності ребра між будь-якими двома вершинами
        min_weight - мінімальна вага для ребра
        max_weight - максимальна вага для ребра
        """
        super().__init__(n)
        self.generate_random_graph(p, min_weight, max_weight)

    def generate_random_graph(self, p, min_weight, max_weight):
        """ Генерує випадковий зважений граф з ймовірністю p для кожної пари вершин. """
        for i in range(1, self.num_vertices + 1):
            for j in range(i + 1, self.num_vertices + 1):  # Avoid self-loops and ensure each pair is checked once
                if random.random() < p:
                    weight = random.randint(min_weight, max_weight)  # Генеруємо випадкову вагу
                    self.add_edge(i, j, weight)
