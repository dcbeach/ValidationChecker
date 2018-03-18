
def importHVLD(filePath, LTN, testType, testName):
    ##RETURNABLE FOR DISPLAY IN THE DATA SECTION OF MAIN SCREEN
    results = []
    sampleCount = 0
    posCount = 0
    negCount = 0
    grossCount = 0
    falsePositives = 0
    limitOfDetection = 0
    pn = []
    profileLetter = 'A'
    # Set Point Variables, kV, Sensitivity, Rotation, Speed, PitchkV = []
    setPoints = []
    kV = []
    sensitivity = []
    rotation = []
    speed = []
    pitch = []
    # Profile Variables
    profile = []
    step = []
    date = []
    tempint = 1

    # Scrape the Data File into memory
    with open(filePath, 'r') as inputfile:
        for line in inputfile:
            tempint += 1
            ### Set Points
            if tempint == 18:
                kV.append(line.strip().split())
                setPoints.append(int(kV[0][3]))
            elif tempint == 19:
                sensitivity.append(line.strip().split())
                setPoints.append(int(sensitivity[0][1]))
            elif tempint == 20:
                rotation.append(line.strip().split())
                setPoints.append(int(rotation[0][1]))
            elif tempint == 21:
                speed.append(line.strip().split())
                setPoints.append(int(speed[0][1]))
            elif tempint == 22:
                pitch.append(line.strip().split())
                setPoints.append(int(pitch[0][1]))
                ### Profile
            elif tempint >= 27 and tempint <= 46:
                step = []
                step.append(line.strip().split())
                if step[0][1] != "0.0":
                    profile.append(step[0])
            elif tempint == 48:
                date.append(line.strip().split())
                del date[0][0]
                date = str(date[0][0])
            elif tempint > 50:
                results.append(line.strip().split())
                sampleCount = sampleCount + 1

    # Determine negatives vs positives
    # Determine Limit of Detect (DOES NOT WORK WITH 1.5 YET)
    # Determine counts of Negtives, Positives, and Gross
    minLOD = False  # minimum limit of detection? If false then all positive controls were detected
    for result in results:
        if '-' in str(result[6]) and 'G' not in str(result[6]):
            pn.append('Positive')
            if float(result[2]) < 4.01:
                minLOD = True
                stringHolder = str(result[6])
                placeHolder = str(result[6]).find('-')
                sizeHolder = stringHolder[placeHolder - 1]
                if int(sizeHolder) > int(limitOfDetection):
                    limitOfDetection = int(sizeHolder)
            posCount = posCount + 1
        elif 'G' in str(result[6]):
            pn.append('Gross')
            grossCount = grossCount + 1
        else:
            pn.append('Negative')
            if float(result[2]) > 3.99:
                falsePositives = falsePositives + 1
            negCount = negCount + 1
    if minLOD == False:
        limitOfDetection = 2


    return sampleCount, posCount, negCount, grossCount, falsePositives, limitOfDetection, profileLetter







