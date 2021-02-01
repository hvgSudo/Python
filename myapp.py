import os
import subprocess

my_env = os.environ.copy()
my_env["PATH"] = os.pathsep.join(["/opot/myapp/", my_env["PATH"]])

resulr = subprocess.run(["myapp"], env=my_env)
