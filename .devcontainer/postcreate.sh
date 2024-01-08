rm -rf .devcontainer/.venv
python3.12 -m venv .devcontainer/.venv
. .devcontainer/.venv/bin/activate
make develop