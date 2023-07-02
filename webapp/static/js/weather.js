document.addEventListener('DOMContentLoaded', async function() {
    await updateWeatherWidget();
});

async function updateWeatherWidget() {
    city_id = 1;
    let response = await fetch(`/weather/${city_id}`);
    if (response.ok == false)
    {
        alert("Ошибка получения погоды: HTTP " + response.status);
        return;
    }

    // todo: вот здесь хочу получить HTML и подставить через .innerHTML в div
    // а сейчас получается уже готовый
    let html = await response.text();
    console.log(html);
}