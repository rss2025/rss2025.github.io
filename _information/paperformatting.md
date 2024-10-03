---
layout: page
title: Submission Formatting and Presentation
description: Submission Formatting and Presentation Guidelines
invisible: true
published: false
---

## Requirements

### Document Format

We only accept submissions in PDF.  We do not accept papers submitted after the
deadline no matter what the reason is, so please check on your ability to
convert to PDF early. 

### Templates

A paper template is available and is linked below.  Do not modify the formatting provided in the templates. Any change to font
sizes, page dimensions, line spacing, etc. may delay the publication of your
paper. Please do not include any additional markings such as <i>Draft</i> or
<i>To appear in...</i> on the pages. Make sure your paper does not contain page
numbers. 

### Paper Length
For RSS 2021, no arbitrary maximum (or minimum) length is imposed on papers.
Reviewers will be instructed that they do not need to review material
other than the abstract, references, and the first eight pages. Papers
will not be summarily rejected for exceeding eight pages of technical
content, but authors should not expect the reviewers to read beyond
eight pages.

<br>

## Recommendations and Suggestions*

### Paper Presentation

Submissions should be written such that their content, style, and appearance 
aid the reviewing process.
Authors should keep in mind that
their submission will be evaluated not only by experts in their subarea but
also by the entire PC. The submission should be addressed to a broad spectrum
of roboticists, not solely to experts in a single subarea.


Poor presentation may result in rejection either indirectly (the reviewers fail
to appreciate the merits of the submission) or directly (the PC decides that
the community will be better served by the paper being revised and
resubmitted). 

### Length Considerations
Since RSS 2021 has no arbitrary maximum page count,
the first eight pages of a submission should contain a concise and lucid 
presentation of the merits of the paper, including a discussion of its
importance, prior work, and an outline of key technical ideas and methods used
to achieve the main claims. The submission should also allow reviewers to
easily expand their understanding of any of the specifics to the extent they
deem important to the evaluation of the submission. Ideally, it should include
all of the ideas necessary for an expert to fully verify the central claims in
the paper.

Authors should anticipate that their papers may be
rejected if the key technical result is not adequately presented and
evaluated in the first eight pages. The reason we have removed the page
limit is to acknowledge that the page limit is arbitrary, and there may
be good reasons to take a little more space.  Papers may be perceived as too long if they are 
verbose or repetitive, or too short if they omit important details or tamper with formatting
rules just to save on page count. 

*In optimization jargon: Think of the paper length not as a constraint but as a
cost.* 

### Templates and Font Embedding

A paper template is available in <a
href="{{site.baseurl}}/docs/paper-template-latex.tar.gz">LaTeX</a> and <a
href="{{site.baseurl}}/docs/paper-template-word.zip">Word</a>.

Submit a PDF-format paper. Delays in the production of proceedings are usually caused by PDF file
submissions that do not embed all fonts. Please follow the below instructions
to ensure that your PDF document will not suffer from this problem.

When preparing your document in LaTeX, make sure to create the PDF file from
your LaTeX source using these (or equivalent, xelatex or pdflatex) commands:

{% highlight js %}
latex paper.tex
dvips paper.dvi -o paper.ps -t letter -Ppdf -G0
ps2pdf paper.ps 
{% endhighlight %}


The arguments provided to dvips will ensure that all fonts are embedded in the PDF file produced by ps2pdf.


<br>

* 
<span style="font-size:smaller;">
These guidelines borrow heavily from those used by <a href="https://s2020.siggraph.org/submissions/technical-papers-submissions/technical-papers-submissions-faq/">Siggraph</a> and <a href="https://windowsontheory.org/2013/02/11/focs-2013-cfp/">FOCS</a>.
RSS's historic role as bellwether for the robotics community, and these <a href="https://windowsontheory.org/2013/01/28/away-with-page-limits-on-submissions/">blog</a> <a href="https://windowsontheory.org/2013/06/03/away-with-page-limits-on-submissions-ii/">posts</a> have motivated this new approach.
</span>
