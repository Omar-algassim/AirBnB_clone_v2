#!/usr/bin/python3
""" full deploying"""



from datetime import datetime
from fabric.api import local, run, put, env
from os.path import isdir, exists

env.user = 'ubuntu'
env.hosts = ['100.27.0.202', '54.237.42.237']

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
    
def deploy():
    """aceive file and transfer it to server"""
    file = do_pack()
    if file is None:
        return False    
    return do_deploy(file)
