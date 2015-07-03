echo $WORKSPACE
export PROJECT_NAME=rockman
export ROOT="/usr/local/$PROJECT_NAME"
export ENV_DIR="$ROOT/envdir"
export ENV_VARS_TXT="$ROOT/envvars.txt"
export SUPERVISOR_CONF="/usr/local/supervisor/${PROJECT_NAME}.conf"
export NGINX_SRC_CONF="/etc/nginx/sites-available/${PROJECT_NAME}.conf"
export NGINX_ENABLED_CONF="/etc/nginx/sites-enabled/${PROJECT_NAME}.conf"

docker build -t "${PROJECT_NAME}:master" -f "./docker/app/Dockerfile" "."

echo "" > ${ENV_VARS_TXT}
for f in ${ENV_DIR}/*;
do
    echo "Processing ${f##*/} file...";
    echo ${f##*/}=$(cat $f) >> ${ENV_VARS_TXT};
done

cp -vf "./jenkins/supervisor.conf" "${SUPERVISOR_CONF}"
cp -vf "./jenkins/nginx.conf" "${NGINX_SRC_CONF}"
ln -snf "${NGINX_SRC_CONF}" "${NGINX_ENABLED_CONF}"
