# ([{data}, {Dictionary}], [list,of,parameters]) -> [[array,of],[arrays,init]]
def extract_for_clustering(data,parameters):
    output = []
    for i in range(len(data)):
        deets = []        
        for p in parameters:
            deets.append(data[i][p])
        output.append(deets)
    return output

# remove primary keys ('Number' & 'Timepoint')
def ditch_primary_keys(data):
    output = data.copy()
    output.pop('Number')
    output.pop('Timepoint')
    return output

