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
        """
        Returns one-way matches where the score from s1 to s2 is above threshold.
        """
        best_matches = []
        for i in range(len(self.students)):
            for j in range(len(self.students)):
                if i == j:
                    continue
                s1 = self.students[i]
                s2 = self.students[j]
                score = self.match_score(s1, s2)
                if score >= threshold:
                    best_matches.append(((s1, s2), score))
        return best_matches

    def get_symmetric_matches(self, threshold=70):
        """Returns only mutual (symmetric) matches where both students score each other >= threshold."""
        symmetric_matches = []
        for i in range(len(self.students)):
            for j in range(i + 1, len(self.students)):
                s1 = self.students[i]
                s2 = self.students[j]
                score1 = self.match_score(s1, s2)
                score2 = self.match_score(s2, s1)
                if score1 >= threshold and score2 >= threshold:
                    avg_score = (score1 + score2) // 2
                    symmetric_matches.append(((s1, s2), avg_score))
        return symmetric_matches

    def get_transitive_matches(self, threshold=70):
        """
        If (a,b) and (b,c) exist, then add (a,c) due to b.
        """
        relations = set()
        for i in range(len(self.students)):
            for j in range(len(self.students)):
                if i == j:
                    continue
                s1 = self.students[i]
                s2 = self.students[j]
                score = self.match_score(s1, s2)
                if score >= threshold:
                    relations.add((s1['id'], s2['id']))

        # Now check transitive closure
        id_to_student = {s['id']: s for s in self.students}
        transitive_matches = []

        for (a, b) in relations:
            for (b2, c) in relations:
                if b == b2 and (a, c) not in relations and a != c:
                    transitive_matches.append((id_to_student[a], id_to_student[c], id_to_student[b]))  # (a, c, via b)

        return transitive_matches