---
layout: post
title: Paper Format
---

We only accept submissions in PDF. Submissions may be up to 8 pages in length, including figures but possibly excluding references. Additional pages can be used for references. However, the 9th page, and any subsequent pages, can contain ONLY references. This will be strictly enforced. Submissions can use a font no smaller than 10 point. Submissions violating these guidelines will not be considered. A paper template is available in <a href="{{site.baseurl}}/docs/paper-template-latex.tar.gz">Latex</a> and <a href="{{site.baseurl}}/docs/paper-template-word.zip">Word</a>.

Do not modify the formatting provided in the templates. Any change to font sizes, page dimensions, line spacing, etc. may delay the publication of your paper. Please do not include any additional markings such as <i>Draft</i> or <i>To appear in...</i> on the pages. Make sure your paper does not contain page numbers. 

Submit a PDF-format paper. We do not accept papers submitted after the deadline no matter what the reason is, so please check on your ability to convert to PDF early. Delays in the production of proceedings are usually caused by PDF file submissions that do not embed all fonts. Please follow the below instructions to ensure that your PDF document will not suffer from this problem.

When preparing your document in LateX, make sure to create the PDF file from your LateX source by use of these commands:

{% highlight js %}
latex paper.tex
dvips paper.dvi -o paper.ps -t letter -Ppdf -G0
ps2pdf paper.ps 
{% endhighlight %}


The arguments provided to dvips will ensure that all fonts are embedded in the PDF file produced by ps2pdf.
Before submitting your PDF file, please open it in Acrobat Reader. In the File menu under Document Properties, you will find information on the fonts used by your document. The PDF file should only contain Type-1 fonts (and Embedded True Type fonts if prepared under Word). If you correctly followed the instructions above but your document contains other types of fonts, then these may have been included as part of your figures. Again, please ensure that your submission contains only Type-1 or Embedded True Type fonts and not Type-3 fonts.