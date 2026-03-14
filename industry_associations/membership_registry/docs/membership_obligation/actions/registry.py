"""Action registry seed for membership_obligation."""

from __future__ import annotations


DOC_ID = "membership_obligation"
ALLOWED_ACTIONS = ['create', 'assign', 'fulfill', 'mark_overdue', 'close', 'archive']
ACTION_RULES = {'create': {'allowed_in_states': ['opened', 'due', 'fulfilled', 'overdue'], 'transitions_to': None}, 'assign': {'allowed_in_states': ['opened', 'due', 'fulfilled', 'overdue'], 'transitions_to': None}, 'fulfill': {'allowed_in_states': ['opened', 'due', 'fulfilled', 'overdue'], 'transitions_to': None}, 'mark_overdue': {'allowed_in_states': ['opened', 'due', 'fulfilled', 'overdue'], 'transitions_to': None}, 'close': {'allowed_in_states': ['opened', 'due', 'fulfilled', 'overdue'], 'transitions_to': 'closed'}, 'archive': {'allowed_in_states': ['opened', 'due', 'fulfilled', 'overdue'], 'transitions_to': 'archived'}}

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
