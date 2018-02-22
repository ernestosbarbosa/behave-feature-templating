import sys
import os
import json
from trender import TRender

params = json.load(open("params/"+sys.argv[1]+".json"))

for file in os.listdir("features"):
    if file.endswith(".feature"):
        os.remove(os.path.join("features", file))

for file in os.listdir("templates"):
    if file.endswith(".feature"):
        with open(os.path.join("templates", file), 'r') as f:
            feature = f.read()
            to_render = TRender(feature)
            render = to_render.render({'message': 'Lorem Ipsum'})
            output = open(os.path.join("features", file), "w")
            output.write(render)
            output.close()
            f.close()