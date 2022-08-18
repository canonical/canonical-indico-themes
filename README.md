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

### Running Indico

```
cd ~/dev/indico
source ./env/bin/activate

## In one terminal
./bin/maintenance/build-assets.py indico --dev --watch

## In a second terminal
indico run -h <your-hostname> -q --enable-evalex
```

### Installing the Canonical theme plugin

`cd` into your project directory and clone the theme project:
```
git clone git@github.com:canonical/canonical-indico-themes.git
```

Run Indico, and install the plugin:
```
pip install -e ~/path/to/directory/canonical-indico-themes/
```
