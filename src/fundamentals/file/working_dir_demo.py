import this
if __name__ == '__main__':
    from working_dir_utils import print_working_dir
    import sys
    del sys.modules["working_dir_utils"]
    from working_dir_utils import print_working_dir
    print_working_dir()