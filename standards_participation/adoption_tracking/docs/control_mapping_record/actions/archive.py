"""Action handler seed for control_mapping_record:archive."""

from __future__ import annotations


DOC_ID = "control_mapping_record"
ACTION_ID = "archive"
ACTION_RULE = {'allowed_in_states': ['draft', 'reviewed', 'accepted'], 'transitions_to': 'archived'}

STATE_FIELD = 'workflow_state'
WORKFLOW_HINTS = {'relation_context': {'related_docs': ['standards_requirement', 'standards_adoption_case', 'policy_document', 'compliance_record'], 'borrowed_fields': ['requirement context from standards_requirement', 'control references from internal policy/compliance docs'], 'inferred_roles': ['compliance officer', 'case owner']}, 'actors': ['compliance officer', 'case owner'], 'action_actors': {'create': ['compliance officer'], 'review': ['case owner'], 'confirm': ['compliance officer'], 'archive': ['case owner']}}

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
