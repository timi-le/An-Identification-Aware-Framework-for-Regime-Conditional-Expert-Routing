# Agentic Causal Macro Intelligence
## An Identification-Aware Framework for Regime-Conditional Expert Routing
Timilehin Olapade. Revised public working paper, 31 October 2026.

![CMTF animated explainer](assets/cmtf-readme.gif)

## Overleaf
Upload this ZIP as a new project. Select `main.tex` as the main document and pdfLaTeX as the compiler. The included vector figure and results let you compile without running Python. Bibliography uses BibTeX (plainnat).

## Reproduce
Tested with Python 3.12.14. Install `pip install -r requirements.txt`, then run `python reproduce.py` and `python -m unittest discover -s tests -v` from this directory. Reproduction regenerates 800 datasets and 4,000 method rows. No API, trading account or private data is needed. Results appear under `results/cmtf/`; the original reference numbers were reproduced with tolerance 1e-12. CPU runtime varies by hardware.

## Compile locally
Run `pdflatex main.tex`, `bibtex main`, then `pdflatex main.tex` twice. Overleaf automates these passes.

## Scope and overlap
This is the focused revision of the saved September architecture manuscript, using the requested identification-aware title. It is not an expansion by page count of the older 55-page workbook. The four-scenario diagnostic and router also appear in the later Market Transitions manuscript; these are shared results, not independent experiments. No validated live alpha, full causal discovery system or FPGA acceleration is claimed. No private logs or production settings are included.



