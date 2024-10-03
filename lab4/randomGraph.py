import random
class WeightedGraph:
    def __init__(self, n):
        """ Ініціалізує порожній граф.
        
        n - кількість вершин
        """
        self.num_vertices = n
        self.edges = []  # Список рёбер графа

    def add_edge(self, u, v, weight):
        """ Додає ребро з вагою у граф.
        
        u, v - вершини, weight - вага ребра
        """
        # Добавляем ребро в формате (u, v, weight) только если u < v, чтобы избежать дублирования
        if u < v:
            self.edges.append((u, v, weight))
        else:
            self.edges.append((v, u, weight))

class RandomWeightedGraph(WeightedGraph):
    def __init__(self, n, p, min_weight=1, max_weight=10):
        """
        Ініціалізує випадковий зважений граф у моделі Ердеша-Шеньї.
        
        n - кількість вершин
        p - ймовірність наявності ребра між будь-якими двома вершинами
        max_weight - максимальна вага для ребра
        """
        super().__init__(n)
        self.generate_random_graph(p, min_weight, max_weight)

    def generate_random_graph(self, p, min_weight, max_weight):
        """ Генерує випадковий зважений граф з ймовірністю p для кожної пари вершин. """
        for i in range(self.num_vertices):
            for j in range(i + 1, self.num_vertices): 
                if random.random() < p:  
                    weight = random.randint(min_weight, max_weight)  
                    self.add_edge(i, j, weight)
