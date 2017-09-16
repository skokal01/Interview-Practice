if __name__ == "__main__":
    with open("dfs.py", "r") as f:
        for line in f:
            # import pdb
            # pdb.set_trace()
            if not line in ['\n','\r\n']:
                print line.rstrip('\n')
