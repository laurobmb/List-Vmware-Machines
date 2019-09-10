#!/usr/bin/python3
import json,os
file_name='.credentials.json'
full_file=os.path.abspath(os.path.join(file_name))
def credencial():
	with open(full_file) as jsonfile:
		parsed = json.load(jsonfile)
		servidor = parsed['informacoes']['vsphere']
		usuario = parsed['informacoes']['user']
		senha = parsed['informacoes']['senha']
	return servidor,usuario,senha

