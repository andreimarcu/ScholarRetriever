"""
Small script that retrieves Scholar resources locally.

Author: Andrei Marcu <andrei@marcu.net>
https://github.com/andreimarcu/[]
"""
import easywebdav
import shutil
import config
import os


class ScholarRetriever(object):

    def __init__(self, username, password, classes, path):
        self.w = easywebdav.connect("scholar.vt.edu", username=username,
                                    protocol="https", password=password,
                                    path="/dav")
        self.classes = classes
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
                if e.name[-1] == "/":
                    bare = os.path.basename(e.name[:-1])
                    get_contents(bare)
                else:
                    bare = os.path.basename(e.name)

                    print os.getcwd()

                    if os.path.exists(bare):
                        print "Skipping " + os.path.join(class_id, path, bare)
                    else:
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
                          config.classes, config.path)
    sr.get_classes()
