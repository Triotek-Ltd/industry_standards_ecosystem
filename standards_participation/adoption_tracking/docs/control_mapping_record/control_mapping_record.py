"""Doc runtime hooks for control_mapping_record."""

class DocRuntime:
    doc_key = "control_mapping_record"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'review', 'confirm', 'archive']
