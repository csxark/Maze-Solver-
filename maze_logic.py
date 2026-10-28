from collections import deque

SIMPLE_MAZE = """
S......
.####..
.....#.
.###.#.
...#.#.
.#.....
.#####G
""".strip()

MEDIUM_MAZE = """
S..........
.#########.
.........#.
.#######.#.
.#.....#.#.
.#.###.#.#.
.#...#...#.
.###.#####.
..........G
""".strip()

HARD_MAZE = """
S....................
###################.#
.....................
#.###.#######.#######
.....................
###################.#
.....................
#.###.#######.#######
.....................
###################.#
.....................
#.###.#######.#######
.....................
###################.#
....................G
""".strip()

PRESETS = {
    "Simple": SIMPLE_MAZE,
    "Medium": MEDIUM_MAZE,
    "Hard": HARD_MAZE,
}

def parse_maze(text):
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines:
        raise ValueError("Maze cannot be empty.")
    cols = len(lines[0])
    s_count = 0
    g_count = 0
    valid_chars = {"S", "G", "#", "."}
    for row_idx, row in enumerate(lines):
        if len(row) != cols:
            raise ValueError(f"Row {row_idx + 1} length ({len(row)}) does not match expected length ({cols}).")
        for ch in row:
            if ch not in valid_chars:
                raise ValueError(f"Invalid character '{ch}' in maze. Allowed characters are S, G, #, and .")
            if ch == "S":
                s_count += 1
            elif ch == "G":
                g_count += 1
    if s_count != 1:
        raise ValueError(f"Maze must contain exactly one 'S', found {s_count}.")
    if g_count != 1:
        raise ValueError(f"Maze must contain exactly one 'G', found {g_count}.")
    return lines

def bfs_search(maze):
    rows = len(maze)
    cols = len(maze[0])
    start = None
    goal = None
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == "S":
                start = (r, c)
            elif maze[r][c] == "G":
                goal = (r, c)

    queue = deque([start])
    parent = {start: None}
    order = []
    goal_found = False
    moves_order = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        curr = queue.popleft()
        order.append(curr)
        if curr == goal:
            goal_found = True
            break
        r, c = curr
        for dr, dc in moves_order:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if maze[nr][nc] != "#" and (nr, nc) not in parent:
                    parent[(nr, nc)] = curr
                    queue.append((nr, nc))

    if goal_found:
        path = []
        curr = goal
        while curr is not None:
            path.append(curr)
            curr = parent[curr]
        path.reverse()
        moves = len(path) - 1
    else:
        path = None
        moves = None

    return {
        "path": path,
        "moves": moves,
        "expanded": len(order),
        "discovered": len(parent),
        "order": order,
        "parent": parent,
        "rows": rows,
        "cols": cols,
    }

def state_at(result, step):
    order = result["order"]
    clamped_step = min(max(0, step), len(order))
    explored = set(order[:clamped_step])
    frontier = set()
    for cell, p in result["parent"].items():
        if (p is None or p in explored) and cell not in explored:
            frontier.add(cell)
    path = result["path"] if (step >= len(order) and result["path"] is not None) else None
    return explored, frontier, path

def compare_presets():
    summary = []
    for name in ["Simple", "Medium", "Hard"]:
        maze = parse_maze(PRESETS[name])
        res = bfs_search(maze)
        summary.append({
            "Maze": name,
            "Size": f"{res['rows']}x{res['cols']}",
            "Moves": res["moves"],
            "Expanded": res["expanded"],
            "Discovered": res["discovered"],
        })
    return summary
