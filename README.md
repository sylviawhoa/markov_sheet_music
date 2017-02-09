# Markov Generated Sheet Music

I started this project for a Music Composition Hackathon at Spotify. I wanted to algorithmically generate music using a trained model. The event centered around a performace at the end of the night so my goal was to create music that could be performed by a person. Generating sheet music seemed like it would be a very difficult problem, but after some research, I was excited to discover a file format called [abc notation](https://en.wikipedia.org/wiki/ABC_notation) that gives a textual representation of a score. All I needed was to find a large dataset of abc sheet music and I was able to generate my own songs. I used a [collection of Irish and Sweedish songs](http://www.norbeck.nu/abc/).

Here's a hint of what the output looks like. To see the whole song, and others, checkout the files in the my_songs folder.

![example of song](https://github.com/sylviawhoa/markov_sheet_music/blob/master/example_score.png?raw=true)

This song, and Markov Song 18:32 were performed at the hackathon on a flute and thumb piano respectively by two very excellent (and talented) volunteers. 