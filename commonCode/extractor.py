# For testing purposes only inside a Jupyter environment.
# Technically the data model being used should not need reducing any further.

# ([{data}, {Dictionary}], [list,of,parameters]) -> [[array,of],[arrays,init]]
def extract_for_clustering(data,parameters):
    output = []
    for i in range(len(data)):
        deets = []        
        for p in parameters:
            deets.append(data[i][p])
        output.append(deets)
    return output