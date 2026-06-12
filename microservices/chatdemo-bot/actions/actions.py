# RASA-CONTAINER (#178): custom-action logic slot for chatdemo-bot.
#
# This is the dev-agent edit surface (the rasa analogue of src/handlers.py in
# realtime services): a passthrough default ships so the actions server boots
# and answers /webhook before any real logic lands. Add Action subclasses
# here and declare them under "actions:" in domain.yml.
#
# Docs: https://rasa.com/docs/rasa/custom-actions
from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHealthCheck(Action):
    """Passthrough default — proves the actions container is wired up."""

    def name(self) -> Text:
        return "action_health_check"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="chatdemo-bot actions server is up.")
        return []
