let res;
let res_data;
const BASE_URL = '';
const INPUT_ID = 'account_link';

function get_nodes(nodes_type) {

    let node_link = document.getElementById(INPUT_ID).value;
    let node_link_seg = node_link.split('/');
    let node_name = node_link_seg.slice(-1)[0];

    axios.get(BASE_URL + '/get_nodes/'+nodes_type+'/'+node_name).then(show_results);
}

function show_results(response){
    res = response;
    res_data = response['data'];

    let result_div = document.getElementById('result');
    result_div.innerHTML = '';
    for(let i=0; i<res_data['data'].length; i++) {
        let node_data = res_data['data'][i];

        let node_el = document.createElement('div');
        let search_el = document.createElement('button');
        let title_el = document.createElement('div');
        let description_el = document.createElement('div');
        let link_el = document.createElement('a');

        link_el.href = node_data['url'];
        search_el.innerText = 'search';
        search_el.className = 're-search-button';
        search_el.onclick = search_again(node_data['screen_name']);
        link_el.innerText = node_data['screen_name'];
        link_el.target = 'blank';
        description_el.innerText = node_data['description'];

        result_div.appendChild(node_el);
        node_el.appendChild(title_el);
        title_el.appendChild(link_el);
        title_el.innerHTML += node_data['name'];
        title_el.appendChild(search_el);
        node_el.appendChild(description_el);
        node_el.className = 'node';
    }
}

function search_again(screen_name){
    return function(){
        let input_el = document.getElementById(INPUT_ID);
        input_el.value = screen_name_to_url(screen_name);
    }
}

function screen_name_to_url(screen_name){
    return 'https://twitter.com/' + screen_name;
}