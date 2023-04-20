
class RomInt:
    def romanToInt(self, s: str) -> int:  # given a roman numeral, convert it to an integer
        result = 0
        legend = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        letterList = list(s) # using list function to parse string into array of characters
        #print(letterList)

        #loop to iterate over my list
        for letter in letterList:
            for key, value in legend.items():
                if letter == key:
                    result = result + value

        return result


if __name__ == '__main__':
    romInt = RomInt()

    print(romInt.romanToInt("V"))