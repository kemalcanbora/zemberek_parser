import os
from subprocess import PIPE
from subprocess import run


def PDFParser(file):
    localpath = os.path.dirname(os.path.realpath(__file__)) + '/'  # local path
    tikapath = localpath + 'tika-app-1.18.jar'  # path to Apache Tika jar file
    command = ['java', '-jar', tikapath, '-t', file]  # command line for Apache Tika parser
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True)  # run command
    content = result.stdout  # get command line output as file content
    return content
