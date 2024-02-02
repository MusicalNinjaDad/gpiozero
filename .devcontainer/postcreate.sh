echo "Removing old venv"
rm -rf .devcontainer/.venv
echo "Creating new venv"
py -m venv .devcontainer/.venv
. .devcontainer/.venv/bin/activate
echo "Make gpiozero develop"
make develop