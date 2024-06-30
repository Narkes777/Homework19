
class Model:
    subs = []

    def save(self):
        for sub in self.subs:
            sub('saving model')
        # saving the model
        for sub in self.subs:
            sub('model is saved')
