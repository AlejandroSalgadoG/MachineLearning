Article_mds.pdf: Article_mds.tex Article_mds.bib
	pdflatex Article_mds.tex
	bibtex Article_mds
	pdflatex Article_mds.tex
	pdflatex Article_mds.tex
	pdflatex Article_mds.tex

clean:
	rm -f Article_mds.pdf
	rm -f *.nav *.snm *.toc *.out *.dvi *.blg *.bbl *.aux *.log

exe:
	evince Article_mds.pdf &
