# 📸PhotoSort

<div align="left">
  <img src="assets/photosort.png" alt="preview of photosort" height="150" />
</div>

Simple python GUI app for sorting photos and videos into folders by year and months.

[![python](https://img.shields.io/badge/Python-3.9-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)

## 📂Table of content
- [Introduction](#introduction)

## 📑Introduction
I wrote this application to solve my problem with unorganized folders with my photos. I had many folders with photos and videos all over my laptop. It wouldn't be much of an issue. But sometimes I just want to look at old photos, which was difficult with that kind of organization. Then I was going through photos that my parents took. They were all organized in folders by year and months. That gave me an idea to make python script to sort my photos the same way.

### Process
First thing I had to think of was how am I going to get an exact date when the photo was taken. I solved this question by accessing metadata of the picture. I made a priority list of metadata tags containing our required date. Next thing was creating folders, which wasn't that hard thanks to python's large amount of libraries. Specifically library os, which can handle both moving files and creating folders.

## Usage
