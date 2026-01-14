# widgets.py — Streamlit Learning Guide ✅

A short, practical guide to the Streamlit widgets demonstrated in `widgets.py`. This README explains how to run the file, what each widget does, simple usage notes, and troubleshooting tips for common errors (e.g., ModuleNotFoundError).

---

## Quick start 🔧

Prerequisites:
- Python 3.8+
- A virtual environment (recommended)
- Packages: `streamlit`, `pandas`

Install dependencies:

```bash
# Using the included virtual environment (Windows PowerShell example)
.\env\Scripts\Activate.ps1
python -m pip install -r requirements.txt
# or install directly
python -m pip install streamlit pandas
```

Run the widget demo:

```bash
# Run the Streamlit file directly
streamlit run widgets.py
# or using the module runner
python -m streamlit run widgets.py
```

---

## What this file demonstrates ✨

`widgets.py` shows basic interactive widgets you can build with Streamlit:

- **Title**: `st.title("Streamlit Text Input")` — adds a page title.
- **Text input** (`st.text_input`) — collects free text, shown conditionally when not empty.

Example:
```py
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!")
```

- **Slider** (`st.slider`) — select a numeric value (used here for age).
- **Color picker** (`st.color_picker`) — pick a color (hex string returned).
- **Date/time inputs** (`st.date_input`, `st.time_input`) — choose dates and times.
- **Selectbox** (`st.selectbox`) — single choice from a list.
- **Multiselect** (`st.multiselect`) — multiple choice selection.
- **File uploader** (`st.file_uploader`) — upload files (example reads CSV with `pandas`).

Example reading uploaded CSV:
```py
uploaded_file = st.file_uploader("upload a file:", type=["csv","txt","xlsx"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
# For Excel files use pd.read_excel(uploaded_file)
```

---

## Tips & troubleshooting ⚠️

- If you see a `ModuleNotFoundError` for `streamlit` or `pandas`:
  - Ensure your virtual environment is active and `pip install streamlit pandas` was run in that environment.
  - Check the active interpreter: `python -V` and `python -m pip show streamlit`.

- Uploaded files should match the expected type. When reading Excel files use `pd.read_excel` instead of `pd.read_csv`.

- For more responsive apps, consider caching expensive computations using `@st.cache_data` or `@st.cache_resource` (see Streamlit docs).

---

## Next steps / Learning resources 💡

- Try adding more widgets: `st.checkbox`, `st.radio`, `st.text_area`.
- Build a small interactive analysis: upload a CSV and create charts with `st.line_chart` or `altair`.
- Read the official docs: https://docs.streamlit.io

---

*Created to help you learn and experiment with Streamlit widgets in `widgets.py`.*
