"""Action registry seed for participation_event."""

from __future__ import annotations


DOC_ID = "participation_event"
ALLOWED_ACTIONS = ['create', 'schedule', 'complete', 'archive']
ACTION_RULES = {'create': {'allowed_in_states': ['planned', 'completed'], 'transitions_to': None}, 'schedule': {'allowed_in_states': ['planned', 'completed'], 'transitions_to': None}, 'complete': {'allowed_in_states': ['planned', 'completed'], 'transitions_to': None}, 'archive': {'allowed_in_states': ['planned', 'completed'], 'transitions_to': 'archived'}}

STATE_FIELD = 'workflow_state'

def get_action_handler_name(action_id: str) -> str:
    return f"handle_{action_id}"

def get_action_module_path(action_id: str) -> str:
    return f"actions/{action_id}.py"

def action_contract(action_id: str) -> dict:
    return {
        "state_field": STATE_FIELD,
        "rule": ACTION_RULES.get(action_id, {}),
    }
