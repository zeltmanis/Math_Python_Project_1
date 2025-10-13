class Matchmaker:
    def __init__(self, students):
        self.students = students

    def get_matches(self):
        matched = []
        for i in range(len(self.students)):
            for j in range(i + 1, len(self.students)):
                s1 = self.students[i]
                s2 = self.students[j]
                if s1['country'] == s2['country']:
                    age_diff = abs(int(s1['age']) - int(s2['age']))
                    if age_diff <= 2:
                        matched.append((s1['name'], s2['name']))
        return matched