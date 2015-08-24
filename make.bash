#!/bin/bash

source ~/.bin/md_report.bash

FILENAME=Report

function clean_project() {
	echo "Cleaning up";
	rm *.aux 2> /dev/null || true;
	rm *.log 2> /dev/null || true;
	return 1;
}

function make_tex() {
	echo "Building TEX";
	md2tex "$FILENAME.md" > "$FILENAME.tex";
}

function make_pdf() {
	echo "Building PDF";
	pdflatex "$FILENAME.tex" > pdflatex1.log;
	pdflatex "$FILENAME.tex" > pdflatex2.log;
}

function open_pdf() {
	echo "Opening PDF";
	open "$FILENAME.pdf";
}

function count_tex() {
	texcount "$FILENAME.tex";
}

function run() {
	clean_project; make_tex; make_pdf; clean_project; open_pdf;
}

function build() {
	clean_project; make_tex; make_pdf; clean_project; count_tex;
}