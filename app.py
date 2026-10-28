import hashlib
import time
import pandas as pd
import streamlit as st
from maze_logic import PRESETS, bfs_search, compare_presets, parse_maze, state_at
from ui_components import (
    get_blueprint_css,
    render_board_component,
    render_hero_header,
    render_stat_cards,
)

def setup_page():
    st.set_page_config(
        page_title="Breadth-First Maze Solver",
        page_icon="🧭",
        layout="wide",
    )
    st.markdown(get_blueprint_css(), unsafe_allow_html=True)
    st.markdown(render_hero_header(), unsafe_allow_html=True)

def render_sidebar():
    st.sidebar.markdown("### Maze setup")
    preset_options = ["Simple", "Medium", "Hard", "Custom"]
    selected_maze = st.sidebar.selectbox("Choose Preset", preset_options)

    if "current_maze_selection" not in st.session_state:
        st.session_state["current_maze_selection"] = selected_maze
        st.session_state[f"grid_{selected_maze}"] = PRESETS.get(selected_maze, PRESETS["Simple"])
    elif st.session_state["current_maze_selection"] != selected_maze:
        st.session_state["current_maze_selection"] = selected_maze
        st.session_state[f"grid_{selected_maze}"] = PRESETS.get(selected_maze, PRESETS["Simple"])

    maze_text = st.sidebar.text_area(
        "Grid Layout",
        key=f"grid_{selected_maze}",
        height=260,
    )

    st.sidebar.markdown("### Playback")
    delay = st.sidebar.slider(
        "Seconds per step",
        min_value=0.02,
        max_value=0.60,
        value=0.12,
        step=0.01,
    )
    return selected_maze, maze_text, delay

def render_path_info(path):
    if path is None:
        st.warning("No path exists between S and G.")
    else:
        with st.expander("Shortest path coordinates"):
            path_str = " -> ".join(f"({r},{c})" for r, c in path)
            st.code(path_str, language="text")

def render_visualizer(maze, result, delay, selected_maze, maze_text):
    st.markdown(
        render_stat_cards(
            result["moves"],
            result["expanded"],
            result["discovered"],
            result["rows"],
            result["cols"],
        ),
        unsafe_allow_html=True,
    )

    total = len(result["order"])
    maze_hash = hashlib.md5(maze_text.encode("utf-8")).hexdigest()[:8]
    slider_key = f"step_{selected_maze}_{maze_hash}"

    if slider_key not in st.session_state:
        st.session_state[slider_key] = 0
    else:
        st.session_state[slider_key] = max(0, min(st.session_state[slider_key], total))

    def solve_instantly():
        st.session_state[slider_key] = total

    def reset_step():
        st.session_state[slider_key] = 0

    col1, col2, col3 = st.columns(3)
    with col1:
        animate_clicked = st.button("Animate", width="stretch")
    with col2:
        st.button("Solve instantly", on_click=solve_instantly, width="stretch")
    with col3:
        st.button("Reset", on_click=reset_step, width="stretch")

    if animate_clicked:
        st.session_state[slider_key] = total

    current_step = st.slider("Step", min_value=0, max_value=total, key=slider_key)

    board_container = st.empty()
    if animate_clicked:
        for s in range(0, total + 1):
            exp, front, pth = state_at(result, s)
            board_container.markdown(
                render_board_component(maze, exp, front, pth, s, total),
                unsafe_allow_html=True,
            )
            time.sleep(delay)
    else:
        exp, front, pth = state_at(result, current_step)
        board_container.markdown(
            render_board_component(maze, exp, front, pth, current_step, total),
            unsafe_allow_html=True,
        )

    render_path_info(result["path"])

def render_comparison():
    summary_data = compare_presets()
    df = pd.DataFrame(summary_data)
    st.dataframe(df, hide_index=True, width="stretch")
    st.subheader("Cells Expanded per Preset")
    st.bar_chart(
        df,
        x="Maze",
        y="Expanded",
        horizontal=True,
        color="#ffb703",
        width="stretch",
    )

def main():
    setup_page()
    selected_maze, maze_text, delay = render_sidebar()

    try:
        maze = parse_maze(maze_text)
    except ValueError as exc:
        st.error(str(exc))
        st.stop()

    result = bfs_search(maze)

    tab_viz, tab_comp = st.tabs(["Visualizer", "Comparison"])
    with tab_viz:
        render_visualizer(maze, result, delay, selected_maze, maze_text)
    with tab_comp:
        render_comparison()

if __name__ == "__main__":
    main()
