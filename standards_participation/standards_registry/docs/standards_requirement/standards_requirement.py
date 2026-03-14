"""Doc runtime hooks for standards_requirement."""

class DocRuntime:
    doc_key = "standards_requirement"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'update', 'review', 'activate', 'retire', 'archive']
