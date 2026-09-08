PYTHON ?= ../.venv/bin/python
PDFLATEX ?= pdflatex
BIBTEX ?= bibtex

.PHONY: all assets analyze clean
all: assets
	$(PDFLATEX) -interaction=nonstopmode -halt-on-error main.tex
	$(BIBTEX) main
	$(PDFLATEX) -interaction=nonstopmode -halt-on-error main.tex
	$(PDFLATEX) -interaction=nonstopmode -halt-on-error main.tex
	cp main.pdf cognitive-atlas-paper.pdf
assets:
	cd .. && $(PYTHON:../%=%) paper/scripts/build_assets.py
analyze:
	cd .. && $(PYTHON:../%=%) paper/scripts/check_distance_structure.py
	cd .. && $(PYTHON:../%=%) paper/scripts/check_language_differences.py
	cd .. && $(PYTHON:../%=%) paper/scripts/local_language.py
clean:
	rm -f main.aux main.bbl main.blg main.log main.out main.pdf
