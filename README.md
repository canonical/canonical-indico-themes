# canonical-indico-themes
This repository holds the Indico plugins used for the Canonical event management system deployment

## Developing on this project

### Install Indico
Original installation guides can be found here: https://docs.getindico.io/en/stable/installation/development/#install-dev

#### Ubuntu

Install dependencies:
```
apt install -y --install-recommends libxslt1-dev libxml2-dev libffi-dev libpcre3-dev \
    libyaml-dev build-essential redis-server postgresql libpq-dev
```

```
apt install -y libjpeg-turbo8-dev zlib1g-dev
```

Create a directory to store Indico and its data in:
```
mkdir -p ~/dev/indico/data
```

Install pyenv (if you don't have it already):
```
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.bashrc
exec "$SHELL"
```

Create a virtual environment for Indico to run in:
```
cd ~/dev/indico
pyenv local 3.9.9
python -m venv env
```

```
git clone https://github.com/indico/indico.git src
```

### Installing sqlite3

```
sudo apt-get install libsqlite3-dev
# reinstall Python via pyenv
```

### Creating the DB
Install postgres if you dont have it already:
```
sudo apt update
sudo apt install postgresql postgresql-contrib
```

Configure a new DB for Indico
```
sudo -u postgres createuser $USER --createdb
sudo -u postgres createdb indico_template -O $USER
sudo -u postgres psql indico_template -c "CREATE EXTENSION unaccent; CREATE EXTENSION pg_trgm;"
createdb indico -T indico_template
```

### Configuring your local instance of Indico

Install the virtualenv dependencies:
```
cd ~/dev/indico
source ./env/bin/activate
pip install -U pip setuptools wheel

cd src
pip install -e '.[dev]'
npm ci
```

Congigure Indico using the setup wizard, this creates an indico.conf file within the Indico project that holds custom settings:
```
indico setup wizard --dev
```

Initialize the DB:
```
indico db prepare
```

Build the locales:
```
indico i18n compile-catalog
indico i18n compile-catalog-react
```

### Running Indico

Open two terminals, enter the Indico virtualenv, then navigate to /src:
```
cd ~/dev/indico
source ./env/bin/activate
cd src
```

In one terminal run the webpack watcher:
```
./bin/maintenance/build-assets.py indico --dev --watch
```

In the second terminal run the development server:
```
indico run -h <your-hostname> -q --enable-evalex
```
Now you should be ready to install the plugin.

### Installing the Canonical theme plugin

Navigate to your Indico project and clone the theme repository:
```
cd ~/dev/indico
git clone git@github.com:canonical/canonical-indico-themes.git
```

Open indico.conf and add the following key-value pair to 'General settings' `PLUGINS = {'themes_canonical'}`:
```
nano ~/dev/indico/src/indico/indico.conf 
```

Enter the virtualenv and pip install the plugin:
```
source ./env/bin/activate
pip install -e ~/path/to/directory/canonical-indico-themes/
```
