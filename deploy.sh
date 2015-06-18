echo $WORKSPACE
export PROJECT_NAME=rockman
export ROOT="/usr/local/$PROJECT_NAME"
export VENV_DIR="$ROOT/venv"

if [[ -e "$VENV_DIR/bin/activate" ]]
then
  rm -rvf "$VENV_DIR"
fi
virtualenv "$VENV_DIR"
. "$VENV_DIR/bin/activate"
pip install -r "./requirements.txt"
python setup.py install


rockman init
rockman migrate
