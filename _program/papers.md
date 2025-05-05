---
layout: page
title: Accepted Papers
description: Accepted papers.
priority: 10
invisible: false
published: true
---

<style>
* {
  box-sizing: border-box;
}

#myInput {
  background-position: 10px 10px;
  background-repeat: no-repeat;
  width: 100%;
  font-size: 100%;
  padding: 12px 20px 12px 40px;
  border: 1px solid #ddd;
  margin-bottom: 12px;
}

#myTable {
  border-collapse: collapse;
  width: 100%;
  border: 1px solid #ddd;
  font-size: 100%;
}

#myTable th, #myTable td {
  text-align: left;
  padding: 12px;
}

#myTable tr {
  border-bottom: 1px solid #ddd;
}

#myTable tr.header, #myTable tr:hover {
  background-color: #f1f1f1;
}

#search{
  border-radius: 5px;
  margin-bottom: 10px;
  width: 50%;
  min-width: 200px;
  max-width: 400px;
  height: 2em;
  border: 1px solid gray;
}
</style>

The overview of the conference program is available <a href="{{ site.baseurl }}/program/overview/"><strong>[here]</strong></a>. Please refer to the conference program for additional information. Check the list of paper sessions <a href="{{ site.baseurl }}/program/allsessions/"><strong>[here]</strong></a>.

<hr>

<div style="align-content: right; text-align: right; justify-content: right;">
  <input type="text" id="search" placeholder="Type to search">
</div>

<table id="myTable">
  <tr class="toprowHeader">
    <th>ID</th>
    <th>Session</th>
    <th>Title</th>
    <th>Authors</th>
  </tr>
 {% for paper in site.data.rss2025CameraReadyInfo %}
 <tr session="{{ paper.SessionName }}">
    <td width="5%" height="100px">{{ paper.PaperID }}</td>
    <td width="15%" height="100px"><span style="font-size: smaller;">{{ paper.CleanSessionName }}</span></td>
    <!-- <td width="40%" height="100px"><a href="{{ site.baseurl }}/program/papers/{{ paper.PaperIDZeroes }}/"><b>{{ paper.PaperTitle }}</b></a></td> -->
    <!-- <td width="40%" height="100px"><b>{{ paper.PaperTitle }}</b></td> -->
    <td width="40%" height="100px">
      <a href="{{ site.baseurl }}/program/papers/{{ paper.PaperID }}/">
        <b>{{ paper.PaperTitle }}</b>
      </a>
    </td>
    <td width="40%" height="100px">
      {{ paper.AuthorNames | replace: ';', ',' | truncatewords: 40, "&nbsp;<button type='button' class='collapsible' style='border:none;background:none;font-size:smaller;color:#222299;'>...more&gt;</button>" }}
      <div class="content" style="display:none; padding-top:20px;">
        {{ paper.AuthorNames | replace: ';', ',' }}
      </div>
    </td>
  </tr>
{% endfor %}
</table>

<br>

<script>
var $rows = $('#myTable tr');
$('#search').keyup(function() {

    var val = '^(?=.*\\b' + $.trim($(this).val()).split(/\s+/).join('\\b)(?=.*\\b') + ').*$',
        reg = RegExp(val, 'i'),
        text;

    $rows.show().filter(function() {
        text = $(this).text().replace(/\s+/g, ' ');
        return !reg.test(text);
    }).not('.toprowHeader').hide();
});
</script>


<script>
var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    this.style.display = "none";
    var content = this.nextElementSibling;
    var c = this.parentElement;
    c.innerHTML = content.innerHTML;
    });
}
</script>


{% comment %}



<div id="papers" class="row text-center">
    {% for paper in site.data.rss2020_papers %}
    {% capture modulo %}{{ forloop.index0 | modulo:4 }}{% endcapture %}
    {% if modulo == '0' %}<div class="row text-center">{% endif %}
        <div class="col-sm-6">
            <a href="{{ paper.PaperTitle }}">temp</a><br>
		<i>{{ paper.AuthorNames }}</i><br>
        </div>
    {% if modulo == '3' or forloop.last %}</div>{% endif %}
    {% endfor %}
</div>


<ul>
{% for paper in site.data.rss2020_papers %}
<li>
  <a href="{{ site.baseurl }}/program/papers/{{ paper.PaperOrder}}/">
    {{ paper.PaperTitle}}
  </a>
  <br/>
  {{ paper.AuthorNames }}
</li>
<br/>
{% endfor %}
</ul>

<ul>
{% for paper in site.data.papers %}
<li>
  <a href="{{ site.baseurl }}/program/papers/{{ paper.external_id }}/">
    {{ paper.title }}
  </a>
  <br/>
  {{ paper.authors }}
  {% for award in site.data.award_finalists %}
  {% if award.internal_id == paper.internal_id %}
  <br/>
  <b>{{ award.type }} Award {{ award.status }}</b>
  {% endif %}
  {% endfor %}
</li>
<br/>
{% endfor %}
</ul>

{% endcomment %}
