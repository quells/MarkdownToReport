# MarkdownToReport

Collection of scripts used to convert a Markdown file into LaTeX for publishing a report as a PDF.

This isn't necessarily meant to be useful to anyone else; it's more a way of forcing myself to clean up and write some documentation for something I made while half-asleep.

This is primarily inspired by [Dr. Drang's](http://www.leancrew.com/all-this/) [report writing workflow](http://www.leancrew.com/all-this/2014/01/my-report-writing-workflow/). These scripts are less sophisticated because I've had about 24 hours to tinker with them instead of years, but it works OK. Mostly I was tired of fighting [Pandoc](http://pandoc.org).

The templates for various LaTeX objects (figures and tables mostly) are defined in `MDToLatexTemplates.py`. These are the settings I use for my school reports. It's an ugly file with randomly formatted strings. I wrote this at one in the morning when I should have been working on an actual lab report. Or sleeping. I should do that now.

Text is parsed in `MDToLatex.py`. It's mostly what you would expect. I tried to write functions in a _functional_ style, with graceful failure if text parsing failed. This is particularly handy towards the end of the script where the different parsing functions are applied.

`Report.md` is a sample document with some basic examples of formatting for metadata, figures, and tables.

`makefile` is what puts everything together. You can have it generate graphs and then build the PDF with the brand new images. I think it's handy.

## Required

- Python 2.7 
- pdflatex (or equivalent LaTeX to PDF program)

## TODO

- Markdown style formatting for _italicized_ and **bolded** body text instead of LaTeX formatting.
- Clean up `MDToLatexTemplates.py`
