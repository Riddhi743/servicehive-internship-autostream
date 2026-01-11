class ConversationState:
    def __init__(self):
        self.name = None
        self.email = None
        self.platform = None

    def is_complete(self):
        return all([self.name, self.email, self.platform])
