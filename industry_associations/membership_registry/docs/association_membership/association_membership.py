"""Doc runtime hooks for association_membership."""

class DocRuntime:
    doc_key = "association_membership"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'update', 'renew', 'suspend', 'archive']
