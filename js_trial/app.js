function find(){

    var data = document.getElementById('details')

    var name = data.elements[0].value;
    var outdoors = data.elements[1].value;
    var indoors = data.elements[2].value;
    var bodypart = data.elements[3].value;
    var budget = data.elements[4].value;
    var times = data.elements[5].value;

    var events = {
        1: ['Mum', false , 'L', 69, 'E'],
        2: ['Dad', true, 'L', 420, 'E'],
        69: ['Dad', true, 'C', 1, 'M'],
        21: ['L', true, 'U', 420, 'M'],
        0: ['Dad', true, 'C', 4200, 'A'],
    };

    var bias = {};

    var eventkey;

    for (eventkey in events) {
        var currentbias = 0;
        if (events[eventkey][1] == outdoors){
            currentbias += 1 ;
        };
        if (events[eventkey][2] == bodypart){
            currentbias += 1 ;
        };
        if (events[eventkey][3] <= budget){
            currentbias += 1 ;
        };
        if (events[eventkey][4] == times){
            currentbias += 1 ;
        };
        bias[eventkey] = currentbias;
    }

    var bias_list = [];
    var bias_list2 = [];

    for (var key in bias){
        bias_list.push([key,bias[key]]);
    };

    bias_list.sort(function(a,b) {
        return a[1]-b[1];
    });

    for (var i in bias_list2){
        bias_list2.push(i[0]);
    }

    var top3keys = bias_list2.slice(0,3);
    var top3events = [];

    for (var eventkey in top3keys){
        top3events.push(events[eventkey]);
    }
    window.alert(top3events.toString());

}






