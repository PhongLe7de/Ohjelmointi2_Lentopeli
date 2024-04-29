
const proxy = 'https://users.metropolia.fi/~ilkkamtk/proxy.php?url='
const URL_API = 'http://localhost:3000/gameboard'; //waiting for URL from BackEnd

const fetchAPI = async () => {
    try {
        const response = await fetch(URL_API, {
            method: 'GET'
        })

        console.log(response);
        if (response.ok) {
            console.log('b');
            const result = await response.json()
            console.log(result);
        } else { 
            console.log('Fetch API FAIL')
        }
    } catch (error) {
        console.error(error);
    }
} 
fetchAPI()

