import datetime, math

def return_variable_s(float_var):
    if round(float_var * 10) / 10 != 1:
        return "s"
    return ""

def return_flat_float(float_var):
    if int(float_var) == round(float_var * 10) / 10:
        return str(int(float_var))
    return str(round(float_var * 10) / 10)

def readable_timedelta(time_delta=None, timestamp=None, accuracy=None, detail=2):
    # detail defines how many time units are output
    # Check if the timestamp is an datetime timestamp or an ISO time string
    if time_delta is None:
        if timestamp is None:
            return ""
        
        try:
            if isinstance(timestamp, datetime.datetime):
                time_delta = datetime.datetime.now() - timestamp
            elif isinstance(timestamp, str):
                time_delta = datetime.datetime.now() - datetime.datetime.fromisoformat(timestamp)
            else:
                return "Failed to parse timestamp"
        except:
            return "Failed to parse timestamp"
        
    time_delta = abs(time_delta)

    # Convert time_delta to seconds
    delta_seconds = time_delta.total_seconds()

    time_value_table = {
        6: {'time_var': 31536000, 'time_string': " year"},
        5: {'time_var': 2592000, 'time_string': " month"},
        4: {'time_var': 86400, 'time_string': " day"},
        3: {'time_var': 3600, 'time_string': " hour"},
        2: {'time_var': 60, 'time_string': " minute"},
        1: {'time_var': 1, 'time_string': " second"}
    }

    # Determine the accuracy if not specified
    if not accuracy:
        accuracy = []
        for i in time_value_table:
            if delta_seconds > time_value_table[i]['time_var']:
                accuracy = [i]
                break

    return_str = ""
    detail_ct = 0
    for i in range(len(time_value_table), 0, -1):
        if i not in accuracy:
            continue

        return_time = math.floor(delta_seconds / time_value_table[i]['time_var'])
        if return_time > 0:
            if return_str != "":
                return_str += " "

            detail_ct = detail_ct+1
            if detail is not None and detail_ct > detail:
                break

            return_str += return_flat_float(return_time) + time_value_table[i]['time_string'] + return_variable_s(return_time)
            delta_seconds -= return_time * time_value_table[i]['time_var']

    return return_str