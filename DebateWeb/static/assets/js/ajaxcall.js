console.log('Logging');

function like(id) {
    var stdData = id;
    console.log(stdData)
    _success = function (res) {
        // console.log(res);
        
    }
    _error = function (error) {
        console.log(error);

    }


    callAjaxPost('/jsonupdates/', stdData, _success, _error, false, '');

}
