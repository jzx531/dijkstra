import heapq
from collections import defaultdict
from math import inf
import time
def calculate_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print("函数 %s 运行时间为 %s 秒" % (func.__name__, end_time - start_time))
        return result
    return wrapper
vertices = ['A', 'B', 'C', 'D', 'E', 'F']
edges = [(3, 'A', 'B'),
         (2, 'A', 'C'),
         (5, 'A', 'D'),
         (1, 'B', 'D'),
         (4, 'B', 'E'),
         (2, 'C', 'D'),
         (1, 'C', 'F'),
         (3, 'D', 'E'),
         (2, 'E', 'F'),
         ]

def AdjacencyList(edges):
    adjacent_dict = defaultdict(list)  # 注意：defaultdict(list)必须以list做为变量
    for weight, v1, v2 in edges:
        adjacent_dict[v2].append((weight, v2, v1))
        adjacent_dict[v1].append((weight, v1, v2))
    for key in adjacent_dict:
        heapq.heapify(adjacent_dict[key])
        #sorted(adjacent_dict[key])
    return adjacent_dict

@calculate_time
def Dijkstra(Adjacent_dict,origin):
    recorded=[]
    origin_emit=list()
    RouterTable = {}
    for key in Adjacent_dict:
        RouterTable[key] = [-1, inf]
    recorded.append(origin)
    RouterTable[origin]=[origin,0]
    routeheap=Adjacent_dict[origin]
    # for weight, v1, v2 in Adjacent_dict[origin]:
    #     origin_emit.append(v2)
    try:
        while len(recorded)<len(vertices):
            #time.sleep(1)#延时从而让装饰器进行计时
            weight, v1, v2 = heapq.heappop(routeheap)
            if v2 not in recorded:
                RouterTable[v2] = [v1, weight]
                recorded.append(v2)
            for adjcent in Adjacent_dict[v2]:
                if(adjcent[2] not in recorded):
                    adjcent=(adjcent[0]+RouterTable[adjcent[1]][-1],adjcent[1],adjcent[2])
                    heapq.heappush(routeheap,adjcent)
        return RouterTable
    except:
       return ("destination is not in this LAN")

@calculate_time
def Dijkstra_originPort(Adjacent_dict,origin):
    recorded=[]
    origin_emit=list()
    RouterTable = {}
    for key in Adjacent_dict:
        RouterTable[key] = [-1, inf]
    recorded.append(origin)
    RouterTable[origin]=[origin,0]
    routeheap=Adjacent_dict[origin]
    # for weight, v1, v2 in Adjacent_dict[origin]:
    #     origin_emit.append(v2)
    try:
        while len(recorded)<len(vertices):
            #time.sleep(1)#延时从而让装饰器进行计时
            weight, v1, v2 = heapq.heappop(routeheap)
            #print(v1,v2,weight)
            if v2 not in recorded:
                if v1 ==origin:
                    RouterTable[v2] = [v2, weight]
                else:
                    RouterTable[v2] = [RouterTable[v1][0], weight]
                recorded.append(v2)
            for adjcent in Adjacent_dict[v2]:
                if(adjcent[2] not in recorded):
                    adjcent=(adjcent[0]+RouterTable[adjcent[1]][-1],adjcent[1],adjcent[2])
                    heapq.heappush(routeheap,adjcent)
        return RouterTable
    except:
       return ("destination is not in this LAN")


if __name__ =='__main__':
    AD=AdjacencyList(edges)
    #print(f"Dijkstra生成得到路由表={Dijkstra(AD,'A')}")
    print(f"Dijkstra生成得到端口路由表={Dijkstra_originPort(AD,'A')}")