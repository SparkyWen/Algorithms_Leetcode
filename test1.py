import sys
from collections import defaultdict

def tarjan_scc(n, graph):
    """使用Tarjan算法找强连通分量"""
    index_counter = [0]
    stack = []
    lowlinks = {}
    index = {}
    on_stack = defaultdict(bool)
    scc_list = []
    
    def strongconnect(node):
        index[node] = index_counter[0]
        lowlinks[node] = index_counter[0]
        index_counter[0] += 1
        stack.append(node)
        on_stack[node] = True
        
        for successor in graph[node]:
            if successor not in index:
                strongconnect(successor)
                lowlinks[node] = min(lowlinks[node], lowlinks[successor])
            elif on_stack[successor]:
                lowlinks[node] = min(lowlinks[node], index[successor])
        
        if lowlinks[node] == index[node]:
            scc = []
            while True:
                successor = stack.pop()
                on_stack[successor] = False
                scc.append(successor)
                if successor == node:
                    break
            scc_list.append(scc)
    
    for node in range(1, n + 1):
        if node not in index:
            strongconnect(node)
    
    return scc_list

def main():
    lines = sys.stdin.readlines()
    idx = 0
    
    while idx < len(lines):
        line = lines[idx].strip()
        if not line:
            idx += 1
            continue
            
        n, m = map(int, line.split())
        idx += 1
        
        # 构建图的邻接表
        graph = defaultdict(list)
        edges = []
        
        # 读入m条规约关系
        for _ in range(m):
            x, y = map(int, lines[idx].strip().split())
            graph[x].append(y)
            edges.append((x, y))
            idx += 1
        
        # 找出所有强连通分量
        scc_list = tarjan_scc(n, graph)
        
        # 为每个节点分配所属的SCC编号
        node_to_scc = {}
        for scc_id, scc in enumerate(scc_list):
            for node in scc:
                node_to_scc[node] = scc_id
        
        # 计算每个SCC的入度（缩点后）
        scc_indegree = [0] * len(scc_list)
        
        for x, y in edges:
            scc_x = node_to_scc[x]
            scc_y = node_to_scc[y]
            # 如果是跨SCC的边，增加目标SCC的入度
            if scc_x != scc_y:
                scc_indegree[scc_y] += 1
        
        # 统计入度为0的SCC数量
        # 这些是必须独立证明为NP完全的问题组
        ans = sum(1 for indeg in scc_indegree if indeg == 0)
        
        print(ans)

if __name__ == "__main__":
    main()