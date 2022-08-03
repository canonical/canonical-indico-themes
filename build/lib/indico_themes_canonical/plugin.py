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


from indico.core import signals
from indico.core.plugins import IndicoPlugin, IndicoPluginBlueprint

# this is the list where we will put all of our theme information.
# this list should contain a series of tuples, each containing three pieces of information as strings:
# `(name, css, title)`
# `name` is the internal name used for the stylesheet which will be stored when the theme is selected in an event.
# `css` is the location of the CSS file, relative to the plugin's `static` folder.
# `title` is the title displayed to the user when selecting the theme.

CANONICAL_THEMES = [("ubuntu_summit", "/css/ubuntu_summit.css", "Ubuntu Summit")]


class CanonicalThemesPlugin(IndicoPlugin):
    """Canonical Themes
    Provides event themes for Canonical Events.
    """

    def init(self):
        super().init()
        self.connect(signals.plugin.get_conference_themes, self._get_conference_themes_canonical)

    def get_blueprints(self):
        return IndicoPluginBlueprint(self.name, __name__)

    def _get_conference_themes_canonical(self, sender, **kwargs):
        for v in CANONICAL_THEMES:
            yield v
