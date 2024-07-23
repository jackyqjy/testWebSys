from wtforms import Form

class BaseForm(Form):
    @property
    def messages(self):
        message_list = []
        if self.errors:
            for error in self.errors.values():
                message_list.extend(error)
        return message_list
