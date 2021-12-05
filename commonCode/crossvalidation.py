# Common functions for use in setting up cross fold validation.

import copy

# Get list of primary keys from DataSet; {DataSet} -> [{Number,Timepoint},...]
def get_primary_keys(dataset):
    output = []
    for record in dataset:
        pk = {
            'Number': record['Number'],
            'Timepoint': record['Timepoint']
        }
        output.append(pk)    
    return output

# Remove primary keys 'Number' & 'Timepoint' from a record; {Record} -> {data}
def ditch_primary_keys(record):
    output = record.copy()
    output.pop('Number')
    output.pop('Timepoint')
    return output

# Extract singular record by primary key; {DataSet} -> {Record}
def get_test_data(dataset, pk):
    output = []
    for record in dataset:
        if record['Number'] == pk['Number']:
            if record['Timepoint'] == pk['Timepoint']:
                output.append(record)
    if len(output) > 1:
        raise Exception('Multiples of primary key found, check data model')
    else:
        return ditch_primary_keys(output[0])

# Extract training data (Dataset - test data); {Dataset} -> {[Records]}
def get_train_data(dataset, testdata):
    return [ditch_primary_keys(a) for a in dataset if (a['Number'],a['Timepoint']) != (testdata['Number'],testdata['Timepoint'])]    

# Get list of subject values from list of records {Record} -> {data}
def get_subject_values(dataset,subject):
    return [x[subject] for x in dataset]

# Strip subject values from list of Records; {Dataset} -> {data}
def strip_subject_values(dataset,subject):
    output = copy.deepcopy(dataset)
    for x in output:
        x.pop(subject)
    return output

# Generate the X,Y (data, subject) structure used by sci-kit learn models, must pass in pandas functions as parameters
def create_model_data(dataset,subject,pdArrayFunc,pdVstackFunc):    
    # Array of subject values
    y = pdArrayFunc(get_subject_values(dataset,subject))
    # Array of non-subject values
    np_arrays = [pdArrayFunc(list(x.values())) for x in strip_subject_values(dataset,subject)]
    x = np_arrays[0]
    for i in range(1,len(np_arrays)):
        x = pdVstackFunc([x,np_arrays[i]])

    return x,y
