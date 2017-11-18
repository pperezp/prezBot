# -*- coding: utf-8 -*-

bashCommand = "/opt/vc/bin/vcgencmd measure_temp"
import subprocess
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
print(output.strip().split("=")[1].split("'")[0]+" Cº")
