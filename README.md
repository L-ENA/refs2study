# refs2study

A basic Python structure for grouping and clustering RIS references into studies.

## Structure

- `/refs2study/models.py`: pydantic reference data model
- `/refs2study/io.py`: CSV (gold standard) and RIS loading utilities
- `/refs2study/ref_linker.py`: baseline `RefLinker` with `predict` and `evaluate`
- `/refs2study/evaluation.py`: duplicate-pair evaluation helpers
- `/notebooks/refs2study_workflow.ipynb`: notebook for loading, display, prediction, evaluation and visualisation

## Quick start

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
```
