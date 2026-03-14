"""Doc runtime hooks for certification_audit_case."""

class DocRuntime:
    doc_key = "certification_audit_case"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'schedule', 'assign', 'complete', 'close', 'archive']
