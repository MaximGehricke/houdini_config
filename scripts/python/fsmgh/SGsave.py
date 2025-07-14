#SGsave
#saves on SG
#icon = cm.pipeline_shelf_shotgun_save

def main(**kwargs):
    import commshoudinilib.suites.tools.cm_pipeline_shelf as shelf
    shelf.shotgun_save(kwargs)


if __name__ == "__main__":
     main()

if __name__ == "builtins":
     main()
