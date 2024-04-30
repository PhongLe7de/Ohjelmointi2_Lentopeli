<<<<<<< HEAD
const URL = ''; //waiting for URL from BackEnd

const fetchAPI = async (URL) =>{
    try {
        const response = await fetch(URL,{
            method:'GET',
            headers:{
                'Content-type':'application/json'
            }
        })
        response ? console.log(response) : console.log('Fetch API FAIL');
    } catch (error) {
        console.log(error);
    }   
}
=======
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

>>>>>>> origin/main
