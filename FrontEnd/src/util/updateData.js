const URL = ''; //waiting for URL from BackEnd

const updateData = async (URL, player, data) => {
    try {
      const response = await fetch(URL, {
        method: "PATCH",
        headers: {
          "Content-type": "application/json",
        },
        body: JSON.stringify({ player, data }),
      });
  
      if (response) {
        console.log("update success");
      } else {
        console.log("update fail");
      }
    } catch (error) {
      console.log(error);
    }
  };