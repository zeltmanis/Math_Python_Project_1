class Matchmaker:
    def __init__(self, students):
        self.students = students

    def match_students(self):
        print("\n--- Match Students ---")
        print("Basic compatibility: same country and age difference ≤ 2 years.\n")

        matched = []
        for i in range(len(self.students)):
            for j in range(i + 1, len(self.students)):
                s1 = self.students[i]
                s2 = self.students[j]
                if s1['country'] == s2['country']:
                    age_diff = abs(int(s1['age']) - int(s2['age']))
                    if age_diff <= 2:
                        matched.append((s1['name'], s2['name']))

        if matched:
            print("Matched Pairs:")
            for pair in matched:
                print(f" - {pair[0]} & {pair[1]}")
        else:
            print("No compatible matches found.")
        print("----------------------\n")