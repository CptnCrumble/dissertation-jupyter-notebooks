# --- support functions ---

# data -> Object of max values for wearble data
def get_max_wearables(data):
    bks = 0
    dks = 0
    fds = 0
    pti = 0
    ptt = 0
    
    for index in range(len(data)):
        for record in data[index]:
            if data[index]["BKS"] > bks:
                bks = data[index]["BKS"]
            if data[index]["DKS"] > dks:
                dks = data[index]["DKS"]
            if data[index]["FDS"] > fds:
                fds = data[index]["FDS"]
            if data[index]["PTI"] > pti:
                pti = data[index]["PTI"]
            if data[index]["PTT"] > ptt:
                ptt = data[index]["PTT"]

    return {
        "BKS": bks,
        "DKS": dks,
        "FDS": fds,
        "PTI": pti,
        "PTT": ptt
    }

def normalise(value,max_value):
    return (value / max_value)

# -> maximum value for any given parameter
def get_max_value(parameter, max_wearables):
    max_summaries = {
        'NMS-TOTAL': 31,
        'PDSS-TOTAL': 60,
        'PDQ8-TOTAL': 32,
        'PDQ8-PDQSI': 100,
        'Anxiety': 21,
        'Depression': 21,
        'PDQ39-PDQSI': 100,
        'PDQ39-Mob': 100,
        'PDQ39-ADL': 100,
        'PDQ39-Emot': 100,
        'PDQ39-Stigma': 100,
        'PDQ39-Soc-Sup': 100,
        'PDQ39-Cog': 100,
        'PDQ39-Comm': 100,
        'PDQ39-Discom': 100,
        'UPDRS-TOTAL': 100,
        'PDQC-PDQSI': 100,
        'PDQC-social/personal-activities': 100,
        'PDQC-anx/dep': 100,
        'PDQC-Self-care': 100,
        'PDQC-Stress': 100
    }    
    
    if parameter in max_wearables.keys():
        return max_wearables[str(parameter)]
    elif parameter in max_summaries.keys():
        return max_summaries[str(parameter)]
    elif str(parameter)[:3] == "NMS-":
        return 1
    elif str(parameter)[:3] == "HADS":
        return 3
    else:
        return 4

# record -> copy of the record where all paramters have been normalised
def normalise_record(record,max_wearables):
    output = record.copy()
    for k,v in output.items():
        if k == 'Number' or k == 'Timepoint':
            pass
        else :
            output[k] = normalise(v,get_max_value(k,max_wearables))
    return output

# --- primary function ---

# dataset -> List of normalised records
def normalise_data_set(dataset):
    max_wearables = get_max_wearables(dataset)
    output = []
    for index in range(len(dataset)):
        output.append(normalise_record(dataset[index],max_wearables))        
    return output