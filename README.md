# Asteroids

This is a recreation of the famous "Asteroids" game in PyGame.

## Requirements

The only requirement for this game is the `pygame` package. At the time of writing, the
latest version was 2.6.1 so you'll need to install at least that version. Here we've
opted to use `uv` in order to manage project dependencies. You can install `uv` by
following [these](https://docs.astral.sh/uv/getting-started/installation/) instructions.
Further instructions will be provided in the next section.

Another way to install `pygame` is by using a package manager like Miniconda. Follow the
instructions [here](https://docs.anaconda.com/miniconda/install/) and then run:

```bash
conda create -n <env_name> python=3.10 pip pygame==2.6.1
```

in order to create a virtual environment with the necessary packages. Don't forget to
activate that environment with `conda activate <env_name>` before attempting to run this
program.

Another alternative is to use the built-in `venv` module to create one in the current
directory:

```bash
python -m venv [/path/to/virtual/env/dir]
```

where you can specify a path to the virtual environment directory. If you don't specify
one then a `.venv` directory will be created in the current directory. Activate the
virtual environment with:

```bash
source <path/to/venv>/bin/activate
```

and then install `pygame` with:

```bash
pip install pygame==2.6.1
```

## How to run

Clone this repo and navigate to it using your terminal. Once inside, activate your virtual
environment. If you're using `uv`, simply call `uv sync` in order to create a virtual
environment with all of the necessary dependencies. You can then activate the environment
using:

```bash
source .venv/bin/activate
```

Once you've activated your virtual environment, you can run the game with:

```bash
python main.py
```
