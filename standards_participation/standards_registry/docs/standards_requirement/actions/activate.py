"""Action handler seed for standards_requirement:activate."""

from __future__ import annotations


DOC_ID = "standards_requirement"
ACTION_ID = "activate"
ACTION_RULE = {'allowed_in_states': ['draft'], 'transitions_to': 'active'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['standards_adoption_case', 'control_mapping_record', 'policy_document'], 'borrowed_fields': ['standard/program context from external references or policy docs where linked'], 'inferred_roles': ['compliance officer', 'case owner']}, 'actors': ['compliance officer', 'case owner'], 'action_actors': {'create': ['compliance officer'], 'update': ['compliance officer'], 'review': ['case owner'], 'activate': ['case owner'], 'retire': ['case owner'], 'archive': ['case owner']}}

def handle_activate(payload: dict, context: dict | None = None) -> dict:
    context = context or {}
    next_state = ACTION_RULE.get("transitions_to")
    updates = {STATE_FIELD: next_state} if STATE_FIELD and next_state else {}
    return {
        "doc_id": DOC_ID,
        "action_id": ACTION_ID,
        "payload": payload,
        "context": context,
        "allowed_in_states": ACTION_RULE.get("allowed_in_states", []),
        "next_state": next_state,
        "updates": updates,
        "workflow_objective": WORKFLOW_HINTS.get("business_objective"),
    }
