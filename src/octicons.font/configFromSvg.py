import os
import uuid


#  - code: 0xf300
#    uid: 280979dd9fcf2e46250e66792edb8092
#    css: alert
#    meta:
#      author: Facebook
#      homepage: https://github.com/primer/octicons
#    search: [alert]

author = "GitHub"    
homepage = "https://primer.style/octicons/"


idx = 62208
for svg in sorted(os.listdir('./src/svg_fixed')):
    id = str(uuid.uuid1()).replace("-","")
    name = svg.strip().replace(".svg", "")
    print("  - code: {}".format(hex(idx)))
    print("    uid: {}".format(id))
    print("    css: {}".format(name))
    print("    meta:")
    print("      author: {}".format(author))
    print("      homepage: {}".format(homepage)
    print("    search: [{}]".format(name))
    print("")

    idx=idx+1
    