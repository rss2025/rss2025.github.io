---
layout: page
title: Author Information
description: Instructions for paper submission.
invisible: false
published: true
priority: 8
---

There are two types of submissions to RSS:  (i) Science/Systems papers, and (ii) Demo papers. Both types of papers appear in the RSS proceedings. 

Science/Systems papers report on novel scientific and systems contributions via a conference paper, and are reviewed via a double-blind review process.  Demo papers must be accompanied by a conference demonstration (see details below), and can be reviewed via a single-blind review process as the demonstration content may reveal the affiliation of the authors. 

A single contribution should only be submitted as one type, either a Science/System paper or a Demo paper. If there is a novel robotic systems contribution that is properly evaluated against alternatives and does not obviously reveal the authors, the authors should submit it as a Science/System paper. If the authors’ contribution entails a demonstration and cannot be easily anonymized, authors should submit it as a Demo paper.

Details on the two types of submission and guidance for preparation are provided below. For details on the review process and rebuttal requirements, see the [Review Process]({{ site.baseurl }}/reviewps/) page.


## Guidance for Demo Preparation


**Type of Submission:** Demo papers will be published as part of the RSS conference proceedings. These submissions should demonstrate systems that are innovative given the state-of-the-art of robotics research across any of the [subject areas]({{ site.baseurl }}/information/cfp/#subject-areas) of RSS 2025. Open-source and open-access systems or interactive systems that are accessible by the community are especially encouraged. Demo papers can relate to hardware or software contributions or their integration. They can also relate to critical system components and useful tools for the community. Examples of such submissions can correspond to demonstrations of:

- useful new mechanisms or software packages for the robotics community,
- large-scale deployments of robotics technology that have not been achieved before,
- mature, production-ready industrial systems of note and lessons from their operation,
- new datasets and benchmarks that will advance robotics research,
- novel applications of robotics technology with important societal impact.

**What to Submit?** Each submitted Demo paper will include a manuscript describing the system (see format and length recommendations below) and demonstrations of the system itself, which can be accessed by reviewers via the supplementary material (e.g., executable software, multimedia showing the operation of robotic hardware, demonstrations of the achieved scalability, etc.), or via a link to a website that is accessible at the time of the review period.

**Single-blind:** Demo paper submissions are allowed (but not required) to be single-blind in contrast to Science/System papers, which must be double-blind. Demo paper submissions are understood to be demonstrating unique systems that will obviously reveal the authors or their affiliations. Demo papers are not opportunities to bypass the double-blind requirement of Science/System submissions. The reviewers will be asked to evaluate whether a submission was appropriately submitted under the Demo paper category.

**Submission Requirements:** The authors of Demo paper submissions are required to start the title of the submission with the word “Demonstrating” to communicate to the reviewers the type of  the submission and that they are allowed to be single-blind. 
The authors of Demo papers are also asked to include a short 1-paragraph section at the time of the submission titled “Intended Demonstration” (e.g., before or after the introduction section of their submitted manuscript), of how they envision that the RSS live audience will experience the demonstrated system. See examples of ways to demonstrate a system below. This section can be removed at the time of the Camera-Ready submission, if the Demo paper is accepted.

**Conference Demonstration:** Authors of accepted demo papers will be asked to demonstrate their system to the RSS attendees. Examples of how this can be achieved include: (i) an interactive demonstration of a software package at the conference, (ii) live demonstration of robotic hardware brought at the conference, (iii) videoconferencing to demonstrate a remote real-world deployment of a robotic system’s abilities. The authors of demo papers are asked to describe at the time of the submission how the RSS live audience will experience the demonstrated system.


**Evaluating Demo Papers:** A Demo paper should outline the design of the system and provide sufficient details to allow the evaluation of its validity, quality, and relevance to RSS. A Demo paper can do this by addressing some of the following questions:

- What problem does the proposed system address?
- Why is the system important and what is its impact?
- What is the novelty in the approach/technology on which this system is based?
- Who is the target audience?
- How does the system work?
- How does it compare with existing systems?
- How is the system licensed?
- Are there any additional concerns about the proposed system (e.g., ethical or environmental concerns)? 

**Review and Camera-ready:** The review process for Demo paper submissions will take place in parallel with the review of Science/System paper submissions. It will be handled by the same Program Committee. The proposed demonstrated system needs to be ready at Camera-Ready time to allow the proposed demonstration to take place. Additional improvements are allowed but should not diverge significantly from the description in the submitted Demo paper.

**Examples of Demo Papers** The Demo paper category was introduced in RSS 2023 and examples of accepted submissions are the following:

- [Demonstrating Mobile Manipulation in the Wild: A Metrics-Driven Approach](https://roboticsconference.org/2023/program/papers/055/)
<!-- - [Demonstrating Large Language Models on Robots](https://roboticsconference.org/2023/program/papers/024/) -->
- [Demonstrating Large-Scale Package Manipulation via Learned Metrics of Pick Success](https://roboticsconference.org/2023/program/papers/023/)
- [Demonstrating A Walk in the Park: Learning to Walk in 20 Minutes With Model-Free Reinforcement Learning](https://roboticsconference.org/2023/program/papers/056/)
<!-- - [Demonstrating RFUniverse: A Multiphysics Simulation Platform for Embodied AI](https://roboticsconference.org/2023/program/papers/087/) -->
- [Demonstrating Arena-Web: A Web-based Development and Benchmarking Platform for Autonomous Navigation Approaches](https://roboticsconference.org/2023/program/papers/088/)


**Note:** _Commercial sales and marketing activities are not appropriate for submissions in the RSS Demo Track and should be arranged instead via the RSS Sponsorship program._

## Paper and Demo Format

A template for paper and demo submissions is available in [LaTeX]({{ site.baseurl }}/docs/paper-template-latex.tar.gz) and [Word]({{ site.baseurl }}/docs/paper-template-word.zip). Do not modify the formatting provided in the templates. Any change to font sizes, page dimensions, line spacing, etc. may delay publication. Please do not include any additional markings such as _Draft or To appear in…_ on the pages. Make sure your paper does not contain page numbers.

We only accept a PDF format for the main submission file. Delays in the production of proceedings are usually caused by PDF file submissions that do not embed all fonts.

Before submitting your PDF file, please open it in Acrobat Reader. In the File menu under Document Properties, you will find information on the fonts used by your document. The PDF file must only contain Type-1 fonts (and Embedded True Type fonts if prepared under Word). On Linux, you may also use [pdffonts](https://www.xpdfreader.com/pdffonts-man.html). Below are instructions to embed PDF fonts for various typesetting systems:

- [Overleaf](https://www.overleaf.com/learn/latex/Questions/My_submission_was_rejected_by_the_journal_because_%22Font_XYZ_is_not_embedded%22._What_can_I_do%3F)
- [Acrobat](https://www.printivity.com/insights/2020/09/13/how-to-embed-fonts-in-pdfs/)
- [dvips](https://www.karlrupp.net/2016/01/embed-all-fonts-in-pdfs-latex-pdflatex/)
<!-- - [Miktex](http://www.boekenenproefschriften.nl/proefschriften/sites/default/files/EmbedLaTeXfonts.pdf) -->

## Paper and Demo Length {#paper-format}

RSS 2025 has no page length requirements on paper or demo submissions. Paper lengths have been typically around 8 pages in the past, and we expect that most submitted papers will have a similar length. The expectation for demo papers submissions is that they can be even shorter than that if the focus is on the supplementary material or an online website that allows the reviewers to experience the demonstrated system.

<!-- The main PDF should contain a concise and lucid presentation of the merits of the paper, including a discussion of its contributions, prior work, and a description of key technical ideas and methods used. The paper should be self-contained and include all the material necessary for an expert to verify the central claims in the paper. -->
The main PDF should contain a concise and lucid presentation of the merits of the paper, including a discussion of its contributions, prior work, and a description of key technical ideas and methods used. **The paper must include a “Limitations” section, describing shortcomings and open problems related to the proposed contribution.**  The paper should be self-contained and include all the material necessary for an expert to verify the central claims in the paper.

Additional supplemental text, such as appendices, data listings, or expanded proofs, should be included as supplementary material (see below). Reviewers will review supplemental material at their discretion for Science/System papers. For Demo papers, the reviewers will be guided to prioritize the supplemental material if the system is primarily available through the corresponding files.

Authors should anticipate that their papers may be rejected if the key technical result is not concisely presented. Reviewers may perceive a paper as too long if it is verbose, repetitive, or belabors obvious points. A paper that is 15 pages long is not necessarily going to be rejected, but the authors must make a compelling case that the length is essential to the key ideas in the paper. Moreover, the aesthetics of a paper also make the case for conciseness, since too much whitespace and poorly cropped figures are detrimental to the “feel” of a high-quality paper. Conversely, reviewers may perceive a paper as too short if it omits important details.


**Note:** _RSS was inspired to make this decision following other conferences, such as SIGGRAPH and FOCS. Researchers have wasted untold hours massaging formatting rules, figure sizes, and trimming paragraphs to fit page limits. The nominal reason for page limits in the electronic era is an upper bound on reviewers’ effort since they are expected to review “all the material” in the submission. It is inevitable that reviewers do not review material uniformly and will skim over text that is uninteresting or too dense; hence, page length is a poor proxy for reviewer effort. We will trust that authors will recognize that respecting reviewers’ time is a necessary condition to get published._

## Double-Blind Submission for Papers

RSS 2025 continues the tradition of double-blind reviews for Science and Systems papers. Authors should not list their names on the title page, and anonymity should be maintained in the paper. Authors are asked to take particular care when referencing their own work — careless use of self-citations can easily violate the requirements for double blind reviewing and this will result in papers being desk rejected.

The following principles should be applied for submissions in the Science/System paper category:

- Authors’ names and affiliations should not appear anywhere in the title or text of the submission.
- Acknowledgments to people or funding agencies should not appear in the submission.
- There should be no links to external websites (e.g. YouTube, github, authors institute pages) in the blinded submission. We recommend avoiding links even if they are anonymized. Links to external resources can be provided (and are highly encouraged) in the final camera-ready version of the paper.
- Authors must ensure that all metadata associated with the submission is anonymized.

In self-citing authors previous work, avoid expressions such as "In the authors earlier work…", rather use alternative expressions such as "In previous work…" or "In related work…", in a manner that does not distinguish their own work from the work of others. Authors should otherwise cite work, including their own, as required for the completeness of the submission.

In presentation of experimental work, avoid logos in pictures, or overt references to an individual laboratory. Use expressions such as "The experimental equipment…" rather than "The University of XYZ's Robby the Robot…". Otherwise, authors should include photographs, graphics and other presentation material as in the normal manner for a paper submission.

**Note:** _Demo submissions are allowed (but not required) to be single-blind in contrast to science and systems papers, which must be double-blind._ 

## Supplementary Materials for Papers and Demos

Authors may submit supplementary material such as a video or an expanded version of a proof. Especially in the context of Demo papers, authors are asked to provide supplementary material that allow the reviewers to experience and evaluate the demo. The deadline for supplementary material is a few days after the paper submission deadline.

Note that reviewers of Science/System paper submissions are not required to view this material and include it in their assessment of the paper.

**Authors of Science/System papers must ensure that all external links are removed for the initial and revised submissions, to ensure that their identities are not revealed for regular papers.**  External links are welcome to be included in the final camera-ready version of the paper.

## Rebuttal Preparation
A template for rebuttal submissions is available in [LaTeX]({{ site.baseurl }}/docs/rss2025-rebuttal-template-latex.zip) and [Word]({{ site.baseurl }}/docs/rss2025-rebuttal-template-word.zip). Rebuttals must be submitted in PDF format, following the same font embedding guidelines as the main paper submission.
<!-- Please refer to the [Paper and Demo Format](#paper-format) section for details on ensuring proper PDF formatting.  -->
For details on the review process and rebuttal requirements, see the [Review Process]({{ site.baseurl }}/reviewps/) page.

<div class="alert alert-warning" style="border: 1px solid #f0ad4e; padding: 10px; margin-top: 20px; background-color: #fcf8e3;">
<strong>Important Rebuttal Policy:</strong>
Rebuttals must be submitted as a <strong>one-page PDF</strong> following the rebuttal template (available in <a href="{{ site.baseurl }}/docs/rss2025-rebuttal-template-latex.zip">LATEX</a> and <a href="{{ site.baseurl }}/docs/rss2025-rebuttal-template-word.zip">Word</a>).
Rebuttals exceeding one page or failing to follow the required template’s formatting and anonymity guidelines will lead to a desk rejection decision for the corresponding paper. The authors will NOT be allowed to submit a new version of the paper during the rebuttal stage.
</div>

## Multiple Submissions of Papers and Demos

RSS submissions that are identical (or substantially similar) to versions that have been previously published, or accepted for publication, or that have been submitted in parallel to other conferences are not appropriate for RSS and violate the conference’s dual submission policy.

Exceptions to this rule are the following:

1. Submission is permitted for papers presented or to be presented at conferences or workshops that do not have published proceedings, or with only abstracts published.
2. It is acceptable to submit to RSS work that has been made available as a technical report (or similar, e.g., in arXiv) without citing it.


None of the above should be construed as overriding the requirements of other publishing venues. Also, keep in mind that author anonymity to RSS reviewers might be compromised for authors availing themselves of exceptions 1 and 2.

<div class="alert alert-warning" style="border: 1px solid #f0ad4e; padding: 10px; margin-top: 20px; background-color: #fcf8e3;">
<strong>Important Submission Policy:</strong> 
Submitting an abstract (by the January 17 deadline) or a semi-complete paper (by the January 24 deadline) for a paper that is currently under submission to another conference (e.g. ICRA, ICLR, CVPR) is still considered a double submission and is forbidden by RSS rules. However, if the paper has substantial innovation with respect to the paper that is already in submission (i.e., it would qualify as a different and novel paper and you would not withdraw it even if the paper under review is accepted), you should feel free to submit it to RSS.
</div>

## Plagiarism in Papers and Demos

RSS is intolerant of plagiarism. Submitted papers are expected to contain original work executed by the authors with adequate, proper, and scholarly citations to the work of others. It is the job of the authors to clearly identify both their own contribution(s) and published results / techniques on which they depend or build. RSS reviewers are charged to ensure these standards are met. In cases of alleged plagiarism, the program chair will be guided by Section 8.2.4 Allegations of Misconduct as laid out by the IEEE in this [document]({{ site.baseurl }}/docs/opsmanual.pdf).

## Policy on the Use of Large Language Models

We are following the example of [ICML](https://icml.cc/Conferences/2023/llm-policy) and adopt the following policy:

Papers that include text generated from a large language model (LLM), such as ChatGPT, are prohibited unless the produced text is presented as a part of the paper’s experimental analysis. Note the following clarification on the above statement:

- The policy prohibits text produced entirely by LLMs (i.e., "generated").  This does not prohibit authors from using LLMs for editing or polishing author-written text.
- The policy is largely predicated on the principle of being conservative with respect to guarding against potential issues of using LLMs, including plagiarism.
- This policy may evolve in future conferences as society understands LLMs and their impacts on scientific publishing better.

We plan to investigate any potential violation of the LLM policy when a submission is brought to our attention with a significant concern about a potential violation. Any submission flagged for the potential violation of this LLM policy will go through the same process as any other submission flagged for plagiarism.

## Uploading Files for Paper and Demo Submissions

Paper submission and review will occur in the OpenReview system at the following link: [https://openreview.net/group?id=roboticsfoundation.org/RSS/2025/Conference](https://openreview.net/group?id=roboticsfoundation.org/RSS/2025/Conference)
<!-- [https://openreview.net/group?id=roboticsfoundation.org/RSS/2025](https://openreview.net/group?id=roboticsfoundation.org/RSS/2025) -->

- **Logging into the system:** All **first** authors require an OpenReview account. If you already have an OpenReview account, use those credentials to login and update your profile. If you do not, sign up as a new user. New OpenReview profiles created without an institutional email will go through a moderation process that **can take up to two weeks**. New OpenReview profiles created with an institutional email will be activated automatically. 
- **Although we use OpenReview, the review process will be private, i.e., the papers will only be public after acceptance and the reviews will not be publicly visible.**
- **Conflict domains:** When you login for the first time, OpenReview will prompt you to enter your conflict domains. If you already have an OpenReview account, update your conflict domains. Please finish this step before you start the submission process.
- **Abstract Submission:** All submissions require the title/abstract of their paper(s) to be submitted by **January 17**, one week before the full paper submission. The PDF and Supplementary Material are not required for the title/abstract deadline, but **must be uploaded by the time of their respective deadlines.**
- **Paper/Demo submission:** Make sure your role is “Author”. Your main submission file may now be uploaded. Science/System and Demo paper descriptions must be in the conference style format and must be submitted as a PDF. Submissions may be edited, updated and replaced up to the paper submission deadline.
<!-- - **Demo paper title:**The authors of Demo paper submissions are asked to start the title of the submission with the word “Demonstrating” to communicate to the reviewers that these are submissions that are allowed to be single-blind. -->
- **Paper ID:** After clicking the Submit link, your paper or demo submission will be assigned an ID. To make sure your PDF submission is reviewer-friendly, enter this ID at the end of your title as instructed in the paper template.
- **Supplementary material:** Authors may submit supplementary material, such as a video or an expanded version of a proof (100MB max, accepted formats: zip). This year, the link to upload Supplementary Material is available from the start, but is not required until the Supplementary Material deadline. The deadline for the submission of supplementary material is **one week** after the deadline for paper and demo submissions.
- **This year the submission website includes checkboxes to ensure that papers comply with the submission requirements. Note that there are two sets of boxes, one for Science/Systems papers and the other one for Demo papers. The authors are only required to fill in the boxes corresponding to the type of paper they are submitting.**