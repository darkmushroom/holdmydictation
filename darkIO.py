class DarkIO():
    """Wraps file reading and writing

    These could be called from HMDmain but we will want encryption here later
    on. Best to separate this utility now.
    """

    def save(fname, text):
        with open(fname, 'w') as f:
            f.write(text)

    def load(fname):
        with open(fname, 'r') as f:
            return f.read()
