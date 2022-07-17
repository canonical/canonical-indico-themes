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

from indico_themes_canonical import canonical_themes


class CanonicalThemesPlugin(IndicoPlugin):
    """Canonical Themes
    Provides event themes for Canonical Events.
    """

    def init(self):
        super().init()
        self.connect(signals.plugin.get_conference_themes, self._get_conference_themes)

    def get_blueprints(self):
        return IndicoPluginBlueprint(self.name, __name__)

    def _get_conference_themes(self, sender, **kwargs):
        for v in canonical_themes.THEMES:
            yield v
