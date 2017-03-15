#!/usr/bin/env bash
#if [ ! -d /data/web_static/releases/test/index.html]; then
#	sudo mkdir /data/web_static/releases/test/index.html
#fi;

if [ ! -d /data/]; then
	mkdir /data/;
fi;
	
if [ ! -d /data/web_static/]; then
	mkdir /data/web_static/;
fi;

if [ ! -d /data/web_static/releases/]; then
	mkdir /data/web_static/releases/;
fi;

if [ ! -d /data/web_static/shared/]; then
	mkdir /data/web_static/shared/;
fi;

if [ ! -d /data/web_static/releases/test/]; then
	mkdir /data/web_static/releases/test/;
fi;

find . -type d -exec touch {}/index.html \;

