function load() {
    document.getElementById('trigger').click();
}



function getGeo() {
    if(navigator.geolocation) {
        var optn = {
            enableHighAccuracy: true,
            timeout: 30000,
            maximumage: 0
        };
        navigator.geolocation.getCurrentPosition(showPosition, showError, optn);
    } else
        alert('Функция определения местоположения не поддерживается вашим браузером...');

    function showPosition(position) {
        let lat = Number(position.coords.latitude);
        let lon = Number(position.coords.longitude);
        let acc = Number(position.coords.accuracy);
        let alt = Number(position.coords.altitude);
        let dir = Number(position.coords.heading);
        let spd = Number(position.coords.speed);



        let lat_id = document.getElementById("latitude");
        lat_id.value = lat
        if (lat_id.value == '')
            lat_id.value = 0.0;
        let lon_id = document.getElementById("longitude");
        lon_id.value = lon
        if (lat_id.value == '')
            lat_id.value = 0.0;
        let acc_id = document.getElementById("accuracy");
        acc_id.value = acc
        if (acc_id.value == '')
            acc_id.value = 0.0;
        let alt_id = document.getElementById("altitude");
        alt_id.value = alt
        if (alt_id.value == '')
            alt_id.value = 0.0;
        let dir_id = document.getElementById("heading");
        dir_id.value = dir
        if (dir_id.value == '')
            dir_id.value = 0.0;
        let spd_id = document.getElementById("speed");
        spd_id.value = spd
        if (spd_id.value == '')
            spd_id.value = 0.0;


        let c = document.getElementById("well_done");
        c.disabled = false;
        let d = document.getElementById("auto_search");
        d.style.display = "none";
        let e = document.getElementById("tes1");
        e.style.display = "block";
    }
}
function showError (error){
    switch (error.code) {
    case 1:
        // PERMISSION_DENIED
        alert("Не удалось определить город. Пожалуйста, разрешите доступ к местоположению на странице браузера или в настройках устройства, или же попробуйте сменить браузер/устройство");
        break;
    case 2:
        // POSITION_UNAVAILABLE
        alert("Геопозиция недоступна");
        break;
    case 3:
        // TIMEOUT
        alert("Время ожидания истекло. Попробуйте обновить страницу и попробовать еще раз");
        break;
    default:
        alert("Произошла неизвестная ошибка")
    }
}

window.onload = load();