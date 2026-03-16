"""Action handler seed for certification_renewal:archive."""

from __future__ import annotations


DOC_ID = "certification_renewal"
ACTION_ID = "archive"
ACTION_RULE = {'allowed_in_states': ['prepared', 'submitted', 'approved', 'rejected', 'renewed'], 'transitions_to': 'archived'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['certification_record', 'certification_audit_case'], 'borrowed_fields': ['certification', 'expiry context from certification_record'], 'inferred_roles': ['auditor', 'case owner']}, 'actors': ['auditor', 'case owner'], 'action_actors': {'create': ['auditor'], 'submit': ['auditor'], 'approve': ['case owner'], 'reject': ['case owner'], 'archive': ['case owner']}}

def handle_archive(payload: dict, context: dict | None = None) -> dict:
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
