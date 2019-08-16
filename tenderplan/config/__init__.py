import json
import os


class Config:
    def __init__(self):
        self.root_dir = '%s/../..' % os.path.dirname(os.path.abspath(__file__))
        file_config = self._read_config_file()

        self.args = file_config["chrome"]["args"]
        self.url = os.environ.get("TEST_HOST") or file_config["url"]
        #         # if not self.url:
        #     raise ValueError("Couldn't get ENV_HOST variable")
        self.browser = os.environ.get("BROWSER")

    def _read_config_file(self):
        file_path = '%s/tenderplan/config/config.json' % self.root_dir
        try:
            with open(file_path, 'r', encoding='utf8') as cfg:
                return json.load(cfg)
        except Exception as e:
            raise Exception('failed to load file `{}` with exception {}'.format(file_path, e))


config = Config()

__all__ = ['config']
