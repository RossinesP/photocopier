__author__ = 'pierrerossines'

class ProgressBar:
    "Represents a progress bar."

    def __init__(self, min_value, max_value):
        self.set_values(min_value, max_value)

    def get_progress(self, current_value):
        "[==========]100%"
        percentage = round((current_value * 100) / self.range)
        message = "["
        i = 0
        for i in xrange(0, 100, 10):
            if percentage > i:
                message = message + "="
            else:
                message = message + " "
        message = message + "] " + str(percentage) + "%"
        return message

    def set_values(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value
        self.range = max_value - min_value