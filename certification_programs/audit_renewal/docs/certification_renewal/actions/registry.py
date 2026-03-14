"""Action registry seed for certification_renewal."""

from __future__ import annotations


DOC_ID = "certification_renewal"
ALLOWED_ACTIONS = ['create', 'prepare', 'submit', 'approve', 'reject', 'archive']
ACTION_RULES = {'create': {'allowed_in_states': ['prepared', 'submitted', 'approved', 'rejected', 'renewed'], 'transitions_to': None}, 'prepare': {'allowed_in_states': ['prepared', 'submitted', 'approved', 'rejected', 'renewed'], 'transitions_to': None}, 'submit': {'allowed_in_states': ['prepared', 'submitted', 'approved', 'rejected', 'renewed'], 'transitions_to': 'submitted'}, 'approve': {'allowed_in_states': ['prepared', 'submitted', 'approved', 'rejected', 'renewed'], 'transitions_to': 'approved'}, 'reject': {'allowed_in_states': ['prepared', 'submitted', 'approved', 'rejected', 'renewed'], 'transitions_to': 'rejected'}, 'archive': {'allowed_in_states': ['prepared', 'submitted', 'approved', 'rejected', 'renewed'], 'transitions_to': 'archived'}}

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
