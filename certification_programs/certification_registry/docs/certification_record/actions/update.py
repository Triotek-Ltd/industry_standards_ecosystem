"""Action handler seed for certification_record:update."""

from __future__ import annotations


DOC_ID = "certification_record"
ACTION_ID = "update"
ACTION_RULE = {'allowed_in_states': ['active', 'suspended', 'expired'], 'transitions_to': None}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['certification_audit_case', 'certification_renewal', 'standards_adoption_case'], 'borrowed_fields': ['certification-program context from standards/adoption docs where linked'], 'inferred_roles': ['auditor', 'case owner']}, 'actors': ['auditor', 'case owner'], 'action_actors': {'create': ['auditor'], 'update': ['auditor'], 'archive': ['case owner']}}

def handle_update(payload: dict, context: dict | None = None) -> dict:
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
