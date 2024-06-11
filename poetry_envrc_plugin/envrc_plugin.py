from pathlib import Path
import os

from poetry.plugins.plugin import Plugin
from dotenv import load_dotenv

class EnvrcPlugin(Plugin):
    def activate(self, poetry, io):
        envrc_path = Path(poetry.file.parent) / '.envrc'
        if envrc_path.exists():
            self.load_envrc(envrc_path)

    def load_envrc(self, envrc_path: Path):
        with envrc_path.open() as f:
            for line in reversed(f.readlines()):
                line = line.strip()
                env_file = line.split('#')[0].strip()
                if not env_file:
                    continue

                env_path = os.path.dirname(envrc_path) / Path(env_file)
                if env_path.exists():
                    self.load_env_file(env_path)

    def load_env_file(self, env_file):
        env_path = Path(env_file)
        if env_path.exists():
            load_dotenv(dotenv_path=env_path, override=False)

