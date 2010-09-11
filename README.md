V - Python starter kit for the Google sponsored University of Waterloo Planet Wars AI Challenge
===============================================================================================
[AI Contest Homepage](http://ai-contest.com)

Use
---
To pit the DualBot and BullyBot against each other on the map1 map:
	java -jar tools/PlayGame.jar examples/maps/map1.txt 500 500 log.txt "java -jar examples/bots/DualBot.jar" "java -jar examples/bots/BullyBot.jar"
	
overlord-bot vs RageBot on map31:
	java -jar tools/PlayGame.jar examples/maps/map1.txt 500 500 log.txt "python bots/overlord-bot.py" "java -jar examples/bots/RageBot.jar"
	
view the same fight in the visualizer:
	java -jar tools/PlayGame.jar examples/maps/map1.txt 500 500 log.txt "python bots/overlord-bot.py" "java -jar examples/bots/RageBot.jar" | java -jar tools/ShowGame.jar
	
MIT License
-----------
Copyright (c) 2010 Chuck Collins

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.