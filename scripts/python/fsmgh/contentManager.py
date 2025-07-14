#contentManager
#opens FS content manager
#icon = cm_pipeline_shelf_content_mgr

def main(**kwargs):
    import commshoudinilib.suites.tools.cm_pipeline_shelf as shelf
    shelf.open_content_manager(kwargs)


if __name__ == "__main__":
     main()

if __name__ == "builtins":
     main()
