# poetry-envrc-plugin

## Because Why Not?

Welcome to `poetry-envrc-plugin`, the plugin you didn't find anywhere else. This nifty tool helps you load environment variables from all .env files listed in `.envrc`.

### Usage
Just list your .env files in your .envrc file and let the magic happen:

```sh
# .envrc
.env
.env.local
```

Then, when you run your project with Poetry, this plugin will dutifully load your .env files as if it had nothing better to do.

Last .env file wins, so if you have a variable in both .env and .env.local, the one in .env.local will be used.
If previous ENV VARS are set, they will remain untouched and will not be overwritten.

### Features

- **Loads `.env` and `.env.local` Files**: Because you love managing multiple files.
- **Prioritizes `.env.local` Over `.env`**: Local variables are obviously superior.
- **Automatic Cleanup**: Because who has time to clean up after themselves?

### Installation

You actually want to use this? Fine, here's how:

```sh
poetry self add git+https://github.com/matias-martini/poetry-envrc-plugin.git
```

### Contributing
Feel free to submit a pull request.

### License
MIT License. Because why not?


