class MatchMaker:
    def __init__(self, students):
        self.students = students

    def calculate_score(self, s1, s2):
        score = 0

        # Age scoring
        age_diff = abs(int(s1['age']) - int(s2['age']))
        if age_diff == 0:
            score += 10
        elif age_diff <= 2:
            score += 5

        # Gender
        if s1['gender'].lower() == s2['gender'].lower():
            score += 10

        # Country
        if s1['country'].lower() == s2['country'].lower():
            score += 10

        # Sports
        if s1['sports'] != 'none' and s2['sports'] != 'none':
            score += 5
            if s1['sports'] == s2['sports']:
                score += 5

        # Art
        if s1['art'] != 'none' and s2['art'] != 'none':
            score += 5
            if s1['art'] == s2['art']:
                score += 5

        # Games
        if s1['games'] != 'none' and s2['games'] != 'none':
            score += 5
            if s1['games'] == s2['games']:
                score += 5

        # Movie
        if s1['movie'] != 'none' and s2['movie'] != 'none':
            score += 5
            if s1['movie'] == s2['movie']:
                score += 5

        return score

    def get_best_matches(self):
        if len(self.students) < 2:
            return []

        best_pairs = []
        max_score = -1

        for i in range(len(self.students)):
            for j in range(i + 1, len(self.students)):
                s1 = self.students[i]
                s2 = self.students[j]
                score = self.calculate_score(s1, s2)
                if score > max_score:
                    best_pairs = [((s1, s2), score)]
                    max_score = score
                elif score == max_score:
                    best_pairs.append(((s1, s2), score))

        return best_pairs