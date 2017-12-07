class MajorScale:
    #Inputs Search scale and Solfege note, outputs corresponding note in scale
    def notes(scale, solf):
        #Assume all inputs valid
        chromatic_scale = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
        solfege_series = {"Do": 0, "Re": 2, "Mi": 4, "Fa": 5, "So": 7, "La": 9, "Ti": 11}

        return chromatic_scale[(chromatic_scale.index(scale) + solfege_series[solf]) % 12]

    #Test Statements
    print(notes("C", "Do"))
    print(notes("C", "Re"))
    print(notes("C", "Mi"))
    print(notes("D", "Mi"))
    print(notes("A#", "Fa"))