const searchBtn = document.getElementById('search-btn');
const searchInput = document.getElementById('search-input');
if (searchBtn) () => {
    searchBtn.addEventListener('click', (e) => {
        e.preventDefault()
        search = searchInput.value;
        alert(123);
    })
}