import json
import os
import time
os.system("cls")
print('Welcome to 114514NotAvailable\'s RPE chart merger v2.1!')
print('Note: Bundled with Ex:Phiedit v4.5, distributing this program separately is not allowed.\n')
loop=True
while loop:
    print('Select an operation to execute:')
    print('  1. Merge all charts')
    print('  2. Move selected charts by a number of bars')
    choice = input('Please enter your choice: ')
    if choice == '1' or choice == '2':
        loop=False
    else:
        print('\nError: Invalid input! Please try again.')
del loop
os.system("md \".\\Selected\" >nul & md \".\\All Charts\" >nul")
#Reading Chartlist.txt
ChartlistRAW = open("Chartlist.txt", mode='r', encoding='UTF-8')
ChartlistRAW = ChartlistRAW.read().splitlines()
ChartlistLST = []
ChartlistTMP = []
for index in range(1,len(ChartlistRAW)):
    if ChartlistRAW[index] != '#':
        ChartlistTMP.append(ChartlistRAW[index])
    else:
        ChartlistLST.append(ChartlistTMP)
        ChartlistTMP = []
del index
ChartlistLST.append(ChartlistTMP)
del ChartlistTMP
del ChartlistRAW
#Create temp files for selection
for index in range(len(ChartlistLST)):
    File = open(".\\All Charts\\"+ChartlistLST[index][1].lstrip("Path: ")+".txt", mode="w", encoding='UTF-8')
    File.write("# Song details: \n\n")
    for lines in ChartlistLST[index]:
        File.write(lines + '\n')
    File.close()
del File
del index
del ChartlistLST
#Call Explorer.exe (In case of mobile devices we use wfm.exe instead of explorer.exe)
os.system("start \"Selected\" \"wfm.exe\" \".\\Selected\\\" & start \"All Charts\" \"wfm.exe\" \".\\All Charts\\\"")
os.system("cls")
print('Welcome to 114514NotAvailable\'s RPE chart merger v2.1!')
print('Note: Bundled with Ex:Phiedit v4.5, distributing this program separately is not allowed.\n')
print('Instructions: ')
print('All your charts are being listed in the "All Charts" folder. ')
print('Double click on the text file to view the song details. ')
print('Drag all the charts you want to add into the "Selected" folder. ')
print('Charts will be ordered with its file name in increasing alphabetical order. ')
print('You may rename these text files to re-order them but you should never edit anything inside the file. ')
print('You can also duplicate files if you want to overlap it with its self. \n')
input('Press the return key when done...')
#Process the user's selection
os.system("md \".\\Selected\\Result\" >nul & attrib \".\\Selected\\Result\" +s +h & dir \".\\Selected\\*.txt\" /b /o:n > \".\\Selected\\Result\\.txt\"")
os.system("del \".\\All Charts\" /f /s /q & rmdir \".\\All Charts\" /s /q")
if os.path.getsize(".\\Selected\\Result\\.txt") <= 0: #File empty?
    os.system("del \".\\Selected\" /f /s /q & rmdir \".\\Selected\" /s /q")
    os.system("cls")
    print('Welcome to 114514NotAvailable\'s RPE chart merger v2.1!')
    print('Note: Bundled with Ex:Phiedit v4.5, distributing this program separately is not allowed.\n')
    print('ERROR: No charts are being selected! \nExiting now...')
    time.sleep(5)
    quit()
else: #The list file is not empty, GOOD! Let's move on.
    result = open(".\\Selected\\Result\\.txt", mode='r', encoding='UTF-8')
    result = result.read().splitlines()
    #'result' now holds the list of files that exist in '.\Selected'
    opened_charts = []
    merge_bpm = False
    merge_chart = False
    obfuscate = False
    super_obf = False
    move_amount = 0.0
    offset_per_file = 0.0
    #Configure some options:
    os.system("cls")
    print('Welcome to 114514NotAvailable\'s RPE chart merger v2.1!')
    print('Note: Bundled with Ex:Phiedit v4.5, distributing this program separately is not allowed.\n')
    print('Options: ')
    loop = True
    while loop:
        selection = input('Do you want to obfuscate this chart? [Y/N]') #Making XPE unable to read this chart, but various chart players should work fine.
        if selection.upper() == 'Y' or selection.upper() == 'N':
            loop = False
            if selection.upper() == 'Y': obfuscate = True
        else:
            print('Error: Invalid input! Please try again.')
    if obfuscate:
        loop = True
        while loop:
            selection = input('Enable extreme obfuscate? (Warning: May slow down event process!) [Y/N]') #Modify more items, making the chart even harder to recover.
            if selection.upper() == 'Y' or selection.upper() == 'N':
                loop = False
                if selection.upper() == 'Y': super_obf = True
            else:
                print('Error: Invalid input! Please try again.')
    if choice == '2':
        from fractions import Fraction
        loop = True
        while loop:
            selection = input('Amount of bars to move: ')
            try:
                move_amount = Fraction(selection)
                loop = False
            except:
                print('Error: Invalid input! Please try again.')
        loop = True
        while loop:
            selection = input('Offset per file: ')
            try:
                offset_per_file = Fraction(selection)
                loop = False
            except:
                print('Error: Invalid input! Please try again.')
        loop = True
        while loop:
            selection = input('Do you want to merge these charts? [Y/N]') #Ask if the user wants to merge all the moved charts into one
            if selection.upper() == 'Y' or selection.upper() == 'N':
                loop = False
                if selection.upper() == 'Y': merge_chart = True
            else:
                print('Error: Invalid input! Please try again.')
    if choice == '1' or merge_chart:
        loop = True
        while loop:
            selection = input('Do you want to merge BPM events? [Y/N]') #Merge BPM?
            if selection.upper() == 'Y' or selection.upper() == 'N':
                loop = False
                if selection.upper() == 'Y': merge_bpm = True
            else:
                print('Error: Invalid input! Please try again.')
    del loop
    del selection
    #Time to open up the actual chart files!
    os.system("cls")
    print('Welcome to 114514NotAvailable\'s RPE chart merger v2.1!')
    print('Note: Bundled with Ex:Phiedit v4.5, distributing this program separately is not allowed.\n')
    print('Please wait...')
    print('Reading charts...')
    opened_chart_list = []
    for filename in result:
        data = open(".\\Selected\\" + filename, mode='r', encoding='UTF-8').read().splitlines()
        opened_chart_list.append(data)
        opened_charts.append(json.load(open('.\\Resources\\' + data[3].lstrip("Path: ") + '\\' + data[6].lstrip("Chart: "), mode='r', encoding='UTF-8')))
        print('Loaded ' + filename.rstrip('.txt'))
    del filename
    del data
    ChartCount = 0
    os.system("del \".\\Selected\" /f /s /q & rmdir \".\\Selected\" /s /q")
    if choice == '2':
        print('Time move begins...')
        chartlist_edit = open("Chartlist.txt", mode='a', encoding='UTF-8')
        for chart in opened_charts:
            for bpm in chart["BPMList"]:
                Start = bpm["startTime"]
                new_value = Fraction(Start[0] * Start[2] + Start[1], Start[2]) + move_amount
                bpm["startTime"] = [0, new_value.numerator, new_value.denominator]
            if obfuscate:
                chart["judgeLineGroup"] = "卧槽，谱面居然被神奇的Ex:Phiedit混淆了！惊不惊喜意不意外？"
                chart["META"] = json.loads('{"offset":' + str(chart["META"]["offset"]) + '}')
            ChartLines = 0
            EventCount = 0
            for line in chart["judgeLineList"]:
                print('Processing line ' + str(ChartLines) + ' in chart ' + result[ChartCount].rstrip('.txt'))
                if obfuscate:
                    line["Group"] = "卧槽，谱面居然被神奇的Ex:Phiedit混淆了！惊不惊喜意不意外？"
                    line["bpmfactor"] = "卧槽，谱面居然被神奇的Ex:Phiedit混淆了！惊不惊喜意不意外？"
                else:
                    line["Group"] = 0
                line["Name"] = "Created with Ex:Phiedit v4.5"
                try:
                    line["eventLayers"]
                    go = True
                except:
                    go = False
                if go:
                    for layer in line["eventLayers"]:
                        if layer != None:
                            for event_type in layer:
                                for event in layer[event_type]:
                                    Start = event["startTime"]
                                    End = event["endTime"]
                                    new_value = Fraction(Start[0] * Start[2] + Start[1], Start[2]) + move_amount
                                    event["startTime"] = [0, new_value.numerator, new_value.denominator]
                                    new_value = Fraction(End[0] * End[2] + End[1], End[2]) + move_amount
                                    event["endTime"] = [0, new_value.numerator, new_value.denominator]
                                    if super_obf: event["linkgroup"] = "卧槽，谱面居然被神奇的Ex:Phiedit混淆了！惊不惊喜意不意外？"
                                    EventCount += 1
                try:
                    line["extended"]
                    go = True
                except:
                    go = False
                if go:
                    for event_type in line["extended"]:
                        for event in line["extended"][event_type]:
                            Start = event["startTime"]
                            End = event["endTime"]
                            new_value = Fraction(Start[0] * Start[2] + Start[1], Start[2]) + move_amount
                            event["startTime"] = [0, new_value.numerator, new_value.denominator]
                            new_value = Fraction(End[0] * End[2] + End[1], End[2]) + move_amount
                            event["endTime"] = [0, new_value.numerator, new_value.denominator]
                            if super_obf: event["linkgroup"] = "卧槽，谱面居然被神奇的Ex:Phiedit混淆了！惊不惊喜意不意外？"
                            EventCount += 1
                try:
                    line["notes"]
                    go = True
                except:
                    go = False
                if go:
                    for note in line["notes"]:
                        Start = note["startTime"]
                        End = note["endTime"]
                        new_value = Fraction(Start[0] * Start[2] + Start[1], Start[2]) + move_amount
                        note["startTime"] = [0, new_value.numerator, new_value.denominator]
                        new_value = Fraction(End[0] * End[2] + End[1], End[2]) + move_amount
                        note["endTime"] = [0, new_value.numerator, new_value.denominator]
                        EventCount += 1
                ChartLines += 1
                print('Processed event: ' + str(EventCount))
            if not merge_chart: #Write to separate files if the user didn't require merging
                if move_amount < 0:
                    os.system('xcopy \".\\Resources\\' + opened_chart_list[ChartCount][3].lstrip("Path: ") + '\" \".\\Resources\\' + opened_chart_list[ChartCount][3].lstrip("Path: ") + '-' + str(-(float(move_amount.numerator) / float(move_amount.denominator))) + '\" /c /e /v /r /y /k /i')
                    print('Writing to ' + '.\\Resources\\' + opened_chart_list[ChartCount][3].lstrip("Path: ") + '-' + str(-(float(move_amount.numerator) / float(move_amount.denominator))) + '\\' + opened_chart_list[ChartCount][6].lstrip("Chart: "))
                    final_output = open('.\\Resources\\' + opened_chart_list[ChartCount][3].lstrip("Path: ") + '-' + str(-(float(move_amount.numerator)/float(move_amount.denominator))) + '\\' + opened_chart_list[ChartCount][6].lstrip("Chart: "), mode='w', encoding='UTF-8')
                else:
                    os.system('xcopy \".\\Resources\\' + opened_chart_list[ChartCount][3].lstrip("Path: ") + '\" \".\\Resources\\' + opened_chart_list[ChartCount][3].lstrip("Path: ") + '+' + str(float(move_amount.numerator) / float(move_amount.denominator)) + '\" /c /e /v /r /y /k /i')
                    print('Writing to ' + '.\\Resources\\' + opened_chart_list[ChartCount][3].lstrip("Path: ") + '+' + str(float(move_amount.numerator) / float(move_amount.denominator)) + '\\' + opened_chart_list[ChartCount][6].lstrip("Chart: "))
                    final_output = open('.\\Resources\\' + opened_chart_list[ChartCount][3].lstrip("Path: ") + '+' + str(float(move_amount.numerator)/float(move_amount.denominator)) + '\\' + opened_chart_list[ChartCount][6].lstrip("Chart: "), mode='w', encoding='UTF-8')
                json.dump(chart, final_output, ensure_ascii=False)
                final_output.close()
                chartlist_edit.write('\n#\n')
                if move_amount < 0:
                    chartlist_edit.write(opened_chart_list[ChartCount][2] + ' -' + str(-(float(move_amount.numerator)/float(move_amount.denominator))) + 'bars\n')
                    chartlist_edit.write(opened_chart_list[ChartCount][3] + '-' + str(-(float(move_amount.numerator)/float(move_amount.denominator))) + '\n')
                else:
                    chartlist_edit.write(opened_chart_list[ChartCount][2] + ' +' + str(float(move_amount.numerator)/float(move_amount.denominator)) + 'bars\n')
                    chartlist_edit.write(opened_chart_list[ChartCount][3] + '+' + str(float(move_amount.numerator)/float(move_amount.denominator)) + '\n')
                chartlist_edit.write(opened_chart_list[ChartCount][4] + '\n')
                chartlist_edit.write(opened_chart_list[ChartCount][5] + '\n')
                chartlist_edit.write(opened_chart_list[ChartCount][6] + '\n')
                chartlist_edit.write(opened_chart_list[ChartCount][7] + '\n')
                chartlist_edit.write(opened_chart_list[ChartCount][8] + '\n')
                chartlist_edit.write(opened_chart_list[ChartCount][9])
                if move_amount < 0:
                    info = open('.\\Resources\\' + opened_chart_list[ChartCount][3].lstrip("Path: ") + '-' + str(-(float(move_amount.numerator)/float(move_amount.denominator))) + '\\info.txt', mode='w', encoding='UTF-8')
                    info.write('#\n')
                    info.write(opened_chart_list[ChartCount][2] + ' -' + str(-(float(move_amount.numerator)/float(move_amount.denominator))) + 'bars\n')
                    info.write(opened_chart_list[ChartCount][3] + '-' + str(-(float(move_amount.numerator)/float(move_amount.denominator))) + '\n')
                else:
                    info = open('.\\Resources\\' + opened_chart_list[ChartCount][3].lstrip("Path: ") + '+' + str(float(move_amount.numerator)/float(move_amount.denominator)) + '\\info.txt', mode='w', encoding='UTF-8')
                    info.write('#\n')
                    info.write(opened_chart_list[ChartCount][2] + ' +' + str(float(move_amount.numerator)/float(move_amount.denominator)) + 'bars\n')
                    info.write(opened_chart_list[ChartCount][3] + '+' + str(float(move_amount.numerator)/float(move_amount.denominator)) + '\n')
                info.write(opened_chart_list[ChartCount][4] + '\n')
                info.write(opened_chart_list[ChartCount][5] + '\n')
                info.write(opened_chart_list[ChartCount][6] + '\n')
                info.write(opened_chart_list[ChartCount][7] + '\n')
                info.write(opened_chart_list[ChartCount][8] + '\n')
                info.write(opened_chart_list[ChartCount][9])
            ChartCount += 1
            move_amount += offset_per_file
        chartlist_edit.close()
        del chartlist_edit
        del ChartCount
        del ChartLines
        del Start
        del End
        del new_value
        del EventCount
        del layer
        del event_type
        del event
        del note
        del line
        del go
        if not merge_chart:
            del info
            del final_output
            del opened_charts
            del opened_chart_list
            del choice
            del obfuscate
            del merge_chart
            del merge_bpm
            del super_obf
            del move_amount
            del offset_per_file
            del result
            os.system("cls")
            print('Welcome to 114514NotAvailable\'s RPE chart merger v2.1!')
            print('Note: Bundled with Ex:Phiedit v4.5, distributing this program separately is not allowed.\n')
            print('All done! The moved charts has been exported to .\\Resources\\')
            print('Thank you for using this program. ')
            time.sleep(5)
            quit()
    ChartCount = 0
    if choice == '1' or merge_chart:
        print('Merging begins...')
        final_chart = opened_charts[0]
        final_chart["judgeLineGroup"] = ["Default"]
        if obfuscate:
            final_chart["META"] = json.loads('{"offset":' + str(final_chart["META"]["offset"]) + '}')
            final_chart["judgeLineGroup"] = "卧槽，谱面居然被神奇的Ex:Phiedit混淆了！惊不惊喜意不意外？"
        TotalLines = 0
        ChartLines = 0
        EventCount = 0
        for line in final_chart["judgeLineList"]:
            print('Processing line ' + str(ChartLines) + ' in chart ' + result[ChartCount].rstrip('.txt'))
            if obfuscate:
                line["Group"] = "卧槽，谱面居然被神奇的Ex:Phiedit混淆了！惊不惊喜意不意外？"
                if line["bpmfactor"] == 0: line["bpmfactor"] = "卧槽，谱面居然被神奇的Ex:Phiedit混淆了！惊不惊喜意不意外？"
                if super_obf:
                    try:
                        line["eventLayers"]
                        go = True
                    except:
                        go = False
                    if go:
                        for layer in line["eventLayers"]:
                            if layer != None:
                                for event_type in layer:
                                    for event in layer[event_type]:
                                        event["linkgroup"] = "卧槽，谱面居然被神奇的Ex:Phiedit混淆了！惊不惊喜意不意外？"
                                        EventCount += 1
                    try:
                        line["extended"]
                        go = True
                    except:
                        go = False
                    if go:
                        for event_type in line["extended"]:
                            for event in line["extended"][event_type]:
                                event["linkgroup"] = "卧槽，谱面居然被神奇的Ex:Phiedit混淆了！惊不惊喜意不意外？"
                                EventCount += 1
            else:
                line["Group"] = 0
            line["Name"] = "Created with Ex:Phiedit v4.5"
            ChartLines += 1
        TotalLines += ChartLines
        opened_charts.pop(0)
        ChartCount += 1
        while len(opened_charts) > 0:
            ChartLines = 0
            EventCount = 0
            if merge_bpm:
                final_chart["BPMList"] += opened_charts[0]["BPMList"]
            opened_charts[0]["judgeLineGroup"] = ["Default"]
            for line in opened_charts[0]["judgeLineList"]:
                print('Processing line ' + str(ChartLines) + ' in chart ' + result[ChartCount].rstrip('.txt'))
                if obfuscate:
                    line["Group"] = "卧槽，谱面居然被神奇的Ex:Phiedit混淆了！惊不惊喜意不意外？"
                    if line["bpmfactor"] == 0: line["bpmfactor"] = "卧槽，谱面居然被神奇的Ex:Phiedit混淆了！惊不惊喜意不意外？"
                    if super_obf:
                        try:
                            line["eventLayers"]
                            go = True
                        except:
                            go = False
                        if go:
                            for layer in line["eventLayers"]:
                                if layer != None:
                                    for event_type in layer:
                                        for event in layer[event_type]:
                                            event["linkgroup"] = "卧槽，谱面居然被神奇的Ex:Phiedit混淆了！惊不惊喜意不意外？"
                                            EventCount += 1
                        try:
                            line["extended"]
                            go = True
                        except:
                            go = False
                        if go:
                            for event_type in line["extended"]:
                                for event in line["extended"][event_type]:
                                    event["linkgroup"] = "卧槽，谱面居然被神奇的Ex:Phiedit混淆了！惊不惊喜意不意外？"
                                    EventCount += 1
                        print('Processed event: ' + str(EventCount))
                else:
                    line["Group"] = 0
                line["Name"] = "Created with Ex:Phiedit v4.5"
                if line["father"] != -1:
                    line["father"] += TotalLines
                ChartLines += 1
            final_chart["judgeLineList"] += opened_charts[0]["judgeLineList"]
            ChartCount += 1
            opened_charts.pop(0)
        os.system('xcopy \".\\Resources\\' + opened_chart_list[0][3].lstrip("Path: ") + '\" \".\\Resources\\' + opened_chart_list[0][3].lstrip("Path: ") + '_merged\" /c /e /v /r /y /k /i')
        print('Writing to ' + '.\\Resources\\' + opened_chart_list[0][3].lstrip("Path: ") + '_merged\\' + opened_chart_list[0][6].lstrip("Chart: "))
        final_output = open('.\\Resources\\' + opened_chart_list[0][3].lstrip("Path: ") + '_merged\\' + opened_chart_list[0][6].lstrip("Chart: "), mode='w', encoding='UTF-8')
        json.dump(final_chart, final_output, ensure_ascii=False)
        final_output.close()
        chartlist_edit = open("Chartlist.txt", mode='a', encoding='UTF-8')
        chartlist_edit.write('\n#\n')
        chartlist_edit.write(opened_chart_list[0][2]+' (Merged)\n')
        chartlist_edit.write(opened_chart_list[0][3]+'_merged\n')
        chartlist_edit.write(opened_chart_list[0][4]+'\n')
        chartlist_edit.write(opened_chart_list[0][5]+'\n')
        chartlist_edit.write(opened_chart_list[0][6]+'\n')
        chartlist_edit.write(opened_chart_list[0][7]+'\n')
        chartlist_edit.write(opened_chart_list[0][8]+'\n')
        chartlist_edit.write(opened_chart_list[0][9])
        chartlist_edit.close()
        info = open('.\\Resources\\' + opened_chart_list[0][3].lstrip("Path: ") + '_merged\\info.txt', mode='w', encoding='UTF-8')
        info.write('#\n')
        info.write(opened_chart_list[0][2] + ' (Merged)\n')
        info.write(opened_chart_list[0][3] + '_merged\n')
        info.write(opened_chart_list[0][4] + '\n')
        info.write(opened_chart_list[0][5] + '\n')
        info.write(opened_chart_list[0][6] + '\n')
        info.write(opened_chart_list[0][7] + '\n')
        info.write(opened_chart_list[0][8] + '\n')
        info.write(opened_chart_list[0][9])
        info.close()
        del chartlist_edit
        del info
        del final_output
        del final_chart
        del opened_charts
        del ChartCount
        del EventCount
        del TotalLines
        del ChartLines
        del choice
        del line
        if super_obf: del go
        del obfuscate
        del merge_chart
        del merge_bpm
        del super_obf
        del move_amount
        del offset_per_file
        del result
        os.system("cls")
        print('Welcome to 114514NotAvailable\'s RPE chart merger v2.1!')
        print('Note: Bundled with Ex:Phiedit v4.5, distributing this program separately is not allowed.\n')
        print('All done! The merged chart has been exported to .\\Resources\\' + opened_chart_list[0][3].lstrip("Path: ") + '_merged\\' + opened_chart_list[0][6].lstrip("Chart: "))
        print('Thank you for using this program. ')
        del opened_chart_list
        time.sleep(5)
        quit()