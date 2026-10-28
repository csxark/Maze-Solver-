# Breadth-First Maze Solver (AISC Project)

An interactive visualizer for Breadth-First Search (BFS) on grid topologies, built with pure Python and Streamlit for an Artificial Intelligence & Soft Computing (uninformed search) course project.

## Run Command

```bash
pip install -r requirements.txt && streamlit run app.py
```

Or step-by-step:

```bash
pip install -r requirements.txt
streamlit run app.py
```

Then navigate to `http://localhost:8501` in your browser.

## Project Structure

- `maze_logic.py`: Pure BFS logic, grid parsing, state extraction, and presets comparison using Python standard library (`collections.deque`).
- `ui_components.py`: "Cartographer's blueprint" design system, responsive stat cards, CSS grid maze renderer, step pill badge, and swatches.
- `app.py`: Streamlit main application, sidebar setup, playback speed control, interactive animation loop, and Comparison tab.
- `.streamlit/config.toml`: Dark blueprint theme configuration and headless server settings.
- `requirements.txt`: Python dependencies (`streamlit>=1.40.0`, `pandas>=2.0.0`).

## Features

- **Blueprint Aesthetics**: Dark navy engineering theme with subtle 36px blueprint grid background, dual ambient glows, Google Fonts (*Bricolage Grotesque* & *IBM Plex Mono*), and outlined amber controls.
- **Layer-by-Layer Visualization**:
  - Start cell: Sky blue
  - Goal cell: Coral
  - Open paths: Navy
  - Walls: Diagonal hatch pattern
  - Search frontier: Glowing amber
  - Explored nodes: Translucent sky
  - Optimal shortest path: Glowing mint green
- **Interactive Controls**:
  - `Animate`: Smooth step-by-step animation from step 0 to the final goal discovery.
  - `Solve instantly`: Jumps directly to the completed search.
  - `Reset`: Returns to step 0.
  - Interactive scrub slider (0 to total steps) for step-by-step inspection.
  - Playback speed slider (0.02s to 0.60s per step).
- **Preset Benchmarks & Custom Mazes**:
  - Simple (7×7): 12 moves, 32 expanded, 32 discovered.
  - Medium (9×11): 18 moves, 57 expanded, 59 discovered.
  - Hard (15×21): 70 moves, 155 expanded, 158 discovered.
  - Custom: Editable grid layout with real-time validation and error diagnostics.
- **Comparative Analysis**:
  - Tabular benchmark comparison across presets.
  - Horizontal bar chart of cells expanded per preset.
