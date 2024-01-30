rm -rf .devcontainer/.venv
py -m venv .devcontainer/.venv
. .devcontainer/.venv/bin/activate
make develop