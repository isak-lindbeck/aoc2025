from dataclasses import dataclass
from pathlib import Path
from typing import Tuple

from aoc2025.utils.io import check_output
from aoc2025.utils.timed import Timed

Node = tuple[int, int, int]


@dataclass(unsafe_hash=True)
class Connection():
    node_a: Node
    node_b: Node

    def distance(self) -> int:
        dx = self.node_a[0] - self.node_b[0]
        dy = self.node_a[1] - self.node_b[1]
        dz = self.node_a[2] - self.node_b[2]
        return dx ** 2 + dy ** 2 + dz ** 2


def run(input_str: str, required_connections=1000) -> Tuple[int, int]:
    out_1, out_2 = 0, 0

    node_list: list[Node] = []
    for line in input_str.splitlines():
        split = line.split(",")
        node_list.append((int(split[0]), int(split[1]), int(split[2])))

    connections: list[Connection] = []
    for i, current in enumerate(node_list):
        for j in range(i + 1, len(node_list)):
            connections.append(Connection(current, node_list[j]))

    sorted_connections = sorted(connections, key=lambda c: c.distance())

    circuits: list[set[Node]] = []
    count = 0
    while True:
        node_a = sorted_connections[count].node_a
        node_b = sorted_connections[count].node_b
        circuit_a = None
        circuit_b = None

        for circuit in circuits:
            if node_a in circuit:
                circuit_a = circuit
            if node_b in circuit:
                circuit_b = circuit

        if not circuit_a and not circuit_b:
            circuit = set()
            circuit.add(node_a)
            circuit.add(node_b)
            circuits.append(circuit)
        elif circuit_b and not circuit_a:
            circuit_b.add(node_a)
        elif circuit_a and not circuit_b:
            circuit_a.add(node_b)
        elif circuit_a is not circuit_b:
            circuit_a.update(circuit_b)
            circuits.remove(circuit_b)

        count += 1

        if count == required_connections:
            sorted_circuits = sorted(circuits, key=lambda c: len(c), reverse=True)
            out_1 = len(sorted_circuits[0]) * len(sorted_circuits[1]) * len(sorted_circuits[2])

        if len(circuits) == 1 and len(circuits[0]) == len(node_list):
            out_2 = node_a[0] * node_b[0]
            break

    return out_1, out_2


if __name__ == '__main__':
    with Timed():
        output = run(Path("inputs/day08.txt").read_text().strip())
        check_output(output, Path("answers/day08.txt").resolve())
