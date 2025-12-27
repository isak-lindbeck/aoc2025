from pathlib import Path

from aoc2025.utils.io import check_output
from aoc2025.utils.timed import Timed


def run(input_str: str) -> tuple[int, int]:
    out_1 = run_1(input_str)
    out_2 = run_2(input_str)
    return out_1, out_2


def run_1(input_str: str) -> int:
    connections: dict[str, list[str]] = {}

    for line in input_str.splitlines():
        split = line.split(" ")
        key = split[0].removesuffix(":")
        connections[key] = split[1:]

    return count_paths(connections, 'you', {})


def run_2(input_str: str) -> int:
    connections: dict[str, list[str]] = {}
    reversed_connections: dict[str, list[str]] = {}

    for line in input_str.splitlines():
        split = line.split(" ")
        key = split[0].removesuffix(":")
        connections[key] = split[1:]
        for x in connections[key]:
            reversed_connections.setdefault(x, [])
            reversed_connections[x].append(key)
    connections.setdefault('out', [])
    reversed_connections.setdefault('svr', [])

    prune_unconnected(connections, reversed_connections, 'fft')
    prune_unconnected(connections, reversed_connections, 'dac')

    return count_paths(connections, 'svr', {})


def count_paths(connections: dict[str, list[str]], key: str, cache: dict[str, int]) -> int:
    if key == 'out':
        return 1

    if result := cache.get(key, None):
        return result

    result = 0
    for next_connection in connections.get(key, []):
        result += count_paths(connections, next_connection, cache)
    cache[key] = result
    return result


def prune_unconnected(connections: dict[str, list[str]], reversed_connections: dict[str, list[str]], from_node: str):
    connected: set[str] = {from_node}

    def prune_graph(graph: dict[str, list[str]]):
        queue = [from_node]
        while queue:
            for x in graph.get(queue.pop(), []):
                if x not in connected:
                    connected.add(x)
                    queue.append(x)

    prune_graph(connections)
    prune_graph(reversed_connections)

    for key in list(connections.keys()):
        if key not in connected:
            connections.pop(key, None)
            reversed_connections.pop(key, None)


if __name__ == '__main__':
    with Timed():
        output = run(Path("inputs/day11.txt").read_text().strip())
        check_output(output, Path("answers/day11.txt").resolve())
