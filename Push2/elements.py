# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Push2\elements.py
# Compiled at: 2022-11-29 09:57:03
# Size of source mod 2**32: 2897 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.elements import SysexElement
from pushbase.control_element_factory import create_button, create_note_button
from pushbase.elements import Elements as ElementsBase
from pushbase.touch_strip_element import TouchStripElement
from . import sysex
from .parameter_mapping_sensitivities import CONTINUOUS_MAPPING_SENSITIVITY, FINE_GRAINED_CONTINUOUS_MAPPING_SENSITIVITY

class Elements(ElementsBase):

    def __init__(self, model=None, *a, **k):
        self._model = model
        (super(Elements, self).__init__)(a, continuous_mapping_sensitivity=CONTINUOUS_MAPPING_SENSITIVITY, fine_grained_continuous_mapping_sensitivity=FINE_GRAINED_CONTINUOUS_MAPPING_SENSITIVITY, **k)
        for button in self.select_buttons_raw:
            button.is_rgb = True

        self.mix_button = self.single_track_mix_mode_button
        self.page_left_button = self.in_button
        self.page_left_button.name = 'Page_Left_Button'
        self.page_right_button = self.out_button
        self.page_right_button.name = 'Page_Right_Button'
        self.global_mute_button.is_rgb = True
        self.global_solo_button.is_rgb = True
        self.global_track_stop_button.is_rgb = True
        self.play_button.is_rgb = True
        self.record_button.is_rgb = True
        self.automation_button.is_rgb = True
        for button in self.side_buttons_raw:
            button.is_rgb = True

        self.convert_button = create_button(35, 'Convert')
        self.setup_button = create_button(30, 'Setup_Button')
        self.layout_button = create_button(31, 'Layout')
        self._create_touch_strip()
        self.aftertouch_control = SysexElement(send_message_generator=(sysex.make_aftertouch_mode_message),
          default_value='polyphonic')

    def _create_touch_strip(self):
        touch_strip_mode_element = SysexElement(send_message_generator=(sysex.make_touch_strip_mode_message))
        touch_strip_light_element = SysexElement(send_message_generator=(sysex.make_touch_strip_light_message))
        self.touch_strip_tap = create_note_button(12, 'Touch_Strip_Tap')
        self.touch_strip_control = TouchStripElement(name='Touch_Strip_Control',
          touch_button=(self.touch_strip_tap),
          mode_element=touch_strip_mode_element,
          light_element=touch_strip_light_element)
        self.touch_strip_control.state_count = 31
        self.touch_strip_control.set_feedback_delay(-1)
        self.touch_strip_control.set_needs_takeover(False)