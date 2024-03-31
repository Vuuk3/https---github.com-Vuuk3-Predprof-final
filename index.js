function get_one_data(date) {
    var url = 'https://olimp.miet.ru/ppo_it_final';
    var day = date[0], month = date[1], year = date[2];
    console.log(day, month, year);
    var data = fetch(url + '?day=' + day + '&month=' + month + '&year=' + year, 
        {mode: 'no-cors',
        headers: {'X-Auth-Token': 'ppo_11_10974'}
        }
    )
    console.log(data);
    //     .then(response => response.json())
    //     .then(data => data['message']);
    // var windows_for_flat = data['windows_for_flat']['data'];
    // var windows = data['windows']['data'];
    // console.log(windows);
    // return build(windows_for_flat, windows);
}




function build(windows_for_flat, windows) {
    let k = [];
    let ans = [];
    let y = 0;
    for (let b in windows) {
        y ++;
    };
    let flat = 1;
    let e = 0;
    let rooms = [];
    for (let i = 0; i < y; i++) {
        for (let j = 0; j < windows_for_flat.length; j++) {
            let r = windows_for_flat[j]
            for (let m = 0; m < r; m++) {
                let floor = `floor_${i + 1}`;
                k.push([flat, windows[floor][e]]);
                if (windows[floor][e] && !rooms.includes(flat)) {
                    rooms.push(flat);
                }
                e += 1;
            }
            flat += 1;
        }
        ans.unshift(k);
        k = [];
        e = 0;
    }
    return [ans, rooms.length, rooms];
}


console.log(get_one_data(['25', '03', '23']));