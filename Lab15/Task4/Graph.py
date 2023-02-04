class Graph():
    __nodes: dict[str, list[str]]

    def __init__(self) -> None:
        self.__nodes = dict()

    def CreateContiguity(self, matrix: list[list[int]]) -> None:
        if len(matrix) != len(matrix[0]):
            return
        for i in range(len(matrix)):
            self.__nodes[f"v{i}"] = []
            for j in range(len(matrix[i])):
                if matrix[i][j] == 1:
                    self.__nodes[f"v{i}"].append(f"v{j}")

    def CreateІncidence(self, matrix: list[list[int]]) -> None:
        rows = len(matrix)
        columns = len(matrix[0])
        for i in range(rows):
            self.__nodes[f"v{i}"] = []
        for i in range(columns):
            source: str = ""
            dest: str = ""
            for j in range(rows):
                if matrix[j][i] == 1:
                    source = f"v{j}"
                if matrix[j][i] == -1:
                    dest = f"v{j}"
                if matrix[j][i] == 2:
                    source = f"v{j}"
                    dest = f"v{j}"
                    break
            self.__nodes[source].append(dest)

    def CreateVectors(self, vectors: dict[str, list[str]]) -> None:
        for key, val in vectors.items():
            if not key in self.__nodes.keys():
                self.__nodes[key] = []
            for el in val:
                if not el in self.__nodes.keys():
                    self.__nodes[el] = []
        for key, val in vectors.items():
            for el in val:
                self.__nodes[key].append(el)

    def PrintContiguity(self) -> None:
        allnodes: list[str] = []
        for key in self.__nodes.keys():
            allnodes.append(key)
        matr: list[list[int]] = [
            [0 for i in range(len(self.__nodes))] for j in range(len(self.__nodes))]
        find: int = 0
        for val in self.__nodes.values():
            for el in val:
                matr[find][allnodes.index(el)] = 1
            find += 1
        print(f"$|".center(5, "_"), end="")
        for item in allnodes:
            print(f"{item}".center(5,"_"), end="")
        print()
        for i in range(len(self.__nodes)):
            print(f"{allnodes[i]}|".center(5), end="")
            for j in range(len(self.__nodes)):
                print(f"{matr[i][j]}".center(5), end="")
            print()

    def PrintVectors(self) -> None:
        for key, val in self.__nodes.items():
            if len(val) == 0:
                continue
            for el in val:
                print(f"{key}->{el}")

    def PrintІncidence(self) -> None:
        allnodes: list[str] = []
        numOfEdges = 0
        for key, val in self.__nodes.items():
            allnodes.append(key)
            numOfEdges += len(val)
        matr: list[list[int]] = [
            [0 for i in range(numOfEdges)] for j in range(len(self.__nodes))]
        sind: int = 0
        for key, val in self.__nodes.items():
            for el in val:
                if key == el:
                    matr[allnodes.index(key)][sind] = 2
                else:
                    matr[allnodes.index(key)][sind] = 1
                    matr[allnodes.index(el)][sind] = -1
                sind += 1
        for i in range(len(self.__nodes)):
            print(f"{allnodes[i]}|".center(5), end="")
            for j in range(numOfEdges):
                print(f"{matr[i][j]}".center(5), end="")
            print()

