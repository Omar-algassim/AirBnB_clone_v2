#!/usr/bin/python3
""" achive the file """


from datetime import datetime
from fabric.api import local
from os.path import isdir


# env.user = 'ubuntu'
# env.hosts = ['100.27.0.202 web-01', '54.237.42.237 web-02']
def do_pack():
    """ buckup the files"""
    local("ls -l")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    if not isdir("versions"):
        local("mkdir versions")
    file_name = "versions/web_static_" + date + ".tgz"
    try:
        local(f"tar -cvzf {file_name} web_static")
        return file_name
    except:
        return None
