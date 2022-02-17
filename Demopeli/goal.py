class Goal:

    def __init__(self, goalid, name, description, reached, target, target_minvalue, target_maxvalue, target_text):
        self.goalid = goalid
        self.name = name
        self.description = description
        self.reached = reached
        self.target = target
        if (target_minvalue is None):
            self.target_minvalue = 0.0
        else:
            self.target_minvalue = float(target_minvalue)
        if (target_maxvalue is None):
            self.target_maxvalue = 0.0
        else:
            self.target_maxvalue = float(target_maxvalue)
        self.target_text = target_text
