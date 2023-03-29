function main(){
    var max_nums = getRndInteger(50, 250);

    var xValues = new Array();
    var standard_array = new Array();
    for(let i=0; i<=max_nums; i++){
        xValues.push(i);
        standard_array.push(i);
    }

    var random_array = new Array();
    for(let i=0; i<=max_nums; i++){
        var random_index = getRndInteger(0, standard_array.length);
        random_array.push(standard_array[random_index]);
        standard_array.splice(random_index, 1);
    }

    var graph = new Chart("myChart", {
        type: "line",
        data: {
            labels: xValues,
            datasets: [{
                data: random_array,
                borderColor: "red",
                fill: true
            }]
        },
        options: {
            legend: {display: false},
            animation: {duration: 0}
        }
    });

    var alg = getRndInteger(1, 4);

    if(alg==1){
        bubble_sort(random_array, 0, random_array.length, graph);
    } else if(alg==2){
        insertion_sort(random_array, 0, graph);
    } else if(alg==3){
        selection_sort(random_array, graph, new Array());
    } else if(alg==4){
        double_selection_sort(random_array, graph, new Array(), new Array());
    } else {
        random_array = radix_sort(random_array);
        graph.data.datasets[0].data = random_array;
        graph.update();
    }
}

function bubble_sort(array, i, j, chart){
    if(array[i]>array[i+1]){
        var temp = array[i];
        array[i] = array[i+1];
        array[i+1] = temp;
        i+=1;
    } else {
        if(i==j){
            i=0;
            j-=1;
        } else {
            i+=1;
        }
    }

    if(j>0){
        requestAnimationFrame(function(){
            chart.data.datasets[0].data = array;
            chart.update();
            bubble_sort(array, i, j, chart);
        });
    } else {
        main();
    }
}

function insertion_sort(array, i, chart){
    var i_element = array[i];
    var ii_element = array[i+1];

    if(i_element>ii_element) {
        array[i] = ii_element;
        array[i+1] = i_element;

        if(i>0){
            i -= 1;
        }
        
        requestAnimationFrame(function(){
            chart.data.datasets[0].data = array;
            chart.update();
            insertion_sort(array, i, chart);
        });
    } else if(i<array.length) {
        i += 1;
        insertion_sort(array, i, chart);
    } else {
        main();
    }
}

function selection_sort(array, chart, temp_array){
    var lowest_number = Math.min(...array);
    var lowest_index = array.indexOf(lowest_number);

    temp_array.push(lowest_number);
    array.splice(lowest_index, 1);
    var final_array = temp_array.concat(array);

    if(array.length != 0){requestAnimationFrame(function(){
        chart.data.datasets[0].data = final_array;
        chart.update();
        selection_sort(array, chart, temp_array);
    })} else {
        main();
    }
}

function double_selection_sort(array, chart, low_array, high_array){
    var lowest_number = Math.min(...array);
    var lowest_index = array.indexOf(lowest_number);
    low_array.push(lowest_number);
    array.splice(lowest_index, 1);

    var highest_number = Math.max(...array);
    var highest_index = array.indexOf(highest_number);
    high_array.splice(0, 0, highest_number);
    array.splice(highest_index, 1);

    var final_array = low_array.concat(array, high_array);

    if(array.length != 0){requestAnimationFrame(function(){
        chart.data.datasets[0].data = final_array;
        chart.update();
        double_selection_sort(array, chart, low_array, high_array);
    })} else {
        main();
    }
}

function radix_sort(array){
    var biggest_num = Math.max(...array);
    var digits = biggest_num.toString().length;
    var temp_array = [];
    var n = array.length;

    for(let i=0; i<n; i++){
        var current_element = array[i];
        var string = current_element.toString();

        string = string.splice(0, 0, '0'.repeat(digits-string.length));
        temp_array.push(string);
    }

    for(let i=digits-1; i>=0; i--){
        var zeroes = [];
        var ones = [];
        var twos = [];
        var threes = [];
        var fours = [];
        var fives = [];
        var sixes = [];
        var sevens = [];
        var eights = [];
        var nines = [];

        for(let j=0; j<n; j++){
            var current_element = temp_array[j];
            var cur_digit = current_element[i];

            if(cur_digit==0){
                zeroes.push(current_element);
            } else if(cur_digit==1){
                ones.push(current_element);
            } else if(cur_digit==2){
                twos.push(current_element);
            } else if(cur_digit==3){
                threes.push(current_element);
            } else if(cur_digit==4){
                fours.push(current_element);
            } else if(cur_digit==5){
                fives.push(current_element);
            } else if(cur_digit==6){
                sixes.push(current_element);
            } else if(cur_digit==7){
                sevens.push(current_element);
            } else if(cur_digit==8){
                eights.push(current_element);
            } else if(cur_digit==9){
                nines.push(current_element);
            }
        }

        temp_array = [].concat(zeroes, ones, twos, threes, fours, fives, sixes, sevens, eights, nines);
    }

    array = [];
    for(let i=0; i<n; i++){
        array.push(Number(temp_array[i]));
    }

    return array;
}

function getRndInteger(min, max){
    return Math.floor(Math.random() * (max - min)) + min;
}

function sleep(milliseconds) {
    const date = Date.now();
    let currentDate = null;
    do {
      currentDate = Date.now();
    } while (currentDate - date < milliseconds);
}

String.prototype.splice = function(start, delCount, newSubStr) {
    return this.slice(0, start) + newSubStr + this.slice(start + Math.abs(delCount));
};