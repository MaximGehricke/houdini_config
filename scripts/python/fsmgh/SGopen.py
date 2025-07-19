#SGopen
#opens SG
#icon = cm.pipeline_shelf_shotgun_open

def main(**kwargs):
    import commshoudinilib.suites.tools.cm_pipeline_shelf as shelf
    shelf.shotgun_open(kwargs)


if __name__ == "__main__":
     main()

if __name__ == "builtins":
     main()
