from random import randint

class Scenario:
    def __init__(self, scene_num, picture_path: str):
        self.picture_path = picture_path
        self.cases = {}
        self.scene_num = scene_num
        self.luck_diff = randint(1, 20)

    def set_cases(
        self,
        caption: str,
        choice1: str,
        pos_outcome1: str,
        neg_outcome1: str,
        choice2: str,
        pos_outcome2: str,
        neg_outcome2: str,
    ) -> None:
        """Must be two cases"""

        self.caption = caption

        # Case 1
        self.cases["choice1"] = ["pos_outcome1", "pos_outcome2"]

        self.cases["choice1"] = choice1
        self.cases["pos_outcome1"] = pos_outcome1
        self.cases["neg_outcome1"] = neg_outcome1

        # Case 2
        self.cases["choice2"] = choice2
        self.cases["pos_outcome2"] = pos_outcome2
        self.cases["neg_outcome2"] = neg_outcome2

        return None

    def __str__(self):
        output_string = f'scenario{self.scene_num}'
        # picture_path: {self.picture_path},
        # \nChoice1: {self.cases["choice1"]}, postive outcome: {self.cases["pos_outcome1"]}, negitive outcome: {self.cases["neg_outcome1"]},
        # \nChoice2: {self.cases["choice2"]}, postive outcome: {self.cases["pos_outcome2"]}, negitive outcome: {self.cases["neg_outcome2"]}"""

        return output_string
