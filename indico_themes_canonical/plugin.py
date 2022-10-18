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

from wtforms.fields import BooleanField

from indico.core import signals
from indico.core.plugins import IndicoPlugin, IndicoPluginBlueprint
from indico.modules.events.timetable.legacy import TimetableSerializer
from indico.util.i18n import _
from indico.web.forms.widgets import SwitchWidget
from indico.web.forms.base import IndicoForm

from indico_themes_canonical import canonical_themes


class HackTimetableSerializer(TimetableSerializer):
    """HackTimetableSerializer
    A replacement TimetableSerialzer that prefers the track's default session color.
    This is a hack to enable track colors in the short term. To use:
    1. Set up tracks for your event
    2. Set up sessions for your event and make them the default for your tracks
    3. Enable the setting in the plugin configuration.
    4. When accepting abstracts, make sure to NOT put the track into the session
    """
    def serialize_contribution_entry(self, entry):
        data = super().serialize_contribution_entry(entry)

        enabled = CanonicalThemesPlugin.settings.get('timetable_use_track_colors')

        if (
            enabled and
            entry.contribution.track and
            entry.contribution.track.default_session
        ):
            data.update(self._get_color_data(entry.contribution.track.default_session))

        return data


class CanonicalThemeSettingsForm(IndicoForm):
    timetable_use_track_colors = BooleanField(
        _('Prefer Track Colors'),
        widget=SwitchWidget(),
        description=_('Prefer the track\'s default session color in the timetable')
    )


class CanonicalThemesPlugin(IndicoPlugin):
    """Canonical Themes
    Provides event themes for Canonical Events.
    """

    configurable = True
    default_settings = {
        'timetable_use_track_colors': False
    }
    settings_form = CanonicalThemeSettingsForm

    def init(self):
        super().init()
        self.connect(signals.plugin.get_conference_themes, self._get_conference_themes)

        # Hack to show timetable using the track's default session color
        import indico.modules.events.timetable.controllers.display
        indico.modules.events.timetable.controllers.display.TimetableSerializer = HackTimetableSerializer

        import indico.modules.events.timetable.controllers.manage
        indico.modules.events.timetable.controllers.manage.TimetableSerializer = HackTimetableSerializer

        import indico.modules.events.timetable.util
        indico.modules.events.timetable.util.TimetableSerializer = HackTimetableSerializer

    def get_blueprints(self):
        return IndicoPluginBlueprint(self.name, __name__)

    def _get_conference_themes(self, sender, **kwargs):
        for v in canonical_themes.THEMES:
            yield v
