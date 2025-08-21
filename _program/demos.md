---
layout: page
title: Demos
description: Demos times, venues, and details.
days: ['Mon', 'Fri']
priority: 7
invisible: false
published: true
---


<div style="display: block; width: 100%; height: 20px;"></div>

<table class="table table-striped table-workshop">
    <thead>
        <tr>
            <th width="5%" align="center">ID</th>
            <th width="15%">Location</th>
            <th width="40%">Title</th>
            <!-- <th width="20%">Website</th> -->
            <th width="15%">Day</th>
            <th width="15%">Time</th>
        </tr>
    </thead>
    <tbody>
        {% for workshop in site.data.demos %}
        <tr>
            <td><span style="font-weight:bold; color: #3a3946;"> {{ workshop.papernumber }} </span></td>
            <td>{{ workshop.demolocation | default: "TBD" }}</td>
            <td>
                <a href="{{ site.baseurl }}{{ workshop.link }}">
                <strong>{{ workshop.papertitle }}</strong>
                </a>
            </td>
            <!-- <td>{{ workshop.papertitle }}</td> -->
            <!-- <td style="word-break: break-all;">
                <a href="{{ workshop.link }}">
                    {{ workshop.link }}
                </a>
            </td> -->
             <td>{{ workshop.demoday | default: "TBD"}}</td>
             <td>{{ workshop.time | default: "TBD" }}</td>
        </tr>
        {% endfor %}
    </tbody>
</table>

<span style="color:white; font-size:50px;">&nbsp;</span><br>

<!-- <div style="text-align: center;">
    <img alt="Lely" src="/2024/images/demos.png" style="width: 50%;" />
</div>


<span style="color:white; font-size:50px;">&nbsp;</span><br>
<span style="color:white; font-size:50px;">&nbsp;</span><br>
<span style="color:white; font-size:50px;">&nbsp;</span><br>
<span style="color:white; font-size:50px;">&nbsp;</span><br> -->


<!-- <script>
var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    this.style.display = "none";
    var content = this.nextElementSibling;
    //if (content.style.display === "block") {
    //  content.style.display = "none";
    //} else {
    //  content.style.display = "block";
    //}
    var c = this.parentElement;
    c.innerHTML = content.innerHTML;
    });
}
</script> -->

