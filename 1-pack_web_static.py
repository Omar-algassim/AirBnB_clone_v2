#!/bin/python3
""" achive the file """


from datetime import datetime
from fabric.api import local
from os.path import isdir

def do_pack():
    """ buckup the files"""
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    if isdir("versions") is False:
        local("mkidr versions")
    file_name = " web_static_" + date
    try:
        local(f"tar -cvzf {file_name} web_static")
        return file_name
    except:
        return None