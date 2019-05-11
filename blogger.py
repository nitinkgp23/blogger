#!/usr/bin/env python
# coding: utf-8

import os
import sys
from datetime import datetime


def read_file(filepath):	

	fname = filepath.split('.')[0].split('/')[-1]
	with open(filepath, 'r') as temp:
	    content = temp.read()

	return content, fname

def take_inputs(fname):
	'''Function for taking inputs for the blog'''

	print("Getting a few more details of the blog..")
	title = input("Please enter the title of the blog ({}):".format(fname)) or fname

	date = datetime.now().strftime("%Y-%m-%d")
	date = input("Please enter the date of publish ({}):".format(date)) or date

	desc = input("Please enter a short description of your blog:")

	categories_inp = input("Please enter the categories separated by a comma:").split(',')
	categories = [x.strip() for x in categories_inp if x]
	categories_str = "\n - ".join(categories)

	tags_inp = input("Please enter the tags separated by a comma:").split(',')
	tags = [x.strip() for x in tags_inp if x]
	tags_str = "\n - ".join(tags)

	return title, date, desc, categories_str, tags_str	

def main():

	blog_path = '/Users/nitinchoudhary/Projects/nitinkgp23.github.io/_posts/'

	math ='''
<script type="text/javascript" async
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
'''
	

	if len(sys.argv) < 1:
		raise Exception("Script requires one argument")
	filepath = os.path.abspath(" ".join(sys.argv[1:]))
	content, fname = read_file(filepath)

	title, date, desc, categories_str, tags_str = take_inputs(fname)
	filename = "{date}-{title}.md".format(date=date, title=title)


	filestring = '''---
title: {title}
description: {desc}
date: {date}
categories:
 - {categories_str}
tags:
 - {tags_str}
comments: true
---

{math}

{content}
'''.format(title=title,
	          desc=desc,
	          date=date,
	          categories_str=categories_str,
	          tags_str=tags_str,
	          math=math,
	          content=content)

	with open(os.path.join(blog_path, filename), 'w') as temp_file:
	    temp_file.write(filestring)

if __name__ == '__main__':
	main()







