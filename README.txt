pytrackviz - the instant user tracking visualizer

Is a prove of concept to show that track analysis can be almost fully
automated, instead of manually querying a DB, extracting the flows of the
tracking in a paper diagram and finally applying the counts and analyse
them.

As input there were series of track sequences as they were found in
log files and the tracking DB.

From those sequences a template for a graph is generated, which is populated in a
later step with statistic date from live web flows.

The final step is the generation of a graph representing the flow of
tracks with in the flow, which enables the user to spot error or oddities quite
easily.

contact: ch.gierling@<my_mail_operator> the one also doing the Android OS ending with .com

Quickstart:
============
Create a data source, for example using the mock_DB.sql script. Then eit
the go.sh script, if all dependencies are resolved you get the result in
the reports folder. In case you want to use your webbrowser you can use a
minimalistic python HTTP server.

Example:
=========
Usage is straightforward:

  ./mock_TrackSource.sh
  ./go.sh
  ./serve.sh

Mocks a DB with some meaningful data, then starts the script and leaves the
processed results in the reports folder. Which is finally served via a simple
http server.

Type

  python App.py -h

To see more options. Make sure to have a look at go.sh in order to get a
feeling of the work flow.

Workflow:
=========
1. call App.py
  a. provide a date
  b. provide config file
  c. provide also an template file for the graph layout

2. pipe the resulting string to dot specifying the output options you want (dot
   is part of the graphviz package)

3. generate the name of the output file

Requirements:
===============
* graphviz
* python version >=2.7 (not tested with 3.x)
   - sqlalchemy 
* a valid DB configuration file pointing to a DB track source.

Restrictions:
===============
* Some parts of the OO architecture are a bit odd engineered, the basic goal
  was to enable unit testing. But the encapsulation should be much stricter and
  in order to change a track source only one class should be affected this
  means at some point I will have to think about a stable interface for my data
  sources. Along this phase I also have to define the responsabilites the
  different modules will share. Those shall be orthogonal.
* Test coverage is very basic, so bugs are likely.
* Automatic analysis of lost users is only implemented for the 1st level (work
  in progress)

TODO:
======
* Some kind of server to accept AJAX calls embeded in websites to track user
  behaviour
* Implement abstraction for graph template generation,
  as generating them is not yet automatic
* Also Thinkable is an implementation in pure python,
  instead of piping things through the bash (graphviz API for python)
* Parsing of log files as track source,
  for example apache access logs (TrackSource as abstraction layer or
  TrackData Factory)
* Improve general architecture, but as I follow a bottom up apporach this is
  secondary.
