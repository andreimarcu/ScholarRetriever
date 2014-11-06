"""
Small script that retrieves Scholar resources locally.

Author: Andrei Marcu <andrei@marcu.net>
https://github.com/andreimarcu/ScholarRetriever
"""
import easywebdav
import urllib
import config
import os


class ScholarRetriever(object):

    def __init__(self, username, password, classes, path, verbose):
        self.w = easywebdav.connect("scholar.vt.edu", username=username,
                                    protocol="https", password=password,
                                    path="/dav")
        self.classes = classes
        self.verbose = verbose
        os.chdir(path)


    def get_classes(self):
        for c in self.classes:
            self.get_class(c[0], c[1])

    def get_class(self, class_id, uid):

        def get_contents(path="."):
            if not os.path.exists(path):
                os.makedirs(path)

            os.chdir(path)

            for e in self.w.ls(path)[1:]:
                fname = urllib.unquote(e.name)

                if fname[-1] == "/":
                    bare = os.path.basename(fname[:-1])
                    get_contents(bare)
                else:
                    bare = os.path.basename(fname)

                    if os.path.exists(bare) or bare[-4:] == ".URL":
                        if self.verbose:
                            print "Skipping " + os.path.join(class_id, path, bare)
                    else:
                        if self.verbose:
                            print "Getting " + os.path.join(class_id, path, bare)
                        self.w.download(os.path.join(path, bare), bare)

            os.chdir("..")

        self.w.cd(uid)

        if not os.path.exists(class_id):
            os.makedirs(class_id)

        os.chdir(class_id)
        get_contents()

        self.w.cd("..")


if __name__ == '__main__':    
    sr = ScholarRetriever(config.username, config.password,
                          config.classes, config.path,
                          config.verbose)
    sr.get_classes()
