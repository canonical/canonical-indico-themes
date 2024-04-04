# Copyright 2022 Canonical Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from indico.modules.events.layout.util import ConferenceTheme

"""
The THEMES table contains 1 or more entries of type ConferenceTheme, each of which containing information
for a given conference theme.

Required:
- ``name``     -- string indicating the internal name used for the stylesheet which will be
                  stored when the theme is selected in an event.
- ``css_path`` -- string indicating the location of the CSS file, relative to the
                  plugin's ``static`` folder.
- ``title``    -- string indicating the title displayed to the user when selecting the theme.

Optional:
- ``js_path``  -- string indicating the location for a simple, static javascript file to be
                  loaded, relative to the plugin's ``static`` folder.
"""


THEMES = [
    ConferenceTheme(
        name="ubuntu_summit",
        css_path="css/ubuntu-summit/index.css",
        title="Ubuntu Summit",
        js_path="js/ubuntu_summit.js",
    ),
    ConferenceTheme(
        name="canonical",
        css_path="css/canonical/index.css",
        title="Canonical",
        js_path="js/default.js",
    ),
    ConferenceTheme(
        name="grad",
        css_path="css/grad/index.css",
        title="Suru Gradient",
        js_path="js/default.js",
    ),
    ConferenceTheme(
        name="dark",
        css_path="css/dark/index.css",
        title="Suru Dark",
        js_path="js/default.js",
    ),
    ConferenceTheme(
        name="snapcraft",
        css_path="css/snapcraft/index.css",
        title="Suru Snapcraft",
        js_path="js/default.js",
    ),
    ConferenceTheme(
        name="aqua",
        css_path="css/aqua/index.css",
        title="Suru Aqua",
        js_path="js/default.js",
    ),
    ConferenceTheme(
        name="k8s",
        css_path="css/k8s/index.css",
        title="Suru k8s",
        js_path="js/default.js",
    ),
    ConferenceTheme(
        name="orange",
        css_path="css/orange/index.css",
        title="Suru Orange",
        js_path="js/default.js",
    ),
]
