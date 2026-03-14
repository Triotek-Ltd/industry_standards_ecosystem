"""Doc runtime hooks for certification_record."""

class DocRuntime:
    doc_key = "certification_record"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'update', 'renew', 'suspend', 'archive']
