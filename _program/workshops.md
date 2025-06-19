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

In case your workshop room becomes too crowded, we have designated three overflow rooms—RTH 306, OHE 542, and OHE 540—where in-person participants can view the workshop via Zoom. Please note that participants in these rooms are expected to use headphones or earphones out of courtesy to others.
<!-- <div style="text-align: center;">
    <img alt="Lely" src="/2024/images/RSS-workshops-map.png" style="width: 70%;" />
</div> -->

<div style="display: block; width: 100%; height: 20px;"></div>

### Locations

The poster sessions of the workshops will take place at <a href="https://maps.app.goo.gl/YTtHP12vrTdBQpce9">Epstein Family Plaza</a>. The workshops themselves will take place in the locations listed below.

<table class="table table-sm table-bordered" style="width: 100%; max-width: 800px;">
    <thead>
        <tr>
            <th>Abbreviation</th>
            <th>Building Name</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>OHE</strong></td>
            <td>
                <a href="https://maps.app.goo.gl/7MeyzQTmTTndmX4V7" target="_blank">
                    Olin Hall of Engineering (OHE)
                </a>
            </td>
        </tr>
        <tr>
            <td><strong>RTH</strong></td>
            <td>
                <a href="https://maps.app.goo.gl/ceZrio6J48qrKjR2A" target="_blank">
                    Ronald Tutor Hall (RTH)
                </a>
            </td>
        </tr>
        <tr>
            <td><strong>EEB</strong></td>
            <td>
                <a href="https://maps.app.goo.gl/NdjNejypwhrFyAJo8" target="_blank">
                    Hughes Aircraft Electrical Engineering Center (EEB)
                </a>
            </td>
        </tr>
        <tr>
            <td><strong>SGM</strong></td>
            <td>
                <a href="https://maps.app.goo.gl/pM3eKVpUak6BXmS36" target="_blank">
                    Seeley G. Mudd Building (SGM)
                </a>
            </td>
        </tr>
    </tbody>
</table>




<div style="text-align: center; margin: 3em auto;">
  <img src="{{ site.baseurl }}/images/local2025/workshops.png"
       alt="Map of RSS 2025 workshop locations"
       style="max-width: 75%; height: auto; border-radius: 6px;">
  <div style="margin-top: 0.5em; font-size: 0.9em; color: #666;">
    Map of RSS 2025 workshop locations
  </div>
</div>


<!-- 
<table class="table table-sm table-bordered" style="width: 100%; max-width: 800px;">
    <thead>
        <tr>
            <th>Abbreviation</th>
            <th>Building Name</th>
            <th>Address</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>OHE</strong></td>
            <td>
                <a href="https://maps.app.goo.gl/7MeyzQTmTTndmX4V7" target="_blank">
                    Olin Hall of Engineering (OHE)
                </a>
            </td>
            <td>3650 McClintock Ave, Los Angeles, CA 90089</td>
        </tr>
        <tr>
            <td><strong>RTH</strong></td>
            <td>
                <a href="https://maps.app.goo.gl/ceZrio6J48qrKjR2A" target="_blank">
                    Ronald Tutor Hall (RTH)
                </a>
            </td>
            <td>3710 McClintock Ave, Los Angeles, CA 90089</td>
        </tr>
        <tr>
            <td><strong>EEB</strong></td>
            <td>
                <a href="https://maps.app.goo.gl/NdjNejypwhrFyAJo8" target="_blank">
                    Hughes Aircraft Electrical Engineering Center (EEB)
                </a>
            </td>
            <td>3740 McClintock Ave, Los Angeles, CA 90089</td>
        </tr>
        <tr>
            <td><strong>SGM</strong></td>
            <td>
                <a href="https://maps.app.goo.gl/pM3eKVpUak6BXmS36" target="_blank">
                    Seeley G. Mudd Building (SGM)
                </a>
            </td>
            <td>3620 McClintock Ave, Los Angeles, CA 90089</td>
        </tr>
    </tbody>
</table> -->


<div style="display: block; width: 100%; height: 20px;"></div>

### Saturday, June 21 
#### (Half-day Morning Events)
<div style="margin-bottom: 10px; font-style: italic; color: #333;">
    <strong>Morning coffee on June 21 will be in <a href="https://maps.app.goo.gl/YTtHP12vrTdBQpce9">Epstein Family Plaza</a> (not Founders Park) from 10:00–11:00 AM.</strong>
</div>

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

