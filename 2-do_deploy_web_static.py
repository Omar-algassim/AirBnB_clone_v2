#!/usr/bin/python3
""" achive the file """


from fabric.api import env, put, run
from os.path import  exists
env.user = "ubuntu"
env.hosts = ['100.27.0.202', '54.237.42.237']

def do_deploy(archive_path):
    """ deploy on server web-01 and web-02"""
    
    if exists(archive_path) is False:
        return False
    
    try:
        achive_file = archive_path.split("/")[-1]
        achive_file_name = achive_file.split(".")[0]
        path = "/data/web_static/releases/"
        put(local_path=archive_path, remote_path="/tmp/")
        run(f"mkdir -p /data/web_static/releases/{achive_file_name}")
        run(f"tar -xzf /tmp/{achive_file} -C {path}{achive_file_name}/")
        run(f"mv {path}{achive_file_name}/web_static/* {path}{achive_file_name}/")
        run(f"rm -rf {path}{achive_file_name}/web_static")
        run(f"rm -rf /data/web_static/current")
        run(f"ln -s {path}{achive_file_name}/ /data/web_static/current")
        print("New version deployed!")
    except:
        return False
        