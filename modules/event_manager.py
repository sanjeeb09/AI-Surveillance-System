import time


class EventManager:

    def __init__(self):

        self.cooldown = 15

        self.last_event = 0

    def should_trigger(self, fusion_score):

        if fusion_score <= 0.75:
            return False

        current = time.time()

        if current - self.last_event < self.cooldown:
            return False

        self.last_event = current

        return True


event_manager = EventManager()