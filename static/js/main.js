
function load() {
    document.getElementById('trigger').click();
}

function pos(position) {
    let a = document.getElementById("latitude");
    a.value = position.coords.latitude;
    let b = document.getElementById("longitude");
    b.value = position.coords.longitude;
    let f = document.getElementById("altitude");
    f.value = position.coords.altitude;
    if (f.value == '')
        f.value = 0.0;

    let c = document.getElementById("well_done");
    c.disabled = false;
    let d = document.getElementById("auto_search");
    d.style.display = "none";
    let e = document.getElementById("tes1");
    e.style.display = "block";
}

function err_pos (error){
    switch (error.code) {
    case 1:
        // PERMISSION_DENIED
        alert("Не удалось определить город. Пожалуйста, разрешите доступ к местоположению на странице браузера или в настройках устройства");
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

function getGeo() {
    navigator.geolocation.getCurrentPosition(pos, err_pos);
}


window.onload = load();