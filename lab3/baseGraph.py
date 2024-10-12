class baseGraph:
    def __init__(self, n):
        """ Ініціалізує порожній граф.
        
        n - кількість вершин
        """
        self.num_vertices = n
        self.graph = {i+1: [] for i in range(n)}  # Порожній граф у вигляді списку суміжності {1: [], 2: [] ... }

    def add_vertex(self):
        """ Додає нову вершину до графа. """
        self.num_vertices += 1  # Збільшуємо кількість вершин
        self.graph[self.num_vertices] = []  # Додаємо нову вершину з порожнім списком сусідів
    
    def del_vertex(self, v):
        """ Видаляє вершину v і всі пов'язані з нею ребра. """
        if v in self.graph:
            # Видаляємо всі ребра, пов'язані з вершиною v
            for neighbor in self.graph[v]:
                if v in self.graph[neighbor]:  # Перевіряємо наявність v серед сусідів
                    self.graph[neighbor].remove(v)  # Видаляємо v з сусідів кожної вершини
            # Видаляємо саму вершину
            del self.graph[v]
            self.num_vertices -= 1  # Зменшуємо кількість вершин
        else:
            print(f"Вершина {v} не існує.")

    def to_adjacency_matrix(self):
        """ Перетворює граф зі списку суміжності у матрицю суміжності. """
        # Ініціалізуємо матрицю розміром num_vertices x num_vertices з нулями
        matrix = [[float('inf')] * self.num_vertices for _ in range(self.num_vertices)]
        for i in range(self.num_vertices):
            matrix[i][i] = 0

        for vertex, neighbors in self.graph.items():
            for neighbor in neighbors:
                if isinstance(neighbor, tuple):
                    # Якщо граф зважений, присвоюємо вагу ребра
                    matrix[vertex-1][neighbor[0]-1] = neighbor[1]
                else:
                    # Якщо граф незважений, просто ставимо 1
                    matrix[vertex-1][neighbor-1] = 1
        return matrix

    def to_adjacency_list(self, matrix, weighted=False):
        """ Перетворює граф з матриці суміжності у список суміжності.
        
        matrix - матриця суміжності
        weighted - булевий параметр, який вказує, чи граф є зваженим
        """
        self.num_vertices = len(matrix)
        self.graph = {i+1: [] for i in range(self.num_vertices)}  # Очищаємо граф і створюємо новий список суміжності

        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                if matrix[i][j] != 0:  # Якщо є ребро
                    if weighted:
                        # Якщо граф зважений, додаємо кортеж (вершина, вага)
                        self.graph[i+1].append((j+1, matrix[i][j]))
                    else:
                        # Якщо граф незважений, додаємо тільки вершину
                        self.graph[i+1].append(j+1)
                        
    def show(self):
        """ Виводить граф у вигляді списку суміжності. """
        for vertex in self.graph:
            print(f"{vertex}: {self.graph[vertex]}")

    def show_matrix(self):
        """ Виводить граф у вигляді матриці суміжності. """
        matrix = self.to_adjacency_matrix()
        for row in matrix:
            print(row)
    
    def makeNonOriented(self):
        """ Робить граф неорієнтованим, додаючи зворотні ребра. """
        for vertex, neighbors in self.graph.items():
            for neighbor in neighbors:
                # Додаємо зворотне ребро, якщо його ще немає
                if vertex not in self.graph[neighbor]:
                    self.graph[neighbor].append(vertex)
