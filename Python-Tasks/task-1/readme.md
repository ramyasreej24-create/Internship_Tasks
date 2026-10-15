
# Predict and Execute Task: Python Fundamentals

A Jupyter notebook of 50 short "predict the output" exercises covering core Python behaviour. Each question is a small code snippet, followed by the actual output and an inline comment explaining *why* Python behaves that way.

## Contents

| File | Description |
|------|-------------|
| `Predict and Execute Task.ipynb` | The notebook with all 50 questions (Q1–Q50), code, outputs and explanations |

## Topics Covered

| Questions | Topic | What it demonstrates |
|-----------|-------|----------------------|
| Q1–Q5 | Dictionaries & sets | `{}` creates a dict, `set()` creates an empty set; `.add()` exists on sets, not dicts |
| Q6–Q10 | Tuples | `(25)` is an `int`, `(25,)` is a tuple; tuple packing; negative indexing |
| Q11–Q15 | Truthiness (`bool()`) | `0`, `""`, `[]`, `()`, `None` are falsy; `" "` and `"None"` are truthy |
| Q16–Q19 | Dictionary key equality | `True`, `1`, `1.0` (and `False`, `0`) are the same key, so later values overwrite earlier ones |
| Q20–Q24 | `==` vs `is` | Value equality vs object identity, including list copies, `str.join` and `int()` results |
| Q25–Q27 | Aliasing & mutation | `b = a` shares one object; `a = a + [x]` rebinds, while `a += [x]` mutates in place |
| Q28–Q30 | Slicing | `a[1:3]`, `a[::2]`, and `a[:]` creating a new list |
| Q31–Q34 | `del` | Deleting a name vs deleting elements; `NameError` after deletion |
| Q35–Q39 | Shallow vs deep copy | `copy.copy`, `list.copy()` and `copy.deepcopy` with nested lists |
| Q40–Q43 | List multiplication | `[[]] * n` repeats references to the *same* inner list |
| Q44–Q47 | `*args` and `**kwargs` | Collected as a `tuple` and a `dict` respectively |
| Q48–Q50 | `print` vs `return` | A function with no `return` gives `None`; side effects vs return values |

## Requirements

- Python 3.8+
- Jupyter Notebook, JupyterLab, or VS Code with the Jupyter extension
- Standard library only (the `copy` module is the only import)

## How to Run

```bash
# 1. (Optional) create a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. Install Jupyter
pip install notebook

# 3. Launch the notebook
jupyter notebook "Predict and Execute Task.ipynb"
```

Then use **Kernel → Restart & Run All**, or run cells one at a time with `Shift + Enter`.

## How to Use This Notebook

1. Read the code in a cell and write down your predicted output.
2. Run the cell and compare the result with your prediction.
3. Read the inline comment to see the reasoning.

## Notes

- **Q5** (`{}.add(10)`) and **Q34** (printing after `del a`) are *intended to raise errors* (`AttributeError` and `NameError`), so they have no printed output when run. Run them to see the traceback.
- **Q49**: the inline comment says nothing is printed, but the `10` shown comes from `print(x)`. The function returns `10` and the caller prints it.
- Results for `is` comparisons involving integers and strings (Q22, Q24) depend on CPython's interning and caching. Don't rely on `is` for value comparison in real code; use `==`.

## Key Takeaways

- Use `==` to compare values and `is` only to check identity (e.g. `x is None`).
- Assignment (`b = a`) never copies; it creates another reference to the same object.
- Use `copy.deepcopy` when you need an independent copy of nested structures.
- Avoid `[[]] * n` for nested lists; use `[[] for _ in range(n)]` instead.
- A single-element tuple needs a trailing comma: `(25,)`.
