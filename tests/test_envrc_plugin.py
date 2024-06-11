import os
from poetry_envrc_plugin.envrc_plugin import EnvrcPlugin

def test_load_without_comments_envrc(tmp_path):
    envrc_content = """
     .env
     .env.local 
    """
    env_content = "TEST_VAR=hello\nTEST_VAR2=world\n"
    env_local_content = "TEST_VAR=actual_hello\n"

    envrc_path = tmp_path / '.envrc'
    env_path = tmp_path / '.env'
    env_local_path = tmp_path / '.env.local'

    envrc_path.write_text(envrc_content)
    env_path.write_text(env_content)
    env_local_path.write_text(env_local_content)

    plugin = EnvrcPlugin()
    plugin.load_envrc(envrc_path)

    try:
        assert os.getenv("TEST_VAR") == "actual_hello"
        assert os.getenv("TEST_VAR2") == "world"
    finally:
        if "TEST_VAR" in os.environ:
            del os.environ["TEST_VAR"]
        if "TEST_VAR2" in os.environ:
            del os.environ["TEST_VAR2"]

def test_load_with_comments_envrc(tmp_path):
    envrc_content = """
     .env # this is the main env file
     # .env.local
    """
    env_content = "TEST_VAR=hello\n"
    env_local_content = "TEST_VAR=world\n"

    envrc_path = tmp_path / '.envrc'
    env_path = tmp_path / '.env'
    env_local_path = tmp_path / '.env.local'
    envrc_path.write_text(envrc_content)
    env_path.write_text(env_content)
    env_local_path.write_text(env_local_content)

    plugin = EnvrcPlugin()
    plugin.load_envrc(envrc_path)

    try:
        assert os.getenv("TEST_VAR") == "hello"
    finally:
        if "TEST_VAR" in os.environ:
            del os.environ["TEST_VAR"]

def test_load_with_previous_env_vars_defined(tmp_path):
    envrc_content = """
     .env
     .env.local
    """
    env_content = "TEST_VAR=hello\n"
    env_local_content = "TEST_VAR=world\n"

    envrc_path = tmp_path / '.envrc'
    env_path = tmp_path / '.env'
    env_local_path = tmp_path / '.env.local'
    envrc_path.write_text(envrc_content)
    env_path.write_text(env_content)
    env_local_path.write_text(env_local_content)

    os.environ["TEST_VAR"] = "previous_hello"

    plugin = EnvrcPlugin()
    plugin.load_envrc(envrc_path)

    try:
        assert os.getenv("TEST_VAR") == "previous_hello"
    finally:
        if "TEST_VAR" in os.environ:
            del os.environ["TEST_VAR"]

