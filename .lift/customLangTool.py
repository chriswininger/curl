#!/usr/bin/env python3
import json
import sys
import shutil
import subprocess
import os
import re

name = "CustomLang"
apiVersion = 3

def emitStartInfo():
    info = { "version": apiVersion, "name": name }
    print(json.dumps(info))

def emitVersion():
    print(json.dumps(apiVersion))

def emitName():
    print(name)

def emitApplicable():
    print(json.dumps(True))

def run(runInfo):
    print(json.dumps({}))

def finalize(args, info):
    codedir = args[1]
    langauage = info['language']

    outputs = {
        'toolNotes': [{
            'type': 'using-crufty-language',
            'message': '"{}" is crufty have you heard of Rust'.format(langauage),
            'file': os.path.join(codedir, 'src/main/java/com/mycompany/app/App.java'),
            'line': 1,
            'column': 0
        }]
    }

    print(json.dumps(outputs))

def main():
    args = sys.argv

    if (len(args) < 4):
        emitStartInfo()
    else:
        cmd = args[3]
        if cmd == "version":
            emitVersion()
        elif cmd == "name":
            emitName()
        elif cmd == "applicable":
            emitApplicable()
        elif cmd == "run":
            info = json.loads(sys.stdin.read())
            run(info)
        elif cmd == "finalize":
            info = json.loads(sys.stdin.read())
            finalize(args, info)

if __name__ == "__main__":
    main()
