class DarkIO():
    def save(fname,text):
        f = open(fname,'w')
        f.write(text)
        f.close()
