"""Doc runtime hooks for participation_event."""

class DocRuntime:
    doc_key = "participation_event"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'schedule', 'complete', 'archive']
