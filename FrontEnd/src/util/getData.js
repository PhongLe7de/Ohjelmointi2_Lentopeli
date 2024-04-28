const proxy = 'https://users.metropolia.fi/~ilkkamtk/proxy.php?url='
const URL_API = proxy + 'http://localhost:3000/gameboard'; //waiting for URL from BackEnd

const fetchAPI = async (URL) => {
    try {
        const response = await fetch(URL, {
            method: 'GET'
        })
        if (response.ok) {
            console.log(response);
            const result = await response.json()
            console.log(result);
        } else { 
            console.log('Fetch API FAIL')
        }
    } catch (error) {
        console.log(error);
    }
}
fetchAPI(URL_API)
