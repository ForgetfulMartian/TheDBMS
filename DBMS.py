import os
import time
from tabulate import tabulate

Databases = {}
Exit = "No"
cls = "True"

cd: str = ""

while Exit == "No":

    # Menu
    if cls:
        print("To get documentation for a command use: Help <command>")
        print("Evaluate mathematical expressions like \"2-324+2134\" just by: EVAL <expression>")
        print("To Create a datasheet: CREATE SHEET <Name>")
        print("To change current datasheet: CHANGE TO <Name>")
        print("To add column: COLUMN ADD <[Column Name, Value 1, Value 2, Value 3]>")
        print("To Join two datasheets: Join <sheet1> <sheet2> <Join Type> <New Sheet name>")
        print("Sum of integral column: SUM <Column Name>")
        print("To show current  datasheet's name: CD")
        print("To Exit enter exit")
        print("To Clear Screen enter cls")
        print("To save in csv form: SAVE ")

        cls = False

    # User Input
    User_Input = input("Enter command:")

    # Eval
    if User_Input[:4].lower() == "eval":

        print(eval(User_Input[5:]))
        pass

    # Create Sheet

    elif User_Input[:12].lower() == "create sheet":

        if User_Input[13:] not in Databases:

            Databases[User_Input[13:]] = []
            cd = User_Input[13:]

        else:

            print("Sheet with name", User_Input[13:], 'exists, change current sheet to', User_Input[13:], '?')
            Y_N = input("Y/N:").lower()

            if Y_N.lower() == "y":
                cd = User_Input[13:]

    # Create Column

    elif User_Input[:10].lower() == "column add":

        User_Input = User_Input[11:]
        Databases[cd].append(eval(User_Input))

    # Change cd

    elif User_Input.lower().startswith("change to"):

        if User_Input[10:] in Databases:
            cd = User_Input[10:]

        else:
            print("Sheet doesn't exist.")

    # Show CD

    elif User_Input.lower() == "cd":
        print(cd)

    # Sum of column

    elif User_Input[:3].lower() == "sum":

        for i in Databases[cd]:

            if i[0] == User_Input[4:]:

                print(sum(i[1:]))

    # Exit

    elif User_Input.lower() == "exit":
        Exit = "Yes"
        pass

    # Clear Screen

    elif User_Input.lower() == "cls":

        os.system("cls")
        cls = True

    # Print Table

    elif User_Input.lower().startswith("print"):

        data = Databases[cd]
        data2 = []
        style = User_Input[6:].lower()

        for i in range(len(data[0])):

            row = []

            for j in data:
                row.append(j[i])

            data2.append(row)

        try:

            print(tabulate(data2, tablefmt=style))

        finally:

            pass

    elif User_Input.lower().startswith("join"):

        a = User_Input.split()
        sheet1 = {}
        sheet2 = {}

        for i in Databases[a[1]]:
            sheet1[i[0]] = i[1:]

        for j in Databases[a[2]]:
            sheet2[j[0]] = j[1:]

        sheet3 = {}
        Ind = list(sheet1.keys())[0]

        # Intersection

        if a[-2].lower() == "i" or a[-2].lower() == 'intersection':

            for i in sheet1:

                if i in sheet2:

                    sheet3[i] = sheet1[i] + sheet2[i]

            # Bloc for post
            sheet = []

            for i in sheet3:
                print(i)
                sheet3[i].insert(0, i)
                sheet.append(sheet3[i])

            print(sheet)

            # Creating new sheet
            if a[-1] in Databases:

                b = input("Datasheet with same name already exists, enter Y to continue by replacing it with new sheet"
                          "or type another name for the datasheet:")

                if b.lower() == 'y':

                    Databases[a[-1]] = sheet
                    cd = a[-1]

                else:

                    Databases[b] = sheet
                    cd = b

        # Union

        if a[-2].lower() == "u" or a[-2].lower() == 'union':

            for i in sheet1:

                if i in sheet2:

                    sheet3[i] = sheet1[i] + sheet2[i]

                else:

                    # noinspection PyUnboundLocalVariable

                    l1 = sheet1[i]

                    for j in range(len(sheet2[Ind])):
                        l1.append('')

                    sheet3[i] = l1

            for q in sheet2:

                if q not in sheet1:
                    l2 = []

                    for j in range(len(sheet1[Ind])):

                        l2.append("")

                    l2 = l2 + sheet2[q]
                    sheet3[q] = l2

            # Bloc for post
            sheet = []

            for i in sheet3:

                sheet3[i].insert(0, i)
                sheet.append(sheet3[i])

            # Creating new sheet
            if a[-1] in Databases:

                b = input(
                    "Datasheet with same name already exists, enter Y to continue by replacing it with new "
                    "sheet "
                    "or type another name for the datasheet:")

                if b.lower() == 'y':

                    Databases[a[-1]] = sheet
                    cd = a[-1]

                else:

                    Databases[b] = sheet
                    cd = b

        # Left

        if a[-2].lower() == "l" or a[-2].lower() == 'left':

            for i in sheet1:

                if i in sheet2:
                    sheet3[i] = sheet1[i] + sheet2[i]

                else:

                    # noinspection PyUnboundLocalVariable

                    l1 = sheet1[i]

                    for j in range(len(sheet2[Ind])):
                        l1.append('')

                    sheet3[i] = l1


            # Bloc for post
            sheet = []

            for i in sheet3:

                sheet3[i].insert(0, i)
                sheet.append(sheet3[i])

            # Creating new sheet
            if a[-1] in Databases:

                b = input(
                    "Datasheet with same name already exists, enter Y to continue by replacing it with new "
                    "sheet "
                    "or type another name for the datasheet:")

                if b.lower() == 'y':

                    Databases[a[-1]] = sheet
                    cd = a[-1]

                else:

                    Databases[b] = sheet
                    cd = b

        # Right

        if a[-2].lower() == "r" or a[-2].lower() == 'right':

            for i in sheet1:

                if i in sheet2:
                    sheet3[i] = sheet1[i] + sheet2[i]

            for q in sheet2:

                if q not in sheet1:
                    l2 = []

                    for j in range(len(sheet1[Ind])):
                        l2.append("")

                    l2 = l2 + sheet2[q]
                    sheet3[q] = l2

            # Bloc for post
            sheet = []

            for i in sheet3:
                sheet3[i].insert(0, i)
                sheet.append(sheet3[i])

            # Creating new sheet
            if a[-1] in Databases:

                b = input(
                    "Datasheet with same name already exists, enter Y to continue by replacing it with new "
                    "sheet "
                    "or type another name for the datasheet:")

                if b.lower() == 'y':

                    Databases[a[-1]] = sheet
                    cd = a[-1]

                else:

                    Databases[b] = sheet
                    cd = b

    # Help
    elif User_Input.lower().startswith("help"):

        if User_Input[5:].lower() == "print":
            print("Use print command to display your datasheet in tabular form, in various different possible formats:")
            print("syntax:")
            print("print <format>")
            print("Valid values for format are:")
            print(''' 
            "plain"
            "simple"
            "github"
            "grid"
            "simple_grid"
            "rounded_grid"
            "heavy_grid"
            "mixed_grid"
            "double_grid"
            "fancy_grid"
            "outline"
            "simple_outline"
            "rounded_outline"
            "heavy_outline"
            "mixed_outline"
            "double_outline"
            "fancy_outline"
            "pipe"
            "orgtbl"
            "asciidoc"
            "jira"
            "presto"
            "pretty"
            "psql"
            "rst"
            "mediawiki"
            "moinmoin"
            "youtrack"
            "html"
            "unsafehtml"
            "latex"
            "latex_raw"
            "latex_booktabs"
            "latex_longtable"
            "textile"
            "tsv"
            ''')

print(Databases)
time.sleep(50)
