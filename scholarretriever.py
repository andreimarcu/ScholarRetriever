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
                                    protocol="https", password=password)
        self.classes = classes
        self.path = path
        self.verbose = verbose


    def get_classes(self):
        for c in self.classes:
            self.get_class(c[0], c[1])


    def get_class(self, class_id, uid):

        path = "/dav/{0}/".format(uid)

        def get_contents(path):

            def dav_path_to_local(path, class_id):
                path = urllib.unquote(path)
                path = path.split("/")[2:]
                path[0] = class_id
                path = os.path.join(self.path, *path)

                return path

            l_path = dav_path_to_local(path, class_id)

            if not os.path.exists(l_path):
                os.makedirs(l_path)

            for e in self.w.ls(path)[1:]:

                if e.name[-1] == "/":
                    get_contents(e.name)

                else:
                    l_fpath = dav_path_to_local(e.name, class_id)

                    if os.path.exists(l_fpath) or e.name[-4:] == ".URL":
                        if self.verbose:
                            print "Skipping " + l_fpath

                    else:
                        if self.verbose:
                            print "Getting " + l_fpath

                        self.w.download(e.name, l_fpath)

        get_contents(path)
        

if __name__ == '__main__':    
    sr = ScholarRetriever(config.username, config.password,
                          config.classes, config.path,
                          config.verbose)
    sr.get_classes()
