def read_file(f_n):
    try:
        with open(f_n, "r") as o_file:
            read_myFile = o_file.read()
            print(f"File \"{f_n}\" has the following message:")
            print(read_myFile)
    except:
        print(f"Failed to read file \"{f_n}\".")


