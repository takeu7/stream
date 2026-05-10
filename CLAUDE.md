# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

A Streamlit learning repository following two Japanese resources:
- Book: *PythonとStreamlitでデータ分析をWebアプリ化* (Data Analysis Web Apps with Python and Streamlit)
- Udemy course: *Streamlit超入門* by いまにゅ

All files are standalone Streamlit apps — there is no shared module or package structure.

## Running Apps

```bash
streamlit run <filename>.py
# e.g.
streamlit run test.py
streamlit run test03.py
streamlit run main04.py
```

Each file is independent; there is no entry point that ties them together.

## File Overview

| File | Content |
|------|---------|
| `test.py` / `test-checkpoint.py` | Basic DataFrame display and LaTeX rendering |
| `test02.py` | Charts: line, area, bar (via Streamlit), and scatter (via matplotlib) |
| `test03.py` | Interactive widgets: checkbox, selectbox, multiselect, radio, number_input, sidebar |
| `main04.py` | Image display, selectbox, text input, slider (Udemy course) |
| `main04-sidebar.py` | Same as `main04.py` with inputs moved to `st.sidebar` |
| `ボストンの住宅価格.xlsx` | Boston housing price data (not yet loaded in any script) |

## Known Issue

`main04.py` and `main04-sidebar.py` load the image with `Image.open('img/obaba.jpg')`, but the file is at the repo root as `obaba.jpg` (the `img/` directory was deleted per git history). Running either file will raise a `FileNotFoundError` unless the path is corrected or an `img/` directory is recreated.

## Dependencies

Python 3, plus: `streamlit`, `pandas`, `numpy`, `matplotlib`, `Pillow`. There is no `requirements.txt`; install manually with pip if needed.
