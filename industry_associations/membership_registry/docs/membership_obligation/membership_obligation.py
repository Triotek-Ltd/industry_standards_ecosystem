"""Doc runtime hooks for membership_obligation."""

class DocRuntime:
    doc_key = "membership_obligation"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'assign', 'fulfill', 'mark_overdue', 'close', 'archive']
