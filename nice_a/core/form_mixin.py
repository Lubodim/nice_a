
class DisabledFormMixin:
    disabled_fields = ()
    fields = None

    def _disable_fields(self):
        for filed_name in self.disabled_fields:
            if filed_name in self.fields:
                field = self.fields[filed_name]
                # field.widget.attrs['disabled'] = 'disabled'
                field.widget.attrs['readonly'] = 'readonly'

