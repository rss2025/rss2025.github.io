---
layout: page
title: Pioneer rooms
description: Roster board numbers and poster roomsdetails
days: ['Mon', 'Fri']
priority: 9
invisible: false
published: false
---


<div style="display: block; width: 100%; height: 20px;"></div>

<div style="text-align: center;">
    <img alt="Lely" src="/2024/images/map.png" style="width: 80%;" />
</div>

## Pioneer (16 July)


<table class="table table-striped table-workshop">
    <thead>
        <tr>
            <th width="25%">Title</th>
            <th width="25%">Location</th>
            <th width="25%">PosterBoardNr</th>
        </tr>
    </thead>
    <tbody>
        {% for workshop in site.data.pioneer1 %}
        <tr>
            <td>{{ workshop.Title }}</td>
            <td>{{ workshop.Location }}</td>
            <td>{{ workshop.PosterBoardNr }}</td>
        </tr>
        {% endfor %}
    </tbody>
</table>

## Pioneer (17 July)



<table class="table table-striped table-workshop">
    <thead>
        <tr>
            <th width="25%">Title</th>
            <th width="25%">Location</th>
            <th width="25%">PosterBoardNr</th>
        </tr>
    </thead>
    <tbody>
        {% for workshop in site.data.pioneer2 %}
        <tr>
            <td>{{ workshop.Title }}</td>
            <td>{{ workshop.Location }}</td>
            <td>{{ workshop.PosterBoardNr }}</td>
        </tr>
        {% endfor %}
    </tbody>
</table>

## Pioneer (18 July)



<table class="table table-striped table-workshop">
    <thead>
        <tr>
            <th width="25%">Title</th>
            <th width="25%">Location</th>
            <th width="25%">PosterBoardNr</th>
        </tr>
    </thead>
    <tbody>
        {% for workshop in site.data.pioneer3 %}
        <tr>
            <td>{{ workshop.Title }}</td>
            <td>{{ workshop.Location }}</td>
            <td>{{ workshop.PosterBoardNr }}</td>
        </tr>
        {% endfor %}
    </tbody>
</table>


