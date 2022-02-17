class Goal:

    def __init__(self, goalid, name, description, icon, reached, target, target_minvalue, target_maxvalue, target_text):
        self.goalid = goalid
        self.name = name
        self.description = description
        self.icon = "https://openweathermap.org/img/wn/" + icon + ".png"
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
        if (target_text is None):
            self.target_text = ""
        else:
            self.target_text = target_text

