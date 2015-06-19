echo $WORKSPACE
export PROJECT_NAME=rockman
export ROOT="/usr/local/$PROJECT_NAME"
export VENV_DIR="$ROOT/venv"
export SUPERVISOR_CONF="/usr/local/supervisor/${PROJECT_NAME}.conf"
export NGINX_SRC_CONF="/etc/nginx/sites-available/${PROJECT_NAME}.conf"
export NGINX_ENABLED_CONF="/etc/nginx/sites-enabled/${PROJECT_NAME}.conf"

if [[ -e "$VENV_DIR/bin/activate" ]]
then
  rm -rvf "$VENV_DIR"
  rm -vf ~/.rockman/rockman.conf.py
fi
virtualenv "$VENV_DIR"
. "$VENV_DIR/bin/activate"
pip install -r "./requirements.txt"
python setup.py install

cp -rv "./jenkins/nginx.conf" "${SUPERVISOR_CONF}"
cp -rv "./jenkins/nginx.conf" "${NGINX_SRC_CONF}"
ln -snf "${NGINX_SRC_CONF}" "${NGINX_ENABLED_CONF}"

rockman init
rockman migrate
