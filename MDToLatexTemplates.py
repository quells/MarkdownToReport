#!/usr/bin/python
# -*- coding: utf-8 -*-

def BuildDocument(doctype):
	if doctype == 'report':
		doctype = 'article'
	return '''\documentclass[11pt, oneside]{%s} 
\usepackage[margin=1in]{geometry} \geometry{letterpaper} 
\usepackage{setspace}
\usepackage[font=singlespacing,labelfont=bf]{caption}
\usepackage{indentfirst}
\usepackage{float}
\usepackage{booktabs}
\usepackage{amsmath, gensymb}
\usepackage{url}

\usepackage{graphicx}
\makeatletter
\def\maxwidth{0.6\columnwidth}
\makeatother
\let\Oldincludegraphics\includegraphics
\\renewcommand{\includegraphics}[1]{\Oldincludegraphics[width=\maxwidth]{#1}}

'''%(doctype)

def BuildTable(caption, alignments, headers, rows, label):
	latex = '''\\begin{table}[H]
\\caption{%s}
\\centering
\\begin{tabular}%s
\\hline
%s\\\\
\\hline
'''%(caption, alignments, headers)
	for r in rows:
		if type(r) == type('s'):
			latex += r
		else:
			latex += r[0] + ' & '.join(r[1:]) + '\\\\\n'
	latex += '''\\hline
\\end{tabular}
\\label{%s}
\\end{table}'''%(label)
	return latex

def BuildFigure(file, caption, label):
	return '''\\begin{figure}[H]
\\centering
\\includegraphics{%s}
\\caption{%s}
\\label{%s}
\\end{figure}'''%(file, caption, label)

def BuildTitle(title, subtitle):
	latex = ''
	if title != None:
		latex += r'\title{%s'%(title)
		if subtitle != None:
			latex += r'\\\vspace{0.5em}{\large %s}'%(subtitle)
		latex += '}\n'
	return latex

def BuildAuthor(author):
	latex = ''
	if author != None:
		latex += '\\author{%s}\n'%(author)
	return latex

def BeginDocument(doctype):
	latex = '\\date{}\n\n\\hyphenpenalty=100000\n\n\\begin{document}\n\n'
	if doctype == 'report':
		latex += '\\pagenumbering{gobble}\n'
	latex += '\\maketitle\n'
	return latex

def BuildInfoTable(Class, due, received):
	latex = ''
	if Class != None or due != None or received != None:
		latex += '''\\begin{table}[H]
\\centering
\\begin{tabular}{l}
'''
		if Class != None:
			latex += '%s\\\\\n'%(Class)
		if due != None:
			latex += 'Due: %s\\\\\n'%(due)
		if received != None:
			latex += 'Received: %s\\\\\n'%(received)
		latex += '''\end{tabular}
\end{table}
'''
	return latex

def BuildThanks(thanks):
	return '\\thanks{\\noindent %s\\\\\\\\}\n'%(thanks) if thanks != None else ''

def BuildAbstract(abstract):
	return '\\begin{noindent}\n\\textbf{%s}\n\\end{noindent}\n\n'%(abstract) if abstract != None else ''

def BuildList(kind, items):
	kind = 'enumerate' if kind == 'ordered' else 'itemize'
	latex = '\\begin{%s}\n'%(kind)
	for i in items:
		latex += '\t\\item %s'%(i)
	latex += '\\end{%s}\n'%(kind)
	return latex