#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import re
import MDToLatexTemplates as Templates
import subprocess

def match(string, regex):
	return True if re.match(re.compile(regex), string) else False

def ConvertMetadata(text):
	metadata_regex = r'^---\n(.*\n)+---$'
	if match(text, metadata_regex):
		metadata = {}
		for line in text.split('\n')[1:-1]:
			data = (':'.join(line.split(':')[1:])).strip(' ').strip('\'')
			for category in ['title', 'subtitle', 'author', 'class', 'due', 'received', 'thanks', 'abstract']:
				if match(line, category):
					metadata[category] = data
		return metadata
	return text

def ConvertHeader(text):
	header_regex = r'^#+ .*$'
	if match(text, header_regex):
		level = int(len(text.split(' ')[0]))
		header = text.split('#')[-1].lstrip(' ')
		if level == 1:
			latex = r'\section{%s}'
		elif level == 2:
			latex = r'\subsection{%s}'
		else:
			latex = r'\subsubsection{%s}'
		return latex%(header)
	return text

def ConvertTable(text):
	def TableJustification(a):
		ends = a[0] + a[-1]
		m = {'::': 'c', ':-': 'l|', '-:': 'r'}
		try:
			return m[ends]
		except KeyError:
			return 'c'
	
	table_regex = r'^\|(.*\|)+\n\|([:\-\|]+)\n(\|(.*\|)+)+'
	hline_regex = r'^[-]{3,}$'
	
	if match(text, table_regex):
		lines = text.split('\n')
		headers = ' & '.join([h.strip(' ') for h in lines[0].split('|')[1:-1]])
		alignments = '{|%s|}'%(''.join([TableJustification(a) for a in lines[1].split('|')[1:-1]]))
		rows = []
		for r in lines[2:-2]:
			if match(r, hline_regex):
				rows.append('\\hline\n')
			else:
				rows.append([c.strip(' ') for c in r.split('|')[:-1]])
		caption = lines[-2].lstrip(': ')
		label = lines[-1].lstrip('[').rstrip(']')
		return Templates.BuildTable(caption, alignments, headers, rows, label)
	return text

def ConvertFigure(text):
	figure_regex = r'^!\[.*\]\(.*\)\n\[.*\]'
	if match(text, figure_regex):
		lines = text.split('\n')
		caption = lines[0].split('[')[1].split(']')
		label = lines[1].lstrip('[').rstrip(']')
		file = caption[1].lstrip('(').rstrip(')')
		caption = caption[0]
		return Templates.BuildFigure(file, caption, label)
	return text

def ConvertList(text):
	ol_regex = r'(^\d+\. .+\n)+'
	if match(text, ol_regex):
		lines = text.split('\n')
		items = ['. '.join(l.split('. ')[1:]) for l in lines]
		return Templates.BuildList('ordered', items)
	
	ul_regex = r'(^- .+\n)+'
	if match(text, ul_regex):
		lines = text.split('\n')
		items = [l[2:] for l in lines]
		return Templates.BuildList('unordered', items)
	
	return text

if __name__ == '__main__':
	if len(sys.argv) > 1:
		filename = sys.argv[1]
		try:
			doctype = sys.argv[2]
		except IndexError:
			doctype = 'report'
	else:
		print 'No file provided.'
		sys.exit()

	with open(filename) as file:
		text = file.read()
		blocks = text.split('\n\n')
	
	latex = Templates.BuildDocument(doctype)
	for i in range(len(blocks)):
		b = blocks[i]
		if i == 0:
			metadata = ConvertMetadata(b)
			if metadata != b:
				title = metadata.get('title', None)
				subtitle = metadata.get('subtitle', None)
				latex += Templates.BuildTitle(title, subtitle)
				
				author = metadata.get('author', None)
				latex += Templates.BuildAuthor(author)
				
				latex += Templates.BeginDocument(doctype)
				
				Class = metadata.get('class', None)
				due = metadata.get('due', None)
				received = metadata.get('received', None)
				latex += Templates.BuildInfoTable(Class, due, received)
				
				thanks = metadata.get('thanks', None)
				latex += Templates.BuildThanks(thanks)
				
				abstract = metadata.get('abstract', None)
				latex += Templates.BuildAbstract(abstract)
				
				if doctype == 'report':
					latex += '\\newpage\n\\doublespacing\n'
				elif doctype == 'article':
					pass
				
				latex += '\\pagenumbering{arabic}\n\n'
				
				continue
		functions = [ConvertHeader, ConvertFigure, ConvertTable, ConvertList]
		c = [f(b) for f in functions if f(b) != b]
		latex += c[0] if len(c) > 0 else b
		latex += '\n\n'
	latex += '\\end{document}'
	print latex