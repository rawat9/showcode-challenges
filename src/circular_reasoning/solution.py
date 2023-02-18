class Network:
    def get_graph(self, total_nodes: int) -> dict[int, list[int]]:
        graph: dict[int, list[int]] = {}
        nodes = list(range(1, total_nodes + 1))

        for i in range(len(nodes)):
            if i == len(nodes) - 1:
                graph[nodes[i]] = [nodes[0]]
            else:
                graph[nodes[i]] = [nodes[i + 1]]

        return graph

    def nodes_visited(
        self, total_nodes: int, starting_node: int, nodes_to_visit: list[int]
    ) -> int:

        graph = self.get_graph(total_nodes)
        visited = set()
        destination = sorted(nodes_to_visit)[-1]

        def dfs(node: int) -> None:
            if node == destination:
                return

            visited.add(node)
            for neighbour in graph[node]:
                dfs(neighbour)

        dfs(starting_node)
        return len(visited)

        # Your code goes here
        # [1,2,3,4,5,6,7,8,9,10,11,12]
        # [1,2,3,4]
        # [3,4,5,6,7,8,9,10,11,12,13,14]


network = Network()
print(network.nodes_visited(12, 3, [10]))  # 7
print(network.nodes_visited(4, 4, [2, 4]))  # 7
