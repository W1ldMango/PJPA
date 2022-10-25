"""
@TODO implementujte dle zadání cvičení 8
"""


class Card:
    VALUES = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    SUITS = ["s", "k", "p", "t"]

    def __init__(self, given_rank, given_suit):

        if given_rank not in self.VALUES:
            self.rank_error(given_rank)

        if given_suit not in self.SUITS:
            self.suit_error(given_suit)

        self._rank = given_rank
        self._suit = given_suit

    @property
    def rank(self):
        """
        rank getter
        """
        return self._rank

    @rank.setter
    def rank(self, given_rank):
        """
        rank setter
        """
        if given_rank in self.VALUES:
            self._rank = given_rank
        else:
            self.rank_error(given_rank)

    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self, given_suit):
        if given_suit in self.SUITS:
            self._suit = given_suit
        else:
            self.suit_error(given_suit)

    def black_jack_rank(self):
        """
        Metoda vrací hodnotu karty dle pravidel pro Black Jack

        """
        if self._rank == 14:
            return 11

        if 13 >= self._rank > 9:
            return 10

        return self._rank

    def __str__(self):
        suit_word = {
            "s": "srdcov",
            "k": "károv",
            "p": "pikov",
            "t": "trefov"
        }
        num_word = {
            2: ["dvojka", "á"], 3: ["trojka", "á"], 4: ["čtyřka", "á"], 5: ["pětka", "á"],
            6: ["šestka", "á"], 7: ["sedmička", "á"], 8: ["osmička", "á"], 9: ["devítka", "á"],
            10: ["desítka", "á"], 11: ["spodek", "ý"], 12: ["královna", "á"], 13: ["král", "ý"],
            14: ["eso", "é"]
        }
        return suit_word[self._suit] + num_word[self._rank][1] + " " + num_word[self._rank][0]

    def __eq__(self, other):

        self.different_types_error(other)
        return self._rank == other.rank

    def __ne__(self, other):

        self.different_types_error(other)
        return self._rank != other.rank

    def __lt__(self, other):

        self.different_types_error(other)
        return self._rank < other.rank

    def __gt__(self, other):

        self.different_types_error(other)
        return self._rank > other.rank

    def __le__(self, other):

        self.different_types_error(other)
        return self._rank <= other.rank

    def __ge__(self, other):

        self.different_types_error(other)
        return self._rank >= other.rank

    @classmethod
    def obj_type_str(cls, obj):
        str_type = str(type(obj))
        str_type = str_type.replace("<class '", "")
        str_type = str_type.replace("'>", "")
        if isinstance(obj, Card):
            str_type = str_type.replace(".Card", "")
        return str_type.upper()

    @classmethod
    def rank_error(cls, given_rank):
        raise TypeError("Invalid rank " + str(given_rank) + "!")

    @classmethod
    def suit_error(cls, given_suit):
        raise TypeError("Invalid suit " + given_suit + "!")

    def different_types_error(self, other):
        if not isinstance(self, type(other)):
            raise TypeError("Type " + self.obj_type_str(self) +
                            " cannot be compared to " + self.obj_type_str(other) + "!")


if __name__ == '__main__':
    pass
