---
layout: page
title: Workshops
description: Workshop times, venues, and details.
days: ['Mon', 'Fri']
priority: 9
invisible: false
published: true
---


Workshops will take place across two days of the conference on **Saturday, June 21 (half-day events held in the morning)** and **Wednesday, June 25 (full-day events)**. Each workshop is organized as a semi-independent event, and has a unique schedule reflecting the planned activities, constraints and preferences of the organizers. Please check the workshop websites for more details on their particular schedules.


<!-- <div style="text-align: center;">
    <img alt="Lely" src="/2024/images/RSS-workshops-map.png" style="width: 70%;" />
</div> -->


<div style="display: block; width: 100%; height: 20px;"></div>

### Saturday, June 21 
#### (Half-day Morning Events)
{% assign innerdays = "19th, tbd" | split: ", " %}

<table class="table table-striped table-workshop">
    <thead>
        <tr>
            <th width="10%" align="center">ID</th>
            <th width="20%">Location</th>
            <th width="40%">Title</th>
            <th width="20%">Website</th>
        </tr>
    </thead>
    <tbody>
        {% for workshop in site.data.rss2025ws_halfday %}
        <tr>
            <td><span style="font-weight:bold; color: #3a3946;"> {{ workshop.id }} </span></td>
            {% if workshop.link != "" %}
                <td><a href="{{ workshop.link }}">{{ workshop.location }}</a></td>
            {% else %}
                <td>{{ workshop.location }}</td>
            {% endif %}
            <td>{{ workshop.title }}</td>
            <td>
                <a href="{{ workshop.website }}">
                    {{ workshop.website }}
                </a>
            </td>
        </tr>
        {% endfor %}
    </tbody>
</table>

### Wednesday, June 25 
#### (Full-day Events)
{% assign innerdays = "19th, tbd" | split: ", " %}

<table class="table table-striped table-workshop">
    <thead>
        <tr>
            <th width="10%" align="center">ID</th>
            <th width="20%">Location</th>
            <th width="40%">Title</th>
            <th width="20%">Website</th>
        </tr>
    </thead>
    <tbody>
        {% for workshop in site.data.rss2025ws_fullday %}
        <tr>
            <td><span style="font-weight:bold; color: #3a3946;"> {{ workshop.id }} </span></td>
            {% if workshop.link != "" %}
                <td><a href="{{ workshop.link }}">{{ workshop.location }}</a></td>
            {% else %}
                <td>{{ workshop.location }}</td>
            {% endif %}
            <td>{{ workshop.title }}</td>
            <td>
                <a href="{{ workshop.website }}">
                    {{ workshop.website }}
                </a>
            </td>
        </tr>
        {% endfor %}
    </tbody>
</table>


<span style="color:white; font-size:50px;">&nbsp;</span><br>
<span style="color:white; font-size:50px;">&nbsp;</span><br>
<span style="color:white; font-size:50px;">&nbsp;</span><br>
<span style="color:white; font-size:50px;">&nbsp;</span><br>
<span style="color:white; font-size:50px;">&nbsp;</span><br>


<script>
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
</script>

