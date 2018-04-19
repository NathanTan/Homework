make:
	rm -f template.pdf
	latex template
	bibtex template
	latex template
	latex template
	dvips template.dvi
	ps2pdf template.ps
	rm -f template.aux
	rm -f template.dvi
	rm -f template.log
	rm -f template.ps
	rm -f template.bbl
	rm -f template.blg
	echo "PDF is complete."
