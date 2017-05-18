#! /usr/bin/env python

def init(data):
	data['first'] = {}
	data['middle'] = {}
	data['last'] = {}

def store(data, fullName):
	names = fullName.split()
	if len(names) == 2: names.insert(1, '')
#	labels = 'first', 'middle', 'last'
	#for label, name in zip(labels, names):
	for label, name in zip(data.keys(), names):
		storage[label].setdefault(name, []).append(fullName)

def lookup(data, label, name):
	return data[label].get(name)

storage = {}
init(storage)
names = 'Arthur Morse Messenger', 'Matthew Doyle Messenger',\
         'Unknow Messenger', 'Unknow Doyle Messenger'

for name in names:
	store(storage, name)

print storage
