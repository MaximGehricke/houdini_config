#setVis
#sets -Use Visibility- to 0 on the alembics inside selected ObjNodes
#icon = SOP_visibility
import hou

def main(**kwargs):
    times = 0
    parents = hou.selectedNodes()
    for parent in parents:
        abc = parent.children()[0]
        print(abc.path)
        abc.setParms({"usevisibility": 0})
        times += 1

    hou.ui.displayMessage("visibility set for "+str(times)+" alembics!")


if __name__ == "__main__":
     main()

if __name__ == "builtins":
     main()