# -*- coding: utf-8 ; mode: python -*-

# AZERTY support for Anki 2
########################################################################
#
# Coded by Jonathan Ballet <jon@multani.info>
# Inspired by the Dvorak keys plugin from https://github.com/ospalh/anki-addons/
# by Roland Sieker <ospalh@gmail.com>
#
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html
#

"""
Anki plugin to use keys from a AZERTY keyboard to answer the card.
"""

from anki.hooks import wrap
from aqt.addons import AddonManager
from aqt.reviewer import Reviewer


__version__ = '0.0.1'


azerty_mapping = {
    # On AZERTY keyboard, the combination Shift+& should be pressed to have "1".
    # This dict just remaps the keys to be used without having to press any keys
    # combinations.
    u'&': 1, u'é': 2, u'"': 3, u"'": 4,
}


def azertyKeyHandler(self, event):
    text = event.text()
    try:
        answer = azerty_mapping[text]
    except KeyError:
        pass
    else:
        self._answerCard(answer)

Reviewer._keyHandler = wrap(Reviewer._keyHandler, azertyKeyHandler)


# Prettier menu entry
def rebuildAddonsMenu(self):
    for menu in self._menus:
        if "azerty_keys" == menu.title():
            menu.setTitle("AZERTY Keys")
            break

AddonManager.rebuildAddonsMenu = wrap(AddonManager.rebuildAddonsMenu,
                                      rebuildAddonsMenu)
