# canonical-indico-themes
This repository holds the Indico plugins used for the Canonical event management system deployment

---
# Building
In order for this plugin to work in production we need to build our final css against the version of indico we are running.

1) To do this, you need to set up a virtual Python 3.9 environment using PyEnv.
Once installed, you can enter the environment manually, or use a tool like PyTorch to make things easier.

2) We will also need a few tools to do the build, as it depends on NPM and Webpack. Download the most recent Snap package of Node.js:
`snap install node --classic`

3) Inside our python environment we need to install a couple of last minute packages: wheel, flask-url-map-serializer, and indico (comes with tons of dependencies). Install them with pip.

4) You need to have a working copy of Indico in the plugin build folder (or somewhere nearby) so we can invoke the scripts out of it to start the build. Likewise, we need the whole indico codebase because it has to build against a ton of files within.
Make sure your version of indico is the one you are running in production.

5) Lastly, we need to install the working copy of our plugin through pip so it can be referenced: 
`pip install -e /path/to/directory`

Once all of these things are in place, we can finally evoke the build.

`./<indico_root_directory>/bin/maintenance/build-assets.py plugin --dev --clean /path/to/plugin`

or

`./<indico_root_directory>/bin/maintenance/build-wheel.py plugin /path/to/plugin`

Once done, you should see a new "dist" directory show up in the assets folder. This is where the files will be sourced at runtime.

---

I learned all this from:

https://talk.getindico.io/t/assets-for-plugin-room-assistance-have-not-been-built-error/2456/5
https://docs.getindico.io/en/stable/installation/production/debian/nginx/
https://docs.getindico.io/en/stable/installation/development/