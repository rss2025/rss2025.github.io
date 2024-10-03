---
layout: default
title: Paper Session
description: Paper Session.
priority: 10
invisible: false
published: false
---

<div class="page" id="inner-content">
<style>
* {
  box-sizing: border-box;
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
</style>

<h1 class="page-title">{{ page.title }}</h1>
<br/>

<div style="width: 100%; text-align: center;">
<div style="width: 100%; text-align: center; margin-top: -20px;  margin-bottom: 15px;">
  <i id="chairedby"></i>
</div>
<div class="paper-authors">
<div class="paper-author-box">
    <div id="c1" class="paper-author-name"></div>
    <div id="c1a" class="paper-author-uni"></div>
</div>
<div class="paper-author-box">
    <div id="c2" class="paper-author-name"></div>
    <div id="c2a" class="paper-author-uni"></div>
</div>
</div>
<hr>

<table id="myTable">
  <tr class="toprowHeader">
    <th>Order In Session</th>
    <th>Title</th>
    <th>Authors</th>
  </tr>
 {% for paper in site.data.rss2023CameraReadyInfo %}
 <tr session="{{ paper.SessionName }}">
    <td width="5%" height="100px">{{paper.OrderinSession }}</td>
    <td width="45%" height="100px" ><a href="{{ site.baseurl }}/program/papers/{{ paper.PaperIDZeroes
}}/"><b>{{paper.PaperTitle}}</b></a></td>
    <!-- <td width="40%" height="100px">{{paper.AuthorNames | replace: ';', ','}}</td> -->
    <td width="40%" height="100px">{{ paper.AuthorNames | replace: ';', ',' | truncatewords: 40, "&nbsp;<button type='button' class='collapsible' style='border:none;background:none;font-size:smaller;color:#222299;'>...more&gt;</button>"}}
      <div class="content" style="display:none; padding-top:20px;">
        {{ paper.AuthorNames | replace: ';', ','}}
      </div>
    </td>
  </tr>
{% endfor %}
</table>

<br>

<script>
(function($) {
    $.QueryString = (function(a) {
        if (a == "") return {};
        var b = {};
        for (var i = 0; i < a.length; ++i)
        {
            var p=a[i].split('=');
            if (p.length != 2) continue;
            b[p[0]] = decodeURIComponent(p[1].replace(/\+/g, " "));
        }
        return b;
    })(window.location.search.substr(1).split('&'))
})(jQuery);
 
// Usage


var $rows = $('#myTable tr');
$(document).ready(function() {
    dirtyParam = jQuery.QueryString["session"];
    sessionName = dirtyParam.replaceAll('%20', ' ').replaceAll('%26','&');
    searchKey = "tr[session='"+ sessionName +"'],.toprowHeader";
    $rows.hide().filter(searchKey).show();
    $(".page-title").text("Session "+sessionName);


    param = jQuery.QueryString["c1"];
    if(param)
    {
      $("#chairedby").text("Chaired By");
    }
    param = jQuery.QueryString["c1"];
    if(param)
    {
      name = param.replaceAll('%20', ' ').replaceAll('%26','&');
      $("#c1").text(name);
    }
    param = jQuery.QueryString["c2"];
    if(param)
    {
      name = param.replaceAll('%20', ' ').replaceAll('%26','&');
      $("#c2").text(name);
    }
    param = jQuery.QueryString["c1a"];
    if(param)
    {
      name = param.replaceAll('%20', ' ').replaceAll('%26','&');
      $("#c1a").text(name);
    }
    param = jQuery.QueryString["c2a"];
    if(param)
    {
      name = param.replaceAll('%20', ' ').replaceAll('%26','&');
      $("#c2a").text(name);
    }
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




<br/>
<br/>
<br/>
<br/>
<br/>
<center><footer style="color: lightslategray;">
  <small style="line-height: 95%;"><p style="padding-bottom: 2px; margin-bottom: 2px;">This page needs javascript to function.</p></small>
</footer>
</center>
</div>