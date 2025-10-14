class MatchMaker:
    def __init__(self, students):
        self.students = students

    def match_score(self, s1, s2):
        score = 0

        # Age
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

        # Study program
        if s1['studies'].lower() == s2['studies'].lower():
            score += 10

        # Interests
        for interest in ['sports', 'art', 'games']:
            if s1[interest].lower() == 'yes' and s2[interest].lower() == 'yes':
                score += 20

        return score

    def get_best_matches(self, threshold=70):
        """Returns all pairs with score >= threshold"""
        best_matches = []
        for i in range(len(self.students)):
            for j in range(i + 1, len(self.students)):
                s1 = self.students[i]
                s2 = self.students[j]
                score = self.match_score(s1, s2)
                if score >= threshold:
                    best_matches.append(((s1, s2), score))
        return best_matches

    def get_mutual_matches(self, threshold=70):
        """Returns only pairs that are mutual matches (both score each other above threshold)"""
        mutual_matches = []
        for i in range(len(self.students)):
            for j in range(i + 1, len(self.students)):
                s1 = self.students[i]
                s2 = self.students[j]
                score1 = self.match_score(s1, s2)
                score2 = self.match_score(s2, s1)
                if score1 >= threshold and score2 >= threshold:
                    avg_score = (score1 + score2) // 2
                    mutual_matches.append(((s1, s2), avg_score))
        return mutual_matches