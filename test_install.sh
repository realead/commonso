set -e

ENV_DIR="p3"
virtualenv -p python3 "$ENV_DIR"

#activate environment
. "$ENV_DIR/bin/activate"


if [ "$1" = "from-github" ]; then
    echo "Installing setup.py from github..."
    pip install https://github.com/realead/indirect_buffer/zipball/master
else
    echo "Installing local setup.py..."
    for dir_name in "build" ".eggs" "dist"
    do
        if [ -d "$dir_name" ]; then
           echo "clean build, deleting $dir_name directory"
           rm -r "$dir_name"
        fi; 
    done  
    python setup.py install
fi;

echo "Installed packages:"
pip freeze

#tests:
(cd tests && python -m unittest discover -s . -v)

#clean or keep the environment
if [ "$2" = "keep" ]; then
   echo "keeping enviroment $ENV_DIR"
else
   rm -r "$ENV_DIR"
fi;

