from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        content = request.urlopen(self._url).read().decode("utf-8")
        parsedtoml=toml.loads(content)
        return Project(
                parsedtoml['tool']['poetry']['name'],
                parsedtoml['tool']['poetry']['description'],
                parsedtoml['tool']['poetry']['dependencies'].keys(),
                parsedtoml['tool']['poetry']['dev-dependencies'].keys()
	)
