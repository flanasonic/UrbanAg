
class Config:
    import os as _os
    import configparser as _cp
    _config = _cp.ConfigParser(interpolation=_cp.ExtendedInterpolation(), allow_no_value=True)

    # public:
    basedir = _os.path.dirname(_os.path.realpath(__name__))

    def __init__(self, configfile="config"):
        config_path = self._os.path.join(self.basedir,configfile)
        with open(config_path, "r") as configfile:
            self._config.read_file(configfile)

    def getDataFiles(self):
        datadir = self._config["DataFiles"]["basedir"]
        from os import walk
        datafiles = {}
        for (dirpath, dirnames, filenames) in walk(datadir):
            for file in filenames:
                fullpath = self._os.path.join(dirpath, file)
                localpath = str.replace(fullpath,datadir,"")
                datafiles[localpath] = fullpath
        return datafiles

    def getStaticWebDir(self):
        return self._config["StaticFiles"]["basedir"]
    
    def get(self,section,option):
        return self._config.get(section,option)

