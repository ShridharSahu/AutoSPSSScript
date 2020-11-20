import pyreadstat

# Read MetaData Only. Read Variable Names, Type and Value Labels
df, meta = pyreadstat.read_sav('D:\Projects\SPSSAutoScript\Data.sav', metadataonly=True)
metaVar = meta.column_names
metaVarFormat = meta.original_variable_types
metaVarValueLabels = meta.variable_value_labels

# For each variable identify type and Value Labels
for var in metaVar:
    varType = metaVarFormat.get(var, '')
    valueLabels = metaVarValueLabels.get(var, '')

    if varType[0] == 'F':
        # Variable is Numeric

        if valueLabels != '':
            # Variable has value labels.
            if len(list(valueLabels.keys())) == 1 and int(list(valueLabels.keys())[0]) == 1:
                # If there are only 1 value label and it is 1 then Multi
                print(var + '-> MultiChoice')
            elif len(list(valueLabels.keys())) == 2 and int(list(valueLabels.keys())[0]) == 0 and int(list(valueLabels.keys())[1]) == 1:
                # If there are only 2 value label and it is 0/1 then Multi
                print(var + '-> MultiChoice')
            else:
                # Otherwise it is Single
                print(var + '-> SingleChoice -> ' + str(valueLabels))

        else:
            # Variable does not have any value labels
            print(var + '-> Numeric')

    elif varType[0] == 'A':
        # Variable is String
        print(var + '-> String')

    elif varType[0] == 'D':
        # Variable is Date-Time
        print(var + '-> Date-Time')

    else:
        # Variable Type not recognized
        print(var + '-> Unrecognized' + str(metaVarFormat.get(var, '')))
