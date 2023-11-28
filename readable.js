const int_test = /^-?\d+$/;
function readable_timedelta(timestamp,accuracy,detail) {
    // detail defines how many time units are output
    if(int_test.test(timestamp)){
        var time_delta = timestamp
    } else {
        var time_delta = new Date() - new Date(timestamp);
    }

    function return_variable_s(float_var) {
        if (Math.round(float_var * 10) / 10 !== 1) {
            return "s";
        }
        return "";
    }

    function return_flat_float(float_var) {
        if (parseInt(float_var) === Math.round(float_var * 10) / 10) {
            return String(parseInt(float_var));
        }
        return String(Math.round(float_var * 10) / 10);
    }

    time_value_table = {
        6:{time_var:31536000,time_string:" year"},
        5:{time_var:2592000,time_string:" month"},
        4:{time_var:86400,time_string:" day"},
        3:{time_var:3600,time_string:" hour"},
        2:{time_var:60,time_string:" minute"},
        1:{time_var:1,time_string:" second"}
    }

    var delta_seconds = Math.floor(time_delta / 1000);

    if(!accuracy){
        for(i=1;i<7;i++){
            if (delta_seconds > time_value_table[i]['time_var']) {
                accuracy = [i]
            } else {
                break
            }
        }
    }

    return_str = ""
    detail_ct = 0
    for(i=6;i>0;i--){
        if(!accuracy.includes(i)){continue}

        var return_time = Math.floor(delta_seconds / time_value_table[i]['time_var']);
        if(return_time>0){
            if(return_str!=""){return_str=return_str+" "}

            detail_ct = detail_ct+1
            if(detail!==undefined&&detail_ct>detail){break}

            return_str = return_str + return_flat_float(return_time) + time_value_table[i]['time_string'] + return_variable_s(return_time);
            delta_seconds = delta_seconds-(return_time*time_value_table[i]['time_var'])
        }
    }

    return return_str
}