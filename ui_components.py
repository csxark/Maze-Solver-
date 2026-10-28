def get_blueprint_css():
    return """
<style>
@import url('https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;600;700;800&family=IBM+Plex+Mono:ital,wght@0,400;0,500;0,600;0,700;1,400&display=swap');

:root {
    --ink: #0a1828;
    --panel: #0f2742;
    --line: #1f4068;
    --text: #e6edf5;
    --muted: #8fa6bf;
    --amber: #ffb703;
    --coral: #ff6b57;
    --mint: #3ddc97;
    --sky: #4cc9f0;
}

html, body, [class*="css"], .stMarkdown, p, div, span, label, input, textarea {
    font-family: 'IBM Plex Mono', monospace;
}

h1, h2, h3, h4, .stat-val, .hero-title {
    font-family: 'Bricolage Grotesque', sans-serif;
}

.stApp {
    background-color: #0a1828;
    background-image:
        radial-gradient(circle at 12% 15%, rgba(76, 201, 240, 0.09) 0%, transparent 45%),
        radial-gradient(circle at 88% 85%, rgba(255, 183, 3, 0.07) 0%, transparent 45%),
        linear-gradient(to right, rgba(31, 64, 104, 0.22) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(31, 64, 104, 0.22) 1px, transparent 1px);
    background-size: 100% 100%, 100% 100%, 36px 36px, 36px 36px;
    color: var(--text);
}

[data-testid="stSidebar"] {
    background-color: #0b1e33;
    border-right: 1px solid #1f4068;
}

[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
    color: var(--muted);
}

div.stButton > button {
    background-color: transparent !important;
    color: #ffb703 !important;
    border: 1px solid #ffb703 !important;
    border-radius: 4px !important;
    font-family: 'IBM Plex Mono', monospace !important;
    font-weight: 600 !important;
    letter-spacing: 0.5px !important;
    transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1) !important;
}

div.stButton > button:hover {
    background-color: #ffb703 !important;
    color: #0a1828 !important;
    border-color: #ffb703 !important;
    box-shadow: 0 0 14px rgba(255, 183, 3, 0.45) !important;
}

div.stButton > button:active {
    transform: scale(0.98) !important;
}

.hero-container {
    animation: heroRise 0.5s ease-out forwards;
    padding: 0.25rem 0 1rem 0;
    margin-bottom: 1.25rem;
    border-bottom: 1px solid var(--line);
}

@keyframes heroRise {
    from {
        opacity: 0;
        transform: translateY(14px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.hero-eyebrow {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.75rem;
    font-weight: 700;
    color: var(--amber);
    letter-spacing: 2.5px;
    margin-bottom: 0.35rem;
}

.hero-title {
    font-size: 2.35rem;
    font-weight: 800;
    color: var(--text);
    margin: 0 0 0.35rem 0;
    line-height: 1.15;
}

.hero-title .title-amber {
    color: var(--amber);
}

.hero-desc {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.88rem;
    color: var(--muted);
    margin: 0;
}

.stat-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 14px;
    margin-bottom: 1.25rem;
}

@media (max-width: 800px) {
    .stat-grid {
        grid-template-columns: repeat(2, 1fr);
    }
}

.stat-card {
    background: var(--panel);
    border: 1px solid var(--line);
    border-radius: 6px;
    padding: 12px 16px;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.card-moves {
    border-left: 4px solid var(--mint);
}

.card-expanded {
    border-left: 4px solid var(--sky);
}

.card-discovered {
    border-left: 4px solid var(--amber);
}

.card-size {
    border-left: 4px solid var(--coral);
}

.stat-label {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.7rem;
    color: var(--muted);
    letter-spacing: 1.2px;
    text-transform: uppercase;
    margin-bottom: 4px;
}

.stat-val {
    font-family: 'Bricolage Grotesque', sans-serif;
    font-size: 1.65rem;
    font-weight: 800;
    color: var(--text);
    line-height: 1.15;
}

.board-frame {
    background: #091a2e;
    border: 1px solid var(--line);
    border-radius: 8px;
    padding: 16px 18px;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
    margin-top: 14px;
    margin-bottom: 20px;
}

.step-pill {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: var(--panel);
    border: 1px solid var(--line);
    padding: 5px 12px;
    border-radius: 9999px;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.78rem;
    letter-spacing: 1px;
    margin-bottom: 12px;
}

.step-label {
    color: var(--muted);
    font-weight: 600;
}

.step-val {
    color: var(--amber);
    font-weight: 700;
}

.maze-grid-wrapper {
    display: flex;
    justify-content: center;
    overflow-x: auto;
    padding: 6px 0;
}

.maze-grid {
    display: grid;
    gap: 2px;
    margin: 0 auto;
}

.cell {
    width: var(--cell-size);
    height: var(--cell-size);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: var(--cell-font);
    font-family: 'IBM Plex Mono', monospace;
    font-weight: 700;
    border-radius: 2px;
    box-sizing: border-box;
}

.cell-open {
    background: #12304f;
    border: 1px solid rgba(31, 64, 104, 0.4);
}

.cell-wall {
    background: repeating-linear-gradient(45deg, #071322, #071322 4px, #0e2035 4px, #0e2035 8px);
    border: 1px solid #14283f;
}

.cell-explored {
    background: rgba(76, 201, 240, 0.28);
    border: 1px solid rgba(76, 201, 240, 0.45);
    color: var(--sky);
}

.cell-frontier {
    background: var(--amber);
    border: 1px solid var(--amber);
    box-shadow: 0 0 10px rgba(255, 183, 3, 0.65);
    color: var(--ink);
}

.cell-path {
    background: var(--mint);
    border: 1px solid var(--mint);
    box-shadow: 0 0 12px rgba(61, 220, 151, 0.85);
    color: var(--ink);
}

.cell-start {
    background: var(--sky);
    border: 1px solid var(--sky);
    color: var(--ink);
}

.cell-goal {
    background: var(--coral);
    border: 1px solid var(--coral);
    color: var(--ink);
}

.maze-legend {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 16px;
    margin-top: 14px;
    padding-top: 12px;
    border-top: 1px solid var(--line);
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.78rem;
    color: var(--muted);
}

.legend-item {
    display: flex;
    align-items: center;
    gap: 6px;
}

.swatch {
    width: 16px;
    height: 16px;
    border-radius: 2px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 10px;
    font-weight: 700;
    box-sizing: border-box;
}

.swatch-start {
    background: var(--sky);
    color: var(--ink);
}

.swatch-goal {
    background: var(--coral);
    color: var(--ink);
}

.swatch-explored {
    background: rgba(76, 201, 240, 0.28);
    border: 1px solid rgba(76, 201, 240, 0.45);
}

.swatch-frontier {
    background: var(--amber);
    box-shadow: 0 0 6px rgba(255, 183, 3, 0.6);
}

.swatch-path {
    background: var(--mint);
    box-shadow: 0 0 8px rgba(61, 220, 151, 0.8);
}

.swatch-wall {
    background: repeating-linear-gradient(45deg, #071322, #071322 2px, #0e2035 2px, #0e2035 4px);
    border: 1px solid #14283f;
}
</style>
""".strip()

def render_hero_header():
    return (
        '<div class="hero-container">'
        '<div class="hero-eyebrow">AISC // UNINFORMED SEARCH</div>'
        '<h1 class="hero-title">Breadth-First <span class="title-amber">Maze Solver</span></h1>'
        '<p class="hero-desc">Watch the search frontier spread layer by layer across the grid topology and see the optimal shortest path light up upon reaching the goal.</p>'
        '</div>'
    )

def render_stat_cards(moves, expanded, discovered, rows, cols):
    moves_display = f"{moves} moves" if moves is not None else "None"
    return (
        '<div class="stat-grid">'
        f'<div class="stat-card card-moves"><div class="stat-label">Shortest path</div><div class="stat-val">{moves_display}</div></div>'
        f'<div class="stat-card card-expanded"><div class="stat-label">Cells expanded</div><div class="stat-val">{expanded}</div></div>'
        f'<div class="stat-card card-discovered"><div class="stat-label">Cells discovered</div><div class="stat-val">{discovered}</div></div>'
        f'<div class="stat-card card-size"><div class="stat-label">Grid size</div><div class="stat-val">{rows} × {cols}</div></div>'
        '</div>'
    )

def render_board_component(maze, explored, frontier, path, step, total):
    rows = len(maze)
    cols = len(maze[0])
    cell_size = max(16, min(40, int(620 / cols)))
    font_size = max(10, int(cell_size * 0.55))
    path_set = set(path) if path else set()

    pill_html = f'<div class="step-pill"><span class="step-label">PROGRESS</span><span class="step-val">STEP {step} / {total}</span></div>'

    cells = []
    for r in range(rows):
        for c in range(cols):
            ch = maze[r][c]
            pos = (r, c)
            if ch == "#":
                cls = "cell cell-wall"
                content = ""
            elif pos in path_set:
                cls = "cell cell-path"
                content = ch if ch in ("S", "G") else ""
            elif pos in frontier:
                cls = "cell cell-frontier"
                content = ch if ch in ("S", "G") else ""
            elif pos in explored:
                cls = "cell cell-explored"
                content = ch if ch in ("S", "G") else ""
            elif ch == "S":
                cls = "cell cell-start"
                content = "S"
            elif ch == "G":
                cls = "cell cell-goal"
                content = "G"
            else:
                cls = "cell cell-open"
                content = ""
            cells.append(f'<div class="{cls}">{content}</div>')

    grid_inner = "".join(cells)
    grid_html = f'<div class="maze-grid" style="grid-template-columns: repeat({cols}, {cell_size}px);">{grid_inner}</div>'

    legend_html = (
        '<div class="maze-legend">'
        '<div class="legend-item"><span class="swatch swatch-start">S</span>Start</div>'
        '<div class="legend-item"><span class="swatch swatch-goal">G</span>Goal</div>'
        '<div class="legend-item"><span class="swatch swatch-explored"></span>Expanded</div>'
        '<div class="legend-item"><span class="swatch swatch-frontier"></span>Frontier</div>'
        '<div class="legend-item"><span class="swatch swatch-path"></span>Shortest path</div>'
        '<div class="legend-item"><span class="swatch swatch-wall"></span>Wall</div>'
        '</div>'
    )

    full = (
        f'<div class="board-frame" style="--cell-size: {cell_size}px; --cell-font: {font_size}px;">'
        f'{pill_html}'
        f'<div class="maze-grid-wrapper">{grid_html}</div>'
        f'{legend_html}'
        '</div>'
    )
    return full.replace("\n", "").strip()
