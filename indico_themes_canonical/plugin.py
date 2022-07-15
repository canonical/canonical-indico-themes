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


import os
from indico.core import signals
from indico.core.plugins import IndicoPlugin, IndicoPluginBlueprint


class CanonicalThemesPlugin(IndicoPlugin):
    """Canonical Themes
    Provides event themes for Canonical Events.
    """

    def init(self):
        super().init()
        self.get_conference_themes("ubuntu_summit", "/css/ubuntu_summit.css", "Ubuntu Summit")

    def get_blueprints(self):
        return IndicoPluginBlueprint(self.name, __name__)


