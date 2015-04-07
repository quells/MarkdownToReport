FILENAME=Report
SCRIPT=MDToLatex.py
SILENCE=2> /dev/null || true

run: graphs tex pdf clean open

graphs:
	@echo Building graphs;
	@./graphs.py;

build: tex pdf clean open

tex: $(FILENAME).md
	@echo Building TEX;
	@python $(SCRIPT) $(FILENAME).md > $(FILENAME).tex

pdf: $(FILENAME).tex
	@echo Building PDF;
	@pdflatex $(FILENAME).tex > pdflatex1.log;
	@pdflatex $(FILENAME).tex > pdflatex2.log;

open: $(FILENAME).pdf
	@echo Opening PDF;
	@open $(FILENAME).pdf;

clean:
	@echo Cleaning up;
	@rm *.aux $(SILENCE);
	@rm *.log $(SILENCE);