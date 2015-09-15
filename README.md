# TrafficMap

Build a Traffic Feed from a Traffic Camera
===============================

A traffic map has green/yellow/red or other kinds of roads indicating traffic status on map. It is built upon real time traffic data feed.

Usually there are public traffic data feed available, but what if in some places the goverments don't offer any real time API for the road traffic? Is it possible to create your own? 

In this simple prototype, I'm building traffic feed for Macau, which doesn't have any public traffic data feed, but has a real time traffic cameras for some roads. 

Ideas:
1. Get the camera photos for roads from: http://www.dsat.gov.mo/en/realtime.aspx
2. Identify the number of cars on the road. Using a pre-trained cascade classifier to detect cars. (Python + OpenCV)
3. Estimate the traffic status using machine learning. (Todo)