PYTHON ?= ../.venv/bin/python
PDFLATEX ?= pdflatex
BIBTEX ?= bibtex

.PHONY: all assets analyze verify clean
all: assets
	$(PDFLATEX) -interaction=nonstopmode -halt-on-error main.tex
	$(BIBTEX) main
	$(PDFLATEX) -interaction=nonstopmode -halt-on-error main.tex
	$(PDFLATEX) -interaction=nonstopmode -halt-on-error main.tex
	cp main.pdf cognitive-atlas-paper.pdf
assets:
	cd .. && $(PYTHON:../%=%) -m paper.revision100.build
verify:
	cd .. && $(PYTHON:../%=%) -m paper.revision100.verify
analyze:
	cd .. && $(PYTHON:../%=%) -m paper.revision100.error_control
	cd .. && $(PYTHON:../%=%) -m paper.revision100.local
	cd .. && $(PYTHON:../%=%) paper/revision100/qc.py
	cd .. && $(PYTHON:../%=%) paper/revision100/geometry.py
	cd .. && $(PYTHON:../%=%) paper/revision100/calibration.py
	cd .. && $(PYTHON:../%=%) paper/revision100/range_geometry.py
clean:
	rm -f main.aux main.bbl main.blg main.log main.out main.pdf
