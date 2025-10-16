class MatchMaker:
    def __init__(self, students):
        # Store the list of students for matching
        self.students = students

    def match_score(self, s1, s2):
        """
        Calculate compatibility score from student s1 to s2 based on:
        - Age difference
        - Gender match
        - Country match
        - Study program match
        - Shared interests (sports, art, games)
        """
        score = 0

        # Age scoring: exact match +10, close age (+/- 2 years) +5
        age_diff = abs(int(s1['age']) - int(s2['age']))
        if age_diff == 0:
            score += 10
        elif age_diff <= 2:
            score += 5

        # Gender match adds 10 points
        if s1['gender'].lower() == s2['gender'].lower():
            score += 10

        # Same country adds 10 points
        if s1['country'].lower() == s2['country'].lower():
            score += 10

        # Same study program adds 10 points
        if s1['studies'].lower() == s2['studies'].lower():
            score += 10

        # Each shared interest (sports, art, games) adds 20 points
        for interest in ['sports', 'art', 'games']:
            if s1[interest].lower() == 'yes' and s2[interest].lower() == 'yes':
                score += 20

        return score

    def get_best_matches(self, threshold=80):
        """
        Return one-way matches: pairs (s1 → s2) where s1's score for s2 is above threshold.
        This does NOT require s2 to score s1 highly.
        """
        best_matches = []
        for i in range(len(self.students)):
            for j in range(len(self.students)):
                if i == j:
                    continue  # Skip matching a student with themselves
                s1 = self.students[i]
                s2 = self.students[j]
                score = self.match_score(s1, s2)
                if score >= threshold:
                    best_matches.append(((s1, s2), score))
        return best_matches

    def get_symmetric_matches(self, threshold=80):
        """
        Return mutual (symmetric) matches: pairs where both students
        score each other at or above threshold.
        """
        symmetric_matches = []
        for i in range(len(self.students)):
            for j in range(i + 1, len(self.students)):
                s1 = self.students[i]
                s2 = self.students[j]
                score1 = self.match_score(s1, s2)
                score2 = self.match_score(s2, s1)
                if score1 >= threshold and score2 >= threshold:
                    avg_score = (score1 + score2) // 2  # Average compatibility score
                    symmetric_matches.append(((s1, s2), avg_score))
        return symmetric_matches

    def get_transitive_matches(self, threshold=80):
        """
        Return transitive matches:
        If (a → b) and (b → c) exist (both above threshold),
        then (a → c) is a transitive match via b (even if a → c is not directly above threshold).
        """
        relations = set()

        # Collect all one-way relations above threshold
        for i in range(len(self.students)):
            for j in range(len(self.students)):
                if i == j:
                    continue  # Skip self-matching
                s1 = self.students[i]
                s2 = self.students[j]
                score = self.match_score(s1, s2)
                if score >= threshold:
                    relations.add((s1['id'], s2['id']))

        # Map student IDs back to student objects for easy lookup
        id_to_student = {s['id']: s for s in self.students}
        transitive_matches = []

        # For each relation (a → b), check if there is (b → c)
        # If so, and (a → c) does NOT exist, add (a → c) as a transitive match
        for (a, b) in relations:
            for (b2, c) in relations:
                if b == b2 and (a, c) not in relations and a != c:
                    # Return tuple of (a, c) connected via b
                    transitive_matches.append((id_to_student[a], id_to_student[c], id_to_student[b]))

        return transitive_matches