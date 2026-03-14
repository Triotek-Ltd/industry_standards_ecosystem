"""Doc runtime hooks for certification_renewal."""

class DocRuntime:
    doc_key = "certification_renewal"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'prepare', 'submit', 'approve', 'reject', 'archive']
