"""Doc runtime hooks for standards_adoption_case."""

class DocRuntime:
    doc_key = "standards_adoption_case"

    def validate(self, payload):
        return payload

    def allowed_actions(self):
        return ['create', 'assign', 'implement', 'defer', 'close', 'archive']
